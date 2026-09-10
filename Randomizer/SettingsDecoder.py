import logging
import os
from typing import Dict, List, Tuple
from ..Locations import LOCATION_TABLE
from ..Items import ITEM_TABLE

char_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"

# Create mappings from IDs to names
location_id_to_name = {
    data.code: name for name, data in LOCATION_TABLE.items() if data.code is not None
}
item_id_to_name = {
    data.item_id: name for name, data in ITEM_TABLE.items() if data.item_id is not None
}

logger = logging.getLogger("Client")


def decode_6_bit_string(encoded: str) -> str:
    """Decodes a 6-bit encoded string back to a bit string."""
    bit_string = ""
    for char in encoded:
        index = char_map.index(char)
        bit_string += bin(index)[2:].zfill(6)
    return bit_string


def decode_vlq16(bits: str) -> Tuple[int, int]:
    """Decodes VLQ16 encoded number from bits, returns (num, bits_used)."""
    prefix = int(bits[:4], 2)
    if prefix == 0:
        num = int(bits[4], 2)
        return num, 5
    else:
        num_bits = prefix
        num = int(bits[4 : 4 + num_bits], 2)
        return num, 4 + num_bits


def decode_item_placements(encoded: str) -> Dict[int, int]:
    """Decodes the encoded item placements string back to a dict of location_code to item_id."""
    bits = decode_6_bit_string(encoded)
    pos = 0
    version, used = decode_vlq16(bits[pos:])
    pos += used
    has_items = bits[pos] == "1"
    pos += 1
    if not has_items:
        return {}
    smallest = int(bits[pos : pos + 9], 2)
    pos += 9
    largest = int(bits[pos : pos + 9], 2)
    pos += 9
    presence = bits[pos : pos + (largest - smallest + 1)]
    pos += largest - smallest + 1
    item_bits = bits[pos:]
    item_pos = 0
    location_to_item = {}
    for i in range(smallest, largest + 1):
        if presence[i - smallest] == "1":
            item_id = int(item_bits[item_pos : item_pos + 8], 2)
            location_to_item[i] = item_id
            item_pos += 8
    return location_to_item


def decode_setting_string(
    setting_string: str,
) -> Tuple[Dict[str, int | bool], List[int]]:
    """Decodes the encoded setting string back to settings dict and starting inventory list."""
    ver = setting_string[0]
    version = int(ver, 16)
    assert setting_string[1] == "s"
    length_info = decode_6_bit_string(setting_string[2:3])
    num = int(length_info, 2)
    extra_bits = num >> 3
    num_length_chars = num & 7
    len_chars = setting_string[3 : 3 + num_length_chars]
    len_bits = decode_6_bit_string(len_chars)
    len_encoded = int(len_bits, 2)
    bits_as_chars = setting_string[
        3 + num_length_chars : 3 + num_length_chars + len_encoded
    ]
    bit_string = decode_6_bit_string(bits_as_chars)
    bit_string = bit_string[:-extra_bits] if extra_bits > 0 else bit_string

    settings_map_keys = [
        "castle_requirements",
        "palace_requirements",
        "faron_woods_logic",
        "small_key_settings",
        "big_key_settings",
        "map_and_compass_settings",
        "skip_prologue",
        "faron_twilight_cleared",
        "eldin_twilight_cleared",
        "lanayru_twilight_cleared",
        "skip_mdh",
        "skip_minor_cutscenes",
        "fast_iron_boots",
        "quick_transform",
        "transform_anywhere",
        "increase_wallet",
        "modify_shop_models",
        "goron_mines_entrance",
        "skip_lakebed_entrance",
        "skip_arbiters_grounds_entrance",
        "skip_snowpeak_entrance",
        "tot_entrance",
        "skip_city_in_the_sky_entrance",
        "instant_message_text",
        "open_map",
        "increase_spinner_speed",
        "open_door_of_time",
        "damage_magnification",
        "bonks_do_damage",
        "skip_major_cutscenes",
        "starting_tod",
    ]
    settings_bits = [
        3,
        2,
        1,
        3,
        3,
        3,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        1,
        1,
        2,
        1,
        1,
        1,
        1,
        1,
        3,
        1,
        1,
        3,
    ]
    pos = 0
    settings = {}
    for key, bits in zip(settings_map_keys, settings_bits):
        if bits == 1:
            settings[key] = bit_string[pos] == "1"
            pos += 1
        else:
            settings[key] = int(bit_string[pos : pos + bits], 2)
            pos += bits
    starting_inventory = []
    while pos + 9 <= len(bit_string) and bit_string[pos : pos + 9] != "111111111":
        item_id = int(bit_string[pos : pos + 9], 2)
        starting_inventory.append(item_id)
        pos += 9
    return settings, starting_inventory


def display_decoded_info(
    item_placements: Dict[int, int],
    settings: Dict[str, int | bool],
    starting_inventory: List[int],
    output_dir: str,
    location_to_item_list: List[Tuple[str, int]] = None,
    output_file_name: str = "decoded_info.txt",
):
    """Displays the decoded item placements, settings, and starting inventory in readable text to a file."""
    output_file = os.path.join(output_dir, output_file_name)
    logger.info(f"outputting to file {output_file}")

    with open(output_file, "w") as f:
        f.write("Decoded Item Placements:\n")
        for loc, item in item_placements.items():
            loc_name = location_id_to_name.get(loc, f"Unknown Location {loc}")
            item_name = item_id_to_name.get(item, f"Unknown Item {item}")
            f.write(f"  {loc_name}: {item_name}\n")
        if location_to_item_list:
            f.write("Location to Item List:\n")
            for loc_name, item_id in location_to_item_list:
                item_name = item_id_to_name.get(item_id, f"Unknown Item {item_id}")
                f.write(f"  {loc_name}: {item_name}\n")
        f.write("\nDecoded Settings:\n")
        for key, value in settings.items():
            f.write(f"  {key}: {value}\n")
        f.write("\nStarting Inventory:\n")
        for item_id in starting_inventory:
            item_name = item_id_to_name.get(item_id, f"Unknown Item {item_id}")
            f.write(f"  {item_name}\n")


def run_decoder(file_string: str, path: str):

    assert (
        file_string[0] != "{"
    ), "Provided file is JSON, This seed was likely generated on an older apworld"
    string_parts = file_string.split(",")
    assert (
        len(string_parts) >= 2
    ), f"Provided file doesn't have enough parts to be valid"

    output_dir = os.path.dirname(path)
    settings, inventory = decode_setting_string(string_parts[0])
    placements = decode_item_placements(string_parts[1])
    display_decoded_info(placements, settings, inventory, output_dir)


# Example usage (uncomment and provide encoded strings to test)
# if __name__ == "__main__":
#     # Example: decode item placements string
#     encoded_placements = "..."  # Replace with actual encoded string
#     placements = decode_item_placements(encoded_placements)
#
#     # Example: decode settings string
#     encoded_settings = "..."  # Replace with actual encoded string
#     settings, inventory = decode_setting_string(encoded_settings)
#
#     # Display to file
#     display_decoded_info(placements, settings, inventory)
