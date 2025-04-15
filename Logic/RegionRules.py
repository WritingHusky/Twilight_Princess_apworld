from worlds.AutoWorld import World
from worlds.generic.Rules import set_rule
from .Macros import *
from ..options import (
    CastleRequirements,
    DamageMagnification,
    GoronMinesEntrance,
    TotEntrance,
    PalaceRequirements,
)


def set_region_access_rules(world: World, player: int):

    assert isinstance(world, World), f"{world=}"

    exit = world.get_entrance("Arbiters Grounds Entrance -> Outside Arbiters Grounds")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Arbiters Grounds Entrance -> Arbiters Grounds Lobby")
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Arbiters Grounds Small Key", player, 1)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
            and state.has("Lantern", player)
        ),
    )

    exit = world.get_entrance("Arbiters Grounds Lobby -> Arbiters Grounds Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Arbiters Grounds Lobby -> Arbiters Grounds East Wing")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Arbiters Grounds Lobby -> Arbiters Grounds West Wing")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Arbiters Grounds Lobby -> Arbiters Grounds After Poe Gate"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_Poe(state, player)
            and state.has("Shadow Crystal", player)
            and state.has("Progressive Clawshot", player, 1)
            and can_defeat_RedeadKnight(state, player)
            and can_defeat_Stalchild(state, player)
            and can_defeat_Bubble(state, player)
            and can_defeat_GhoulRat(state, player)
            and can_defeat_Stalfos(state, player)
            and (
                state.has("Arbiters Grounds Small Key", player, 4)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance("Arbiters Grounds East Wing -> Arbiters Grounds Lobby")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Arbiters Grounds West Wing -> Arbiters Grounds Lobby")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Arbiters Grounds After Poe Gate -> Arbiters Grounds Lobby"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Arbiters Grounds After Poe Gate -> Arbiters Grounds Boss Room"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Spinner", player)
            and (
                state.has("Arbiters Grounds Big Key", player)
                # Holdover from Keysy
                # or (
                #     state._tp_big_key_settings(player) == BigKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance("Arbiters Grounds Boss Room -> Mirror Chamber Lower")
    set_rule(
        exit,
        lambda state: (can_defeat_Stallord(state, player)),
    )

    exit = world.get_entrance("City in The Sky Boss Room -> City in The Sky Entrance")
    set_rule(
        exit,
        lambda state: (can_defeat_Argorok(state, player)),
    )

    exit = world.get_entrance(
        "City in The Sky Central Tower Second Floor -> City in The Sky West Wing"
    )
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 2)),
    )

    exit = world.get_entrance(
        "City in The Sky Central Tower Second Floor -> City in The Sky Lobby"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Progressive Clawshot", player, 1)
                and state.has("Iron Boots", player)
                and state.has("Shadow Crystal", player)
            )
            and (
                state._tp_damage_magnification(player)
                != DamageMagnification.option_ohko
            )
        ),
    )

    exit = world.get_entrance("City in The Sky East Wing -> City in The Sky Lobby")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("City in The Sky Entrance -> Lake Hylia")
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 1)),
    )

    exit = world.get_entrance("City in The Sky Entrance -> City in The Sky Lobby")
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 1)),
    )

    exit = world.get_entrance("City in The Sky Lobby -> City in The Sky Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("City in The Sky Lobby -> City in The Sky East Wing")
    set_rule(
        exit,
        lambda state: (
            state.has("Spinner", player)
            and (
                state.has("City in The Sky Small Key", player, 1)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance("City in The Sky Lobby -> City in The Sky West Wing")
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 2)),
    )

    exit = world.get_entrance("City in The Sky Lobby -> City in The Sky North Wing")
    set_rule(
        exit,
        lambda state: (
            state.has("Progressive Clawshot", player, 2)
            and can_defeat_BabaSerpent(state, player)
            and can_defeat_Kargarok(state, player)
            and state.has("Shadow Crystal", player)
            and state.has("Iron Boots", player)
        ),
    )

    exit = world.get_entrance("City in The Sky North Wing -> City in The Sky Lobby")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("City in The Sky North Wing -> City in The Sky Boss Room")
    set_rule(
        exit,
        lambda state: (
            state.has("Progressive Clawshot", player, 2)
            and can_defeat_Aeralfos(state, player)
            and (
                state.has("City in The Sky Big Key", player)
                # Holdover from Keysy
                # or (
                #     state._tp_big_key_settings(player) == BigKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance("City in The Sky West Wing -> City in The Sky Lobby")
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 2)),
    )

    exit = world.get_entrance(
        "City in The Sky West Wing -> City in The Sky Central Tower Second Floor"
    )
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 2)),
    )

    exit = world.get_entrance("Forest Temple Boss Room -> South Faron Woods")
    set_rule(
        exit,
        lambda state: (can_defeat_Diababa(state, player)),
    )

    exit = world.get_entrance("Forest Temple East Wing -> Forest Temple Lobby")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Forest Temple East Wing -> Forest Temple North Wing")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Forest Temple Entrance -> North Faron Woods")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Forest Temple Entrance -> Forest Temple Lobby")
    set_rule(
        exit,
        lambda state: (
            can_defeat_Walltula(state, player)
            and can_defeat_Bokoblin(state, player)
            and can_break_monkey_cage(state, player)
        ),
    )

    exit = world.get_entrance("Forest Temple Lobby -> Forest Temple Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Forest Temple Lobby -> Forest Temple East Wing")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Forest Temple Lobby -> Forest Temple West Wing")
    set_rule(
        exit,
        lambda state: (
            can_burn_webs(state, player)
            and (
                (
                    (
                        state.has("Forest Temple Small Key", player, 2)
                        # Holdover from Keysy
                        # or (
                        #     state._tp_small_key_settings(player)
                        #     == SmallKeySettings.option_anywhere
                        # )
                    )
                    and can_defeat_Bokoblin(state, player)
                )
                or state.has("Progressive Clawshot", player, 1)
            )
        ),
    )

    exit = world.get_entrance("Forest Temple Lobby -> Ook")
    set_rule(
        exit,
        lambda state: (
            state.has("Lantern", player)
            and can_defeat_Walltula(state, player)
            and can_defeat_Bokoblin(state, player)
            and can_break_monkey_cage(state, player)
            and (
                state.has("Forest Temple Small Key", player, 4)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance("Forest Temple North Wing -> Forest Temple East Wing")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Forest Temple North Wing -> Forest Temple Boss Room")
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Forest Temple Big Key", player)
                # Holdover from Keysy
                # or (
                #     state._tp_big_key_settings(player) == BigKeySettings.option_anywhere
                # )
            )
            and state.has("Gale Boomerang", player)
            and (
                can_free_all_monkeys(state, player)
                or state.has("Progressive Clawshot", player, 1)
            )
        ),
    )

    exit = world.get_entrance("Forest Temple West Wing -> Forest Temple Lobby")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Forest Temple West Wing -> Ook")
    set_rule(
        exit,
        lambda state: (state.has("Gale Boomerang", player)),
    )

    exit = world.get_entrance("Ook -> Forest Temple West Wing")
    set_rule(
        exit,
        lambda state: (
            can_defeat_Ook(state, player) and state.has("Gale Boomerang", player)
        ),
    )

    exit = world.get_entrance("Goron Mines Boss Room -> Lower Kakariko Village")
    set_rule(
        exit,
        lambda state: (can_defeat_Fyrus(state, player)),
    )

    exit = world.get_entrance(
        "Goron Mines Crystal Switch Room -> Goron Mines Magnet Room"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Goron Mines Crystal Switch Room -> Goron Mines North Wing"
    )
    set_rule(
        exit,
        lambda state: (
            (
                (state.has("Iron Boots", player) and has_sword(state, player))
                or state.has("Progressive Hero's Bow", player, 1)
            )
            and (
                state.has("Goron Mines Small Key", player, 2)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Goron Mines Entrance -> Death Mountain Sumo Hall Goron Mines Tunnel"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Goron Mines Entrance -> Goron Mines Magnet Room")
    set_rule(
        exit,
        lambda state: (
            state.has("Iron Boots", player) and can_break_wooden_door(state, player)
        ),
    )

    exit = world.get_entrance("Goron Mines Lower West Wing -> Goron Mines Magnet Room")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Goron Mines Magnet Room -> Goron Mines Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Goron Mines Magnet Room -> Goron Mines Lower West Wing")
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Goron Mines Small Key", player, 1)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Goron Mines Magnet Room -> Goron Mines Crystal Switch Room"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Goron Mines Small Key", player, 1)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
            and state.has("Iron Boots", player)
        ),
    )

    exit = world.get_entrance(
        "Goron Mines North Wing -> Goron Mines Crystal Switch Room"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Goron Mines North Wing -> Goron Mines Upper East Wing")
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Goron Mines Small Key", player, 3)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance("Goron Mines North Wing -> Goron Mines Boss Room")
    set_rule(
        exit,
        lambda state: (
            state.has("Progressive Hero's Bow", player, 1)
            and state.has("Iron Boots", player)
            and can_defeat_Bulblin(state, player)
            and (
                state.has("Goron Mines Key Shard", player, 3)
                # Holdover from Keysy
                # or (
                #     state._tp_big_key_settings(player) == BigKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance("Goron Mines Upper East Wing -> Goron Mines North Wing")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Goron Mines Upper East Wing -> Goron Mines Magnet Room")
    set_rule(
        exit,
        lambda state: (
            state.has("Iron Boots", player)
            and can_defeat_Dangoro(state, player)
            and state.has("Progressive Hero's Bow", player, 1)
        ),
    )

    exit = world.get_entrance("Ganondorf Castle -> Hyrule Castle Tower Climb")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Hyrule Castle Entrance -> Castle Town North Inside Barrier"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Hyrule Castle Entrance -> Hyrule Castle Main Hall")
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Hyrule Castle Small Key", player, 1)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Hyrule Castle Entrance -> Hyrule Castle Outside West Wing"
    )
    set_rule(
        exit,
        lambda state: (can_defeat_Bokoblin_Red(state, player)),
    )

    exit = world.get_entrance(
        "Hyrule Castle Entrance -> Hyrule Castle Outside East Wing"
    )
    set_rule(
        exit,
        lambda state: (can_defeat_Bokoblin_Red(state, player)),
    )

    exit = world.get_entrance(
        "Hyrule Castle Graveyard -> Hyrule Castle Outside East Wing"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Hyrule Castle Inside East Wing -> Hyrule Castle Main Hall"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Hyrule Castle Inside East Wing -> Hyrule Castle Third Floor Balcony"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Lantern", player) and can_defeat_Dinalfos(state, player)
        ),
    )

    exit = world.get_entrance(
        "Hyrule Castle Inside West Wing -> Hyrule Castle Main Hall"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Hyrule Castle Inside West Wing -> Hyrule Castle Third Floor Balcony"
    )
    set_rule(
        exit,
        lambda state: (
            can_knock_down_hc_painting(state, player)
            and can_defeat_Lizalfos(state, player)
            and can_defeat_Darknut(state, player)
        ),
    )

    exit = world.get_entrance("Hyrule Castle Main Hall -> Hyrule Castle Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Hyrule Castle Main Hall -> Hyrule Castle Inside East Wing"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_Bokoblin(state, player)
            and can_defeat_Lizalfos(state, player)
            and state.has("Progressive Clawshot", player, 2)
            and can_defeat_Darknut(state, player)
            and state.has("Gale Boomerang", player)
        ),
    )

    exit = world.get_entrance(
        "Hyrule Castle Main Hall -> Hyrule Castle Inside West Wing"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_Bokoblin(state, player)
            and can_defeat_Lizalfos(state, player)
            and state.has("Progressive Clawshot", player, 2)
            and can_defeat_Darknut(state, player)
            and state.has("Gale Boomerang", player)
        ),
    )

    exit = world.get_entrance(
        "Hyrule Castle Outside East Wing -> Hyrule Castle Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Hyrule Castle Outside East Wing -> Hyrule Castle Graveyard"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Hyrule Castle Outside West Wing -> Hyrule Castle Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Hyrule Castle Third Floor Balcony -> Hyrule Castle Inside West Wing"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_Darknut(state, player)
            and can_defeat_Lizalfos(state, player)
            and can_knock_down_hc_painting(state, player)
        ),
    )

    exit = world.get_entrance(
        "Hyrule Castle Third Floor Balcony -> Hyrule Castle Inside East Wing"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Lantern", player) and can_defeat_Dinalfos(state, player)
        ),
    )

    exit = world.get_entrance(
        "Hyrule Castle Third Floor Balcony -> Hyrule Castle Tower Climb"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Hyrule Castle Small Key", player, 2)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Hyrule Castle Tower Climb -> Hyrule Castle Third Floor Balcony"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Hyrule Castle Tower Climb -> Hyrule Castle Treasure Room"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Hyrule Castle Small Key", player, 3)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
            and state.has("Spinner", player)
            and state.has("Progressive Clawshot", player, 2)
            and can_defeat_Darknut(state, player)
            and can_defeat_Lizalfos(state, player)
        ),
    )

    exit = world.get_entrance("Hyrule Castle Tower Climb -> Ganondorf Castle")
    set_rule(
        exit,
        lambda state: (
            state.has("Spinner", player)
            and state.has("Progressive Clawshot", player, 2)
            and can_defeat_Darknut(state, player)
            and can_defeat_Lizalfos(state, player)
            and (
                state.has("Hyrule Castle Big Key", player)
                # Holdover from Keysy
                # or (
                #     state._tp_big_key_settings(player) == BigKeySettings.option_anywhere
                # )
            )
            and can_defeat_Ganondorf(state, player)
        ),
    )

    exit = world.get_entrance(
        "Hyrule Castle Treasure Room -> Hyrule Castle Tower Climb"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lakebed Temple Boss Room -> Lake Hylia Lanayru Spring")
    set_rule(
        exit,
        lambda state: (can_defeat_Morpheel(state, player)),
    )

    exit = world.get_entrance("Lakebed Temple Central Room -> Lakebed Temple Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Lakebed Temple Central Room -> Lakebed Temple East Wing Second Floor"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Lakebed Temple Small Key", player, 1)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Lakebed Temple Central Room -> Lakebed Temple East Wing First Floor"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lakebed Temple Central Room -> Lakebed Temple West Wing")
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Lakebed Temple Small Key", player, 3)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
            and can_smash(state, player)
            and state.has("Progressive Clawshot", player, 1)
        ),
    )

    exit = world.get_entrance("Lakebed Temple Central Room -> Lakebed Temple Boss Room")
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Lakebed Temple Small Key", player, 3)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
            and can_launch_bombs(state, player)
            and state.has("Progressive Clawshot", player, 1)
            and (
                state.has("Lakebed Temple Big Key", player)
                # Holdover from Keysy
                # or (
                #     state._tp_big_key_settings(player) == BigKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Lakebed Temple East Wing First Floor -> Lakebed Temple Central Room"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Lakebed Temple East Wing Second Floor -> Lakebed Temple Central Room"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Lakebed Temple East Wing Second Floor -> Lakebed Temple East Wing First Floor"
    )
    set_rule(
        exit,
        lambda state: (
            can_launch_bombs(state, player)
            or state.has("Progressive Clawshot", player, 1)
        ),
    )

    exit = world.get_entrance(
        "Lakebed Temple Entrance -> Lake Hylia Lakebed Temple Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lakebed Temple Entrance -> Lakebed Temple Central Room")
    set_rule(
        exit,
        lambda state: (can_launch_bombs(state, player)),
    )

    exit = world.get_entrance("Lakebed Temple West Wing -> Lakebed Temple Central Room")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Palace of Twilight Entrance -> Mirror Chamber Upper")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Palace of Twilight Entrance -> Palace of Twilight West Wing"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Palace of Twilight Entrance -> Palace of Twilight East Wing"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Palace of Twilight Entrance -> Palace of Twilight Central First Room"
    )
    set_rule(
        exit,
        lambda state: (state.has("Progressive Master Sword", player, 4)),
    )

    exit = world.get_entrance(
        "Palace of Twilight West Wing -> Palace of Twilight Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Palace of Twilight East Wing -> Palace of Twilight Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Palace of Twilight Central First Room -> Palace of Twilight Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Palace of Twilight Central First Room -> Palace of Twilight Outside Room"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Palace of Twilight Small Key", player, 5)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
            and state.has("Progressive Master Sword", player, 4)
        ),
    )

    exit = world.get_entrance(
        "Palace of Twilight Outside Room -> Palace of Twilight Central First Room"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Palace of Twilight Outside Room -> Palace of Twilight North Tower"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Palace of Twilight Small Key", player, 6)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Palace of Twilight North Tower -> Palace of Twilight Outside Room"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Palace of Twilight North Tower -> Palace of Twilight Boss Room"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_ZantHead(state, player)
            and state.has("Progressive Master Sword", player, 4)
            and (
                state.has("Palace of Twilight Big Key", player)
                # Holdover from Keysy
                # or (
                #     state._tp_big_key_settings(player) == BigKeySettings.option_anywhere
                # )
            )
            and can_defeat_ShadowBeast(state, player)
            and state.has("Progressive Clawshot", player, 1)
            and (
                state.has("Palace of Twilight Small Key", player, 7)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Palace of Twilight Boss Room -> Palace of Twilight Entrance"
    )
    set_rule(
        exit,
        lambda state: (can_defeat_Zant(state, player)),
    )

    exit = world.get_entrance("Snowpeak Ruins Left Door -> Snowpeak Ruins Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Ruins Left Door -> Snowpeak Summit Lower")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Ruins Right Door -> Snowpeak Ruins Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Ruins Right Door -> Snowpeak Summit Lower")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Ruins Boss Room -> Snowpeak Summit Lower")
    set_rule(
        exit,
        lambda state: (can_defeat_Blizzeta(state, player)),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Caged Freezard Room -> Snowpeak Ruins Yeto and Yeta"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Caged Freezard Room -> Snowpeak Ruins Second Floor Mini Freezard Room"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Ball and Chain", player)
            and (
                state.has("Snowpeak Ruins Small Key", player, 3)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Caged Freezard Room -> Snowpeak Ruins Wooden Beam Room"
    )
    set_rule(
        exit,
        lambda state: (state.has("Ball and Chain", player)),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Caged Freezard Room -> Snowpeak Ruins West Courtyard"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Snowpeak Ruins Small Key", player, 2)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance("Snowpeak Ruins Chapel -> Snowpeak Ruins West Courtyard")
    set_rule(
        exit,
        lambda state: (can_defeat_Chilfos(state, player)),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Darkhammer Room -> Snowpeak Ruins West Courtyard"
    )
    set_rule(
        exit,
        lambda state: (can_defeat_Darkhammer(state, player)),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins East Courtyard -> Snowpeak Ruins Yeto and Yeta"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Shadow Crystal", player) or state.has("Ball and Chain", player)
        ),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins East Courtyard -> Snowpeak Ruins West Courtyard"
    )
    set_rule(
        exit,
        lambda state: (state.has("Ball and Chain", player)),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins East Courtyard -> Snowpeak Ruins Northeast Chilfos Room First Floor"
    )
    set_rule(
        exit,
        lambda state: (
            (
                (
                    state.has("Snowpeak Ruins Small Key", player, 4)
                    # Holdover from Keysy
                    # or (
                    #     state._tp_small_key_settings(player)
                    #     == SmallKeySettings.option_anywhere
                    # )
                )
                and can_defeat_MiniFreezard(state, player)
            )
            or (
                (
                    state.has("Snowpeak Ruins Small Key", player, 2)
                    # Holdover from Keysy
                    # or (
                    #     state._tp_small_key_settings(player)
                    #     == SmallKeySettings.option_anywhere
                    # )
                )
                and state.has("Progressive Clawshot", player, 1)
                and can_defeat_MiniFreezard(state, player)
            )
        ),
    )

    exit = world.get_entrance("Snowpeak Ruins Entrance -> Snowpeak Ruins Left Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Ruins Entrance -> Snowpeak Ruins Right Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Ruins Entrance -> Snowpeak Ruins Yeto and Yeta")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Northeast Chilfos Room First Floor -> Snowpeak Ruins East Courtyard"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Northeast Chilfos Room First Floor -> Snowpeak Ruins Yeto and Yeta"
    )
    set_rule(
        exit,
        lambda state: (can_defeat_Chilfos(state, player)),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Northeast Chilfos Room Second Floor -> Snowpeak Ruins Northeast Chilfos Room First Floor"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Northeast Chilfos Room Second Floor -> Snowpeak Ruins Yeto and Yeta"
    )
    set_rule(
        exit,
        lambda state: (state.has("Ball and Chain", player)),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Second Floor Mini Freezard Room -> Snowpeak Ruins Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Second Floor Mini Freezard Room -> Snowpeak Ruins East Courtyard"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Shadow Crystal", player) or state.has("Ball and Chain", player)
        ),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Second Floor Mini Freezard Room -> Snowpeak Ruins Northeast Chilfos Room Second Floor"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Ball and Chain", player)
            and state.has("Progressive Clawshot", player, 1)
            and can_defeat_Chilfos(state, player)
        ),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Second Floor Mini Freezard Room -> Snowpeak Ruins Caged Freezard Room"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Snowpeak Ruins Small Key", player, 4)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins West Cannon Room -> Snowpeak Ruins West Courtyard"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins West Cannon Room -> Snowpeak Ruins Wooden Beam Room"
    )
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins West Courtyard -> Snowpeak Ruins Yeto and Yeta"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins West Courtyard -> Snowpeak Ruins East Courtyard"
    )
    set_rule(
        exit,
        lambda state: (state.has("Ball and Chain", player)),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins West Courtyard -> Snowpeak Ruins West Cannon Room"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Ruins West Courtyard -> Snowpeak Ruins Chapel")
    set_rule(
        exit,
        lambda state: (
            (
                (
                    state.has("Snowpeak Ruins Small Key", player, 4)
                    and state.has("Ordon Goat Cheese", player)
                )
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
            and state.has("Ball and Chain", player)
            and has_bombs(state, player)
        ),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins West Courtyard -> Snowpeak Ruins Darkhammer Room"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Ball and Chain", player)
            or (
                (
                    (
                        state.has("Snowpeak Ruins Small Key", player, 2)
                        or state.has("Ordon Goat Cheese", player)
                    )
                    # Holdover from Keysy
                    # or (
                    #     state._tp_small_key_settings(player)
                    #     == SmallKeySettings.option_anywhere
                    # )
                )
                and has_bombs(state, player)
            )
        ),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins West Courtyard -> Snowpeak Ruins Boss Room"
    )
    set_rule(
        exit,
        lambda state: (
            (
                (
                    state.has("Snowpeak Ruins Small Key", player, 4)
                    and state.has("Ordon Goat Cheese", player)
                )
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
            and state.has("Ball and Chain", player)
            and has_bombs(state, player)
            and (
                state.has("Bedroom Key", player)
                # Holdover from Keysy
                # or (
                #     state._tp_big_key_settings(player) == BigKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Wooden Beam Room -> Snowpeak Ruins West Cannon Room"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Ruins Yeto and Yeta -> Snowpeak Ruins Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Yeto and Yeta -> Snowpeak Ruins Caged Freezard Room"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Ordon Goat Cheese", player)
            # Holdover from Keysy
            # or (
            #     state._tp_small_key_settings(player) == SmallKeySettings.option_anywhere
            # )
        ),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Yeto and Yeta -> Snowpeak Ruins West Courtyard"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Ordon Pumpkin", player)
            # Holdover from Keysy
            # or (
            #     state._tp_small_key_settings(player) == SmallKeySettings.option_anywhere
            # )
        ),
    )

    exit = world.get_entrance(
        "Snowpeak Ruins Yeto and Yeta -> Snowpeak Ruins East Courtyard"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Shadow Crystal", player) or state.has("Ball and Chain", player)
        ),
    )

    exit = world.get_entrance(
        "Temple of Time Armos Antechamber -> Temple of Time Central Mechanical Platform"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Temple of Time Boss Room -> Sacred Grove Past")
    set_rule(
        exit,
        lambda state: (can_defeat_Armogohma(state, player)),
    )

    exit = world.get_entrance(
        "Temple of Time Central Mechanical Platform -> Temple of Time Connecting Corridors"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Temple of Time Central Mechanical Platform -> Temple of Time Armos Antechamber"
    )
    set_rule(
        exit,
        lambda state: (state.has("Spinner", player)),
    )

    exit = world.get_entrance(
        "Temple of Time Central Mechanical Platform -> Temple of Time Moving Wall Hallways"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Spinner", player)
            and (
                state.has("Temple of Time Small Key", player, 2)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Temple of Time Connecting Corridors -> Temple of Time Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Temple of Time Connecting Corridors -> Temple of Time Central Mechanical Platform"
    )
    set_rule(
        exit,
        lambda state: (
            has_ranged_item(state, player)
            and can_defeat_YoungGohma(state, player)
            and can_defeat_Lizalfos(state, player)
        ),
    )

    exit = world.get_entrance(
        "Temple of Time Crumbling Corridor -> Temple of Time Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Temple of Time Crumbling Corridor -> Temple of Time Boss Room"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Progressive Dominion Rod", player, 1)
            and (
                state.has("Temple of Time Big Key", player)
                # Holdover from Keysy
                # or (
                #     state._tp_big_key_settings(player) == BigKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Temple of Time Darknut Arena -> Temple of Time Upper Spike Trap Corridor"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_Darknut(state, player)
            and state.has("Progressive Dominion Rod", player, 1)
        ),
    )

    exit = world.get_entrance(
        "Temple of Time Entrance -> Sacred Grove Past Behind Window"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Temple of Time Entrance -> Temple of Time Connecting Corridors"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Temple of Time Small Key", player, 1)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance(
        "Temple of Time Entrance -> Temple of Time Crumbling Corridor"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Progressive Dominion Rod", player, 1)
                and state.has("Progressive Hero's Bow", player, 1)
                and state.has("Spinner", player)
                and can_defeat_Lizalfos(state, player)
                and can_defeat_Dinalfos(state, player)
                and can_defeat_Darknut(state, player)
                and (
                    state.has("Temple of Time Small Key", player, 3)
                    # Holdover from Keysy
                    # or (
                    #     state._tp_small_key_settings(player)
                    #     == SmallKeySettings.option_anywhere
                    # )
                )
            )
            or (state._tp_tot_entrance(player))
        ),
    )

    exit = world.get_entrance(
        "Temple of Time Floor Switch Puzzle Room -> Temple of Time Scales of Time"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Temple of Time Moving Wall Hallways -> Temple of Time Central Mechanical Platform"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Temple of Time Moving Wall Hallways -> Temple of Time Scales of Time"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Progressive Hero's Bow", player, 1)
            and can_defeat_Lizalfos(state, player)
            and can_defeat_Dinalfos(state, player)
        ),
    )

    exit = world.get_entrance(
        "Temple of Time Scales of Time -> Temple of Time Moving Wall Hallways"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Temple of Time Scales of Time -> Temple of Time Floor Switch Puzzle Room"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Progressive Clawshot", player, 1)
            and state.has("Spinner", player)
        ),
    )

    exit = world.get_entrance(
        "Temple of Time Scales of Time -> Temple of Time Upper Spike Trap Corridor"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Temple of Time Upper Spike Trap Corridor -> Temple of Time Scales of Time"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Temple of Time Upper Spike Trap Corridor -> Temple of Time Darknut Arena"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_Lizalfos(state, player)
            and can_defeat_BabyGohma(state, player)
            and can_defeat_YoungGohma(state, player)
            and can_defeat_Armos(state, player)
            and (
                state.has("Temple of Time Small Key", player, 3)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
        ),
    )

    exit = world.get_entrance("Death Mountain Near Kakariko -> Lower Kakariko Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Death Mountain Near Kakariko -> Death Mountain Trail")
    set_rule(
        exit,
        lambda state: (
            state.has("Iron Boots", player) or can_complete_goron_mines(state, player)
        ),
    )

    exit = world.get_entrance("Death Mountain Trail -> Death Mountain Near Kakariko")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Death Mountain Trail -> Death Mountain Volcano")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Death Mountain Volcano -> Death Mountain Trail")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Death Mountain Volcano -> Death Mountain Outside Sumo Hall"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Iron Boots", player)
            and (
                can_defeat_Goron(state, player)
                or can_complete_goron_mines(state, player)
            )
        ),
    )

    exit = world.get_entrance("Death Mountain Volcano -> Death Mountain Elevator Lower")
    set_rule(
        exit,
        lambda state: (
            state.can_reach_region("Death Mountain Elevator Lower", player)
            or (
                state._tp_goron_mines_enterance(player)
                == GoronMinesEntrance.option_open
            )
        ),
    )

    exit = world.get_entrance(
        "Death Mountain Outside Sumo Hall -> Death Mountain Volcano"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Death Mountain Outside Sumo Hall -> Death Mountain Sumo Hall"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Death Mountain Elevator Lower -> Death Mountain Volcano")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Death Mountain Elevator Lower -> Death Mountain Sumo Hall Elevator"
    )
    set_rule(
        exit,
        lambda state: (state.has("Iron Boots", player)),
    )

    exit = world.get_entrance(
        "Death Mountain Sumo Hall -> Death Mountain Outside Sumo Hall"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Death Mountain Sumo Hall -> Death Mountain Sumo Hall Elevator"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Iron Boots", player)
            or (
                state._tp_goron_mines_enterance(player)
                == GoronMinesEntrance.option_no_wrestling
            )
            or (
                state._tp_goron_mines_enterance(player)
                != GoronMinesEntrance.option_closed
            )
        ),
    )

    exit = world.get_entrance(
        "Death Mountain Sumo Hall -> Death Mountain Sumo Hall Goron Mines Tunnel"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Iron Boots", player)
            or (
                state._tp_goron_mines_enterance(player)
                == GoronMinesEntrance.option_no_wrestling
            )
            or (
                state._tp_goron_mines_enterance(player)
                != GoronMinesEntrance.option_closed
            )
        ),
    )

    exit = world.get_entrance(
        "Death Mountain Sumo Hall Elevator -> Death Mountain Elevator Lower"
    )
    set_rule(
        exit,
        lambda state: (state.has("Iron Boots", player)),
    )

    exit = world.get_entrance(
        "Death Mountain Sumo Hall Elevator -> Death Mountain Sumo Hall"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.can_reach_region("Death Mountain Sumo Hall", player)
                and state.has("Iron Boots", player)
            )
            or (
                state._tp_goron_mines_enterance(player)
                == GoronMinesEntrance.option_no_wrestling
            )
            or (
                state._tp_goron_mines_enterance(player)
                != GoronMinesEntrance.option_closed
            )
        ),
    )

    exit = world.get_entrance(
        "Death Mountain Sumo Hall Goron Mines Tunnel -> Death Mountain Sumo Hall"
    )
    set_rule(
        exit,
        lambda state: (
            (
                state.can_reach_region("Death Mountain Sumo Hall", player)
                and state.has("Iron Boots", player)
            )
            or (
                state._tp_goron_mines_enterance(player)
                == GoronMinesEntrance.option_no_wrestling
            )
            or (
                state._tp_goron_mines_enterance(player)
                != GoronMinesEntrance.option_closed
            )
        ),
    )

    exit = world.get_entrance(
        "Death Mountain Sumo Hall Goron Mines Tunnel -> Goron Mines Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Hidden Village -> Eldin Field Outside Hidden Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Hidden Village -> Hidden Village Impaz House")
    set_rule(
        exit,
        lambda state: (
            state.has("Progressive Hero's Bow", player, 1)
            and state.has("Progressive Dominion Rod", player, 1)
        ),
    )

    exit = world.get_entrance("Hidden Village Impaz House -> Hidden Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Gorge -> Kakariko Gorge Cave Entrance")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Kakariko Gorge -> Kakariko Gorge Behind Gate")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Gorge -> Faron Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Gorge -> Eldin Field")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Kakariko Gorge -> Kakariko Gorge Keese Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Kakariko Gorge Cave Entrance -> Kakariko Gorge")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Kakariko Gorge Cave Entrance -> Eldin Lantern Cave")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Gorge Behind Gate -> Kakariko Gorge")
    set_rule(
        exit,
        lambda state: (
            state.has("Shadow Crystal", player)
            or state.has("Gate Keys", player)
            # Holdover from Keysy
            # or (
            #     state._tp_small_key_settings(player) == SmallKeySettings.option_anywhere
            # )
        ),
    )

    exit = world.get_entrance("Kakariko Gorge Behind Gate -> Lower Kakariko Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Eldin Lantern Cave -> Kakariko Gorge Cave Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Gorge Keese Grotto -> Kakariko Gorge")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Eldin Field -> Eldin Field Near Castle Town")
    set_rule(
        exit,
        lambda state: (state.can_reach_region("Eldin Field Near Castle Town", player)),
    )

    exit = world.get_entrance("Eldin Field -> Eldin Field Lava Cave Ledge")
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 1)),
    )

    exit = world.get_entrance("Eldin Field -> Kakariko Gorge")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Eldin Field -> Kakariko Village Behind Gate")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Eldin Field -> North Eldin Field")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Eldin Field -> Eldin Field Bomskit Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Eldin Field -> Eldin Field Water Bomb Fish Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Eldin Field Near Castle Town -> Eldin Field")
    set_rule(
        exit,
        lambda state: (state.can_reach_region("Kakariko Malo Mart", player)),
    )

    exit = world.get_entrance(
        "Eldin Field Near Castle Town -> Outside Castle Town East"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Eldin Field Lava Cave Ledge -> Eldin Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Eldin Field Lava Cave Ledge -> Eldin Field Lava Cave Upper"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Eldin Field From Lava Cave Lower -> Eldin Field")
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 1)),
    )

    exit = world.get_entrance(
        "Eldin Field From Lava Cave Lower -> Eldin Field Lava Cave Lower"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("North Eldin Field -> Eldin Field")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("North Eldin Field -> Eldin Field Outside Hidden Village")
    set_rule(
        exit,
        lambda state: (
            state.can_reach_region("Kakariko Renados Sanctuary", player)
            and state.has("Wooden Statue", player)
        ),
    )

    exit = world.get_entrance("North Eldin Field -> Eldin Field Grotto Platform")
    set_rule(
        exit,
        lambda state: (state.has("Spinner", player)),
    )

    exit = world.get_entrance("North Eldin Field -> Lanayru Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Eldin Field Outside Hidden Village -> North Eldin Field")
    set_rule(
        exit,
        lambda state: (
            state.can_reach_region("Kakariko Renados Sanctuary", player)
            and state.has("Wooden Statue", player)
        ),
    )

    exit = world.get_entrance("Eldin Field Outside Hidden Village -> Hidden Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Eldin Field Grotto Platform -> North Eldin Field")
    set_rule(
        exit,
        lambda state: (state.has("Spinner", player)),
    )

    exit = world.get_entrance(
        "Eldin Field Grotto Platform -> Eldin Field Stalfos Grotto"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Eldin Field Lava Cave Upper -> Eldin Field Lava Cave Ledge"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Eldin Field Lava Cave Upper -> Eldin Field Lava Cave Lower"
    )
    set_rule(
        exit,
        lambda state: (state.has("Iron Boots", player)),
    )

    exit = world.get_entrance(
        "Eldin Field Lava Cave Lower -> Eldin Field From Lava Cave Lower"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Eldin Field Bomskit Grotto -> Eldin Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Eldin Field Water Bomb Fish Grotto -> Eldin Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Eldin Field Stalfos Grotto -> Eldin Field Grotto Platform"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lower Kakariko Village -> Upper Kakariko Village")
    set_rule(
        exit,
        lambda state: (
            (can_complete_goron_mines(state, player) and can_change_time(state, player))
            or can_smash(state, player)
        ),
    )

    exit = world.get_entrance("Lower Kakariko Village -> Kakariko Village Behind Gate")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lower Kakariko Village -> Kakariko Gorge Behind Gate")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lower Kakariko Village -> Kakariko Graveyard")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lower Kakariko Village -> Death Mountain Near Kakariko")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Lower Kakariko Village -> Kakariko Renados Sanctuary Front Left Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Lower Kakariko Village -> Kakariko Renados Sanctuary Front Right Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Lower Kakariko Village -> Kakariko Renados Sanctuary Back Left Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Lower Kakariko Village -> Kakariko Renados Sanctuary Back Right Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lower Kakariko Village -> Kakariko Malo Mart")
    set_rule(
        exit,
        lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance("Lower Kakariko Village -> Kakariko Elde Inn Left Door")
    set_rule(
        exit,
        lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance("Lower Kakariko Village -> Kakariko Elde Inn Right Door")
    set_rule(
        exit,
        lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance("Lower Kakariko Village -> Kakariko Bug House Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Lower Kakariko Village -> Kakariko Bug House Ceiling Hole"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Lower Kakariko Village -> Kakariko Barnes Bomb Shop Lower"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Upper Kakariko Village -> Lower Kakariko Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Upper Kakariko Village -> Kakariko Top of Watchtower")
    set_rule(
        exit,
        lambda state: (
            can_complete_goron_mines(state, player) and can_change_time(state, player)
        ),
    )

    exit = world.get_entrance(
        "Upper Kakariko Village -> Kakariko Barnes Bomb Shop Upper"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Upper Kakariko Village -> Kakariko Watchtower Lower Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Upper Kakariko Village -> Kakariko Watchtower Dig Spot")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Kakariko Top of Watchtower -> Upper Kakariko Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Top of Watchtower -> Kakariko Watchtower Upper Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Village Behind Gate -> Lower Kakariko Village")
    set_rule(
        exit,
        lambda state: (
            state.has("Gate Keys", player)
            # Holdover from Keysy
            # or (
            #     state._tp_small_key_settings(player) == SmallKeySettings.option_anywhere
            # )
        ),
    )

    exit = world.get_entrance("Kakariko Village Behind Gate -> Eldin Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary Front Left Door -> Lower Kakariko Village"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary Front Left Door -> Kakariko Renados Sanctuary"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary Front Right Door -> Lower Kakariko Village"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary Front Right Door -> Kakariko Renados Sanctuary"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary Back Left Door -> Lower Kakariko Village"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary Back Left Door -> Kakariko Renados Sanctuary"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary Back Right Door -> Lower Kakariko Village"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary Back Right Door -> Kakariko Renados Sanctuary"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary -> Kakariko Renados Sanctuary Front Left Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary -> Kakariko Renados Sanctuary Front Right Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary -> Kakariko Renados Sanctuary Back Left Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary -> Kakariko Renados Sanctuary Back Right Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary -> Kakariko Renados Sanctuary Basement"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Renados Sanctuary Basement -> Kakariko Renados Sanctuary"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Malo Mart -> Lower Kakariko Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Elde Inn Left Door -> Lower Kakariko Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Elde Inn Left Door -> Kakariko Elde Inn")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Elde Inn Right Door -> Lower Kakariko Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Elde Inn Right Door -> Kakariko Elde Inn")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Elde Inn -> Kakariko Elde Inn Left Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Elde Inn -> Kakariko Elde Inn Right Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Bug House Door -> Lower Kakariko Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Bug House Door -> Kakariko Bug House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Bug House Ceiling Hole -> Kakariko Bug House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Bug House Ceiling Hole -> Lower Kakariko Village"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Bug House -> Kakariko Bug House Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Bug House -> Kakariko Bug House Ceiling Hole")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Kakariko Barnes Bomb Shop Lower -> Lower Kakariko Village"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Barnes Bomb Shop Lower -> Kakariko Barnes Bomb Shop Upper"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Barnes Bomb Shop Upper -> Upper Kakariko Village"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Barnes Bomb Shop Upper -> Kakariko Barnes Bomb Shop Lower"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Watchtower Lower Door -> Upper Kakariko Village"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Watchtower Lower Door -> Kakariko Watchtower")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Watchtower Dig Spot -> Upper Kakariko Village")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Kakariko Watchtower Dig Spot -> Kakariko Watchtower")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Kakariko Watchtower Upper Door -> Kakariko Top of Watchtower"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Watchtower Upper Door -> Kakariko Watchtower")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Watchtower -> Kakariko Watchtower Lower Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Watchtower -> Kakariko Watchtower Dig Spot")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Watchtower -> Kakariko Watchtower Upper Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Graveyard -> Lower Kakariko Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Kakariko Graveyard -> Lake Hylia")
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Gate Keys", player)
                # Holdover from Keysy
                # or (
                #     state._tp_small_key_settings(player)
                #     == SmallKeySettings.option_anywhere
                # )
            )
            and (state.has("Iron Boots", player) or state.has("Zora Armor", player))
            and can_use_water_bombs(state, player)
        ),
    )

    exit = world.get_entrance("South Faron Woods -> South Faron Woods Behind Gate")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("South Faron Woods -> South Faron Woods Owl Statue Area")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("South Faron Woods -> Ordon Bridge")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("South Faron Woods -> Faron Field")
    set_rule(
        exit,
        lambda state: (can_clear_forest(state, player)),
    )

    exit = world.get_entrance("South Faron Woods -> Faron Woods Coros House Lower")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("South Faron Woods Behind Gate -> South Faron Woods")
    set_rule(
        exit,
        lambda state: (
            state.can_reach_region("South Faron Woods", player)
            or state.has("Shadow Crystal", player)
            or can_clear_forest(state, player)
        ),
    )

    exit = world.get_entrance(
        "South Faron Woods Behind Gate -> Faron Woods Cave Southern Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("South Faron Woods Coros Ledge -> South Faron Woods")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "South Faron Woods Coros Ledge -> Faron Woods Coros House Upper"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("South Faron Woods Owl Statue Area -> South Faron Woods")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance(
        "South Faron Woods Owl Statue Area -> South Faron Woods Above Owl Statue"
    )
    set_rule(
        exit,
        lambda state: (
            can_clear_forest(state, player)
            and state.has("Progressive Dominion Rod", player, 2)
            and state.has("Shadow Crystal", player)
        ),
    )

    exit = world.get_entrance(
        "South Faron Woods Above Owl Statue -> South Faron Woods Owl Statue Area"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "South Faron Woods Above Owl Statue -> Mist Area Near Owl Statue Chest"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Faron Woods Coros House Lower -> Faron Woods Coros House Upper"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Faron Woods Coros House Lower -> South Faron Woods")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Faron Woods Coros House Upper -> Faron Woods Coros House Lower"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Faron Woods Coros House Upper -> South Faron Woods Coros Ledge"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Faron Woods Cave Southern Entrance -> South Faron Woods Behind Gate"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Faron Woods Cave Southern Entrance -> Faron Woods Cave")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Faron Woods Cave -> Faron Woods Cave Southern Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Faron Woods Cave -> Faron Woods Cave Northern Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Mist Area Near Faron Woods Cave -> Mist Area Inside Mist"
    )
    set_rule(
        exit,
        lambda state: (state.has("Lantern", player)),
    )

    exit = world.get_entrance(
        "Mist Area Near Faron Woods Cave -> Mist Area Under Owl Statue Chest"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Lantern", player) or state.has("Shadow Crystal", player)
        ),
    )

    exit = world.get_entrance(
        "Mist Area Near Faron Woods Cave -> Faron Woods Cave Northern Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Mist Area Inside Mist -> Mist Area Near Faron Woods Cave"
    )
    set_rule(
        exit,
        lambda state: (state.has("Lantern", player)),
    )

    exit = world.get_entrance(
        "Mist Area Inside Mist -> Mist Area Under Owl Statue Chest"
    )
    set_rule(
        exit,
        lambda state: (state.has("Lantern", player)),
    )

    exit = world.get_entrance(
        "Mist Area Inside Mist -> Mist Area Outside Faron Mist Cave"
    )
    set_rule(
        exit,
        lambda state: (state.has("Lantern", player)),
    )

    exit = world.get_entrance(
        "Mist Area Inside Mist -> Mist Area Near North Faron Woods"
    )
    set_rule(
        exit,
        lambda state: (state.has("Lantern", player)),
    )

    exit = world.get_entrance(
        "Mist Area Under Owl Statue Chest -> Mist Area Inside Mist"
    )
    set_rule(
        exit,
        lambda state: (state.has("Lantern", player)),
    )

    exit = world.get_entrance(
        "Mist Area Under Owl Statue Chest -> Mist Area Center Stump"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Mist Area Near Owl Statue Chest -> Mist Area Under Owl Statue Chest"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Mist Area Near Owl Statue Chest -> South Faron Woods Above Owl Statue"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Mist Area Center Stump -> Mist Area Inside Mist")
    set_rule(
        exit,
        lambda state: (state.has("Lantern", player)),
    )

    exit = world.get_entrance(
        "Mist Area Center Stump -> Mist Area Near North Faron Woods"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Mist Area Outside Faron Mist Cave -> Mist Area Inside Mist"
    )
    set_rule(
        exit,
        lambda state: (state.has("Lantern", player)),
    )

    exit = world.get_entrance(
        "Mist Area Outside Faron Mist Cave -> Mist Area Faron Mist Cave"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Mist Area Near North Faron Woods -> Mist Area Inside Mist"
    )
    set_rule(
        exit,
        lambda state: (state.has("Lantern", player)),
    )

    exit = world.get_entrance(
        "Mist Area Near North Faron Woods -> Mist Area Near Faron Woods Cave"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Mist Area Near North Faron Woods -> North Faron Woods")
    set_rule(
        exit,
        lambda state: (
            state.has("Gate Keys", player)
            # or (state._tp_skip_prologue(player))
        ),
    )

    exit = world.get_entrance(
        "Faron Woods Cave Northern Entrance -> Mist Area Near Faron Woods Cave"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Faron Woods Cave Northern Entrance -> Faron Woods Cave")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Mist Area Faron Mist Cave -> Mist Area Outside Faron Mist Cave"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("North Faron Woods -> Mist Area Near North Faron Woods")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("North Faron Woods -> Lost Woods")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("North Faron Woods -> Forest Temple Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Faron Field -> Faron Field Behind Boulder")
    set_rule(
        exit,
        lambda state: (
            can_get_hot_spring_water(state, player)
            and state.can_reach_region("Outside Castle Town South", player)
        ),
    )

    exit = world.get_entrance("Faron Field -> South Faron Woods")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Faron Field -> Kakariko Gorge")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Faron Field -> Lake Hylia Bridge")
    set_rule(
        exit,
        lambda state: (
            state.has("Gate Keys", player)
            # Holdover from Keysy
            # or (
            #     state._tp_small_key_settings(player) == SmallKeySettings.option_anywhere
            # )
        ),
    )

    exit = world.get_entrance("Faron Field -> Faron Field Corner Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Faron Field -> Faron Field Fishing Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    # NOTE: Continuation of bottleless reachability
    exit = world.get_entrance("Faron Field Behind Boulder -> Faron Field")
    set_rule(
        exit,
        # lambda state: (True),
        lambda state: (can_get_hot_spring_water(state, player)),
    )

    exit = world.get_entrance(
        "Faron Field Behind Boulder -> Outside Castle Town South Inside Boulder"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Faron Field Corner Grotto -> Faron Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Faron Field Fishing Grotto -> Faron Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lost Woods -> Lost Woods Lower Battle Arena")
    set_rule(
        exit,
        lambda state: (
            (can_defeat_SkullKid(state, player) and state.has("Shadow Crystal", player))
            or (state._tp_tot_entrance(player) == TotEntrance.option_open)
            or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)
        ),
    )

    exit = world.get_entrance("Lost Woods -> Lost Woods Upper Battle Arena")
    set_rule(
        exit,
        lambda state: (
            (can_defeat_SkullKid(state, player) and state.has("Shadow Crystal", player))
            or (state._tp_tot_entrance(player) == TotEntrance.option_open)
            or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)
        ),
    )

    exit = world.get_entrance("Lost Woods -> North Faron Woods")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lost Woods Lower Battle Arena -> Lost Woods")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lost Woods Lower Battle Arena -> Sacred Grove Lower")
    set_rule(
        exit,
        lambda state: (
            can_defeat_SkullKid(state, player)
            or (state._tp_tot_entrance(player) == TotEntrance.option_open)
            or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)
        ),
    )

    exit = world.get_entrance(
        "Lost Woods Lower Battle Arena -> Lost Woods Baba Serpent Grotto"
    )
    set_rule(
        exit,
        lambda state: (
            can_smash(state, player) and state.has("Shadow Crystal", player)
        ),
    )

    exit = world.get_entrance(
        "Lost Woods Upper Battle Arena -> Sacred Grove Before Block"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_SkullKid(state, player)
            or (state._tp_tot_entrance(player) == TotEntrance.option_open)
            or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)
        ),
    )

    exit = world.get_entrance(
        "Lost Woods Baba Serpent Grotto -> Lost Woods Lower Battle Arena"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Sacred Grove Before Block -> Lost Woods Upper Battle Arena"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Sacred Grove Before Block -> Sacred Grove Upper")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Sacred Grove Upper -> Sacred Grove Lower")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Sacred Grove Upper -> Sacred Grove Past")
    set_rule(
        exit,
        lambda state: (
            (state._tp_tot_entrance(player) == TotEntrance.option_open)
            or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)
            or (
                state.can_reach_region("Sacred Grove Lower", player)
                and state.has("Progressive Master Sword", player, 3)
                and can_defeat_ShadowBeast(state, player)
            )
        ),
    )

    exit = world.get_entrance("Sacred Grove Lower -> Lost Woods Lower Battle Arena")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Sacred Grove Lower -> Sacred Grove Upper")
    set_rule(
        exit,
        lambda state: (
            state.can_reach_region("Sacred Grove Before Block", player)
            or (state._tp_tot_entrance(player) == TotEntrance.option_open)
            or (state._tp_tot_entrance(player) == TotEntrance.option_open_grove)
        ),
    )

    exit = world.get_entrance("Sacred Grove Past -> Sacred Grove Past Behind Window")
    set_rule(
        exit,
        lambda state: (
            (state._tp_tot_entrance(player) == TotEntrance.option_open)
            or state.has("Progressive Master Sword", player, 3)
        ),
    )

    exit = world.get_entrance("Sacred Grove Past -> Sacred Grove Upper")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Sacred Grove Past Behind Window -> Sacred Grove Past")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Sacred Grove Past Behind Window -> Temple of Time Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Gerudo Desert Cave of Ordeals Floors 01-11 -> Gerudo Desert Cave of Ordeals Plateau"
    )
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 1)),
    )

    exit = world.get_entrance(
        "Gerudo Desert Cave of Ordeals Floors 01-11 -> Gerudo Desert Cave of Ordeals Floors 12-21"
    )
    set_rule(
        exit,
        lambda state: (
            state.has("Spinner", player)
            and can_defeat_Bokoblin(state, player)
            and can_defeat_Keese(state, player)
            and can_defeat_Rat(state, player)
            and can_defeat_BabaSerpent(state, player)
            and can_defeat_Skulltula(state, player)
            and can_defeat_Bulblin(state, player)
            and can_defeat_TorchSlug(state, player)
            and can_defeat_FireKeese(state, player)
            and can_defeat_Dodongo(state, player)
            and can_defeat_Tektite(state, player)
            and can_defeat_Lizalfos(state, player)
        ),
    )

    exit = world.get_entrance(
        "Gerudo Desert Cave of Ordeals Floors 12-21 -> Gerudo Desert Cave of Ordeals Floors 22-31"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_Helmasaur(state, player)
            and can_defeat_Rat(state, player)
            and state.has("Ball and Chain", player)
            and can_defeat_Chu(state, player)
            and can_defeat_ChuWorm(state, player)
            and can_defeat_Bubble(state, player)
            and can_defeat_Bulblin(state, player)
            and can_defeat_Keese(state, player)
            and can_defeat_Rat(state, player)
            and can_defeat_Stalhound(state, player)
            and can_defeat_Poe(state, player)
            and can_defeat_Leever(state, player)
        ),
    )

    exit = world.get_entrance(
        "Gerudo Desert Cave of Ordeals Floors 22-31 -> Gerudo Desert Cave of Ordeals Floors 32-41"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_Bokoblin(state, player)
            and can_defeat_IceKeese(state, player)
            and state.has("Progressive Dominion Rod", player, 2)
            and can_defeat_Keese(state, player)
            and can_defeat_Rat(state, player)
            and can_defeat_GhoulRat(state, player)
            and can_defeat_Stalchild(state, player)
            and can_defeat_RedeadKnight(state, player)
            and can_defeat_Bulblin(state, player)
            and can_defeat_Stalfos(state, player)
            and can_defeat_Skulltula(state, player)
            and can_defeat_Bubble(state, player)
            and can_defeat_Lizalfos(state, player)
            and can_defeat_FireBubble(state, player)
        ),
    )

    exit = world.get_entrance(
        "Gerudo Desert Cave of Ordeals Floors 32-41 -> Gerudo Desert Cave of Ordeals Floors 42-50"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_Beamos(state, player)
            and can_defeat_Keese(state, player)
            and state.has("Progressive Clawshot", player, 2)
            and can_defeat_TorchSlug(state, player)
            and can_defeat_FireKeese(state, player)
            and can_defeat_Dodongo(state, player)
            and can_defeat_FireBubble(state, player)
            and can_defeat_RedeadKnight(state, player)
            and can_defeat_Poe(state, player)
            and can_defeat_GhoulRat(state, player)
            and can_defeat_Chu(state, player)
            and can_defeat_IceKeese(state, player)
            and can_defeat_Freezard(state, player)
            and can_defeat_Chilfos(state, player)
            and can_defeat_IceBubble(state, player)
            and can_defeat_Leever(state, player)
            and can_defeat_Darknut(state, player)
        ),
    )

    exit = world.get_entrance(
        "Gerudo Desert Cave of Ordeals Floors 42-50 -> Lake Hylia Lanayru Spring"
    )
    set_rule(
        exit,
        lambda state: (
            can_defeat_Armos(state, player)
            and can_defeat_Bokoblin(state, player)
            and can_defeat_BabaSerpent(state, player)
            and can_defeat_Lizalfos(state, player)
            and can_defeat_Bulblin(state, player)
            and can_defeat_Dinalfos(state, player)
            and can_defeat_Poe(state, player)
            and can_defeat_RedeadKnight(state, player)
            and can_defeat_Chu(state, player)
            and can_defeat_Freezard(state, player)
            and can_defeat_Chilfos(state, player)
            and can_defeat_GhoulRat(state, player)
            and can_defeat_Rat(state, player)
            and can_defeat_Stalchild(state, player)
            and can_defeat_Aeralfos(state, player)
            and can_defeat_Darknut(state, player)
        ),
    )

    exit = world.get_entrance("Gerudo Desert -> Gerudo Desert Cave of Ordeals Plateau")
    set_rule(
        exit,
        lambda state: (
            state.has("Progressive Clawshot", player, 1)
            and can_defeat_ShadowBeast(state, player)
        ),
    )

    exit = world.get_entrance("Gerudo Desert -> Gerudo Desert Basin")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Gerudo Desert -> Gerudo Desert Skulltula Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Gerudo Desert Cave of Ordeals Plateau -> Gerudo Desert")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Gerudo Desert Cave of Ordeals Plateau -> Gerudo Desert Cave of Ordeals Floors 01-11"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Gerudo Desert Basin -> Gerudo Desert")
    set_rule(
        exit,
        lambda state: (can_defeat_Bulblin(state, player)),
    )

    exit = world.get_entrance("Gerudo Desert Basin -> Gerudo Desert North East Ledge")
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 1)),
    )

    exit = world.get_entrance(
        "Gerudo Desert Basin -> Gerudo Desert Outside Bulblin Camp"
    )
    set_rule(
        exit,
        lambda state: (can_defeat_Bulblin(state, player)),
    )

    exit = world.get_entrance("Gerudo Desert Basin -> Gerudo Desert Chu Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Gerudo Desert North East Ledge -> Gerudo Desert Basin")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Gerudo Desert North East Ledge -> Gerudo Desert Rock Grotto"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Gerudo Desert Outside Bulblin Camp -> Gerudo Desert Basin"
    )
    set_rule(
        exit,
        lambda state: (
            state.can_reach_region("Gerudo Desert Basin", player)
            and can_defeat_Bulblin(state, player)
        ),
    )

    exit = world.get_entrance("Gerudo Desert Outside Bulblin Camp -> Bulblin Camp")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Gerudo Desert Skulltula Grotto -> Gerudo Desert")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Gerudo Desert Chu Grotto -> Gerudo Desert Basin")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Gerudo Desert Rock Grotto -> Gerudo Desert North East Ledge"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Bulblin Camp -> Gerudo Desert Outside Bulblin Camp")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Bulblin Camp -> Outside Arbiters Grounds")
    set_rule(
        exit,
        lambda state: (
            (
                (
                    state.has("Gerudo Desert Bublin Camp Key", player)
                    # Holdover from Keysy
                    # or (
                    #     state._tp_small_key_settings(player)
                    #     == SmallKeySettings.option_anywhere
                    # )
                )
                and can_defeat_KingBulblinDesert(state, player)
            )
            or (state._tp_skip_arbiters_entrance(player))
        ),
    )

    exit = world.get_entrance("Outside Arbiters Grounds -> Bulblin Camp")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Outside Arbiters Grounds -> Arbiters Grounds Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Mirror Chamber Lower -> Arbiters Grounds Boss Room")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Mirror Chamber Lower -> Mirror Chamber Upper")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Mirror Chamber Upper -> Mirror Chamber Lower")
    set_rule(
        exit,
        lambda state: (can_defeat_ShadowBeast(state, player)),
    )

    exit = world.get_entrance("Mirror Chamber Upper -> Mirror of Twilight")
    set_rule(
        exit,
        lambda state: (
            can_defeat_ShadowBeast(state, player)
            and (
                (
                    state._tp_palace_requirements(player)
                    == PalaceRequirements.option_open
                )
                or (
                    (
                        state._tp_palace_requirements(player)
                        == PalaceRequirements.option_fused_shadows
                    )
                    and state.has("Progressive Fused Shadow", player, 3)
                )
                or (
                    (
                        state._tp_palace_requirements(player)
                        == PalaceRequirements.option_mirror_shards
                    )
                    and state.has("Progressive Mirror Shard", player, 4)
                )
                or (
                    (
                        state._tp_palace_requirements(player)
                        == PalaceRequirements.option_vanilla
                    )
                    and can_complete_city_in_the_sky(state, player)
                )
            )
        ),
    )

    exit = world.get_entrance("Mirror of Twilight -> Mirror Chamber Upper")
    set_rule(
        exit,
        lambda state: (can_defeat_ShadowBeast(state, player)),
    )

    exit = world.get_entrance("Mirror of Twilight -> Palace of Twilight Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town West -> Outside Castle Town West")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town West -> Castle Town Center")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town West -> Castle Town South")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town West -> Castle Town STAR Game")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town STAR Game -> Castle Town West")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Center -> Castle Town West")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Center -> Castle Town North")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Center -> Castle Town East")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Center -> Castle Town South")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Center -> Castle Town Goron House Left Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Center -> Castle Town Goron House Right Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Center -> Castle Town Malo Mart")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Goron House Left Door -> Castle Town Center")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Goron House Left Door -> Castle Town Goron House"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Goron House Right Door -> Castle Town Center"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Goron House Right Door -> Castle Town Goron House"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Goron House -> Castle Town Goron House Left Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Goron House -> Castle Town Goron House Right Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Malo Mart -> Castle Town Center")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town North -> Castle Town North Behind First Door"
    )
    set_rule(exit, lambda state: True)  # (can_complete_MDH(state, player)),

    exit = world.get_entrance("Castle Town North -> Castle Town Center")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town North Behind First Door -> Castle Town North"
    )
    set_rule(exit, lambda state: True)  # (can_complete_MDH(state, player)),

    exit = world.get_entrance(
        "Castle Town North Behind First Door -> Castle Town North Inside Barrier"
    )
    set_rule(
        exit,
        lambda state: (
            (state._tp_castle_requirements(player) == CastleRequirements.option_open)
            or (
                (
                    state._tp_castle_requirements(player)
                    == CastleRequirements.option_vanilla
                )
                and can_complete_palace_of_twilight(state, player)
            )
            or (
                (
                    state._tp_castle_requirements(player)
                    == CastleRequirements.option_fused_shadows
                )
                and state.has("Progressive Fused Shadow", player, 3)
            )
            or (
                (
                    state._tp_castle_requirements(player)
                    == CastleRequirements.option_mirror_shards
                )
                and state.has("Progressive Mirror Shard", player, 4)
            )
            or (
                (
                    state._tp_castle_requirements(player)
                    == CastleRequirements.option_all_dungeons
                )
                and can_complete_all_dungeons(state, player)
            )
        ),
    )

    exit = world.get_entrance(
        "Castle Town North Inside Barrier -> Castle Town North Behind First Door"
    )
    set_rule(exit, lambda state: True)  # (can_complete_MDH(state, player)),

    exit = world.get_entrance(
        "Castle Town North Inside Barrier -> Hyrule Castle Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town East -> Castle Town Center")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town East -> Outside Castle Town East")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town East -> Castle Town South")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town East -> Castle Town Doctors Office Left Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town East -> Castle Town Doctors Office Right Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Doctors Office Balcony -> Castle Town East")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Balcony -> Castle Town Doctors Office Upper"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Left Door -> Castle Town East"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Left Door -> Castle Town Doctors Office Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Right Door -> Castle Town East"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Right Door -> Castle Town Doctors Office Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Entrance -> Castle Town Doctors Office Left Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Entrance -> Castle Town Doctors Office Right Door"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Entrance -> Castle Town Doctors Office Lower"
    )
    set_rule(
        exit,
        lambda state: (state.has("Invoice", player)),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Lower -> Castle Town Doctors Office Entrance"
    )
    set_rule(
        exit,
        lambda state: (state.has("Invoice", player)),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Lower -> Castle Town Doctors Office Upper"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Upper -> Castle Town Doctors Office Lower"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Castle Town Doctors Office Upper -> Castle Town Doctors Office Balcony"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town South -> Castle Town West")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town South -> Castle Town Center")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town South -> Castle Town East")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town South -> Outside Castle Town South")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town South -> Castle Town Agithas House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town South -> Castle Town Seer House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town South -> Castle Town Jovanis House")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Castle Town South -> Castle Town Telmas Bar")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Agithas House -> Castle Town South")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Seer House -> Castle Town South")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Jovanis House -> Castle Town South")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Castle Town Telmas Bar -> Castle Town South")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lanayru Field -> Lanayru Field Cave Entrance")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Lanayru Field -> Lanayru Field Behind Boulder")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Lanayru Field -> Hyrule Field Near Spinner Rails")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Lanayru Field -> North Eldin Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lanayru Field -> Outside Castle Town West")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lanayru Field -> Lanayru Field Chu Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Lanayru Field -> Lanayru Field Skulltula Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Lanayru Field -> Lanayru Field Poe Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Lanayru Field Cave Entrance -> Lanayru Field")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Lanayru Field Cave Entrance -> Lanayru Ice Puzzle Cave")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lanayru Field Behind Boulder -> Lanayru Field")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Lanayru Field Behind Boulder -> Zoras Domain West Ledge")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Hyrule Field Near Spinner Rails -> Lanayru Field")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Hyrule Field Near Spinner Rails -> Lake Hylia Bridge")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Lanayru Ice Puzzle Cave -> Lanayru Field Cave Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lanayru Field Chu Grotto -> Lanayru Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lanayru Field Skulltula Grotto -> Lanayru Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lanayru Field Poe Grotto -> Lanayru Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Outside Castle Town West -> Outside Castle Town West Grotto Ledge"
    )
    set_rule(
        exit,
        lambda state: (state.has("Progressive Clawshot", player, 1)),
    )

    exit = world.get_entrance("Outside Castle Town West -> Lanayru Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Outside Castle Town West -> Castle Town West")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Outside Castle Town West -> Lake Hylia Bridge")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Outside Castle Town West Grotto Ledge -> Outside Castle Town West"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Outside Castle Town West Grotto Ledge -> Outside Castle Town West Helmasaur Grotto"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Outside Castle Town West Helmasaur Grotto -> Outside Castle Town West Grotto Ledge"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Outside Castle Town East -> Eldin Field Near Castle Town"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Outside Castle Town East -> Castle Town East")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Outside Castle Town South -> Castle Town South")
    set_rule(
        exit,
        lambda state: (True),
    )

    # NOTE: This is a hotfix to get full region reachablity without making bottles progression
    exit = world.get_entrance(
        "Outside Castle Town South Inside Boulder -> Faron Field Behind Boulder"
    )
    set_rule(
        exit,
        lambda state: (can_get_hot_spring_water(state, player)),
        # lambda stat: (True),
    )

    exit = world.get_entrance(
        "Outside Castle Town South -> Outside Castle Town South Inside Boulder"
    )
    set_rule(
        exit,
        lambda state: (True),
    )
    exit = world.get_entrance("Outside Castle Town South -> Lake Hylia")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Outside Castle Town South -> Outside Castle Town South Tektite Grotto"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Outside Castle Town South Inside Boulder -> Outside Castle Town South"
    )
    set_rule(
        exit,
        lambda state: (
            can_get_hot_spring_water(state, player)
            and state.can_reach_region("Outside Castle Town South", player)
        ),
    )

    exit = world.get_entrance(
        "Outside Castle Town South Tektite Grotto -> Outside Castle Town South"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia Bridge -> Lake Hylia Bridge Grotto Ledge")
    set_rule(
        exit,
        lambda state: (
            can_launch_bombs(state, player)
            and state.has("Progressive Clawshot", player, 1)
        ),
    )

    exit = world.get_entrance("Lake Hylia Bridge -> Hyrule Field Near Spinner Rails")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Lake Hylia Bridge -> Outside Castle Town West")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia Bridge -> Lake Hylia")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia Bridge -> Faron Field")
    set_rule(
        exit,
        lambda state: (
            state.has("Gate Keys", player)
            # Holdover from Keysy
            # or (
            #     state._tp_small_key_settings(player) == SmallKeySettings.option_anywhere
            # )
        ),
    )

    exit = world.get_entrance("Lake Hylia Bridge Grotto Ledge -> Lake Hylia Bridge")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance(
        "Lake Hylia Bridge Grotto Ledge -> Lake Hylia Bridge Bubble Grotto"
    )
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance(
        "Lake Hylia Bridge Bubble Grotto -> Lake Hylia Bridge Grotto Ledge"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia -> Lake Hylia Cave Entrance")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Lake Hylia -> Lake Hylia Lakebed Temple Entrance")
    set_rule(
        exit,
        lambda state: (
            state.has("Zora Armor", player)
            and (
                (state._tp_skip_lakebed_entrance(player))
                or (
                    state.has("Iron Boots", player)
                    and can_use_water_bombs(state, player)
                )
            )
        ),
    )

    exit = world.get_entrance("Lake Hylia -> Lake Hylia Bridge")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia -> Gerudo Desert")
    set_rule(
        exit,
        lambda state: (state.has("Auru's Memo", player)),
    )

    exit = world.get_entrance("Lake Hylia -> Upper Zoras River")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Lake Hylia -> Lake Hylia Lanayru Spring")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia -> Lake Hylia Shell Blade Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Lake Hylia -> Lake Hylia Water Toadpoli Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Lake Hylia -> City in The Sky Entrance")
    set_rule(
        exit,
        lambda state: (
            (
                state.has("Progressive Sky Book", player, 1)
                or (state._tp_skip_city_in_the_sky_entrance(player))
            )
            and state.has("Progressive Clawshot", player, 1)
        ),
    )

    exit = world.get_entrance("Lake Hylia Cave Entrance -> Lake Hylia")
    set_rule(
        exit,
        lambda state: (can_smash(state, player)),
    )

    exit = world.get_entrance("Lake Hylia Cave Entrance -> Lake Hylia Long Cave")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia Lakebed Temple Entrance -> Lake Hylia")
    set_rule(
        exit,
        lambda state: (
            state.has("Zora Armor", player)
            and (
                (state._tp_skip_lakebed_entrance(player))
                or (
                    state.has("Iron Boots", player)
                    and can_use_water_bombs(state, player)
                )
            )
        ),
    )

    exit = world.get_entrance(
        "Lake Hylia Lakebed Temple Entrance -> Lakebed Temple Entrance"
    )
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia Lanayru Spring -> Lake Hylia")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia Long Cave -> Lake Hylia Cave Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia Shell Blade Grotto -> Lake Hylia")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Lake Hylia Water Toadpoli Grotto -> Lake Hylia")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Upper Zoras River -> Lanayru Field")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Upper Zoras River -> Fishing Hole")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Upper Zoras River -> Zoras Domain")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Upper Zoras River -> Upper Zoras River Izas House")
    set_rule(
        exit,
        lambda state: (
            has_sword(state, player)
            or (
                can_defeat_ShadowBeast(state, player)
                and (state._tp_transform_anywhere(player))
            )
        ),
    )

    exit = world.get_entrance("Upper Zoras River Izas House -> Upper Zoras River")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Upper Zoras River Izas House -> Lake Hylia")
    set_rule(
        exit,
        lambda state: (state.has("Progressive Hero's Bow", player, 1)),
    )

    exit = world.get_entrance("Fishing Hole -> Upper Zoras River")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Fishing Hole -> Fishing Hole House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Fishing Hole House -> Fishing Hole")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Zoras Domain -> Zoras Domain West Ledge")
    set_rule(
        exit,
        lambda state: (
            state.has("Progressive Clawshot", player, 1)
            or state.has("Shadow Crystal", player)
            or can_smash(state, player)
        ),
    )

    exit = world.get_entrance("Zoras Domain -> Upper Zoras River")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Zoras Domain -> Zoras Domain Throne Room")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Zoras Domain -> Snowpeak Climb Lower")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Zoras Domain West Ledge -> Zoras Domain")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Zoras Domain West Ledge -> Lanayru Field Behind Boulder")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Zoras Domain Throne Room -> Zoras Domain")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Outside Links House -> Ordon Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Outside Links House -> Ordon Spring")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Outside Links House -> Ordon Links House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Links House -> Outside Links House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Village -> Outside Links House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Village -> Ordon Ranch Entrance")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Village -> Ordon Seras Shop")
    set_rule(
        exit,
        lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance("Ordon Village -> Ordon Shield House")
    set_rule(
        exit,
        lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance("Ordon Village -> Ordon Sword House")
    set_rule(
        exit,
        lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance("Ordon Village -> Ordon Bos House Left Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Village -> Ordon Bos House Right Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Seras Shop -> Ordon Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Shield House -> Ordon Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Sword House -> Ordon Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Bos House Left Door -> Ordon Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Bos House Left Door -> Ordon Bos House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Bos House Right Door -> Ordon Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Bos House Right Door -> Ordon Bos House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Bos House -> Ordon Bos House Left Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Bos House -> Ordon Bos House Right Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Ranch Entrance -> Ordon Ranch")
    set_rule(
        exit,
        lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance("Ordon Ranch Entrance -> Ordon Village")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Ranch -> Ordon Ranch Entrance")
    set_rule(
        exit,
        lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance("Ordon Ranch -> Ordon Ranch Stable")
    set_rule(
        exit,
        lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance("Ordon Ranch Stable -> Ordon Ranch")
    set_rule(
        exit,
        lambda state: (can_change_time(state, player)),
    )

    exit = world.get_entrance("Ordon Ranch Stable -> Ordon Ranch Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Ordon Ranch Grotto -> Ordon Ranch Stable")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Spring -> Outside Links House")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Ordon Spring -> Ordon Bridge")
    set_rule(
        exit,
        lambda state: (
            True
            # (
            #     state.can_reach_region("Outside Links House", player)
            #     and has_sword(state, player)
            #     and state.has("Slingshot", player)
            # )
            # or (state._tp_skip_prologue(player))
        ),
    )

    exit = world.get_entrance("Ordon Bridge -> Ordon Spring")
    set_rule(
        exit,
        lambda state: (
            (
                state.can_reach_region("Outside Links House", player)
                and has_sword(state, player)
                and state.has("Slingshot", player)
            )
            # or (state._tp_skip_prologue(player))
        ),
    )

    exit = world.get_entrance("Ordon Bridge -> South Faron Woods")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Climb Lower -> Snowpeak Climb Upper")
    set_rule(
        exit,
        lambda state: (
            (
                (state._tp_skip_snowpeak_entrance(player))
                or (
                    state.can_reach_region("Zoras Domain", player)
                    and state.has("Progressive Fishing Rod", player, 2)
                )
            )
            and state.has("Shadow Crystal", player)
        ),
    )

    exit = world.get_entrance("Snowpeak Climb Lower -> Zoras Domain")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Climb Upper -> Snowpeak Climb Lower")
    set_rule(
        exit,
        lambda state: (
            (
                (state._tp_skip_snowpeak_entrance(player))
                or (
                    state.can_reach_region("Zoras Domain", player)
                    and state.has("Progressive Fishing Rod", player, 2)
                )
            )
            and state.has("Shadow Crystal", player)
        ),
    )

    exit = world.get_entrance("Snowpeak Climb Upper -> Snowpeak Summit Upper")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Snowpeak Climb Upper -> Snowpeak Ice Keese Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Snowpeak Climb Upper -> Snowpeak Freezard Grotto")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Snowpeak Ice Keese Grotto -> Snowpeak Climb Upper")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Freezard Grotto -> Snowpeak Climb Upper")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Summit Upper -> Snowpeak Summit Lower")
    set_rule(
        exit,
        lambda state: (
            can_defeat_ShadowBeast(state, player)
            and (
                (not state._tp_bonks_do_damage(player))
                or (
                    (state._tp_bonks_do_damage(player))
                    and (
                        (
                            state._tp_damage_magnification(player)
                            != DamageMagnification.option_ohko
                        )
                        or can_use_bottled_fairy(state, player)
                    )
                )
            )
        ),
    )

    exit = world.get_entrance("Snowpeak Summit Upper -> Snowpeak Climb Upper")
    set_rule(
        exit,
        lambda state: (state.has("Shadow Crystal", player)),
    )

    exit = world.get_entrance("Snowpeak Summit Lower -> Snowpeak Ruins Left Door")
    set_rule(
        exit,
        lambda state: (True),
    )

    exit = world.get_entrance("Snowpeak Summit Lower -> Snowpeak Ruins Right Door")
    set_rule(
        exit,
        lambda state: (True),
    )
