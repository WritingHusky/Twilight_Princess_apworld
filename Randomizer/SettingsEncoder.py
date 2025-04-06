from BaseClasses import Item, MultiWorld
from ..Locations import LOCATION_TABLE, TPLocation

char_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"

# Based off of:
# https://github.com/lunarsoap5/Randomizer-Web-Generator-1/blob/9a5f38e972669209f3d21596b0a9744f1319412f/Generator/Logic/SeedGenResults.cs#L130

FILLER_ITEM_CODE = 0x8F


def get_item_placements(multiworld: MultiWorld, player: int) -> str:
    assert isinstance(multiworld, MultiWorld)
    assert isinstance(player, int)

    location_number_to_item_code: dict[int, int] = {}

    for location in multiworld.get_locations(player):
        assert isinstance(location, TPLocation)
        assert isinstance(location.item, Item), f"{location.name}, {location.item}"

        # Ignore event locations
        if not isinstance(location.code, int):
            continue

        # If item is local then encode it as
        if location.item.player == player:
            location_number_to_item_code[location.code] = location.item.code
        else:
            location_number_to_item_code[location.code] = FILLER_ITEM_CODE

    # All locations that ap tracks are given a number and an item (ignore Story locations, Logic Event locations)
    assert len(location_number_to_item_code) == len(
        [
            location
            for location in multiworld.get_locations(player)
            # Filer
            if isinstance(location.address, int)
        ]
    ), f"{len(location_number_to_item_code)},{len(multiworld.get_locations(player))}"

    result = encode_item_placements(location_number_to_item_code)
    assert isinstance(result, str)

    return result


def encode_item_placements(check_num_id_to_item_id: dict[int, int]):

    def encode_num_as_bits(num: int, num_bits: int):
        """Encodes a number as a bit string of a specified length."""
        return bin(num)[2:].zfill(num_bits)

    # version = 0
    result = encode_as_vlq16(0)

    if not check_num_id_to_item_id:
        result += "0"
        return encode_as_6_bit_string(result)

    result += "1"

    smallest = next(iter(check_num_id_to_item_id))  # Get the first key (0)
    assert smallest == 0
    largest = next(reversed(check_num_id_to_item_id))  # Get the last key (474)
    assert largest == 474

    result += encode_num_as_bits(smallest, 9)
    result += encode_num_as_bits(largest, 9)

    item_bits = ""

    for i in range(smallest, largest + 1):
        if i in check_num_id_to_item_id:
            result += "1"
            item_bits += encode_num_as_bits(check_num_id_to_item_id[i], 8)
        else:
            result += "0"

    result += item_bits

    return encode_as_6_bit_string(result)


def encode_as_vlq16(num: int):
    assert isinstance(num, int)

    def get_vlq16_bit_length(n: int):
        """Helper function to determine the bit length needed for the VLQ16 encoding."""
        if n < 2:
            return 5
        return (
            1 + n.bit_length()
        )  # Equivalent to log2(n) + 1, but avoids floating-point calculations

    if num < 2:
        return "0000" + bin(num)[2:].zfill(1)

    bits_needed = get_vlq16_bit_length(num) - 1

    return bin(bits_needed)[2:].zfill(4) + bin(num)[2:].zfill(16)[1:]


def encode_as_6_bit_string(bit_string: str):
    assert isinstance(bit_string, str), f"{bit_string=}"
    # if not bit_string:
    #     return ""

    remainder = len(bit_string) % 6
    if remainder > 0:
        bit_string += "0" * (6 - remainder)

    assert (len(bit_string) % 6) == 0

    result = ""
    iterations = len(bit_string) // 6
    for i in range(iterations):
        # Convert the 6-bit substring to an integer and map to a character
        six_bit_substring = bit_string[i * 6 : (i + 1) * 6]
        index = int(six_bit_substring, 2)
        result += char_map[index]

    return result


def convert_location_to_check_num(location: str) -> int:
    assert isinstance(location, str)
    assert location in LOCATION_TABLE
    return check_list.index(location)


