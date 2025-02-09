from base64 import b64encode
from collections.abc import Mapping
from dataclasses import fields
import json
import os
from typing import Any, ClassVar, Dict, List, Optional, Set, Tuple

from BaseClasses import CollectionState, Item
from BaseClasses import ItemClassification as IC
from BaseClasses import MultiWorld, Tutorial
from .ClientUtils import VERSION
from .Items import ITEM_TABLE, TPItem, item_name_groups
from Options import Toggle
from .Locations import LOCATION_TABLE, LOCATION_TO_REGION, TPFlag, TPLocation
from .options import (
    BigKeySettings,
    DungeonItem,
    MapAndCompassSettings,
    SmallKeySettings,
    tp_option_groups,
    TPOptions,
)
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import (
    Component,
    SuffixIdentifier,
    Type,
    components,
    launch_subprocess,
)

from .Randomizer.ItemPool import (
    generate_itempool,
    place_deterministic_items,
)

from .Logic.Rules import set_location_access_rules
from .Logic.RegionConnection import connect_regions
from .Logic.RegionCreation import (
    create_regions,
    add_location_to_regions,
)
from .Logic.RegionRules import set_region_access_rules


def run_client() -> None:
    """
    Launch the Twilight Princess client.
    """
    print("Running Twilight Princess Client")
    from .TPClient import main

    launch_subprocess(main, name="TwilightPrincessClient")


components.append(
    Component(
        "Twilight Princess Client",
        func=run_client,
        component_type=Type.CLIENT,
        file_identifier=SuffixIdentifier(".aptp"),
    )
)


# class TPSettings(settings.Group):
#     """
#     This class handles the game settings for Twilight Princess.
#     """

#     game: str = "Twilight Princess"


class TPWeb(WebWorld):
    """
    This class handles the web interface for Twilight Princess.

    The web interface includes the setup guide and the options page for generating YAMLs.
    """

    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Archipelago Twilight Princess software on your computer.",
            "English",
            "setup_en.md",
            "setup/en",
            ["WritingHusky"],
        )
    ]
    theme = "grass"
    option_groups = tp_option_groups
    rich_text_options_doc = True


