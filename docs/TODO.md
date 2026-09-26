MACROS IS NOT WORKING YET:

# "ToTEntrance" done

options.py defines class ToTEntrance with option_closed/open_grove/open, NOT option_none/wooden_sword/ordon_sword/master_sword/light_sword. can_strike_pedestal (Macros.py:1572-1586) uses ToTEntrance + sword tiers; will NameError.
1.3 split open grove and tot entrance requirements into 2 options - tot entrance needs to be changed to new system

# CastleBKRequirements

no such class in options.py (only CastleRequirements and PalaceRequirements). can_open_hc_bk_gate (Macros.py:2152-2185) uses .option_none/fused_shadows_mirror_shards/dungeons/poe_souls/hearts
new setting for the door to the hyrule castle big key chest

# CastleRequirements.option_poe_souls / option_hearts

options.py CastleRequirements only has open/fused_shadows/mirror_shards/all_dungeons/vanilla. can_break_hc_barrier (Macros.py:2089/2096) uses them; will AttributeError.
poe souls and hearts got added

# WalletSize

no such class; options.py only has IncreaseWalletCapacity (Toggle). can_buy_magic_armor (Macros.py:2104-2122) uses WalletSize.Large/Reduced/Vanilla/HD.
before it was named "increase wallet", but now can be reduced (99, 500, 1000), vanilla (300, 600, 1000), hd (500, 1000, 2000) or large (1000, 5000, 9999)
Missing state getters (defined nowhere in Rules.py):
\_tp_hc_amount
\_tp_castle_bk_requirements
\_tp_hc_bk_amount
\_tp_wallet_size

Things to add:

# Portals

Need to make portals into items. Also need to confirm usage, should be treat as events or items?

# Quest items

need to bring back quest items to fill out logic. (should check spellings of the items)

# Seed encoder

fun times

# Key Rings

NOT YET WORKING:
used in Rules.py:
new: \_tp_wallet_size
WalletSize.option_reduced
WalletSize.option_vanilla
WalletSize.option_hd
WalletSize.option_large
new: \_tp_ilia_quest:
IliaQuest.option_vanilla
not used anymore: \_tp_increase_wallet
used in RegionRules.py:
new: \_tp_ilia_quest:
IliaQuest.option_charm
IliaQuest.option_statue
new: \_tp_open_door_of_time - True/False
new: \_tp_gm_shortcut - True/False
new: \_tp_hc_shortcut - True/False
used in both:
new: \_tp_skip_bridge_donation - True/False
