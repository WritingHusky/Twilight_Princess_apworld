"""Generate TrackerData.py (Universal Tracker map data) from the TPRAP PopTracker pack.

The pack (https://github.com/Kizugaya/TPRAP_poptracker) is not vendored. Point this script at a checkout or at
the pack .zip and it rebuilds the mapping from the pack's own files:

    python tools/gen_tracker_data.py <pack dir or .zip> [--ap-root <Archipelago checkout>]

Inputs read from the pack:
  * scripts/location_mapping.lua      AP location id -> PopTracker section code ("@Region/.../Location/Section")
  * locations/**/*.json               to resolve each code to the location/section names UT matches on, and to
                                      find "ref" sections (the grouped dungeon pins on the overworld map)
  * layouts/layouts_maps.json         the pack's own map tabs, turned into UT's map_page_groups
  * maps/*.json                       to check every grouped map exists

Universal Tracker matches a pin by the key f"{location name}/{section name}" (the last two parts of the PopTracker
code, the same format DK64's SECTION_NAMES uses). An unnamed section gives an empty section name, e.g.
"Faron Mist North Chest/". Keys that the pack uses for more than one AP location (e.g. "Big Key Chest/" in every
dungeon) cannot be told apart by UT and are left out rather than pointing pins at the wrong check.
"""

import argparse
import collections
import json
import os
import pathlib
import re
import subprocess
import sys
import zipfile

HERE = pathlib.Path(__file__).parent
OUTPUT = HERE.parent / "TrackerData.py"
# Location json files that hold pins. rooms/ and access_function.json are logic-only; tutorial.json is the
# pack's tutorial page.
LOCATION_FILE_PATTERN = re.compile(r"^locations/(dungeons|overworld)/[^/]+\.json$")
MAP_FILE_PATTERN = re.compile(r"^maps/[^/]+\.json$")
LAYOUT_FILE = "layouts/layouts_maps.json"
LAYOUT_KEY = "layout_maps"


class Pack:
    """Read-only view over a pack directory or zip."""

    def __init__(self, path: pathlib.Path):
        self.path = path
        if path.is_dir():
            self.names = sorted(p.relative_to(path).as_posix() for p in path.rglob("*") if p.is_file())
            self._read = lambda name: (path / name).read_bytes()
        else:
            zf = zipfile.ZipFile(path)
            self.names = sorted(n for n in zf.namelist() if not n.endswith("/"))
            self._read = zf.read
            if "manifest.json" not in self.names:
                sys.exit(f"{path}: manifest.json must be at the root of the zip (Universal Tracker reads it there)")

    def text(self, name: str) -> str:
        return self._read(name).decode("utf-8-sig")

    def json(self, name: str):
        return json.loads(self.text(name))

    def describe(self) -> str:
        version = self.json("manifest.json").get("package_version", "?")
        desc = f"TPRAP_poptracker {version}"
        if self.path.is_dir():
            try:
                commit = subprocess.run(["git", "-C", str(self.path), "rev-parse", "--short", "HEAD"],
                                        capture_output=True, text=True, check=True).stdout.strip()
                desc += f" (commit {commit})"
            except (OSError, subprocess.CalledProcessError):
                pass
        return desc


def parse_location_mapping(text: str) -> tuple[int, dict[int, list[str]]]:
    base_match = re.search(r"^\s*BASE\s*=\s*(\d+)", text, re.MULTILINE)
    if not base_match:
        sys.exit("location_mapping.lua: no BASE = <number> line")
    base = int(base_match.group(1))
    entries: dict[int, list[str]] = {}
    for line_no, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("--"):
            continue
        match = re.match(r"\[BASE\s*\+\s*(\d+)\]\s*=\s*\{(.*)\}\s*,?\s*(--.*)?$", stripped)
        if not match:
            if stripped.startswith("["):
                sys.exit(f"location_mapping.lua:{line_no}: could not parse {stripped!r}")
            continue
        loc_id = base + int(match.group(1))
        if loc_id in entries:
            sys.exit(f"location_mapping.lua:{line_no}: id BASE + {match.group(1)} appears twice")
        entries[loc_id] = re.findall(r'"([^"]*)"', match.group(2))
    return base, entries


def leaf_key(location: str, section: str) -> tuple[str, str]:
    return location.strip().lower(), section.strip().lower()


