from copy import deepcopy
from typing import TYPE_CHECKING
from BaseClasses import CollectionState, Item, Location
from Fill import fill_restrictive
from ..Locations import LOCATION_TABLE
from ..options import *
from ..Items import ITEM_TABLE, item_factory
from .ItemPool import (
    VANILLA_GOLDEN_BUG_LOCATIONS,
    VANILLA_POE_LOCATIONS,
    VANILLA_SKY_CHARACTER_LOCATIONS,
    VANILLA_SMALL_KEYS_LOCATIONS,
    VANILLA_BIG_KEY_LOCATIONS,
    VANILLA_MAP_AND_COMPASS_LOCATIONS,
)

if TYPE_CHECKING:
    from .. import TPWorld


def place_vanilla_dungeon_items(world: "TPWorld"):

    def _place_dungeon_items(vanilla: dict[str, dict[str, list[str]]]):
        for dungeon, data in vanilla.items():
            for key_name, locations in data.items():
                assert (
                    key_name in ITEM_TABLE
                ), f"[Twilight Princess] {key_name=} not in item table"

                key_list = [key_name] * len(locations)
                key_items = item_factory(key_list, world)

                assert isinstance(
                    key_items, list
                ), f"[Twilight Princess] item factory should be given a list and therefore create a list {key_list=} {key_items=}"
                assert len(key_items) == len(
                    locations
                ), f"[Twilight Princess] {len(key_items)=}!={len(locations)=}"

                for key, location in zip(key_items, locations):
                    assert (
                        location in LOCATION_TABLE
                    ), f"[Twilight Princess] {location=} not in location table"
                    world.get_location(location).place_locked_item(key)

    if world.options.small_key_settings.value == SmallKeySettings.option_vanilla:
        _place_dungeon_items(VANILLA_SMALL_KEYS_LOCATIONS)

    if world.options.big_key_settings.value == BigKeySettings.option_vanilla:
        _place_dungeon_items(VANILLA_BIG_KEY_LOCATIONS)

    if (
        world.options.map_and_compass_settings.value
        == MapAndCompassSettings.option_vanilla
    ):
        _place_dungeon_items(VANILLA_MAP_AND_COMPASS_LOCATIONS)


