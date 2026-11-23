"""Universal Tracker support.

Map pages come from the Twilight Princess PopTracker pack by Kizugaya (https://github.com/Kizugaya/TPRAP_poptracker),
loaded from the zip set as `ut_pack_path` in host.yaml. The pack is not bundled; TrackerData.py only holds the names
needed to find its files and match its pins, and is generated from the pack by tools/gen_tracker_data.py.
"""

import logging
from typing import Any

from Options import NumericOption, Range

from .TrackerData import MAP_PAGE_GROUPS, MAP_PAGE_LOCATIONS, MAP_PAGE_MAPS, POPTRACKER_NAME_MAPPING
from .options import TPOptions

logger = logging.getLogger("Twilight Princess")

tracker_world = {
    "external_pack_key": "ut_pack_path",
    "map_page_maps": MAP_PAGE_MAPS,
    "map_page_locations": MAP_PAGE_LOCATIONS,
    "map_page_groups": MAP_PAGE_GROUPS,
    "poptracker_name_mapping": POPTRACKER_NAME_MAPPING,
}

# slot_data["Settings"] key -> option name. Keys match TPWorld.get_settings_map(), including its spelling.
# Keys a seed does not have (older apworld versions) keep the option's default.
SETTINGS_TO_OPTIONS = {
    "Skip Minor Cutscenes": "skip_minor_cutscenes",
    "Skip Major Cutscenes": "skip_major_cutscenes",
    "Fast Iron Boots": "fast_iron_boots",
    "Quick Transform": "quick_transform",
    "Instant Message Text": "instant_message_text",
    "Open Map": "open_map",
    "Increase Spinner Speed": "increase_spinner_speed",
    "Open Door of Time": "open_door_of_time",
    "Early Shadow Crystal": "early_shadow_crystal",
    "Goron Mines Shortcut": "goron_mines_sc",
    "Castle Shortcut": "castle_sc",
    "Skip Bridge Donation": "skip_bridge_don",
    "Transform Anywhere": "transform_anywhere",
    "Wallet Size": "wallet_size",
    "Auto Fill Wallet": "auto_fill_wallet",
    "Bonks do Damage": "bonks_do_damage",
    "Trap Frequency": "trap_frequency",
    "Damage Magnification": "damage_magnification",
    "Starting ToD": "starting_tod",
    "Ilia Quest": "ilia_quest",
    "Modify Shop Models": "modify_shop_models",
    "Goron Mines Entrance Requirements": "goron_mines_entrance",
    "Lakebed Entrance Requirements": "skip_lakebed_entrance",
    "Arbiters Grounds Entrance Requirements": "skip_arbiters_grounds_entrance",
    "Snowpeak Entrance Requirements": "skip_snowpeak_entrance",
    "Sacred Grove Entrance Requirements": "grove_entrance",
    "City in the Sky Entrance Requirements": "skip_city_in_the_sky_entrance",
    "Temple of Time Sword Requirement": "tot_entrance",
    "Logic Settings": "logic_rules",
    "Castle Requirements": "castle_requirements",
    "Castle Requirements Count": "castle_requirements_count",
    "Castle Big Key Requirements": "castle_bk_requirements",
    "Castle Big Key Requirements Count": "castle_bk_requirements_count",
    "Palace of Twilight Requirements": "palace_requirements",
    "Faron Woods Logic": "faron_woods_logic",
    "Golden Bugs Shuffled": "golden_bugs_shuffled",
    "Sky Chracters Shuffled": "sky_characters_shuffled",
    "NPC Items Shuffled": "npc_items_shuffled",
    "Shop Items Shuffled": "shop_items_shuffled",
    "Hidden Skills Shuffled": "hidden_skills_shuffled",
    "Poes Shuffled": "poe_shuffled",
    "Heart Pieces Shuffled": "heart_piece_shuffled",
    "Freestanding Rupee Shuffled": "freestanding_rupee_shuffled",
    "Hidden Rupee Shuffled": "hidden_rupee_shuffled",
    "Overworld Shuffled": "overworld_shuffled",
    "Dungeons Shuffled": "dungeons_shuffled",
    "Dungeon Rewards Progression": "dungeon_rewards_progression",
    "Small Key Settings": "small_key_settings",
    "Big Key Settings": "big_key_settings",
    "Map and Compass Settings": "map_and_compass_settings",
    "Small Keys On Bosses": "small_keys_on_bosses",
}


def option_value_from_name(option_name: str, display: Any) -> int:
    """Invert Option.get_option_name(), which is how get_settings_map() wrote the value."""
    option_type = TPOptions.type_hints[option_name]
    if issubclass(option_type, Range):
        return int(display)
    assert issubclass(option_type, NumericOption)
    for value in option_type.name_lookup:
        if option_type.get_option_name(value) == display:
            return value
    raise ValueError(f"{display!r} is not a value of {option_name}")


def options_from_slot_data(slot_data: dict[str, Any]) -> dict[str, int]:
    """Rebuild the options that shape logic from slot_data, so Universal Tracker can regenerate without a YAML."""
    options: dict[str, int] = {}
    for key, display in slot_data.get("Settings", {}).items():
        option_name = SETTINGS_TO_OPTIONS.get(key)
        if option_name is None:
            logger.warning(f"[Twilight Princess] Universal Tracker: unknown slot data setting {key!r}, ignoring it")
            continue
        options[option_name] = option_value_from_name(option_name, display)
    if "DeathLink" in slot_data:
        options["death_link"] = int(slot_data["DeathLink"])
    return options