def walk_locations(pack: Pack, files: list[str]):
    """Yield (full code, location name, section dict, has map_locations) for every section UT will see.

    Mirrors UT's traversal: a node with map_locations is a pin and its children are not visited."""
    def walk(node, parent_path):
        name = node.get("name", "")
        path = f"{parent_path}/{name}" if parent_path else name
        has_pin = "map_locations" in node
        for section in node.get("sections", []):
            yield f"@{path}/{section.get('name', '')}", name, section, has_pin
        if not has_pin:
            for child in node.get("children", []):
                yield from walk(child, path)

    for file in files:
        for node in pack.json(file):
            yield from walk(node, "")


def layout_to_groups(node, maps_seen: list[str]):
    """Convert a PopTracker tabbed layout into UT map_page_groups: [(title, [map name | (title, [...])])]."""
    if isinstance(node, list):
        out = []
        for item in node:
            out.extend(layout_to_groups(item, maps_seen))
        return out
    if not isinstance(node, dict):
        return []
    if node.get("type") == "map":
        maps_seen.extend(node.get("maps", []))
        return list(node.get("maps", []))
    if "tabs" in node:
        out = []
        for tab in node["tabs"]:
            children = layout_to_groups(tab.get("content", []), maps_seen)
            if children:
                out.append((tab["title"], children))
        return out
    if "content" in node:
        return layout_to_groups(node["content"], maps_seen)
    return []


