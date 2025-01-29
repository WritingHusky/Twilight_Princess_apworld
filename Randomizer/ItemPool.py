from typing import TYPE_CHECKING, Dict, List, Tuple

from BaseClasses import ItemClassification

from ..Items import ITEM_TABLE, TPItem, TPItemData, item_factory

# from ..Options import DungeonItem
# from .Dungeons import get_dungeon_item_pool_player

if TYPE_CHECKING:
    from .. import TPWorld

VANILLA_DUNGEON_ITEM_LOCATIONS: Dict[str, List[str]] = {
    "Forest Temple Small Key": [
        "Forest Temple Big Baba Key",
        "Forest Temple North Deku Like Chest",
        "Forest Temple Totem Pole Chest",
        "Forest Temple Windless Bridge Chest",
    ],
    "Goron Mines Small Key": [
        "Goron Mines Main Magnet Room Bottom Chest",
        "Goron Mines Crystal Switch Room Underwater Chest",
        "Goron Mines Outside Beamos Chest",
    ],
    "Lakebed Temple Small Key": [
        "Lakebed Temple Before Deku Toad Alcove Chest",
        "Lakebed Temple East Lower Waterwheel Stalactite Chest",
        "Lakebed Temple East Second Floor Southeast Chest",
    ],
    "Arbiter's Grounds Small Key": [
        "Arbiters Grounds Entrance Chest",
        "Arbiters Grounds East Lower Turnable Redead Chest",
        "Arbiters Grounds East Upper Turnable Redead Chest",
        "Arbiters Grounds Ghoul Rat Room Chest",
        "Arbiters Grounds North Turning Room Chest",
    ],
    "Snowpeak Ruins Small Key": [
        "Snowpeak Ruins East Courtyard Chest",
        "Snowpeak Ruins West Courtyard Buried Chest",
        "Snowpeak Ruins Wooden Beam Chandelier Chest",
        "Snowpeak Ruins Northeast Chandelier Chest",
    ],
    "Temple of Time Small Key": [
        "Temple of Time Lobby Lantern Chest",
        "Temple of Time Armos Antechamber East Chest",
        "Temple of Time Gilloutine Chest",
    ],
    "City in the Sky Small Key": [
        "City in The Sky West Wing First Chest",
    ],
    "Palace of Twilight Small Key": [
        "Palace of Twilight West Wing First Room Central Chest",
        "Palace of Twilight West Wing Second Room Central Chest",
        "Palace of Twilight East Wing First Room Zant Head Chest",
        "Palace of Twilight East Wing Second Room Southeast Chest",
        "Palace of Twilight Central Tower Chest",
        "Palace of Twilight Central Outdoor Chest",
        "Palace of Twilight Central First Room Chest",
    ],
    "Hyrule Castle Small Key": [
        "Hyrule Castle King Bulblin Key",
        "Hyrule Castle Graveyard Owl Statue Chest",
        "Hyrule Castle Southeast Balcony Tower Chest",
    ],
    "Forest Temple Big Key": [
        "Forest Temple Big Key Chest",
    ],
    "Goron Mines Key Shard": [
        "Goron Mines Gor Amato Key Shard",
        "Goron Mines Gor Ebizo Key Shard",
        "Goron Mines Gor Liggs Key Shard",
    ],
    "Lakebed Temple Big Key": [
        "Lakebed Temple Big Key Chest",
    ],
    "Arbiter's Grounds Big Key": [
        "Arbiters Grounds Big Key Chest",
    ],
    "Bedroom Key": [
        "Snowpeak Ruins Chapel Chest",
    ],
    "Temple of Time Big Key": [
        "Temple of Time Big Key Chest",
    ],
    "City in the Sky Big Key": [
        "City in The Sky Big Key Chest",
    ],
    "Palace of Twilight Big Key": [
        "Palace of Twilight Big Key Chest",
    ],
    "Hyrule Castle Big Key": [
        "Hyrule Castle Big Key Chest",
    ],
    "Forest Temple Map": [
        "Forest Temple Central North Chest",
    ],
    "Goron Mines Map": [
        "Goron Mines Gor Amato Chest",
    ],
    "Lakebed Temple Map": [
        "Lakebed Temple Central Room Chest",
    ],
    "Arbiter's Grounds Map": [
        "Arbiters Grounds Torch Room West Chest",
    ],
    "Snowpeak Ruins Map": [
        "Snowpeak Ruins Mansion Map",
    ],
    "Temple of Time Map": [
        "Temple of Time First Staircase Armos Chest",
    ],
    "City in the Sky Map": [
        "City in The Sky East First Wing Chest After Fans",
    ],
    "Palace of Twilight Map": [
        "Palace of Twilight East Wing Second Room Southwest Chest",
    ],
    "Hyrule Castle Map": [
        "Hyrule Castle East Wing Boomerang Puzzle Chest",
    ],
    "Forest Temple Compass": [
        "Forest Temple Central Chest Hanging From Web",
    ],
    "Goron Mines Compass": [
        "Goron Mines Beamos Room Chest",
    ],
    "Lakebed Temple Compass": [
        "Lakebed Temple West Water Supply Chest",
    ],
    "Arbiter's Grounds Compass": [
        "Arbiters Grounds East Upper Turnable Chest",
    ],
    "Snowpeak Ruins Compass": [
        "Snowpeak Ruins Wooden Beam Northwest Chest",
    ],
    "Temple of Time Compass": [
        "Temple of Time Moving Wall Beamos Room Chest",
    ],
    "City in the Sky Compass": [
        "City in The Sky East Wing Lower Level Chest",
    ],
    "Palace of Twilight Compass": [
        "Palace of Twilight West Wing Second Room Lower South Chest",
    ],
    "Hyrule Castle Compass": [
        "Hyrule Castle Main Hall Northeast Chest",
    ],
}


