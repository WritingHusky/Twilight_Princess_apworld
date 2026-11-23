from argparse import Namespace
import unittest

from BaseClasses import CollectionState, MultiWorld
from Options import Range
from test.bases import WorldTestBase
from worlds.AutoWorld import call_all

from worlds.twilight_princess import TPSettings, TPWorld
from worlds.twilight_princess.options import *
from worlds.twilight_princess.Tracker import (
    SETTINGS_TO_OPTIONS,
    option_value_from_name,
    tracker_world,
)
from worlds.twilight_princess.TrackerData import MAP_PAGE_GROUPS, POPTRACKER_NAME_MAPPING

GAME = "Twilight Princess"


class TestTrackerData(unittest.TestCase):
    def test_mapped_ids_exist(self) -> None:
        """Every location id in the Universal Tracker mapping is a location in this apworld."""
        location_ids = set(TPWorld.location_name_to_id.values())
        unknown = {key: loc_id for key, loc_id in POPTRACKER_NAME_MAPPING.items() if loc_id not in location_ids}
        self.assertEqual(unknown, {})

    def test_mapping_keys(self) -> None:
        """Keys use Universal Tracker's "<location>/<section>" format."""
        for key in POPTRACKER_NAME_MAPPING:
            self.assertNotIn("@", key)
            self.assertIn("/", key)

    def test_tracker_world(self) -> None:
        self.assertIs(TPWorld.tracker_world, tracker_world)
        self.assertIn(tracker_world["external_pack_key"], TPSettings.__annotations__)
        self.assertTrue(tracker_world["map_page_maps"])
        self.assertTrue(tracker_world["map_page_locations"])
        self.assertIs(tracker_world["map_page_groups"], MAP_PAGE_GROUPS)

        def check_group(node) -> None:
            if isinstance(node, str):
                return
            title, children = node
            self.assertIsInstance(title, str)
            self.assertIsInstance(children, list)
            for child in children:
                check_group(child)

        for group in MAP_PAGE_GROUPS:
            check_group(group)

    def test_unset_pack_path(self) -> None:
        """An empty ut_pack_path reads back as "", which makes Universal Tracker ask for the pack."""
        group = TPSettings()
        self.assertEqual(group.ut_pack_path, "")
        group.ut_pack_path = TPSettings.UTPackPath("pack.zip")
        self.assertTrue(group.ut_pack_path.endswith("pack.zip"))

    def test_settings_options_exist(self) -> None:
        for key, option_name in SETTINGS_TO_OPTIONS.items():
            self.assertIn(option_name, TPOptions.type_hints, key)

    def test_option_values_round_trip(self) -> None:
        """option_value_from_name inverts get_option_name, the format slot_data["Settings"] is written in."""
        for option_name in SETTINGS_TO_OPTIONS.values():
            option_type = TPOptions.type_hints[option_name]
            if issubclass(option_type, Range):
                values = {option_type.range_start, option_type.default, option_type.range_end}
            else:
                values = set(option_type.name_lookup)
            for value in values:
                with self.subTest(option=option_name, value=value):
                    display = option_type.get_option_name(value)
                    self.assertEqual(option_value_from_name(option_name, display), value)


class TestTrackerRegen(WorldTestBase):
    """Universal Tracker can rebuild a seed's options and logic from slot data alone."""

    game = GAME
    run_default_tests = False
    options = {
        "faron_woods_logic": FaronWoodsLogic.option_closed,
        "castle_requirements": CastleRequirements.option_dungeons,
        "castle_requirements_count": 5,
        "castle_bk_requirements": CastleBKRequirements.option_fused_shadows,
        "castle_bk_requirements_count": 2,
        "palace_requirements": PalaceRequirements.option_mirror_shards,
        "goron_mines_entrance": GoronMinesEntrance.option_no_wrestling,
        "skip_lakebed_entrance": False,
        "grove_entrance": True,
        "open_door_of_time": True,
        "small_key_settings": SmallKeySettings.option_own_dungeon,
        "big_key_settings": BigKeySettings.option_any_dungeon,
        "wallet_size": WalletSize.option_large,
        "damage_magnification": DamageMagnification.option_double,
        "early_shadow_crystal": True,
        "poe_shuffled": False,
    }

    def regenerate(self) -> MultiWorld:
        """Mirror Universal Tracker's YAML-less generation: default options, then interpret_slot_data."""
        slot_data = dict(self.world.fill_slot_data())
        multiworld = MultiWorld(1)
        multiworld.generation_is_fake = True
        multiworld.re_gen_passthrough = {GAME: TPWorld.interpret_slot_data(slot_data)}
        multiworld.game = {1: GAME}
        multiworld.player_name = {1: self.multiworld.player_name[1]}
        multiworld.set_seed()
        args = Namespace(**{
            name: {1: option_type.from_any(option_type.default)}
            for name, option_type in TPWorld.options_dataclass.type_hints.items()
        })
        multiworld.set_options(args)
        multiworld.state = CollectionState(multiworld)
        for step in ("generate_early", "create_regions", "create_items", "set_rules", "connect_entrances"):
            call_all(multiworld, step)
        return multiworld

    def test_interpret_slot_data_is_static(self) -> None:
        """UT only skips the first, default-options generation when interpret_slot_data is a staticmethod."""
        self.assertIsInstance(TPWorld.__dict__["interpret_slot_data"], staticmethod)
        self.assertTrue(TPWorld.ut_can_gen_without_yaml)

    def test_options_rebuilt(self) -> None:
        regen = self.regenerate().worlds[1]
        settings = self.world.get_settings_map()
        for key in settings:
            self.assertIn(key, SETTINGS_TO_OPTIONS, f"slot_data['Settings'][{key!r}] is not read back")
        for key, option_name in SETTINGS_TO_OPTIONS.items():
            if key not in settings:
                continue  # not in this version's slot data
            with self.subTest(option=option_name):
                self.assertEqual(getattr(regen.options, option_name).value,
                                 getattr(self.world.options, option_name).value)

    def test_logic_matches(self) -> None:
        regen = self.regenerate()
        progression = sorted(
            location.item.name
            for location in self.multiworld.get_locations(1)
            if location.address is not None and location.item and location.item.advancement
        )
        for items in ([], progression[::3], progression[::2], progression):
            with self.subTest(items=len(items)):
                self.assertEqual(self.reachable(regen, items), self.reachable(self.multiworld, items))

    @staticmethod
    def reachable(multiworld: MultiWorld, item_names: list[str]) -> set[str]:
        world = multiworld.worlds[1]
        state = CollectionState(multiworld)
        for name in item_names:
            state.collect(world.create_item(name), True)
        state.sweep_for_advancements(locations=[loc for loc in multiworld.get_locations(1) if loc.address is None])
        return {loc.name for loc in multiworld.get_reachable_locations(state, 1) if loc.address is not None}
