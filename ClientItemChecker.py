import dolphin_memory_engine  # type: ignore


def check_flag(flag: int, address: int) -> bool:
    result = dolphin_memory_engine.read_byte(address)
    return (result & flag) != 0


def check_for_item(item_name: str, count: int, base_addr: int) -> bool:
    """Checks the save data for if the item / number of items is in the inventory"""
    match (item_name):
        case "Progressive Master Sword":
            if check_flag(0x2, base_addr + 0xD6) and count > 3:  # Light Sword
                return True
            if check_flag(0x2, base_addr + 0xD2) and count > 2:  # Master Sword
                return True
            if check_flag(0x1, base_addr + 0xD2) and count > 1:  # Ordon Sword
                return True
            if check_flag(0x80, base_addr + 0xD0) and count > 0:  # Wooden Sword
                return True
            return False

        case "Ordon Shield":
            return check_flag(0x4, base_addr + 0xD2)

        case "Hylian Shield":
            return check_flag(0x10, base_addr + 0xD2)

        case "Magic Armor":
            return check_flag(0x1, base_addr + 0xD1)

        case "Zora Armor":
            return check_flag(0x2, base_addr + 0xD1)

        case "Shadow Crystal":
            return check_flag(0x4, base_addr + 0xD1)

        case "Progressive Wallet":
            if check_flag(0x40, base_addr + 0xD1) and count > 1:  # Giant Wallet
                return True
            if check_flag(0x20, base_addr + 0xD1) and count > 0:  # Big Wallet
                return True
            return False

        case "Hawkeye":
            return check_flag(0x40, base_addr + 0xD0)

        case "Gale Boomerang":
            return check_flag(0x1, base_addr + 0xD7)

        case "Spinner":
            return check_flag(0x2, base_addr + 0xD7)

        case "Ball and Chain":
            return check_flag(0x4, base_addr + 0xD7)

        case "Progressive Hero's Bow":
            if check_flag(0x40, base_addr + 0xD5) and count > 2:  # Giant Quiver
                return True
            if check_flag(0x20, base_addr + 0xD5) and count > 1:  # Big Quiver
                return True
            if check_flag(0x8, base_addr + 0xD7) and count > 0:  # Hero's Bow
                return True
            return False

        case "Progressive Clawshot":
            if check_flag(0x80, base_addr + 0xD7) and count > 1:  # Double Clawshot
                return True
            if check_flag(0x10, base_addr + 0xD7) and count > 0:  # Clawshot
                return True
            return False

        case "Iron Boots":
            return check_flag(0x20, base_addr + 0xD7)

        case "Progressive Dominion Rod":
            if check_flag(0x40, base_addr + 0xD7) and count > 1:  # Dominion Rod
                return True
            if (
                check_flag(0x10, base_addr + 0xD6) and count > 0
            ):  # Powerless Dominion Rod
                return True
            return False

        case "Lantern":
            return check_flag(0x1, base_addr + 0xD6)

        case "Progressive Fishing Rod":
            if check_flag(0x20, base_addr + 0xD0) and count > 1:  # Coral Earing
                return True
            if check_flag(0x8, base_addr + 0xD6) and count > 0:  # Fishing Rod
                return True
            return False

        case "Slingshot":
            return check_flag(0x1, base_addr + 0xD8)

        case "Bomb Bag":
            if (
                dolphin_memory_engine.read_byte(base_addr + 0xAD) != 0xFF and count > 2
            ):  # Bomb Bag 3
                return True
            if (
                dolphin_memory_engine.read_byte(base_addr + 0xAC) != 0xFF and count > 1
            ):  # Bomb Bag 2
                return True
            if (
                dolphin_memory_engine.read_byte(base_addr + 0xAB) != 0xFF and count > 0
            ):  # Bomb Bag 1
                return True
            return False

        case "Horse Call":
            return check_flag(0x10, base_addr + 0xDF)

        case "Auru's Memo":
            return check_flag(0x1, base_addr + 0xDD)

        case "Ashei's Sketch":
            return check_flag(0x2, base_addr + 0xDD)

        case "Progressive Mirror Shard":
            if check_flag(0x8, base_addr + 0x10A) and count > 3:  # City Shard
                return True
            if check_flag(0x4, base_addr + 0x10A) and count > 2:  # Temple of Time Shard
                return True
            if check_flag(0x2, base_addr + 0x10A) and count > 1:  # Snowpeak Shard
                return True
            if check_flag(0x1, base_addr + 0x10A) and count > 0:  # Arbiters Shard
                return True
            return False

        case "Progressive Fused Shadow":
            if check_flag(0x4, base_addr + 0x109) and count > 2:  # Lakebed Shadow
                return True
            if check_flag(0x2, base_addr + 0x109) and count > 1:  # Goron Shadow
                return True
            if check_flag(0x1, base_addr + 0x109) and count > 0:  # Forest Shadow
                return True
            return False

        case "Progressive Hidden Skill":
            if check_flag(0x40, base_addr + 0x81A) and count > 5:  # Jump Strike
                return True
            if check_flag(0x80, base_addr + 0x81A) and count > 4:  # Mortal Draw
                return True
            if check_flag(0x1, base_addr + 0x819) and count > 3:  # Helm Splitter
                return True
            if check_flag(0x2, base_addr + 0x819) and count > 2:  # Backslice
                return True
            if check_flag(0x8, base_addr + 0x819) and count > 1:  # Shield Attack
                return True
            if check_flag(0x4, base_addr + 0x819) and count > 0:  # Ending Blow
                return True
            return False

        case "Giant Bomb Bag":
            return check_flag(0x80, base_addr + 0xD6)

        case _:
            assert False, f"[Twilight Princess Client] {item_name=} "