# This takes all the items form the world and adds them to the multiworld itempool
def generate_itempool(world: "TPWorld", location_count: int) -> None:
    multiworld = world.multiworld

    # Get the core pool of items.
    pool, precollected_items = get_pool_core(world, location_count)

    # Add precollected items to the multiworld's `precollected_items` list.
    for item in precollected_items:
        multiworld.push_precollected(item_factory(item, world))

    # Create the pool of the remaining shuffled items.
    items = item_factory(pool, world)
    multiworld.random.shuffle(items)

    multiworld.itempool += items


# This gets all the items from the world and
def get_pool_core(world: "TPWorld", location_count: int) -> Tuple[List[str], List[str]]:
    pool: List[str] = []
    precollected_items: List[str] = []
    n_pending_junk: int = location_count

    # Add regular items to the item pool.
    for item, data in ITEM_TABLE.items():
        if data.classification != ItemClassification.filler and item != "Victory":
            pool.extend([item] * data.quantity)
            n_pending_junk -= data.quantity

    # TODO: Precollected items and filler items

    # Place filler items ensure that the pool has the correct number of items.
    pool.extend([world.get_filler_item_name() for _ in range(n_pending_junk)])

    return pool, precollected_items


def place_deterministic_items(world: "TPWorld") -> None:
    """This function places items that are: Not shuffled, only part of logic, or are used for the spoiler log."""

    # Place a "Victory" item on "Defeat Ganondorf" for the spoiler log.
    world.get_location("Hyrule Castle Ganondorf").place_locked_item(
        item_factory("Victory", world)
    )

    # Place a Boss Defeated item on the boss rooms
    world.get_location("Forest Temple Diababa").place_locked_item(
        TPItem(
            "Diababa Defeated",
            world.player,
            TPItemData(
                code=None,
                type="Boss Defeated",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Goron Mines Fyrus").place_locked_item(
        TPItem(
            "Fyrus Defeated",
            world.player,
            TPItemData(
                code=None,
                type="Boss Defeated",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Lakebed Temple Morpheel").place_locked_item(
        TPItem(
            "Morpheel Defeated",
            world.player,
            TPItemData(
                code=None,
                type="Boss Defeated",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Arbiters Grounds Stallord").place_locked_item(
        TPItem(
            "Stallord Defeated",
            world.player,
            TPItemData(
                code=None,
                type="Boss Defeated",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Snowpeak Ruins Blizzeta").place_locked_item(
        TPItem(
            "Blizzeta Defeated",
            world.player,
            TPItemData(
                code=None,
                type="Boss Defeated",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Temple of Time Armogohma").place_locked_item(
        TPItem(
            "Armogohma Defeated",
            world.player,
            TPItemData(
                code=None,
                type="Boss Defeated",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("City in The Sky Argorok").place_locked_item(
        TPItem(
            "Argorok Defeated",
            world.player,
            TPItemData(
                code=None,
                type="Boss Defeated",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Palace of Twilight Zant").place_locked_item(
        TPItem(
            "Zant Defeated",
            world.player,
            TPItemData(
                code=None,
                type="Boss Defeated",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )

    # Manually place items that cannot be randomized yet.
    # These are still items post generation, but are not shuffled (yet?). (this means getting them will fire a message?)
    world.get_location("Renados Letter").place_locked_item(
        TPItem(
            "Renado's Letter",
            world.player,
            TPItemData(
                code=None,
                type="Quest",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Telma Invoice").place_locked_item(
        TPItem(
            "Invoice",
            world.player,
            TPItemData(
                code=None,
                type="Quest",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Wooden Statue").place_locked_item(
        TPItem(
            "Wooden Statue",
            world.player,
            TPItemData(
                code=None,
                type="Quest",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Ilia Charm").place_locked_item(
        TPItem(
            "Ilia's Charm",
            world.player,
            TPItemData(
                code=None,
                type="Quest",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location(  # TODO: Maybe change this to a different item?
        "Ilia Memory Reward"
    ).place_locked_item(item_factory("Horse Call", world))

    # Portal items are used only for logic, so we can place them here.
    # TODO: Set portal location here as well as the item.?
    world.get_location("Ordon Spring Portal").place_locked_item(
        TPItem(
            "Ordon Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("North Faron Portal").place_locked_item(
        TPItem(
            "North Faron Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("South Faron Portal").place_locked_item(
        TPItem(
            "South Faron Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Kakariko Gorge Portal").place_locked_item(
        TPItem(
            "Kakariko Gorge Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Kakariko Village Portal").place_locked_item(
        TPItem(
            "Kakariko Village Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Death Mountain Portal").place_locked_item(
        TPItem(
            "Death Mountain Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Castle Town Portal").place_locked_item(
        TPItem(
            "Castle Town Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Zoras Domain Portal").place_locked_item(
        TPItem(
            "Zoras Domain Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Lake Hylia Portal").place_locked_item(
        TPItem(
            "Lake Hylia Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Gerudo Desert Portal").place_locked_item(
        TPItem(
            "Gerudo Desert Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Mirror Chamber Portal").place_locked_item(
        TPItem(
            "Mirror Chamber Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Snowpeak Portal").place_locked_item(
        TPItem(
            "Snowpeak Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Sacred Grove Portal").place_locked_item(
        TPItem(
            "Sacred Grove Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Bridge of Eldin Portal").place_locked_item(
        TPItem(
            "Bridge of Eldin Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
    world.get_location("Upper Zoras River Portal").place_locked_item(
        TPItem(
            "Upper Zoras River Portal",
            world.player,
            TPItemData(
                code=None,
                type="Portal",
                quantity=1,
                classification=ItemClassification.progression,
                item_id=1,
            ),
        )
    )