def load_apworld_locations(ap_root: pathlib.Path) -> dict[int, str]:
    sys.path.insert(0, str(ap_root))
    from worlds.twilight_princess import TPWorld  # noqa: E402  (needs Archipelago on sys.path)
    return {loc_id: name for name, loc_id in TPWorld.location_name_to_id.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("pack", type=pathlib.Path, help="TPRAP_poptracker checkout or pack .zip")
    parser.add_argument("--ap-root", type=pathlib.Path, default=HERE.parent.parent.parent,
                        help="Archipelago checkout containing worlds/twilight_princess (default: three levels up)")
    parser.add_argument("--output", type=pathlib.Path, default=OUTPUT)
    args = parser.parse_args()

    pack = Pack(args.pack)
    apworld = load_apworld_locations(args.ap_root)
    from worlds.twilight_princess.ClientUtils import ITEM_APID_BASE

    base, lua = parse_location_mapping(pack.text("scripts/location_mapping.lua"))
    if base != ITEM_APID_BASE:
        sys.exit(f"location_mapping.lua BASE {base} != apworld base {ITEM_APID_BASE}")

    location_files = [n for n in pack.names if LOCATION_FILE_PATTERN.match(n)]
    sections = list(walk_locations(pack, location_files))
    by_code: dict[str, list] = collections.defaultdict(list)
    by_leaf: dict[tuple[str, str], list] = collections.defaultdict(list)
    for code, loc_name, section, has_pin in sections:
        by_code[code.lower()].append((code, loc_name, section, has_pin))
        by_leaf[leaf_key(loc_name, section.get("name", ""))].append((code, loc_name, section, has_pin))

    report: dict[str, list[str]] = collections.defaultdict(list)
    keys: dict[str, set[int]] = collections.defaultdict(set)
    code_to_id: dict[str, int] = {}

    # 1. Direct sections named by location_mapping.lua.
    for loc_id, codes in sorted(lua.items()):
        if loc_id not in apworld:
            report["ids in location_mapping.lua that the apworld does not have"].append(f"{loc_id} {codes}")
            continue
        for code in codes:
            if not code.startswith("@"):
                continue  # item/toggle codes, not map pins
            code_to_id[code.lower()] = loc_id
            matches = by_code.get(code.lower())
            if not matches:
                # The parent path in the lua sometimes differs from the json (renamed regions, stray spaces).
                # UT only looks at the last two parts, so accept a unique match on those.
                parts = code.split("/")
                matches = [m for m in by_leaf.get(leaf_key(parts[-2], parts[-1]), []) if m[3]]
                if len(matches) != 1:
                    report["codes not found in the pack's location files"].append(f"{loc_id} {code}")
                    continue
                report["codes resolved by location/section name only"].append(f"{code} -> {matches[0][0]}")
            elif all(m[0] != code for m in matches):
                report["codes that only match ignoring case (resolved)"].append(f"{code} -> {matches[0][0]}")
            for _, loc_name, section, has_pin in matches:
                if not has_pin:
                    report["sections with no map pin"].append(f"{loc_id} {code}")
                    continue
                keys[f"{loc_name}/{section.get('name', '')}"].add(loc_id)

    # 2. "ref" sections: grouped pins (e.g. a whole dungeon on the overworld) that point at a direct section.
    for code, loc_name, section, has_pin in sections:
        ref = section.get("ref")
        if not ref or not has_pin:
            continue
        loc_id = code_to_id.get("@" + ref.lstrip("@").lower())
        if loc_id is not None:
            keys[f"{loc_name}/{section.get('name', '')}"].add(loc_id)

    mapping: dict[str, int] = {}
    for key, ids in keys.items():
        if len(ids) == 1:
            mapping[key] = next(iter(ids))
        else:
            report["keys shared by several AP locations (left out: UT cannot tell them apart)"].append(
                f"{key!r}: " + ", ".join(f"{apworld[i]} ({i})" for i in sorted(ids)))

    mapped_ids = set(mapping.values())
    lua_ids = set(lua)
    for loc_id, name in sorted(apworld.items()):
        if loc_id not in lua_ids:
            report["apworld locations with no section in location_mapping.lua"].append(f"{loc_id} {name}")
        elif loc_id not in mapped_ids:
            report["apworld locations in location_mapping.lua but with no usable UT key"].append(f"{loc_id} {name}")

    maps_seen: list[str] = []
    groups = layout_to_groups(pack.json(LAYOUT_FILE)[LAYOUT_KEY], maps_seen)
    map_files = [n for n in pack.names if MAP_FILE_PATTERN.match(n)]
    pack_maps = {m["name"] for f in map_files for m in pack.json(f)}
    for name in maps_seen:
        if name not in pack_maps:
            report["maps in the layout that maps/maps.json does not define"].append(name)
    for name in sorted(pack_maps - set(maps_seen)):
        report["maps not reachable from the map groups"].append(name)

    write_output(args.output, pack.describe(), mapping, apworld, map_files, location_files, groups)

    print(f"{pack.describe()}: {len(lua)} entries in location_mapping.lua, {len(mapping)} UT keys "
          f"covering {len(mapped_ids)} of {len(apworld)} apworld locations -> {args.output}")
    for title, lines in report.items():
        print(f"\n{title}: {len(lines)}")
        for line in lines:
            print(f"  {line}")


def write_output(path: pathlib.Path, source: str, mapping: dict[str, int], apworld: dict[int, str],
                 map_files: list[str], location_files: list[str], groups: list) -> None:
    out = [
        f'"""Universal Tracker map data generated from {source}.',
        "",
        "Do not edit by hand: regenerate with tools/gen_tracker_data.py.",
        '"""',
        "",
        "# Pack files Universal Tracker loads.",
        f"MAP_PAGE_MAPS = {json.dumps(map_files)}",
        "MAP_PAGE_LOCATIONS = [",
        *(f"    {json.dumps(f)}," for f in location_files),
        "]",
        "",
        "# The pack's own map tabs (layouts/layouts_maps.json).",
        "MAP_PAGE_GROUPS = " + format_groups(groups, 0),
        "",
        '# "<PopTracker location>/<section>" -> AP location id. Unnamed sections have an empty section name.',
        "POPTRACKER_NAME_MAPPING = {",
    ]
    for key, loc_id in sorted(mapping.items(), key=lambda kv: (kv[1], kv[0])):
        out.append(f"    {json.dumps(key, ensure_ascii=False)}: {loc_id},  # {apworld[loc_id]}")
    out.append("}")
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def format_groups(nodes: list, indent: int) -> str:
    pad = " " * indent
    if all(isinstance(n, str) for n in nodes):
        return json.dumps(nodes, ensure_ascii=False)
    lines = ["["]
    for node in nodes:
        if isinstance(node, str):
            lines.append(f"{pad}    {json.dumps(node, ensure_ascii=False)},")
        else:
            title, children = node
            lines.append(f"{pad}    ({json.dumps(title, ensure_ascii=False)}, {format_groups(children, indent + 4)}),")
    lines.append(f"{pad}]")
    return "\n".join(lines)


if __name__ == "__main__":
    os.environ.setdefault("SKIP_REQUIREMENTS_UPDATE", "1")
    main()
