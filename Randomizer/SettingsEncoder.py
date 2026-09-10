import math
from typing import TYPE_CHECKING
from BaseClasses import Item, MultiWorld
from ..Items import TPItem
from ..Locations import TPLocation
from ..options import *

if TYPE_CHECKING:
    from .. import TPWorld

char_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"

# Based off of:
# https://github.com/lunarsoap5/Randomizer-Web-Generator-1/blob/9a5f38e972669209f3d21596b0a9744f1319412f/Generator/Logic/SeedGenResults.cs#L130

FILLER_ITEM_CODE = 0x8F


def get_item_placements(
    multiworld: MultiWorld, player: int
) -> tuple[str, list[tuple[str, int]]]:
    assert isinstance(multiworld, MultiWorld)
    assert isinstance(player, int)

    location_number_to_item_code: dict[int, int] = {}
    loaction_to_item = []

    for location in multiworld.get_locations(player):
        assert isinstance(location, TPLocation)
        assert isinstance(
            location.item, Item
        ), f"[Twilight Princess] {location.name}, {location.item}"

        # Ignore event locations
        if not isinstance(location.code, int):
            continue

        # If item is local then encode it as
        if location.item.player == player:
            assert isinstance(location.item, TPItem)
            loaction_to_item.append([location.name, location.item.item_id])
            location_number_to_item_code[location.code] = location.item.item_id
        else:
            loaction_to_item.append([location.name, FILLER_ITEM_CODE])
            location_number_to_item_code[location.code] = FILLER_ITEM_CODE

    # All locations that ap tracks are given a number and an item (ignore Story locations, Logic Event locations)
    assert len(location_number_to_item_code) == len(
        [
            location
            for location in multiworld.get_locations(player)
            # Filer
            if isinstance(location.address, int)
        ]
    ), f"[Twilight Princess] {len(location_number_to_item_code)},{len(multiworld.get_locations(player))}"

    result = encode_item_placements(location_number_to_item_code)
    assert isinstance(result, str)

    return [result, loaction_to_item]


def encode_num_as_bits(num: int, num_bits: int):
    """Encodes a number as a bit string of a specified length."""
    return bin(num)[2:].zfill(num_bits)


def encode_item_placements(check_num_id_to_item_id: dict[int, int]):

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


def get_setting_string(multiworld: MultiWorld, player: int):
    assert isinstance(multiworld, MultiWorld)

    # Skip prolougue, Twilights and MDH are hardcoded currently.
    # In the future I may want to add them so it's better to have them in the setting string to start

    settings_map: list[int | tuple[int, int]] = [
        # (multiworld.worlds[player].options.logic_rules.value, 2), # Just in ccase
        (multiworld.worlds[player].options.castle_requirements.value, 3),
        (multiworld.worlds[player].options.palace_requirements.value, 2),
        (multiworld.worlds[player].options.faron_woods_logic.value, 1),
        (multiworld.worlds[player].options.small_key_settings.value, 3),
        (multiworld.worlds[player].options.big_key_settings.value, 3),
        (multiworld.worlds[player].options.map_and_compass_settings.value, 3),
        True,  # Skip prologue
        True,  # Faron Twilight Cleared
        True,  # Eldin Twilight Cleared
        True,  # Lanayru Twilight Cleared
        True,  # Skip MDH
        bool(multiworld.worlds[player].options.skip_minor_cutscenes.value),
        bool(multiworld.worlds[player].options.fast_iron_boots.value),
        bool(multiworld.worlds[player].options.quick_transform.value),
        bool(multiworld.worlds[player].options.transform_anywhere.value),
        bool(multiworld.worlds[player].options.increase_wallet.value),
        bool(multiworld.worlds[player].options.modify_shop_models.value),
        (multiworld.worlds[player].options.goron_mines_entrance.value, 2),
        bool(multiworld.worlds[player].options.skip_lakebed_entrance.value),
        bool(multiworld.worlds[player].options.skip_arbiters_grounds_entrance.value),
        bool(multiworld.worlds[player].options.skip_snowpeak_entrance.value),
        (multiworld.worlds[player].options.tot_entrance.value, 2),
        bool(multiworld.worlds[player].options.skip_city_in_the_sky_entrance.value),
        bool(multiworld.worlds[player].options.instant_message_text.value),
        bool(multiworld.worlds[player].options.open_map.value),
        bool(multiworld.worlds[player].options.increase_spinner_speed.value),
        bool(multiworld.worlds[player].options.open_door_of_time.value),
        (multiworld.worlds[player].options.damage_magnification.value, 3),
        bool(multiworld.worlds[player].options.bonks_do_damage.value),
        bool(multiworld.worlds[player].options.skip_major_cutscenes.value),
        (multiworld.worlds[player].options.starting_tod.value, 3),
    ]

    bit_string = ""

    for setting_value in settings_map:
        if isinstance(setting_value, bool):
            bit_string += "1" if setting_value else "0"
        elif isinstance(setting_value, tuple):
            assert (
                len(setting_value) == 2
            ), f"[Twilight Princess] Unexpected length for setting value tuple {setting_value=}, {settings_map=}"
            assert isinstance(
                setting_value[0], int
            ), f"[Twilight Princess] Found an invalid setting value number {setting_value=}, {settings_map=}"
            assert isinstance(
                setting_value[1], int
            ), f"[Twilight Princess] Found an invalid setting value bit count {setting_value=}, {settings_map=}"
            bit_string += encode_num_as_bits(setting_value[0], setting_value[1])
        else:
            assert (
                False
            ), f"[Twilight Princess] Unexpected format for setting value {setting_value=}, {settings_map=}"

    # Create the starting inventory
    item_bit_string = ""
    for item in multiworld.precollected_items[player]:
        assert isinstance(
            item, TPItem
        ), f"[Twilight Princess] TP Player has precollected a non TP Item, {item=} \nSeed String cannot generate with Non TP precollected items"
        assert isinstance(
            item.item_id, int
        ), f"[Twilight Princess] {item=} does not have a valid item id"
        item_bit_string += encode_num_as_bits(item.item_id, 9)

    world: TPWorld = multiworld.worlds[player]
    if world.options.start_with_horse_call:
        item_bit_string += encode_num_as_bits(0x84, 9)

    item_bit_string += "111111111"

    bit_string += item_bit_string

    extra_bits = len(bit_string) % 6
    seed_body = encode_as_6_bit_string(bit_string)
    version = 5
    ver = hex(version)[2:]

    num_length_chars = 0
    for i in range(1, 8):  # max number of len chars is 7
        max_num = math.pow(64, i)
        if len(seed_body) < max_num:
            num_length_chars = i
            break

    length_char = encode_as_6_bit_string(
        encode_num_as_bits((extra_bits << 3) + num_length_chars, 6)
    )
    len_chars = encode_as_6_bit_string(
        encode_num_as_bits(len(seed_body), num_length_chars * 6)
    )
    assert (
        len(len_chars) == num_length_chars
    ), f"[Twilight Princess] Failed to create Setting String. Length of size chars {len_chars=} does not match expected size {num_length_chars=}"

    return ver + "s" + length_char + len_chars + seed_body