def place_vanilla_items(world: "TPWorld"):
    if world.options.golden_bugs_shuffled.value == GoldenBugsShuffled.option_false:
        for bug_name, location in VANILLA_GOLDEN_BUG_LOCATIONS.items():
            assert (
                bug_name in ITEM_TABLE
            ), f"[Twilight Princess] {bug_name=} not in item table"
            assert (
                bug_name in world.pre_shuffle_pool
            ), f"[Twilight Princess] {bug_name=} not in pre_shuffle_pool"
            assert (
                location in LOCATION_TABLE
            ), f"[Twilight Princess] {location=} not in location table"

            bug_item = item_factory(bug_name, world)

            assert isinstance(
                bug_item, Item
            ), f"[Twilight Princess] item factory should be given a str and therefore create a item {bug_name=} {bug_item=}"

            world.get_location(location).place_locked_item(bug_item)
            world.remove_from_pre_shuffle_pool(bug_name)
            assert bug_name not in world.pre_shuffle_pool

    if world.options.poe_shuffled.value == PoeShuffled.option_false:
        poe_name = "Poe Soul"
        assert (
            poe_name in ITEM_TABLE
        ), f"[Twilight Princess] {poe_name=} not in item table"
        assert len(VANILLA_POE_LOCATIONS) == world.pre_shuffle_pool.count(
            poe_name
        ), f"[Twilight Princess] {len(VANILLA_POE_LOCATIONS)=}!={world.pre_shuffle_pool.count(poe_name)=}"

        for location in VANILLA_POE_LOCATIONS:
            assert (
                location in LOCATION_TABLE
            ), f"[Twilight Princess] {location=} not in location table"

            poe_item = item_factory(poe_name, world)

            assert isinstance(
                poe_item, Item
            ), f"[Twilight Princess] item factory should be given a str and therefore create a item {poe_name=} {poe_item=}"

            world.get_location(location).place_locked_item(poe_item)
            world.remove_from_pre_shuffle_pool(poe_name)
        assert poe_name not in world.pre_shuffle_pool

    if (
        world.options.sky_characters_shuffled.value
        == SkyCharactersShuffled.option_false
    ):
        sky_character_name = "Progressive Sky Book"
        assert (
            sky_character_name in ITEM_TABLE
        ), f"[Twilight Princess] {sky_character_name=} not in item table"
        assert (
            len(VANILLA_SKY_CHARACTER_LOCATIONS) + 1
        ) == world.pre_shuffle_pool.count(
            sky_character_name
        ), f"[Twilight Princess] {len(VANILLA_SKY_CHARACTER_LOCATIONS)=}!={world.pre_shuffle_pool.count(sky_character_name)=}"

        for location in VANILLA_SKY_CHARACTER_LOCATIONS:
            assert (
                location in LOCATION_TABLE
            ), f"[Twilight Princess] {location=} not in location table"

            sky_character_item = item_factory(sky_character_name, world)

            assert isinstance(
                sky_character_item, Item
            ), f"[Twilight Princess] item factory should be given a str and therefore create a item {sky_character_name=} {sky_character_item=}"

            world.get_location(location).place_locked_item(sky_character_item)
            world.remove_from_pre_shuffle_pool(sky_character_name)

        # need to add 7th character to precollected as only 6 locations
        sky_character_item = item_factory(sky_character_name, world)
        world.push_precollected(sky_character_item)
        world.remove_from_pre_shuffle_pool(sky_character_name)
        assert sky_character_name not in world.pre_shuffle_pool


def _on_place(location: Location):
    # logging.info(location.name)
    pass


def _place_own_dungeon(
    world: "TPWorld",
    state: CollectionState,
    vanilla: dict[str, dict[str, list[str]]],
):
    for dungeon_name, data in vanilla.items():
        locations_base = [
            world.get_location(location)
            for location, data in LOCATION_TABLE.items()
            if data.stage_id.value == dungeon_name
        ]
        locations = [
            location
            for location in locations_base
            if location.item is None and location.address is not None
        ]
        assert (
            len(locations) > 0
        ), f"[Twilight Princess] (Own Dungeon) no locations for {dungeon_name=}"

        full_item_list: list[Item] = []

        for item_name, location_names in data.items():
            assert (
                item_name in ITEM_TABLE
            ), f"[Twilight Princess] (Own Dungeon) {item_name=} not in item table"
            assert (
                item_name in world.pre_shuffle_pool
            ), f"[Twilight Princess] (Own Dungeon) {item_name=} not in pre_shuffle_pool"

            item_list = [item_name] * len(location_names)

            assert len(item_list) == world.pre_shuffle_pool.count(
                item_name
            ), f"[Twilight Princess] (Own Dungeon) {len(item_list)=}!={world.pre_shuffle_pool.count(item_name)=}"

            items = item_factory(item_list, world)

            assert isinstance(
                items, list
            ), f"[Twilight Princess] (Own Dungeon) items not a list {items=} {item_list=}"
            assert len(items) == len(
                location_names
            ), f"[Twilight Princess] (Own Dungeon) {len(items)=}!={len(location_names)=}"

            full_item_list.extend(items)

        state_copy = None
        if dungeon_name == "Palace of Twilight":
            state_copy = state.copy()
            if not state.has("Arbiters Grounds Big Key", world.player):
                state.collect(world.create_item("Arbiters Grounds Big Key"))
            if not state.has("Arbiters Grounds Small Key", world.player, 5):
                for _ in range(5):
                    state.collect(world.create_item("Arbiters Grounds Small Key"))

            if world.options.palace_requirements == PalaceRequirements.option_vanilla:
                state.collect(world.boss_defeat_items["Argorok"])
            state.sweep_for_advancements()

        elif dungeon_name == "Hyrule Castle":
            state_copy = state.copy()

            if (
                world.options.castle_requirements
                == CastleRequirements.option_all_dungeons
            ):
                for name, item in world.boss_defeat_items.items():
                    state.collect(item)
            elif world.options.castle_requirements == CastleRequirements.option_vanilla:
                state.collect(world.boss_defeat_items["Zant"])
            state.sweep_for_advancements()

        assert len(locations) >= len(
            full_item_list
        ), f"[Twilight Princess] (Own Dungeon) There are not enough locations for items in {dungeon_name=} acording to final counts {locations=}, {items=}"

        items_copy = deepcopy(items)
        world.multiworld.random.shuffle(full_item_list)
        world.multiworld.random.shuffle(locations)

        fill_restrictive(
            world.multiworld,
            state,
            locations,
            full_item_list,
            single_player_placement=True,
            lock=True,
            allow_excluded=True,
            on_place=_on_place,
        )

        # All items should be placed
        assert (
            len(full_item_list) == 0
        ), f"[Twilight Princess] (Own dungeon) Not all items placed {full_item_list=}"

        for item in items_copy:
            world.remove_from_pre_shuffle_pool(item.name)

        # Restore state if in palace of twilight
        if state_copy:
            state = state_copy


