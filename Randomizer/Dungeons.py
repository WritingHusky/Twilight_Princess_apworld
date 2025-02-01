from typing import TYPE_CHECKING, Any, List, Optional, Set, Tuple

from BaseClasses import CollectionState, Location, MultiWorld
from Fill import fill_restrictive
from ..Items import TPItem, item_factory

if TYPE_CHECKING:
    from .. import TPWorld


class Dungeon:
    def __init__(
        self,
        name: str,
        big_key: Optional[TPItem],
        small_keys: List[TPItem],
        dungeon_items: List[TPItem],
        player: int,
    ):
        self.name = name
        self.big_key = big_key
        self.small_keys = small_keys
        self.dungeon_items = dungeon_items
        self.player = player

    @property
    def keys(self) -> List[TPItem]:
        return self.small_keys + ([self.big_key] if self.big_key else [])

    @property
    def all_items(self) -> List[TPItem]:
        return self.dungeon_items + self.keys

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Dungeon):
            return self.name == other.name and self.player == other.player
        return False

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.name} (Player {self.player})"


def create_dungeons(world: "TPWorld") -> None:
    player = world.player

    def make_dungeon(
        name: str,
        big_key: Optional[TPItem],
        small_keys: List[TPItem],
        dungeon_items: List[TPItem],
    ) -> Dungeon:
        dungeon = Dungeon(name, big_key, small_keys, dungeon_items, player)
        for item in dungeon.all_items:
            item.dungeon = dungeon
        return dungeon

    FT = make_dungeon(
        "Forest Temple",
        item_factory("Forest Temple Big Key", world),
        item_factory(["Forest Temple Small Key"] * 4, world),
        item_factory(["Forest Temple Dungeon Map", "Forest Temple Compass"], world),
    )
    GM = make_dungeon(
        "Goron Mines",
        item_factory(["Goron Mines Key Shard"] * 3, world),
        item_factory(["Goron Mines Small Key"] * 3, world),
        item_factory(["Goron Mines Dungeon Map", "Goron Mines Compass"], world),
    )
    LBT = make_dungeon(
        "Lakebed Temple",
        item_factory("Lakebed Temple Big Key", world),
        item_factory(["Lakebed Temple Small Key"] * 3, world),
        item_factory(["Lakebed Temple Dungeon Map", "Lakebed Temple Compass"], world),
    )
    AG = make_dungeon(
        "Arbiters Grounds",
        item_factory("Arbiters Grounds Big Key", world),
        item_factory(["Arbiters Grounds Small Key"] * 5, world),
        item_factory(
            ["Arbiters Grounds Dungeon Map", "Arbiters Grounds Compass"], world
        ),
    )
    SPR = make_dungeon(
        "Snowpeak Ruins",
        item_factory("Snowpeak Ruins Bedroom Key", world),
        item_factory(["Snowpeak Ruins Small Key"] * 4, world),
        item_factory(["Snowpeak RUins Dungeon Map", "Snowpeak Ruins Compass"], world),
    )
    ToT = make_dungeon(
        "Temple of Time",
        item_factory("Temple of Time Big Key", world),
        item_factory(["Temple of Time Small Key"] * 3, world),
        item_factory(["Temple of Time Dungeon Map", "Temple of Time Compass"], world),
    )
    CiTS = make_dungeon(
        "City in The Sky",
        item_factory("City in The Sky Big Key", world),
        item_factory(["City in The Sky Small Key"] * 1, world),
        item_factory(["City in The Sky Dungeon Map", "City in The Sky Compass"], world),
    )
    PoT = make_dungeon(
        "Palace of Twilight",
        item_factory("Palace of Twilight Big Key", world),
        item_factory(["Palace of Twilight Small Key"] * 7, world),
        item_factory(
            ["Palace of Twilight Dungeon Map", "Palace of Twilight Compass"], world
        ),
    )
    HC = make_dungeon(
        "Hyrule Castle",
        item_factory("Hyrule Castle Big Key", world),
        item_factory(["Hyrule Castle Small Key"] * 3, world),
        item_factory(["Hyrule Castle Dungeon Map", "Hyrule Castle Compass"], world),
    )

    for dungeon in [FT, GM, LBT, AG, SPR, ToT, CiTS, PoT, HC]:
        world.dungeons[dungeon.name] = dungeon