class TPWorld(World):
    """
    Join Link and Midna on their adventure through Hyrule in Twilight Princess.
    """

    # Currently using can reach region to check for access rules. may update later
    explicit_indirect_conditions = False

    options_dataclass = TPOptions
    options: TPOptions

    game: ClassVar[str] = "Twilight Princess"
    topology_present: bool = True

    item_name_to_id: ClassVar[dict[str, int]] = {
        name: TPItem.get_apid(data.code)
        for name, data in ITEM_TABLE.items()
        if data.code is not None
    }
    location_name_to_id: ClassVar[dict[str, int]] = {
        name: TPLocation.get_apid(data.code)
        for name, data in LOCATION_TABLE.items()
        if data.code is not None
    }

    item_name_groups: ClassVar[dict[str, set[str]]] = item_name_groups

    required_client_version: Tuple[int, int, int] = (0, 5, 0)

    web: ClassVar[TPWeb] = TPWeb()

    origin_region_name: str = "Menu"

    def __init__(self, *args, **kwargs):
        super(TPWorld, self).__init__(*args, **kwargs)

        # self.dungeon_local_item_names: Set[str] = set()
        # self.dungeon_specific_item_names: Set[str] = set()
        # self.dungeons: Dict[str, Dungeon] = {}

        self.nonprogress_locations: Set[str] = set()
        self.progress_locations: set[str] = set()

        self.useful_pool: list[str] = []
        self.filler_pool: list[str] = []

        self.invalid_locations: List[str] = []

        # self.boss_reqs = RequiredBossesRandomizer(self)

    def _determine_nonprogress_and_progress_locations(
        self,
    ) -> tuple[set[str], set[str]]:

        def add_flag(option: Toggle, flag: TPFlag) -> TPFlag:
            return flag if option else TPFlag.Always

        options = self.options

        enabled_flags = TPFlag.Always
        enabled_flags |= add_flag(options.golden_bugs_shuffled, TPFlag.Bug)
        enabled_flags |= add_flag(options.shop_items_shuffled, TPFlag.Shop)
        enabled_flags |= add_flag(options.sky_characters_shuffled, TPFlag.Sky_Book)
        enabled_flags |= add_flag(options.poe_shuffled, TPFlag.Poe)
        enabled_flags |= add_flag(options.npc_items_shuffled, TPFlag.Npc)
        enabled_flags |= add_flag(options.hidden_skills_shuffled, TPFlag.Skill)
        enabled_flags |= add_flag(options.heart_piece_shuffled, TPFlag.Heart)
        enabled_flags |= add_flag(options.overworld_shuffled, TPFlag.Overworld)
        enabled_flags |= add_flag(options.dungeons_shuffled, TPFlag.Dungeon)

        # If not all the flags for a location are set, then force that location to have a non-progress item.
        nonprogress_locations: Set[str] = set()
        progress_locations: set[str] = set()

        for location, data in LOCATION_TABLE.items():
            if data.flags & enabled_flags == data.flags:
                progress_locations.add(location)
            else:
                nonprogress_locations.add(location)

        assert progress_locations.isdisjoint(nonprogress_locations)

        return nonprogress_locations, progress_locations

    # Start of generation Process -----------------------------------------------------------------------

    # stage_assert_generate() not used currently

    def generate_early(self) -> None:
        """
        Setup things ready for generation.
        """
        # Early into generation, set the options for the keys and map/compass.
        options = self.options

        self.nonprogress_locations, self.progress_locations = (
            self._determine_nonprogress_and_progress_locations()
        )

        # if dungeons are not progression, then keys should be vanilla
        # if not options.dungeons_shuffled:
        #     options.small_key_settings.value = SmallKeySettings.option_vanilla
        #     options.big_key_settings.value = BigKeySettings.option_vanilla
        #     options.map_and_compass_settings.value = (
        #         MapAndCompassSettings.option_vanilla
        #     )

        # Here we assign dungeon items (Keys, Map, Compass) to the dungeon pools.
        # for dungeon_item in [
        #     "small_key_settings",
        #     "big_key_settings",
        #     "map_and_compass_settings",
        # ]:
        #     option = getattr(options, dungeon_item)
        #     if option.value == DungeonItem.option_keysy:
        #         options.local_items.value |= self.item_name_to_id[
        #             option.item_name_group
        #         ]
        #     # If dungeon items are randomized in the local world.
        #     elif option.in_dungeon:
        #         # Add them to the local item pool.
        #         self.dungeon_local_item_names |= self.item_name_groups[
        #             option.item_name_group
        #         ]
        #         # If items are to be in own dungeon
        #         if option == DungeonItem.option_own_dungeon:
        #             self.dungeon_specific_item_names |= self.item_name_groups[
        #                 option.item_name_group
        #             ]
        #         # If items are to be in any dungeon
        #         elif option == DungeonItem.option_any_dungeon:
        #             self.options.local_items.value |= self.dungeon_local_item_names

    # create_dungeons = create_dungeons

    # TODO
    def create_regions(self) -> None:
        """
        Create and connect regions for the Twilight Princess world.

        This method first creates all the regions and adds the locations to them.
        Then it connects the regions to each other.


        This method first randomizes the charts and picks the required bosses if these options are enabled.
        It then loops through all the world's progress locations and creates the locations, assigning dungeon locations
        to their respective dungeons.
        Finally, the flags for sunken treasure locations are updated as appropriate, and the entrances are randomized
        if that option is enabled.
        """
        # Here we will call region creation and connection
        # This will create the regions, connect them and put the locations in them.

        # This adds all the regions and assingns the locations to them. (build vertices)
        create_regions(self.multiworld, self.player)
        # create_portal_location(
        #     self.multiworld, self.player
        # )  # This adds the portal locations to the regions. address None so only for logic
        # This connects all the regions to each other. (build edges)

        connect_regions(self.multiworld, self.player)

        # Debug to catch if all locations are caught TODO: Remove debug
        if len(self.progress_locations) + len(self.nonprogress_locations) != len(
            LOCATION_TABLE.items()
        ):
            locations_set = set(LOCATION_TABLE.keys())
            locations_set.difference_update(self.progress_locations)
            locations_set.difference_update(self.nonprogress_locations)
            if len(locations_set) > 0:
                raise RuntimeError(
                    f"location(s) dropped from the locations lists {locations_set=}"
                )

        # Place progess locations in their locations
        for location in self.progress_locations:
            add_location_to_regions(
                self.multiworld, self.player, LOCATION_TO_REGION[location], location
            )
        # print(f"{self.progress_locations}")

        # Create_items

    def create_items(self) -> None:
        """
        Create the items for the Twilight Princess world.
        """
        # First Items with deterministic locations are placed (mostly for logic in generation)
        place_deterministic_items(self)

        # Get the number of locations that have not been filled yet (So we can fill the itempool with filler items)
        location_count = len(
            [
                location
                for location in self.multiworld.get_locations(self.player)
                if location.address is not None and location.item is None
            ]
        )

        # This fills the itempool with items according to the location count (any precollected items are pushed to precollected_items)
        generate_itempool(self, location_count)

    # No more items, locations, or regions can be created past this point

    # set_rules() this is where access rules are set
    def set_rules(self) -> None:
        """
        Set the access rules for the Twilight Princess world.
        """
        set_region_access_rules(self, self.player)
        set_location_access_rules(self)

    # generate_basic() This is where player specific randomization that does not affect logic is done

    def pre_fill(self) -> None:
        """
        Apply special fill rules before the fill stage.
        """
        # For the MVP, we will not be pre-filling anything.

        # Ban the Bait Bag slot from having bait.
        # if "The Great Sea - Beedle's Shop Ship - 20 Rupee Item" in self.progress_locations:
        #     beedle_20 = self.get_location("The Great Sea - Beedle's Shop Ship - 20 Rupee Item")
        #     add_item_rule(beedle_20, lambda item: item.name not in ["All-Purpose Bait", "Hyoi Pear"])
        #
        # # Also, the same item should not appear more than once on the Rock Spire Isle shop ship.
        # locations = [f"Rock Spire Isle - Beedle's Special Shop Ship - {v} Rupee Item" for v in [500, 950, 900]]
        # if all(loc in self.progress_locations for loc in locations):
        #     rock_spire_shop_ship_locations = [self.get_location(location_name) for location_name in locations]
        #
        #     for i in range(len(rock_spire_shop_ship_locations)):
        #         curr_loc = rock_spire_shop_ship_locations[i]
        #         other_locs = rock_spire_shop_ship_locations[:i] + rock_spire_shop_ship_locations[i + 1:]
        #
        #         add_item_rule(
        #             curr_loc,
        #             lambda item, locations=other_locs: (
        #                                                        item.game == "Twilight Princess"
        #                                                        and all(
        #                                                    location.item is None or item.name != location.item.name for
        #                                                    location in locations)
        #                                                )
        #                                                or (
        #                                                        item.game != "Twilight Princess"
        #                                                        and all(
        #                                                    location.item is None or location.item.game == "Twilight Princess"
        #                                                    for location in locations
        #                                                )
        #                                                ),
        #         )

    @classmethod
    def stage_pre_fill(cls, world: MultiWorld) -> None:
        """
        Class method used to correctly place dungeon items for Twilight Princess worlds.

        :param world: The MultiWorld.
        """
        # from .Randomizer.Dungeons import fill_dungeons_restrictive

        # fill_dungeons_restrictive(world)

    def generate_output(self, output_directory: str) -> None:
        """
        Create the output APTP file that is used to randomize the GCI.

        :param output_directory: The output directory for the APTP file.
        """
        multiworld = self.multiworld
        player = self.player

        # Output seed name and slot number to seed RNG in randomizer client.
        output_data = {
            "Version": VERSION,
            "Seed": multiworld.seed_name,
            "Slot": player,
            "Name": self.player_name,
            "Options": {},
            # "Required Bosses": self.boss_reqs.required_boss_item_locations,
            "Locations": {},
            "Entrances": {},
        }

        # Output relevant options to file.
        for field in fields(self.options):
            output_data["Options"][field.name] = getattr(self.options, field.name).value

        # Output which item has been placed at each location.
        # locations = multiworld.get_locations(player)
        # for location in locations:
        #     if location.name:
        #         if location.item:
        #             item_info = {
        #                 "player": location.item.player,
        #                 "name": location.item.name,
        #                 "game": location.item.game,
        #                 "classification": location.item.classification.name,
        #             }
        #         else:
        #             item_info = {
        #                 "name": "Nothing",
        #                 "game": "Twilight Princess",
        #                 "classification": "filler",
        #             }
        #         output_data["Locations"][location.name] = item_info

        output_data["InvalidLocations"] = self.invalid_locations
        output_data["UsefulPool"] = self.useful_pool
        output_data["FillerPool"] = self.filler_pool

        #
        # # Output the mapping of entrances to exits.
        # all_entrance_names = [en.entrance_name for en in ALL_ENTRANCES]
        # entrances = multiworld.get_entrances(player)
        # for entrance in entrances:
        #     assert entrance.parent_region is not None
        #     if entrance.parent_region.name in all_entrance_names:
        #         assert entrance.connected_region is not None
        #         output_data["Entrances"][entrance.parent_region.name] = entrance.connected_region.name

        def custom_serializer(obj):
            if hasattr(obj, "__dict__"):
                return obj.__dict__
            return str(obj)

        # Output the plando details to file.
        file_path = os.path.join(
            output_directory, f"{multiworld.get_out_file_name_base(player)}.aptp"
        )
        with open(file_path, "w") as f:
            f.write(json.dumps(output_data, indent=4, default=custom_serializer))

    def extend_hint_information(self, hint_data: dict[int, dict[int, str]]) -> None:
        """
        Fill in additional information text into locations, displayed when hinted.

        :param hint_data: A dictionary of mapping a player ID to a dictionary mapping location IDs to the extra hint
        information text. This dictionary should be modified as a side-effect of this method.
        """
        # Build out the hint data for this player. by telling them where each location is.
        # Regardless of ER settings, always hint the outermost entrance for every "interior" location
        hint_data[self.player] = {}
        for location in self.multiworld.get_locations(self.player):
            if location.address is not None and location.item is not None:
                assert location.stage_id is not None
                hint_data[self.player][location.address] = location.stage_id.name

    # Overides the base classification of an item if not None
    def determine_item_classification(self, name: str) -> IC | None:
        # TODO: calculate nonprogress items dynamically

        adjusted_classification = None
        if not self.options.golden_bugs_shuffled and name in item_name_groups["Bugs"]:
            adjusted_classification = IC.filler
        elif (
            not self.options.sky_characters_shuffled
            and name == "Progressive Ancient Sky Book"
        ):
            adjusted_classification = IC.filler
        elif (
            not self.options.npc_items_shuffled
            and name in item_name_groups["NPC Items"]
        ):
            adjusted_classification = IC.filler
        elif (
            not self.options.shop_items_shuffled
            and name in item_name_groups["Shop Items"]
        ):
            adjusted_classification = IC.filler
        # elif (
        #     not self.options.hidden_skills_shuffled
        #     and name == "Progressive Hidden Skill"
        # ):
        #     adjusted_classification = IC.filler
        elif not self.options.poe_shuffled and name == "Poe Soul":
            adjusted_classification = IC.filler
        elif (
            not self.options.overworld_shuffled
            and name in item_name_groups["Overworld Items"]
        ):
            adjusted_classification = IC.filler
        elif (
            not self.options.heart_piece_shuffled and name in item_name_groups["Heart"]
        ):
            adjusted_classification = IC.filler

        return adjusted_classification

    def create_item(self, name: str) -> TPItem:
        """
        Create an item for this world type and player.

        :param name: The name of the item to create.
        :raises KeyError: If an invalid item name is provided.
        """
        if name in ITEM_TABLE:
            return TPItem(
                name,
                self.player,
                ITEM_TABLE[name],
                self.determine_item_classification(name),
            )
        raise KeyError(f"Invalid item name: {name}")

    def get_filler_item_name(self) -> str:
        """
        This method is called when the item pool needs to be filled with additional items to match the location count.

        :return: The name of a filler item from this world.
        """

        # If there are still useful items to place, place those first.
        if len(self.useful_pool) > 0:
            return self.useful_pool.pop()

        # If there are still vanilla filler items to place, place those first.
        if len(self.filler_pool) > 0:
            return self.filler_pool.pop()

        # Use the same weights for filler items used in the base randomizer.
        filler_consumables = [
            "Green Rupee",
            "Blue Rupee",
            "Yellow Rupee",
            "Red Rupee",
            "Purple Rupee",
            "Orange Rupee",
            "Silver Rupee",
            # "Arrows (10)",
            "Arrows (20)",
            "Arrows (30)",
            "Seeds (50)",
            # "Bombs (5)",
            # "Bombs (10)",
            "Bombs (20)",
            "Bombs (30)",
            # "Bomblings (3)",
            # "Bomblings (5)",
            "Bomblings (10)",
            # "Water Bombs (3)",
            # "Water Bombs (5)",
            "Water Bombs (10)",
            "Ice Trap",
        ]
        filler_weights = [
            1,  # Green Rupee
            2,  # Blue Rupee
            3,  # Yellow Rupee
            3,  # Red Rupee
            2,  # Purple Rupee
            1,  # Orange Rupee
            1,  # Silver Rupee
            # 1,  # Arrows 10
            2,  # Arrows 20
            1,  # Arrows 30
            1,  # Seeds 50
            # 1,  # Bombs 5
            # 2,  # Bombs 10
            2,  # Bombs 20
            1,  # Bombs 30
            # 1,  # Bomblings 3
            # 2,  # Bomblings 5
            1,  # Bomblings 10
            # 1,  # Water Bombs 3
            # 2,  # Water Bombs 5
            2,  # Water Bombs 10
            1,  # Ice Trap
        ]
        return self.multiworld.random.choices(
            filler_consumables, weights=filler_weights, k=1
        )[0]

    def get_pre_fill_items(self) -> list[Item]:
        """
        Return items that need to be collected when creating a fresh `all_state` but don't exist in the multiworld's
        item pool.

        :return: A list of pre-fill items.
        """
        # Dungeon Items need to be pre-filled to ensure that the dungeons are filled with the correct items.
        res = []
        # if self.dungeon_local_item_names:
        #     for dungeon in self.dungeons.values():
        #         for item in dungeon.all_items:
        #             if item.name in self.dungeon_local_item_names:
        #                 res.append(item)
        return res

    def fill_slot_data(self) -> Mapping[str, Any]:
        """
        Return the `slot_data` field that will be in the `Connected` network package.

        This is a way the generator can give custom data to the client.
        The client will receive this as JSON in the `Connected` response.

        :return: A dictionary to be sent to the client when it connects to the server.
        """
        slot_data = {"World Version": VERSION}

        return slot_data

    def collect_item(
        self, state: "CollectionState", item: "Item", remove: bool = False
    ) -> Optional[str]:
        """
        Collect an item name into state. For speed reasons items that aren't logically useful get skipped.
        Collect None to skip item.
        :param state: CollectionState to collect into
        :param item: Item to decide on if it should be collected into state
        :param remove: indicate if this is meant to remove from state instead of adding.
        """
        if item.advancement:
            return item.name
        return None