# https://github.com/lunarsoap5/Randomizer-Web-Generator-1/blob/main/Generator/Logic/CheckIds.cs#L25
check_list = [
    "Palace of Twilight East Wing Second Room Southwest Chest",
    "Faron Field Poe",
    "Goron Mines Crystal Switch Room Small Chest",
    "Goron Mines Gor Liggs Key Shard",
    "Wrestling With Bo",
    "Goron Mines After Crystal Switch Room Magnet Wall Chest",
    "Agitha Female Phasmid Reward",
    "Snowpeak Ruins East Courtyard Buried Chest",
    "Snowpeak Ruins Lobby East Armor Chest",
    "Bridge of Eldin Owl Statue Sky Character",
    "Arbiters Grounds Entrance Chest",
    "Hyrule Castle Treasure Room Third Chest",
    "Arbiters Grounds Torch Room Poe",
    "Palace of Twilight East Wing Second Room Northwest Chest",
    "Hyrule Castle Graveyard Owl Statue Chest",
    "Faron Field Corner Grotto Rear Chest",
    "Zoras Domain Male Dragonfly",
    "Gerudo Desert Lone Small Chest",
    "Gerudo Desert Rock Grotto Lantern Chest",
    "Lake Hylia Water Toadpoli Grotto Chest",
    "Faron Mist Stump Chest",
    "Lanayru Field Poe Grotto Left Poe",
    "City in The Sky Underwater West Chest",
    "Temple of Time Dungeon Reward",
    "Ordon Spring Golden Wolf",
    "Hyrule Castle Main Hall Northeast Chest",
    "Gerudo Desert Northeast Chest Behind Gates",
    "Ilias Charm",
    "Agitha Male Ladybug Reward",
    "Hyrule Castle Treasure Room Seventh Small Chest",
    "Lake Hylia Tower Poe",
    "Arbiters Grounds Spinner Room Lower North Chest",
    "Sacred Grove Past Owl Statue Chest",
    "Lakebed Temple Morpheel Heart Container",
    "Lost Woods Lantern Chest",
    "Lanayru Field Skulltula Grotto Chest",
    "Faron Mist Cave Lantern Chest",
    "Eldin Lantern Cave First Chest",
    "Faron Field Corner Grotto Right Chest",
    "Ordon Ranch Grotto Lantern Chest",
    "Sera Shop Slingshot",
    "Lakebed Temple East Lower Waterwheel Stalactite Chest",
    "Snowpeak Ruins Chest After Darkhammer",
    "Goron Mines Gor Liggs Chest",
    "Arbiters Grounds East Turning Room Poe",
    "Lanayru Field Female Stag Beetle",
    "Zoras Domain Chest By Mother and Child Isles",
    "North Faron Woods Deku Baba Chest",
    "City in The Sky Baba Tower Top Small Chest",
    "Kakariko Village Bomb Rock Spire Heart Piece",
    "Arbiters Grounds Stallord Heart Container",
    "Zoras Domain Chest Behind Waterfall",
    "City in The Sky Central Outside Ledge Chest",
    "Palace of Twilight East Wing First Room West Alcove Chest",
    "Bulblin Camp First Chest Under Tower At Entrance",
    "Arbiters Grounds West Stalfos Northeast Chest",
    "Outside South Castle Town Male Ladybug",
    "Jovani 20 Poe Soul Reward",
    "West Hyrule Field Helmasaur Grotto Chest",
    "Zoras Domain Underwater Goron",
    "Kakariko Inn Chest",
    "Agitha Female Beetle Reward",
    "Lanayru Spring Back Room Left Chest",
    "Agitha Female Grasshopper Reward",
    "City in The Sky Baba Tower Alcove Chest",
    "Goron Mines Gor Amato Chest",
    "Goron Mines Gor Ebizo Chest",
    "Faron Mist North Chest",
    "Lakebed Temple West Lower Small Chest",
    "Agitha Male Phasmid Reward",
    "City in The Sky Chest Behind North Fan",
    "Lake Lantern Cave Final Poe",
    "Temple of Time Lobby Lantern Chest",
    "Lakebed Temple East Second Floor Southeast Chest",
    "Hyrule Field Amphitheater Poe",
    "Gerudo Desert Peahat Ledge Chest",
    "Iza Helping Hand",
    "Lake Lantern Cave Second Chest",
    "Lakebed Temple Central Room Small Chest",
    "Links Basement Chest",
    "Snowpeak Cave Ice Lantern Chest",
    "Gerudo Desert Poe Above Cave of Ordeals",
    "Eldin Field Water Bomb Fish Grotto Chest",
    "Kakariko Village Watchtower Poe",
    "Agitha Female Dragonfly Reward",
    "Gift From Ralis",
    "South Faron Cave Chest",
    "Lakebed Temple West Second Floor Southeast Chest",
    "Temple of Time Darknut Chest",
    "Forest Temple Central North Chest",
    "Lanayru Field Male Stag Beetle",
    "City in The Sky Underwater East Chest",
    "Forest Temple East Water Cave Chest",
    "Hyrule Castle Treasure Room Second Small Chest",
    "Lake Hylia Bridge Vines Chest",
    "City in The Sky East Wing After Dinalfos Ledge Chest",
    "Snowpeak Ruins Lobby Armor Poe",
    "Faron Field Tree Heart Piece",
    "Eldin Field Stalfos Grotto Right Small Chest",
    "Lake Lantern Cave First Poe",
    "Hyrule Castle Treasure Room Fourth Small Chest",
    "Kakariko Village Malo Mart Hawkeye",
    "Uli Cradle Delivery",
    "Flight By Fowl Ledge Poe",
    "Lakebed Temple West Water Supply Chest",
    "Palace of Twilight East Wing Second Room Northeast Chest",
    "Kakariko Village Bomb Shop Poe",
    "Faron Mist Poe",
    "Lake Hylia Bridge Cliff Poe",
    "Hyrule Castle Main Hall Southwest Chest",
    "Wooden Sword Chest",
    "Goron Mines Dangoro Chest",
    "City in The Sky Garden Island Poe",
    "Faron Field Female Beetle",
    "Eldin Field Male Grasshopper",
    "Gerudo Desert Rock Grotto First Poe",
    "Eldin Lantern Cave Second Chest",
    "Palace of Twilight West Wing Second Room Southeast Chest",
    "Arbiters Grounds East Upper Turnable Redead Chest",
    "Sacred Grove Temple of Time Owl Statue Poe",
    "Forest Temple West Tile Worm Room Vines Chest",
    "Agitha Male Dragonfly Reward",
    "City in The Sky East Tile Worm Small Chest",
    "Palace of Twilight Central Tower Chest",
    "Outside Arbiters Grounds Poe",
    "Outside South Castle Town Double Clawshot Chasm Chest",
    "Hyrule Field Amphitheater Owl Statue Chest",
    "Snowpeak Ruins Northeast Chandelier Chest",
    "Hyrule Castle West Courtyard North Small Chest",
    "Agitha Female Stag Beetle Reward",
    "Lakebed Temple West Second Floor Central Small Chest",
    "Agitha Female Mantis Reward",
    "Lakebed Temple Lobby Rear Chest",
    "Bridge of Eldin Owl Statue Chest",
    "West Hyrule Field Golden Wolf",
    "Lake Hylia Bridge Cliff Chest",
    "City in The Sky West Garden Lower Chest",
    "Goron Mines Outside Clawshot Chest",
    "Lake Lantern Cave Fifth Chest",
    "Palace of Twilight Big Key Chest",
    "Agitha Male Beetle Reward",
    "Gerudo Desert Campfire East Chest",
    "Hyrule Castle Big Key Chest",
    "Temple of Time Moving Wall Beamos Room Chest",
    "Lake Lantern Cave Fourth Chest",
    "Lakebed Temple East Lower Waterwheel Bridge Chest",
    "City in The Sky East First Wing Chest After Fans",
    "Lake Lantern Cave Tenth Chest",
    "Lake Lantern Cave Ninth Chest",
    "Kakariko Watchtower Alcove Chest",
    "West Hyrule Field Male Butterfly",
    "Hyrule Castle King Bulblin Key",
    "Hyrule Castle East Wing Boomerang Puzzle Chest",
    "Palace of Twilight Central Outdoor Chest",
    "Hyrule Castle Treasure Room First Small Chest",
    "Goron Mines Outside Underwater Chest",
    "Lake Lantern Cave Eleventh Chest",
    "Agitha Female Ant Reward",
    "Cave of Ordeals Great Fairy Reward",
    "Forest Temple Central Chest Hanging From Web",
    "Lost Woods Waterfall Poe",
    "Kakariko Graveyard Open Poe",
    "Eldin Field Bomskit Grotto Left Chest",
    "Hyrule Castle West Courtyard Central Small Chest",
    "City in The Sky West Wing Narrow Ledge Chest",
    "Snowpeak Ruins Ordon Pumpkin Chest",
    "Skybook From Impaz",
    "STAR Prize 1",
    "Hyrule Castle Treasure Room Fifth Chest",
    "Zoras Domain Mother and Child Isle Poe",
    "Ordon Shield",
    "Flight By Fowl Fourth Platform Chest",
    "Goron Springwater Rush",
    "Arbiters Grounds Hidden Wall Poe",
    "Agitha Female Dayfly Reward",
    "Outside South Castle Town Tightrope Chest",
    "Lake Hylia Bridge Bubble Grotto Chest",
    "Hyrule Castle Main Hall Northwest Chest",
    "Snowpeak Ruins Ice Room Poe",
    "Forest Temple Dungeon Reward",
    "Arbiters Grounds Spinner Room Lower Central Small Chest",
    "Hyrule Castle Treasure Room Fifth Small Chest",
    "Goron Mines Chest Before Dangoro",
    "Agitha Male Snail Reward",
    "Agitha Male Ant Reward",
    "Lakebed Temple Before Deku Toad Underwater Left Chest",
    "Temple of Time Poe Above Scales",
    "Forest Temple North Deku Like Chest",
    "Lakebed Temple Central Room Chest",
    "Temple of Time First Staircase Gohma Gate Chest",
    "Temple of Time First Staircase Window Chest",
    "Forest Temple Totem Pole Chest",
    "Faron Mist South Chest",
    "Lake Lantern Cave Eighth Chest",
    "Snowpeak Ruins Lobby Chandelier Chest",
    "Lakebed Temple Deku Toad Chest",
    "Lake Hylia Dock Poe",
    "Lake Hylia Shell Blade Grotto Chest",
    "Forest Temple West Tile Worm Chest Behind Stairs",
    "Renados Letter",
    "Lake Lantern Cave Thirteenth Chest",
    "Arbiters Grounds Spinner Room First Small Chest",
    "Palace of Twilight Collect Both Sols",
    "Upper Zoras River Female Dragonfly",
    "Temple of Time Moving Wall Dinalfos Room Chest",
    "Lanayru Spring Underwater Right Chest",
    "Gerudo Desert East Canyon Chest",
    "Forest Temple Central Chest Behind Stairs",
    "City in The Sky Baba Tower Narrow Ledge Chest",
    "Outside South Castle Town Golden Wolf",
    "Snowpeak Blizzard Poe",
    "Hyrule Castle Treasure Room Fourth Chest",
    "Arbiters Grounds West Poe",
    "Arbiters Grounds Torch Room East Chest",
    "Temple of Time Big Key Chest",
    "Lanayru Spring Back Room Right Chest",
    "City in The Sky East Wing Lower Level Chest",
    "Lakebed Temple West Second Floor Southwest Underwater Chest",
    "Kakariko Graveyard Golden Wolf",
    "Goron Mines Beamos Room Chest",
    "Ashei Sketch",
    "West Hyrule Field Female Butterfly",
    "Sacred Grove Female Snail",
    "Faron Woods Owl Statue Sky Character",
    "Arbiters Grounds Spinner Room Stalfos Alcove Chest",
    "Eldin Stockcave Lowest Chest",
    "Kakariko Gorge Poe",
    "Lanayru Field Behind Gate Underwater Chest",
    "Arbiters Grounds East Lower Turnable Redead Chest",
    "Sacred Grove Male Snail",
    "Eldin Field Stalfos Grotto Left Small Chest",
    "Coro Bottle",
    "Lake Lantern Cave Second Poe",
    "Lake Lantern Cave Fourteenth Chest",
    "Snowpeak Ruins Mansion Map",
    "Flight By Fowl Third Platform Chest",
    "Lake Lantern Cave Twelfth Chest",
    "Snowpeak Ruins Dungeon Reward",
    "Gerudo Desert Golden Wolf",
    "Gerudo Desert Campfire West Chest",
    "Lakebed Temple West Second Floor Northeast Chest",
    "Gerudo Desert Female Dayfly",
    "Palace of Twilight West Wing Chest Behind Wall of Darkness",
    "Forest Temple Big Baba Key",
    "Sacred Grove Master Sword Poe",
    "Temple of Time First Staircase Armos Chest",
    "Outside South Castle Town Fountain Chest",
    "Arbiters Grounds Big Key Chest",
    "Hyrule Castle Treasure Room Eighth Small Chest",
    "Snowpeak Ruins West Courtyard Buried Chest",
    "Cave of Ordeals Floor 33 Poe",
    "Agitha Male Dayfly Reward",
    "Palace of Twilight East Wing First Room Zant Head Chest",
    "City in The Sky Big Key Chest",
    "Hyrule Castle Treasure Room Third Small Chest",
    "Goron Mines Main Magnet Room Top Chest",
    "Agitha Male Butterfly Reward",
    "Outside South Castle Town Tektite Grotto Chest",
    "Palace of Twilight West Wing Second Room Lower South Chest",
    "Goron Mines Gor Ebizo Key Shard",
    "Bridge of Eldin Female Phasmid",
    "East Castle Town Bridge Poe",
    "Forest Temple Entrance Vines Chest",
    "Hyrule Castle Southeast Balcony Tower Chest",
    "Hyrule Castle Treasure Room Sixth Small Chest",
    "Faron Field Bridge Chest",
    "Death Mountain Trail Poe",
    "Snowpeak Ruins Lobby West Armor Chest",
    "Charlo Donation Blessing",
    "Snowpeak Ruins Lobby Poe",
    "City in The Sky Aeralfos Chest",
    "Faron Woods Owl Statue Chest",
    "Snowpeak Ruins Wooden Beam Chandelier Chest",
    "City in The Sky Argorok Heart Container",
    "Hyrule Castle Graveyard Grave Switch Room Front Left Chest",
    "Snowpeak Ruins Courtyard Central Chest",
    "Flight By Fowl Second Platform Chest",
    "Gerudo Desert Male Dayfly",
    "Gerudo Desert Northwest Chest Behind Gates",
    "Eldin Spring Underwater Chest",
    "Kakariko Gorge Owl Statue Chest",
    "City in The Sky West Garden Lone Island Chest",
    "Hyrule Castle Graveyard Grave Switch Room Right Chest",
    "Lanayru Spring West Double Clawshot Chest",
    "Snowpeak Ruins Broken Floor Chest",
    "Arbiters Grounds Torch Room West Chest",
    "Isle of Riches Poe",
    "Goron Mines Crystal Switch Room Underwater Chest",
    "City in The Sky West Wing First Chest",
    "Snowboard Racing Prize",
    "Sacred Grove Baba Serpent Grotto Chest",
    "Lost Woods Boulder Poe",
    "City in The Sky Poe Above Central Fan",
    "Ordon Sword",
    "Hyrule Castle Treasure Room Second Chest",
    "Gerudo Desert South Chest Behind Wooden Gates",
    "Snowpeak Freezard Grotto Chest",
    "Goron Mines Outside Beamos Chest",
    "Palace of Twilight Zant Heart Container",
    "Castle Town Malo Mart Magic Armor",
    "Lakebed Temple East Water Supply Clawshot Chest",
    "Jovani House Poe",
    "Arbiters Grounds West Chandelier Chest",
    "Hyrule Field Amphitheater Owl Statue Sky Character",
    "Cave of Ordeals Floor 44 Poe",
    "Kakariko Graveyard Lantern Chest",
    "Forest Temple East Tile Worm Chest",
    "Agitha Female Snail Reward",
    "Lakebed Temple East Water Supply Small Chest",
    "Eldin Field Female Grasshopper",
    "Goron Mines Dungeon Reward",
    "Arbiters Grounds Death Sword Chest",
    "Lake Hylia Bridge Female Mantis",
    "Arbiters Grounds East Upper Turnable Chest",
    "City in The Sky West Wing Baba Balcony Chest",
    "Outside Arbiters Grounds Lantern Chest",
    "Lakebed Temple West Water Supply Small Chest",
    "Faron Mist Cave Open Chest",
    "Lakebed Temple Lobby Left Chest",
    "Bulblin Guard Key",
    "Lake Hylia Underwater Chest",
    "Temple of Time Armos Antechamber North Chest",
    "Lakebed Temple Big Key Chest",
    "City in The Sky Chest Below Big Key Chest",
    "Kakariko Village Female Ant",
    "Temple of Time Poe Behind Gate",
    "Kakariko Gorge Male Pill Bug",
    "Palace of Twilight East Wing Second Room Southeast Chest",
    "Hyrule Castle Graveyard Grave Switch Room Back Left Chest",
    "City in The Sky West Garden Ledge Chest",
    "Lake Hylia Bridge Male Mantis",
    "Eldin Stockcave Upper Chest",
    "Temple of Time Floor Switch Puzzle Room Upper Chest",
    "Lake Lantern Cave Third Chest",
    "Snowpeak Ruins Blizzeta Heart Container",
    "Lanayru Field Spinner Track Chest",
    "Iza Raging Rapids Minigame",
    "Arbiters Grounds North Turning Room Chest",
    "Agitha Female Pill Bug Reward",
    "Goron Mines Main Magnet Room Bottom Chest",
    "Goron Mines Gor Amato Small Chest",
    "Zoras Domain Waterfall Poe",
    "Forest Temple Diababa Heart Container",
    "Arbiters Grounds Spinner Room Second Small Chest",
    "Sacred Grove Spinner Chest",
    "Arbiters Grounds West Stalfos West Chest",
    "Forest Temple Big Key Chest",
    "Gerudo Desert Rock Grotto Second Poe",
    "Lakebed Temple East Second Floor Southwest Chest",
    "Temple of Time Armos Antechamber East Chest",
    "Temple of Time Armogohma Heart Container",
    "Snowpeak Ruins West Cannon Room Central Chest",
    "Kakariko Graveyard Grave Poe",
    "Gerudo Desert Campfire North Chest",
    "Goron Mines Fyrus Heart Container",
    "Hyrule Castle Lantern Staircase Chest",
    "Goron Mines Magnet Maze Chest",
    "Barnes Bomb Bag",
    "Eldin Field Bomskit Grotto Lantern Chest",
    "City in The Sky Central Outside Poe Island Chest",
    "STAR Prize 2",
    "City in The Sky West Garden Corner Chest",
    "Death Mountain Alcove Chest",
    "North Castle Town Golden Wolf",
    "Forest Temple Second Monkey Under Bridge Chest",
    "Gerudo Desert West Canyon Chest",
    "Agitha Male Mantis Reward",
    "Lanayru Ice Block Puzzle Cave Chest",
    "City in The Sky West Wing Tile Worm Chest",
    "Fishing Hole Heart Piece",
    "Bridge of Eldin Male Phasmid",
    "Forest Temple Windless Bridge Chest",
    "Zoras Domain Light All Torches Chest",
    "Palace of Twilight West Wing Second Room Central Chest",
    "Rutelas Blessing",
    "City in The Sky East Wing After Dinalfos Alcove Chest",
    "Snowpeak Cave Ice Poe",
    "Lakebed Temple Stalactite Room Chest",
    "Temple of Time Armos Antechamber Statue Chest",
    "Cave of Ordeals Floor 17 Poe",
    "Arbiters Grounds West Small Chest Behind Block",
    "Temple of Time Gilloutine Chest",
    "Cats Hide and Seek Minigame",
    "Goron Mines Entrance Chest",
    "Auru Gift To Fyer",
    "Snowpeak Above Freezard Grotto Poe",
    "Lake Lantern Cave First Chest",
    "Flight By Fowl Fifth Platform Chest",
    "Kakariko Watchtower Chest",
    "Faron Field Corner Grotto Left Chest",
    "Outside Lanayru Spring Left Statue Chest",
    "Hidden Village Poe",
    "Arbiters Grounds Ghoul Rat Room Chest",
    "Gerudo Desert East Poe",
    "Bulblin Camp Small Chest in Back of Camp",
    "Ilia Memory Reward",
    "Lanayru Spring Back Room Lantern Chest",
    "Agitha Female Ladybug Reward",
    "Palace of Twilight West Wing First Room Central Chest",
    "City in The Sky Dungeon Reward",
    "Kakariko Gorge Owl Statue Sky Character",
    "Forest Temple Gale Boomerang",
    "Gerudo Desert Skulltula Grotto Chest",
    "Forest Temple West Deku Like Chest",
    "Agitha Male Stag Beetle Reward",
    "Faron Field Male Beetle",
    "Palace of Twilight East Wing First Room North Small Chest",
    "Kakariko Graveyard Male Ant",
    "Temple of Time Scales Upper Chest",
    "Eldin Field Stalfos Grotto Stalfos Chest",
    "Ordon Cat Rescue",
    "Lakebed Temple Underwater Maze Small Chest",
    "Snowpeak Ruins West Cannon Room Corner Chest",
    "Lanayru Spring Underwater Left Chest",
    "Lake Hylia Bridge Owl Statue Chest",
    "Talo Sharpshooting",
    "Lakebed Temple Central Room Spire Chest",
    "Lake Hylia Bridge Owl Statue Sky Character",
    "Gerudo Desert North Small Chest Before Bulblin Camp",
    "Lakebed Temple Chandelier Chest",
    "Zoras Domain Extinguish All Torches Chest",
    "Lake Lantern Cave End Lantern Chest",
    "Temple of Time Chest Before Darknut",
    "Snowpeak Poe Among Trees",
    "Agitha Male Pill Bug Reward",
    "Herding Goats Reward",
    "Gerudo Desert North Peahat Poe",
    "Snowpeak Ruins Chapel Chest",
    "Lakebed Temple Dungeon Reward",
    "Lake Lantern Cave Sixth Chest",
    "Eldin Field Bomb Rock Chest",
    "Agitha Male Grasshopper Reward",
    "Flight By Fowl Top Platform Reward",
    "Kakariko Gorge Double Clawshot Chest",
    "Lanayru Field Bridge Poe",
    "Wooden Statue",
    "Fishing Hole Bottle",
    "Snowpeak Ruins East Courtyard Chest",
    "Lake Hylia Alcove Poe",
    "Lanayru Field Poe Grotto Right Poe",
    "Gerudo Desert Owl Statue Sky Character",
    "Gerudo Desert Owl Statue Chest",
    "Palace of Twilight Central First Room Chest",
    "Snowpeak Ruins Wooden Beam Central Chest",
    "Snowpeak Ruins Ball and Chain",
    "Plumm Fruit Balloon Minigame",
    "Kakariko Gorge Spire Heart Piece",
    "Lakebed Temple Before Deku Toad Underwater Right Chest",
    "Outside Bulblin Camp Poe",
    "Doctors Office Balcony Chest",
    "Outside Lanayru Spring Right Statue Chest",
    "Upper Zoras River Poe",
    "Bulblin Camp Poe",
    "Hyrule Castle East Wing Balcony Chest",
    "Lake Lantern Cave Seventh Chest",
    "Lanayru Spring East Double Clawshot Chest",
    "Snowpeak Icy Summit Poe",
    "Outside South Castle Town Poe",
    "Temple of Time Scales Gohma Chest",
    "Goron Mines Gor Amato Key Shard",
    "Kakariko Gorge Female Pill Bug",
    "Eldin Stockcave Lantern Chest",
    "Eldin Lantern Cave Lantern Chest",
    "Agitha Female Butterfly Reward",
    "Outside South Castle Town Female Ladybug",
    "Hyrule Castle Treasure Room First Chest",
    "Telma Invoice",
    "Snowpeak Ruins Wooden Beam Northwest Chest",
    "Lakebed Temple Before Deku Toad Alcove Chest",
    "Eldin Lantern Cave Poe",
    "Kakariko Village Malo Mart Hylian Shield",
    "Palace of Twilight East Wing First Room East Alcove Chest",
    "Bulblin Camp Roasted Boar",
    "Faron Woods Golden Wolf",
    "Jovani 60 Poe Soul Reward",
    "Kakariko Village Malo Mart Red Potion",
    "Kakariko Village Malo Mart Wooden Shield",
    "Arbiters Grounds Dungeon Reward",
    "Sacred Grove Pedestal Master Sword",
    "Sacred Grove Pedestal Shadow Crystal",
]
