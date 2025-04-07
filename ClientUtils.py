VERSION = "v0.2.4"

Settings_Format = {
    "Golden Bugs Shuffled": "Yes/No",
    "Sky Chracters Shuffled": "Yes/No",
    "NPC Items Shuffled": "Yes/No",
    "Shop Items Shuffled": "Yes/No",
    "Hidden Skills Shuffled": "Yes/No",
    "Poes Shuffled": "Yes/No",
    "Heart Pieces Shuffled": "Yes/No",
    "Overworld Shuffled": "Yes/No",
    "Dungeons Shuffled": "Yes/No",
    "Small Key Settings": "Start With/Vanilla/Own Dungeon/Any Dungeon/Anywhere",
    "Big Key Settings": "Start With/Vanilla/Own Dungeon/Any Dungeon/Anywhere",
    "Map and Compass Settings": "Start With/Vanilla/Own Dungeon/Any Dungeon/Anywhere",
    "Dungeon Rewards Progression": "Yes/No",
    "Logic Settings": "Glitchless/Glitched/No Logic",
    "Castle Requirements": "Open/Fused Shadows/Mirror Shards/All Dungeons/Vanilla",
    "Palace of Twilight Requirements": "Open/Fused Shadows/Mirror Shards/Vanilla",
    "Faron Woods Logic": "Open/Closed",
    "Open Map": "Yes/No",
    "Increase Wallet": "Yes/No",
    "Transform Anywhere": "Yes/No",
    "Bonks do Damage": "Yes/No",
    "Trap Frequency": "No Traps/Few/Many/Mayhem/Nightmare",
    "Damage Magnification": "Vanilla/Double/Triple/Quadruple/Ohko",
    "Lakebed Entrance Requirements": "Yes/No",
    "Arbiters Grounds Entrance Requirements": "Yes/No",
    "Snowpeak Entrance Requirements": "Yes/No",
    "City in the Sky Entrance Requirements": "Yes/No",
    "Goron Mines Entrance Requirements": "Open/No Wrestling/Closed",
    "Temple of Time Entrance Requirements": "Open/Open Grove/Closed",
    "Early Shadow Crystal": "Yes/No",
    "Skip Prologue": "Yes",
    "Faron Twilight Cleared": "Yes",
    "Eldin Twilight Cleared": "Yes",
    "Lanayru Twilight Cleared": "Yes",
    "Skip MDH": "Yes",
    "Open Door of Time": "Yes",
    "Small keys on Bosses": "No",  # Can be removed if not needed by anyone
}

server_copy: dict[str, bool | str] = {
    "Death Mountain Stone": False,
    "Zora River Stone": False,
    "Sacred Grove Stone": False,
    "Lake Hylia Stone": False,
    "Snowpeak Stone": False,
    "Hidden Village Stone": False,
    "Youth Scent": False,
    "Ilias Scent": False,
    "Medicine Scent": False,
    "ReekFish Scent": False,
    "Poe Scent": False,
    "Renados letter": False,
    "Telmas Invoice": False,
    "Wooden Statue": False,
    "Ilias Charm": False,
    "Memory Reward": False,
    "Current Region": "Menu",  # See NODE_TO_STRING for full breakdown
    "Diababa Defeated": False,
    "Fyrus Defeated": False,
    "Morpheel Defeated": False,
    "Stallord Defeated": False,
    "Blizzeta Defeated": False,
    "Armogohma Defeated": False,
    "Argorok Defeated": False,
    "Zant Defeated": False,
}