def get_dungeon_item_pool(multiworld: MultiWorld) -> List[TPItem]:
    return [
        item
        for world in multiworld.get_game_worlds("Twilight Princess")
        for item in get_dungeon_item_pool_player(world)
    ]


def get_dungeon_item_pool_player(world: "TPWorld") -> List[TPItem]:
    return [item for dungeon in world.dungeons.values() for item in dungeon.all_items]


def get_unfilled_dungeon_locations(multiworld: MultiWorld) -> List[Location]:
    return [
        location
        for world in multiworld.get_game_worlds("Twilight Princess")
        for location in multiworld.get_locations(world.player)
        if location.dungeon and not location.item
    ]


def modify_dungeon_location_rules(
    locations: List[Location], dungeon_specific: Set[Tuple[int, str]]
) -> None:
    for location in locations:
        orig_rule = location.item_rule
        if dungeon_specific:
            # Restrict dungeon items to be in their own dungeons.
            dungeon = location.dungeon
            location.item_rule = lambda item, dungeon=dungeon, orig_rule=orig_rule: (
                not (item.player, item.name) in dungeon_specific
                or item.dungeon is dungeon
            ) and orig_rule(item)
        else:
            # Restrict dungeon items to be in any dungeon in the player's local world.
            player = location.player
            location.item_rule = lambda item, player=player, orig_rule=orig_rule: (
                item.player == player
            ) and orig_rule(item)


def fill_dungeons_restrictive(multiworld: MultiWorld) -> None:
    localized: Set[Tuple[int, str]] = set()
    dungeon_specific: Set[Tuple[int, str]] = set()
    for subworld in multiworld.get_game_worlds("Twilight Princess"):
        player = subworld.player
        if player not in multiworld.groups:
            localized |= {
                (player, item_name) for item_name in subworld.dungeon_local_item_names
            }
            dungeon_specific |= {
                (player, item_name)
                for item_name in subworld.dungeon_specific_item_names
            }

    if localized:
        in_dungeon_items = [
            item
            for item in get_dungeon_item_pool(multiworld)
            if (item.player, item.name) in localized
        ]
        if in_dungeon_items:
            locations = [
                location for location in get_unfilled_dungeon_locations(multiworld)
            ]
            modify_dungeon_location_rules(locations, dungeon_specific)

            multiworld.random.shuffle(locations)

            # Dungeon-locked items have to be placed first, to not run out of spaces for dungeon-locked items.
            # Subsort in the order Small Key, Big Key, Other before placing dungeon items.
            sort_order = {"Small Key": 3, "Big Key": 2}
            in_dungeon_items.sort(
                key=lambda item: sort_order.get(item.type, 1)
                + (5 if (item.player, item.name) in dungeon_specific else 0),
                reverse=True,
            )

            # Construct a partial `all_state` which contains only the items from `get_pre_fill_items`, which aren't
            # in a dungeon.
            in_dungeon_player_ids = {item.player for item in in_dungeon_items}
            all_state_base = CollectionState(multiworld)
            for item in multiworld.itempool:
                multiworld.worlds[item.player].collect(all_state_base, item)
            pre_fill_items = []
            for player in in_dungeon_player_ids:
                pre_fill_items += multiworld.worlds[player].get_pre_fill_items()
            for item in in_dungeon_items:
                try:
                    pre_fill_items.remove(item)
                except ValueError:
                    # `pre_fill_items` should be a subset of `in_dungeon_items`, but just in case.
                    pass
            for item in pre_fill_items:
                multiworld.worlds[item.player].collect(all_state_base, item)
            all_state_base.sweep_for_events()

            # Remove completion condition so that minimal-accessibility worlds place keys properly.
            for player in (item.player for item in in_dungeon_items):
                if all_state_base.has("Victory", player):
                    all_state_base.remove(
                        multiworld.worlds[player].create_item("Victory")
                    )

            fill_restrictive(
                multiworld,
                all_state_base,
                locations,
                in_dungeon_items,
                lock=True,
                allow_excluded=True,
                name="TP Dungeon Items",
            )