def _place_any_dungeon(
    world: "TPWorld",
    state: CollectionState,
    vanilla: dict[str, dict[str, list[str]]],
):
    items = []
    locations = []
    skip_hyrule_castle = False
    skip_palace_of_twilight = False
    skip_forest_temple = False
    for dungeon_name in vanilla:

        if dungeon_name == "Hyrule Castle":
            if world.options.castle_requirements.value in [
                CastleRequirements.option_vanilla,
                CastleRequirements.option_all_dungeons,
            ]:
                skip_hyrule_castle = True
                continue
        elif dungeon_name == "Palace of Twilight":
            if (
                world.options.palace_requirements.value
                == PalaceRequirements.option_vanilla
            ):
                skip_palace_of_twilight = True
                continue
        elif dungeon_name == "Forest Temple":
            if world.options.faron_woods_logic == FaronWoodsLogic.option_closed:
                skip_forest_temple = True
                continue

        locations_base = [
            world.get_location(location)
            for location, data in LOCATION_TABLE.items()
            if data.stage_id.value == dungeon_name
        ]
        new_locations = [
            location
            for location in locations_base
            if location.item is None
            and location.address is not None
            and location not in locations
        ]
        assert (
            len(new_locations) > 0
        ), f"[Twilight Princess] (Any Dungeon) no locations for {dungeon_name=}"

        locations.extend(new_locations)

        for item_name, item_location_names in vanilla[dungeon_name].items():
            assert (
                item_name in ITEM_TABLE
            ), f"[Twilight Princess] (Any Dungeon) {item_name=} not in item table"
            assert (
                item_name in world.pre_shuffle_pool
            ), f"[Twilight Princess] (Any Dungeon) {item_name=} not in pre_shuffle_pool"

            new_item_list = [item_name] * len(item_location_names)

            assert len(new_item_list) == world.pre_shuffle_pool.count(
                item_name
            ), f"[Twilight Princess] (Any Dungeon)  {len(new_item_list)=}!={world.pre_shuffle_pool.count(item_name)=}"

            new_items = item_factory(new_item_list, world)

            assert isinstance(
                new_items, list
            ), f"[Twilight Princess] (Any Dungeon) items not a list {new_items=} {new_item_list=}"

            items.extend(new_items)

        # Sanity check
        item_name = None

    assert len(locations) >= len(
        items
    ), f"[Twilight Princess] (Any Dungeon) There are not enough locations for items in {dungeon_name=} acording to final counts {locations=}, {items=}"

    items_copy = deepcopy(items)
    world.multiworld.random.shuffle(items)
    world.multiworld.random.shuffle(locations)

    fill_restrictive(
        world.multiworld,
        state,
        locations,
        items,
        single_player_placement=True,
        lock=True,
        allow_excluded=True,
        on_place=_on_place,
    )

    # All items should be placed
    assert (
        len(items) == 0
    ), f"[Twilight Princess] (Any dungeon) Not all items placed {items=}"

    for item in items_copy:
        world.remove_from_pre_shuffle_pool(item.name)

    # Now deal with POT and HC items
    # Which will be own_dungeon
    skipped_dungeons = []
    if skip_hyrule_castle:
        skipped_dungeons.append("Hyrule Castle")
    if skip_palace_of_twilight:
        skipped_dungeons.append("Palace of Twilight")
    if skip_forest_temple:
        skipped_dungeons.append("Forest Temple")
    for dungeon_name in skipped_dungeons:

        locations_base = [
            world.get_location(location)
            for location, data in LOCATION_TABLE.items()
            if data.stage_id.value == dungeon_name
        ]
        locations = [
            location
            for location in locations_base
            if location.item is None and location.address is not None
        ]
        assert (
            len(locations) > 0
        ), f"[Twilight Princess] (Any-Own Dungeon) no locations for {dungeon_name=}"

        items: list[Item] = []

        for item_name, item_location_names in vanilla[dungeon_name].items():
            assert (
                item_name in ITEM_TABLE
            ), f"[Twilight Princess] (Any-Own Dungeon) {item_name=} not in item table"
            assert (
                item_name in world.pre_shuffle_pool
            ), f"[Twilight Princess] (Any-Own Dungeon) {item_name=} not in pre_shuffle"

            new_item_list = [item_name] * len(item_location_names)

            assert len(new_item_list) == world.pre_shuffle_pool.count(
                item_name
            ), f"[Twilight Princess] (Any-Own Dungeon)  {len(new_item_list)=}!={world.pre_shuffle_pool.count(item_name)=}"

            new_items = item_factory(new_item_list, world)

            assert isinstance(
                new_items, list
            ), f"[Twilight Princess] (Any-Own Dungeon) items not a list {new_items=} {new_item_list=}"

            items.extend(new_items)

        # Sanity check
        item_name = None

        # Palace of Twilight needs arbiters grounds to be able to be commpleted
        state_copy = None
        if dungeon_name == "Palace of Twilight":
            state_copy = state.copy()
            if not state.has("Arbiters Grounds Big Key", world.player):
                state.collect(world.create_item("Arbiters Grounds Big Key"))
            if not state.has("Arbiters Grounds Small Key", world.player, 5):
                for _ in range(5):
                    state.collect(world.create_item("Arbiters Grounds Small Key"))

            if world.options.palace_requirements == PalaceRequirements.option_vanilla:
                state.collect(world.boss_defeat_items["Argorok"])
            state.sweep_for_advancements()

        elif dungeon_name == "Hyrule Castle":
            state_copy = state.copy()

            if (
                world.options.castle_requirements
                == CastleRequirements.option_all_dungeons
            ):
                for name, item in world.boss_defeat_items.items():
                    state.collect(item)
            elif world.options.castle_requirements == CastleRequirements.option_vanilla:
                state.collect(world.boss_defeat_items["Zant"])

        assert len(locations) >= len(
            items
        ), f"[Twilight Princess] (Any-Own Dungeon) There are not enough locations for items in {dungeon_name=} acording to final counts {locations=}, {items=}"

        items_copy = deepcopy(items)
        world.multiworld.random.shuffle(items_copy)
        world.multiworld.random.shuffle(locations)

        fill_restrictive(
            world.multiworld,
            state,
            locations,
            items,
            single_player_placement=True,
            lock=True,
            allow_excluded=True,
            on_place=_on_place,
        )

        # All items should be placed
        assert (
            len(items) == 0
        ), f"[Twilight Princess] (Any-Own dungeon) Not all items placed {items=}"

        # Restore state if in palace of twilight
        if state_copy:
            state = state_copy

        for item in items_copy:
            world.remove_from_pre_shuffle_pool(item.name)