NODE_TO_STRING = {
    "Ordon": 0x0,
    "Sewers": 0x01,
    "Faron": 0x02,
    "Eldin": 0x03,
    "Lanayru": 0x04,
    "Hyrule Field": 0x06,
    "Sacred Grove": 0x07,
    "Snowpeak": 0x08,
    "Castle Town": 0x09,
    "Gerudo Desert": 0x0A,
    "Fishing Pond": 0x0B,
    "Forest Temple": 0x10,
    "Goron Mines": 0x11,
    "Lakebed Temple": 0x12,
    "Arbiters Grounds": 0x13,
    "Snowpeak Ruins": 0x14,
    "Temple of Time": 0x15,
    "City in the Sky": 0x16,
    "Palace of Twilight": 0x17,
    "Hyrule Castle": 0x18,
    "Cave of Ordeals": 0x19,
    "Lake Hylia Cave": 0x1A,
    "Grotto": 0x1B,
    "Menu": 0xFF,
}


server_data = [
    {
        "key": "Death Mountain Stone",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0x82A,
        "Flag": 0x80,
    },
    {
        "key": "Zora River Stone",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0x82A,
        "Flag": 0x40,
    },
    {
        "key": "Sacred Grove Stone",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0x82A,
        "Flag": 0x20,
    },
    {
        "key": "Lake Hylia Stone",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0x82A,
        "Flag": 0x10,
    },
    {
        "key": "Snowpeak Stone",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0x82A,
        "Flag": 0x8,
    },
    {
        "key": "Hidden Village Stone",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0x82A,
        "Flag": 0x4,
    },
    {
        "key": "Youth Scent",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0xE1,
        "Flag": 0x10,
    },
    {
        "key": "Ilias Scent",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0xE1,
        "Flag": 0x1,
    },
    {
        "key": "Medicine Scent",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0xE1,
        "Flag": 0x20,
    },
    {
        "key": "ReekFish Scent",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0xE1,
        "Flag": 0x8,
    },
    {
        "key": "Poe Scent",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0xE1,
        "Flag": 0x4,
    },
    {
        "key": "Renados letter",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0xDF,
        "Flag": 0x1,
    },
    {
        "key": "Telmas Invoice",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0xDF,
        "Flag": 0x2,
    },
    {
        "key": "Wooden Statue",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0xDF,
        "Flag": 0x4,
    },
    {
        "key": "Ilias Charm",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0xDF,
        "Flag": 0x8,
    },
    {
        "key": "Memory Reward",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Flag",
        "Offset": 0xDF,
        "Flag": 0x10,
    },
    {
        "key": "Current Region",
        "default": "Menu",
        "want_reply": False,
        "operations": [],
        "Region": "Node Number",  # This will use current node from the context
    },
    {
        "key": "Diababa Defeated",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Region",
        "Offset": 0x1D,
        "Flag": 0x8,
        "Node": 0x10,
    },
    {
        "key": "Fyrus Defeated",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Region",
        "Offset": 0x1D,
        "Flag": 0x8,
        "Node": 0x11,
    },
    {
        "key": "Morpheel Defeated",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Region",
        "Offset": 0x1D,
        "Flag": 0x8,
        "Node": 0x12,
    },
    {
        "key": "Stallord Defeated",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Region",
        "Offset": 0x1D,
        "Flag": 0x8,
        "Node": 0x13,
    },
    {
        "key": "Blizzeta Defeated",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Region",
        "Offset": 0x1D,
        "Flag": 0x8,
        "Node": 0x14,
    },
    {
        "key": "Armogohma Defeated",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Region",
        "Offset": 0x1D,
        "Flag": 0x8,
        "Node": 0x15,
    },
    {
        "key": "Argorok Defeated",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Region",
        "Offset": 0x1D,
        "Flag": 0x8,
        "Node": 0x16,
    },
    {
        "key": "Zant Defeated",
        "default": False,
        "want_reply": False,
        "operations": [],
        "Region": "Region",
        "Offset": 0x1D,
        "Flag": 0x8,
        "Node": 0x17,
    },
]

base_server_data_connection = [
    {
        "cmd": "Set",
        "key": data["key"],
        "default": data["default"],
        "want_reply": False,
        "operations": [],
    }
    for data in server_data
]
