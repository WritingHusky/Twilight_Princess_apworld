from BaseClasses import Item, MultiWorld
from ..Locations import TPLocation

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