def place_restricted_dungeon_items(world: "TPWorld"):

    collection_state_base = CollectionState(world.multiworld)
    for item in world.progression_pool:
        collection_state_base.collect(world.create_item(item))

    # If faron woods is closed open it so that dungeons can be accessed
    if world.options.faron_woods_logic.value == FaronWoodsLogic.option_closed:
        collection_state_base.collect(world.boss_defeat_items["Diababa"])

    if world.options.early_shadow_crystal.value == EarlyShadowCrystal.option_true:
        collection_state_base.collect(world.create_item("Shadow Crystal"))

    collection_state_base.sweep_for_advancements()

    collection_state_small_key = collection_state_base.copy()
    collection_state_big_key = collection_state_base.copy()
    collection_state_map_and_compass = collection_state_base.copy()

    # Fill collection states, b/c if small keys are in the prefill pool then they are not in the item_pool
    # and Big Keys need small keys to define access, similar for map and compass etc
    if world.options.small_key_settings.in_dungeon:
        for dungeon_name in VANILLA_SMALL_KEYS_LOCATIONS:
            for item_name in VANILLA_SMALL_KEYS_LOCATIONS[dungeon_name]:
                assert (
                    item_name in world.pre_shuffle_pool
                ), f"[Twilight Princess] {item_name=} not in prefill pool"
                for _ in range(
                    len(VANILLA_SMALL_KEYS_LOCATIONS[dungeon_name][item_name])
                ):
                    collection_state_big_key.collect(world.create_item(item_name))
                    collection_state_map_and_compass.collect(
                        world.create_item(item_name)
                    )

    if world.options.big_key_settings.in_dungeon:
        for dungeon_name in VANILLA_BIG_KEY_LOCATIONS:
            for item_name in VANILLA_BIG_KEY_LOCATIONS[dungeon_name]:
                assert (
                    item_name in world.pre_shuffle_pool
                ), f"[Twilight Princess] {item_name=} not in prefill pool"
                for _ in range(len(VANILLA_BIG_KEY_LOCATIONS[dungeon_name][item_name])):
                    collection_state_small_key.collect(
                        world.create_item(item_name)
                    )  # TODO: Check if works
                    collection_state_map_and_compass.collect(
                        world.create_item(item_name)
                    )

    # Realisticlly this is not needed
    if world.options.map_and_compass_settings.in_dungeon:
        for dungeon_name in VANILLA_MAP_AND_COMPASS_LOCATIONS:
            for item_name in VANILLA_MAP_AND_COMPASS_LOCATIONS[dungeon_name]:
                assert (
                    item_name in world.pre_shuffle_pool
                ), f"[Twilight Princess] {item_name=} not in prefill pool"
                for _ in range(
                    len(VANILLA_MAP_AND_COMPASS_LOCATIONS[dungeon_name][item_name])
                ):
                    collection_state_small_key.collect(world.create_item(item_name))
                    collection_state_big_key.collect(world.create_item(item_name))

    collection_state_small_key.sweep_for_advancements()
    collection_state_big_key.sweep_for_advancements()
    collection_state_map_and_compass.sweep_for_advancements()

    # Valdiate collection states
    for dungeon_name in VANILLA_SMALL_KEYS_LOCATIONS:
        for item_name in VANILLA_SMALL_KEYS_LOCATIONS[dungeon_name]:
            assert collection_state_big_key.has(
                item_name,
                world.player,
                len(VANILLA_SMALL_KEYS_LOCATIONS[dungeon_name][item_name]) - 1,
            ), f"[Twilight Princess] {item_name} not in big key state count={collection_state_big_key.count(item_name,world.player)}"
            assert collection_state_map_and_compass.has(
                item_name,
                world.player,
                len(VANILLA_SMALL_KEYS_LOCATIONS[dungeon_name][item_name]) - 1,
            ), f"[Twilight Princess] {item_name} not in MnC state count={collection_state_map_and_compass.count(item_name,world.player)}"

    for dungeon_name in VANILLA_BIG_KEY_LOCATIONS:
        for item_name in VANILLA_BIG_KEY_LOCATIONS[dungeon_name]:
            # TODO Figure out precollected items with this
            assert collection_state_small_key.has(
                item_name,
                world.player,
                len(VANILLA_BIG_KEY_LOCATIONS[dungeon_name][item_name]) - 1,
            ), f"[Twilight Princess] {item_name} not in small key state count={collection_state_small_key.count(item_name,world.player)}"
            assert collection_state_map_and_compass.has(
                item_name,
                world.player,
                len(VANILLA_BIG_KEY_LOCATIONS[dungeon_name][item_name]) - 1,
            ), f"[Twilight Princess] {item_name} not in MnC state count={collection_state_map_and_compass.count(item_name,world.player)}"

    for dungeon_name in VANILLA_MAP_AND_COMPASS_LOCATIONS:
        for item_name in VANILLA_MAP_AND_COMPASS_LOCATIONS[dungeon_name]:
            assert collection_state_big_key.has(
                item_name,
                world.player,
                len(VANILLA_MAP_AND_COMPASS_LOCATIONS[dungeon_name][item_name]) - 1,
            ), f"[Twilight Princess] {item_name} not in big key state count={collection_state_big_key.count(item_name,world.player)}"
            assert collection_state_small_key.has(
                item_name,
                world.player,
                len(VANILLA_MAP_AND_COMPASS_LOCATIONS[dungeon_name][item_name]) - 1,
            ), f"[Twilight Princess] {item_name} not in small key state count={collection_state_small_key.count(item_name,world.player)}"

    dungeon_name = None
    item_name = None

    if world.options.small_key_settings.value == SmallKeySettings.option_own_dungeon:
        _place_own_dungeon(
            world, collection_state_small_key, VANILLA_SMALL_KEYS_LOCATIONS
        )
    if world.options.big_key_settings.value == BigKeySettings.option_own_dungeon:
        _place_own_dungeon(world, collection_state_big_key, VANILLA_BIG_KEY_LOCATIONS)
    if (
        world.options.map_and_compass_settings.value
        == MapAndCompassSettings.option_own_dungeon
    ):
        _place_own_dungeon(
            world, collection_state_map_and_compass, VANILLA_MAP_AND_COMPASS_LOCATIONS
        )

    if world.options.small_key_settings.value == SmallKeySettings.option_any_dungeon:
        _place_any_dungeon(
            world, collection_state_small_key, VANILLA_SMALL_KEYS_LOCATIONS
        )
    if world.options.big_key_settings.value == BigKeySettings.option_any_dungeon:
        _place_any_dungeon(world, collection_state_big_key, VANILLA_BIG_KEY_LOCATIONS)
    if (
        world.options.map_and_compass_settings.value
        == MapAndCompassSettings.option_any_dungeon
    ):
        _place_any_dungeon(
            world, collection_state_map_and_compass, VANILLA_MAP_AND_COMPASS_LOCATIONS
        )

    assert (
        len(world.pre_shuffle_pool) == 0
    ), f"[Twilight Princess]aaaaaaaa missed items in pre_shuffle_pool {world.pre_shuffle_pool=}"


def place_pre_shuffled_items(world: "TPWorld"):
    place_vanilla_dungeon_items(world)
    place_vanilla_items(world)

    place_restricted_dungeon_items(world)

    assert (
        len(world.pre_shuffle_pool) == 0
    ), f"[Twilight Princess] missed items in pre_shuffle_pool {world.pre_shuffle_pool=}"
