from typing import Dict
from BaseClasses import MultiWorld, Region
from ..Locations import TPLocation, LOCATION_TABLE
from ..options import SkipArbitersGroundsEntrance


def create_regions(multiworld: MultiWorld, player: int) -> Dict[str, Region]:
    regions: dict[str, Region] = {}

    # Create Menu region
    menu = Region("Menu", player, multiworld)
    regions["Menu"] = menu
    multiworld.regions.append(menu)

    arbiters_grounds_entrance = Region("Arbiters Grounds Entrance", player, multiworld)
    regions["Arbiters Grounds Entrance"] = arbiters_grounds_entrance
    multiworld.regions.append(arbiters_grounds_entrance)

    arbiters_grounds_lobby = Region("Arbiters Grounds Lobby", player, multiworld)
    regions["Arbiters Grounds Lobby"] = arbiters_grounds_lobby
    multiworld.regions.append(arbiters_grounds_lobby)

    arbiters_grounds_east_wing = Region(
        "Arbiters Grounds East Wing", player, multiworld
    )
    regions["Arbiters Grounds East Wing"] = arbiters_grounds_east_wing
    multiworld.regions.append(arbiters_grounds_east_wing)

    arbiters_grounds_west_wing = Region(
        "Arbiters Grounds West Wing", player, multiworld
    )
    regions["Arbiters Grounds West Wing"] = arbiters_grounds_west_wing
    multiworld.regions.append(arbiters_grounds_west_wing)

    arbiters_grounds_after_poe_gate = Region(
        "Arbiters Grounds After Poe Gate", player, multiworld
    )
    regions["Arbiters Grounds After Poe Gate"] = arbiters_grounds_after_poe_gate
    multiworld.regions.append(arbiters_grounds_after_poe_gate)

    arbiters_grounds_boss_room = Region(
        "Arbiters Grounds Boss Room", player, multiworld
    )
    regions["Arbiters Grounds Boss Room"] = arbiters_grounds_boss_room
    multiworld.regions.append(arbiters_grounds_boss_room)

    city_in_the_sky_boss_room = Region("City in The Sky Boss Room", player, multiworld)
    regions["City in The Sky Boss Room"] = city_in_the_sky_boss_room
    multiworld.regions.append(city_in_the_sky_boss_room)

    city_in_the_sky_central_tower_second_floor = Region(
        "City in The Sky Central Tower Second Floor", player, multiworld
    )
    regions["City in The Sky Central Tower Second Floor"] = (
        city_in_the_sky_central_tower_second_floor
    )
    multiworld.regions.append(city_in_the_sky_central_tower_second_floor)

    city_in_the_sky_east_wing = Region("City in The Sky East Wing", player, multiworld)
    regions["City in The Sky East Wing"] = city_in_the_sky_east_wing
    multiworld.regions.append(city_in_the_sky_east_wing)

    city_in_the_sky_entrance = Region("City in The Sky Entrance", player, multiworld)
    regions["City in The Sky Entrance"] = city_in_the_sky_entrance
    multiworld.regions.append(city_in_the_sky_entrance)

    city_in_the_sky_lobby = Region("City in The Sky Lobby", player, multiworld)
    regions["City in The Sky Lobby"] = city_in_the_sky_lobby
    multiworld.regions.append(city_in_the_sky_lobby)

    city_in_the_sky_north_wing = Region(
        "City in The Sky North Wing", player, multiworld
    )
    regions["City in The Sky North Wing"] = city_in_the_sky_north_wing
    multiworld.regions.append(city_in_the_sky_north_wing)

    city_in_the_sky_west_wing = Region("City in The Sky West Wing", player, multiworld)
    regions["City in The Sky West Wing"] = city_in_the_sky_west_wing
    multiworld.regions.append(city_in_the_sky_west_wing)

    forest_temple_boss_room = Region("Forest Temple Boss Room", player, multiworld)
    regions["Forest Temple Boss Room"] = forest_temple_boss_room
    multiworld.regions.append(forest_temple_boss_room)

    forest_temple_east_wing = Region("Forest Temple East Wing", player, multiworld)
    regions["Forest Temple East Wing"] = forest_temple_east_wing
    multiworld.regions.append(forest_temple_east_wing)

    forest_temple_entrance = Region("Forest Temple Entrance", player, multiworld)
    regions["Forest Temple Entrance"] = forest_temple_entrance
    multiworld.regions.append(forest_temple_entrance)

    forest_temple_lobby = Region("Forest Temple Lobby", player, multiworld)
    regions["Forest Temple Lobby"] = forest_temple_lobby
    multiworld.regions.append(forest_temple_lobby)

    forest_temple_north_wing = Region("Forest Temple North Wing", player, multiworld)
    regions["Forest Temple North Wing"] = forest_temple_north_wing
    multiworld.regions.append(forest_temple_north_wing)

    forest_temple_west_wing = Region("Forest Temple West Wing", player, multiworld)
    regions["Forest Temple West Wing"] = forest_temple_west_wing
    multiworld.regions.append(forest_temple_west_wing)

    ook = Region("Ook", player, multiworld)
    regions["Ook"] = ook
    multiworld.regions.append(ook)

    goron_mines_boss_room = Region("Goron Mines Boss Room", player, multiworld)
    regions["Goron Mines Boss Room"] = goron_mines_boss_room
    multiworld.regions.append(goron_mines_boss_room)

    goron_mines_crystal_switch_room = Region(
        "Goron Mines Crystal Switch Room", player, multiworld
    )
    regions["Goron Mines Crystal Switch Room"] = goron_mines_crystal_switch_room
    multiworld.regions.append(goron_mines_crystal_switch_room)

    goron_mines_entrance = Region("Goron Mines Entrance", player, multiworld)
    regions["Goron Mines Entrance"] = goron_mines_entrance
    multiworld.regions.append(goron_mines_entrance)

    goron_mines_lower_west_wing = Region(
        "Goron Mines Lower West Wing", player, multiworld
    )
    regions["Goron Mines Lower West Wing"] = goron_mines_lower_west_wing
    multiworld.regions.append(goron_mines_lower_west_wing)

    goron_mines_magnet_room = Region("Goron Mines Magnet Room", player, multiworld)
    regions["Goron Mines Magnet Room"] = goron_mines_magnet_room
    multiworld.regions.append(goron_mines_magnet_room)

    goron_mines_north_wing = Region("Goron Mines North Wing", player, multiworld)
    regions["Goron Mines North Wing"] = goron_mines_north_wing
    multiworld.regions.append(goron_mines_north_wing)

    goron_mines_upper_east_wing = Region(
        "Goron Mines Upper East Wing", player, multiworld
    )
    regions["Goron Mines Upper East Wing"] = goron_mines_upper_east_wing
    multiworld.regions.append(goron_mines_upper_east_wing)

    ganondorf_castle = Region("Ganondorf Castle", player, multiworld)
    regions["Ganondorf Castle"] = ganondorf_castle
    multiworld.regions.append(ganondorf_castle)

    hyrule_castle_entrance = Region("Hyrule Castle Entrance", player, multiworld)
    regions["Hyrule Castle Entrance"] = hyrule_castle_entrance
    multiworld.regions.append(hyrule_castle_entrance)

    hyrule_castle_graveyard = Region("Hyrule Castle Graveyard", player, multiworld)
    regions["Hyrule Castle Graveyard"] = hyrule_castle_graveyard
    multiworld.regions.append(hyrule_castle_graveyard)

    hyrule_castle_inside_east_wing = Region(
        "Hyrule Castle Inside East Wing", player, multiworld
    )
    regions["Hyrule Castle Inside East Wing"] = hyrule_castle_inside_east_wing
    multiworld.regions.append(hyrule_castle_inside_east_wing)

    hyrule_castle_inside_west_wing = Region(
        "Hyrule Castle Inside West Wing", player, multiworld
    )
    regions["Hyrule Castle Inside West Wing"] = hyrule_castle_inside_west_wing
    multiworld.regions.append(hyrule_castle_inside_west_wing)

    hyrule_castle_main_hall = Region("Hyrule Castle Main Hall", player, multiworld)
    regions["Hyrule Castle Main Hall"] = hyrule_castle_main_hall
    multiworld.regions.append(hyrule_castle_main_hall)

    hyrule_castle_outside_east_wing = Region(
        "Hyrule Castle Outside East Wing", player, multiworld
    )
    regions["Hyrule Castle Outside East Wing"] = hyrule_castle_outside_east_wing
    multiworld.regions.append(hyrule_castle_outside_east_wing)

    hyrule_castle_outside_west_wing = Region(
        "Hyrule Castle Outside West Wing", player, multiworld
    )
    regions["Hyrule Castle Outside West Wing"] = hyrule_castle_outside_west_wing
    multiworld.regions.append(hyrule_castle_outside_west_wing)

    hyrule_castle_third_floor_balcony = Region(
        "Hyrule Castle Third Floor Balcony", player, multiworld
    )
    regions["Hyrule Castle Third Floor Balcony"] = hyrule_castle_third_floor_balcony
    multiworld.regions.append(hyrule_castle_third_floor_balcony)

    hyrule_castle_tower_climb = Region("Hyrule Castle Tower Climb", player, multiworld)
    regions["Hyrule Castle Tower Climb"] = hyrule_castle_tower_climb
    multiworld.regions.append(hyrule_castle_tower_climb)

    hyrule_castle_treasure_room = Region(
        "Hyrule Castle Treasure Room", player, multiworld
    )
    regions["Hyrule Castle Treasure Room"] = hyrule_castle_treasure_room
    multiworld.regions.append(hyrule_castle_treasure_room)

    lakebed_temple_boss_room = Region("Lakebed Temple Boss Room", player, multiworld)
    regions["Lakebed Temple Boss Room"] = lakebed_temple_boss_room
    multiworld.regions.append(lakebed_temple_boss_room)

    lakebed_temple_central_room = Region(
        "Lakebed Temple Central Room", player, multiworld
    )
    regions["Lakebed Temple Central Room"] = lakebed_temple_central_room
    multiworld.regions.append(lakebed_temple_central_room)

    lakebed_temple_east_wing_first_floor = Region(
        "Lakebed Temple East Wing First Floor", player, multiworld
    )
    regions["Lakebed Temple East Wing First Floor"] = (
        lakebed_temple_east_wing_first_floor
    )
    multiworld.regions.append(lakebed_temple_east_wing_first_floor)

    lakebed_temple_east_wing_second_floor = Region(
        "Lakebed Temple East Wing Second Floor", player, multiworld
    )
    regions["Lakebed Temple East Wing Second Floor"] = (
        lakebed_temple_east_wing_second_floor
    )
    multiworld.regions.append(lakebed_temple_east_wing_second_floor)

    lakebed_temple_entrance = Region("Lakebed Temple Entrance", player, multiworld)
    regions["Lakebed Temple Entrance"] = lakebed_temple_entrance
    multiworld.regions.append(lakebed_temple_entrance)

    lakebed_temple_west_wing = Region("Lakebed Temple West Wing", player, multiworld)
    regions["Lakebed Temple West Wing"] = lakebed_temple_west_wing
    multiworld.regions.append(lakebed_temple_west_wing)

    palace_of_twilight_entrance = Region(
        "Palace of Twilight Entrance", player, multiworld
    )
    regions["Palace of Twilight Entrance"] = palace_of_twilight_entrance
    multiworld.regions.append(palace_of_twilight_entrance)

    palace_of_twilight_west_wing = Region(
        "Palace of Twilight West Wing", player, multiworld
    )
    regions["Palace of Twilight West Wing"] = palace_of_twilight_west_wing
    multiworld.regions.append(palace_of_twilight_west_wing)

    palace_of_twilight_east_wing = Region(
        "Palace of Twilight East Wing", player, multiworld
    )
    regions["Palace of Twilight East Wing"] = palace_of_twilight_east_wing
    multiworld.regions.append(palace_of_twilight_east_wing)

    palace_of_twilight_central_first_room = Region(
        "Palace of Twilight Central First Room", player, multiworld
    )
    regions["Palace of Twilight Central First Room"] = (
        palace_of_twilight_central_first_room
    )
    multiworld.regions.append(palace_of_twilight_central_first_room)

    palace_of_twilight_outside_room = Region(
        "Palace of Twilight Outside Room", player, multiworld
    )
    regions["Palace of Twilight Outside Room"] = palace_of_twilight_outside_room
    multiworld.regions.append(palace_of_twilight_outside_room)

    palace_of_twilight_north_tower = Region(
        "Palace of Twilight North Tower", player, multiworld
    )
    regions["Palace of Twilight North Tower"] = palace_of_twilight_north_tower
    multiworld.regions.append(palace_of_twilight_north_tower)

    palace_of_twilight_boss_room = Region(
        "Palace of Twilight Boss Room", player, multiworld
    )
    regions["Palace of Twilight Boss Room"] = palace_of_twilight_boss_room
    multiworld.regions.append(palace_of_twilight_boss_room)

    snowpeak_ruins_left_door = Region("Snowpeak Ruins Left Door", player, multiworld)
    regions["Snowpeak Ruins Left Door"] = snowpeak_ruins_left_door
    multiworld.regions.append(snowpeak_ruins_left_door)

    snowpeak_ruins_right_door = Region("Snowpeak Ruins Right Door", player, multiworld)
    regions["Snowpeak Ruins Right Door"] = snowpeak_ruins_right_door
    multiworld.regions.append(snowpeak_ruins_right_door)

    snowpeak_ruins_boss_room = Region("Snowpeak Ruins Boss Room", player, multiworld)
    regions["Snowpeak Ruins Boss Room"] = snowpeak_ruins_boss_room
    multiworld.regions.append(snowpeak_ruins_boss_room)

    snowpeak_ruins_caged_freezard_room = Region(
        "Snowpeak Ruins Caged Freezard Room", player, multiworld
    )
    regions["Snowpeak Ruins Caged Freezard Room"] = snowpeak_ruins_caged_freezard_room
    multiworld.regions.append(snowpeak_ruins_caged_freezard_room)

    snowpeak_ruins_chapel = Region("Snowpeak Ruins Chapel", player, multiworld)
    regions["Snowpeak Ruins Chapel"] = snowpeak_ruins_chapel
    multiworld.regions.append(snowpeak_ruins_chapel)

    snowpeak_ruins_darkhammer_room = Region(
        "Snowpeak Ruins Darkhammer Room", player, multiworld
    )
    regions["Snowpeak Ruins Darkhammer Room"] = snowpeak_ruins_darkhammer_room
    multiworld.regions.append(snowpeak_ruins_darkhammer_room)

    snowpeak_ruins_east_courtyard = Region(
        "Snowpeak Ruins East Courtyard", player, multiworld
    )
    regions["Snowpeak Ruins East Courtyard"] = snowpeak_ruins_east_courtyard
    multiworld.regions.append(snowpeak_ruins_east_courtyard)

    snowpeak_ruins_entrance = Region("Snowpeak Ruins Entrance", player, multiworld)
    regions["Snowpeak Ruins Entrance"] = snowpeak_ruins_entrance
    multiworld.regions.append(snowpeak_ruins_entrance)

    snowpeak_ruins_northeast_chilfos_room_first_floor = Region(
        "Snowpeak Ruins Northeast Chilfos Room First Floor", player, multiworld
    )
    regions["Snowpeak Ruins Northeast Chilfos Room First Floor"] = (
        snowpeak_ruins_northeast_chilfos_room_first_floor
    )
    multiworld.regions.append(snowpeak_ruins_northeast_chilfos_room_first_floor)

    snowpeak_ruins_northeast_chilfos_room_second_floor = Region(
        "Snowpeak Ruins Northeast Chilfos Room Second Floor", player, multiworld
    )
    regions["Snowpeak Ruins Northeast Chilfos Room Second Floor"] = (
        snowpeak_ruins_northeast_chilfos_room_second_floor
    )
    multiworld.regions.append(snowpeak_ruins_northeast_chilfos_room_second_floor)

    snowpeak_ruins_second_floor_mini_freezard_room = Region(
        "Snowpeak Ruins Second Floor Mini Freezard Room", player, multiworld
    )
    regions["Snowpeak Ruins Second Floor Mini Freezard Room"] = (
        snowpeak_ruins_second_floor_mini_freezard_room
    )
    multiworld.regions.append(snowpeak_ruins_second_floor_mini_freezard_room)

    snowpeak_ruins_west_cannon_room = Region(
        "Snowpeak Ruins West Cannon Room", player, multiworld
    )
    regions["Snowpeak Ruins West Cannon Room"] = snowpeak_ruins_west_cannon_room
    multiworld.regions.append(snowpeak_ruins_west_cannon_room)

    snowpeak_ruins_west_courtyard = Region(
        "Snowpeak Ruins West Courtyard", player, multiworld
    )
    regions["Snowpeak Ruins West Courtyard"] = snowpeak_ruins_west_courtyard
    multiworld.regions.append(snowpeak_ruins_west_courtyard)

    snowpeak_ruins_wooden_beam_room = Region(
        "Snowpeak Ruins Wooden Beam Room", player, multiworld
    )
    regions["Snowpeak Ruins Wooden Beam Room"] = snowpeak_ruins_wooden_beam_room
    multiworld.regions.append(snowpeak_ruins_wooden_beam_room)

    snowpeak_ruins_yeto_and_yeta = Region(
        "Snowpeak Ruins Yeto and Yeta", player, multiworld
    )
    regions["Snowpeak Ruins Yeto and Yeta"] = snowpeak_ruins_yeto_and_yeta
    multiworld.regions.append(snowpeak_ruins_yeto_and_yeta)

    temple_of_time_armos_antechamber = Region(
        "Temple of Time Armos Antechamber", player, multiworld
    )
    regions["Temple of Time Armos Antechamber"] = temple_of_time_armos_antechamber
    multiworld.regions.append(temple_of_time_armos_antechamber)

    temple_of_time_boss_room = Region("Temple of Time Boss Room", player, multiworld)
    regions["Temple of Time Boss Room"] = temple_of_time_boss_room
    multiworld.regions.append(temple_of_time_boss_room)

    temple_of_time_central_mechanical_platform = Region(
        "Temple of Time Central Mechanical Platform", player, multiworld
    )
    regions["Temple of Time Central Mechanical Platform"] = (
        temple_of_time_central_mechanical_platform
    )
    multiworld.regions.append(temple_of_time_central_mechanical_platform)

    temple_of_time_connecting_corridors = Region(
        "Temple of Time Connecting Corridors", player, multiworld
    )
    regions["Temple of Time Connecting Corridors"] = temple_of_time_connecting_corridors
    multiworld.regions.append(temple_of_time_connecting_corridors)

    temple_of_time_crumbling_corridor = Region(
        "Temple of Time Crumbling Corridor", player, multiworld
    )
    regions["Temple of Time Crumbling Corridor"] = temple_of_time_crumbling_corridor
    multiworld.regions.append(temple_of_time_crumbling_corridor)

    temple_of_time_darknut_arena = Region(
        "Temple of Time Darknut Arena", player, multiworld
    )
    regions["Temple of Time Darknut Arena"] = temple_of_time_darknut_arena
    multiworld.regions.append(temple_of_time_darknut_arena)

    temple_of_time_entrance = Region("Temple of Time Entrance", player, multiworld)
    regions["Temple of Time Entrance"] = temple_of_time_entrance
    multiworld.regions.append(temple_of_time_entrance)

    temple_of_time_floor_switch_puzzle_room = Region(
        "Temple of Time Floor Switch Puzzle Room", player, multiworld
    )
    regions["Temple of Time Floor Switch Puzzle Room"] = (
        temple_of_time_floor_switch_puzzle_room
    )
    multiworld.regions.append(temple_of_time_floor_switch_puzzle_room)

    temple_of_time_moving_wall_hallways = Region(
        "Temple of Time Moving Wall Hallways", player, multiworld
    )
    regions["Temple of Time Moving Wall Hallways"] = temple_of_time_moving_wall_hallways
    multiworld.regions.append(temple_of_time_moving_wall_hallways)

    temple_of_time_scales_of_time = Region(
        "Temple of Time Scales of Time", player, multiworld
    )
    regions["Temple of Time Scales of Time"] = temple_of_time_scales_of_time
    multiworld.regions.append(temple_of_time_scales_of_time)

    temple_of_time_upper_spike_trap_corridor = Region(
        "Temple of Time Upper Spike Trap Corridor", player, multiworld
    )
    regions["Temple of Time Upper Spike Trap Corridor"] = (
        temple_of_time_upper_spike_trap_corridor
    )
    multiworld.regions.append(temple_of_time_upper_spike_trap_corridor)

    death_mountain_near_kakariko = Region(
        "Death Mountain Near Kakariko", player, multiworld
    )
    regions["Death Mountain Near Kakariko"] = death_mountain_near_kakariko
    multiworld.regions.append(death_mountain_near_kakariko)

    death_mountain_trail = Region("Death Mountain Trail", player, multiworld)
    regions["Death Mountain Trail"] = death_mountain_trail
    multiworld.regions.append(death_mountain_trail)

    death_mountain_volcano = Region("Death Mountain Volcano", player, multiworld)
    regions["Death Mountain Volcano"] = death_mountain_volcano
    multiworld.regions.append(death_mountain_volcano)

    death_mountain_outside_sumo_hall = Region(
        "Death Mountain Outside Sumo Hall", player, multiworld
    )
    regions["Death Mountain Outside Sumo Hall"] = death_mountain_outside_sumo_hall
    multiworld.regions.append(death_mountain_outside_sumo_hall)

    death_mountain_elevator_lower = Region(
        "Death Mountain Elevator Lower", player, multiworld
    )
    regions["Death Mountain Elevator Lower"] = death_mountain_elevator_lower
    multiworld.regions.append(death_mountain_elevator_lower)

    death_mountain_sumo_hall = Region("Death Mountain Sumo Hall", player, multiworld)
    regions["Death Mountain Sumo Hall"] = death_mountain_sumo_hall
    multiworld.regions.append(death_mountain_sumo_hall)

    death_mountain_sumo_hall_elevator = Region(
        "Death Mountain Sumo Hall Elevator", player, multiworld
    )
    regions["Death Mountain Sumo Hall Elevator"] = death_mountain_sumo_hall_elevator
    multiworld.regions.append(death_mountain_sumo_hall_elevator)

    death_mountain_sumo_hall_goron_mines_tunnel = Region(
        "Death Mountain Sumo Hall Goron Mines Tunnel", player, multiworld
    )
    regions["Death Mountain Sumo Hall Goron Mines Tunnel"] = (
        death_mountain_sumo_hall_goron_mines_tunnel
    )
    multiworld.regions.append(death_mountain_sumo_hall_goron_mines_tunnel)

    hidden_village = Region("Hidden Village", player, multiworld)
    regions["Hidden Village"] = hidden_village
    multiworld.regions.append(hidden_village)

    hidden_village_impaz_house = Region(
        "Hidden Village Impaz House", player, multiworld
    )
    regions["Hidden Village Impaz House"] = hidden_village_impaz_house
    multiworld.regions.append(hidden_village_impaz_house)

    kakariko_gorge = Region("Kakariko Gorge", player, multiworld)
    regions["Kakariko Gorge"] = kakariko_gorge
    multiworld.regions.append(kakariko_gorge)

    kakariko_gorge_cave_entrance = Region(
        "Kakariko Gorge Cave Entrance", player, multiworld
    )
    regions["Kakariko Gorge Cave Entrance"] = kakariko_gorge_cave_entrance
    multiworld.regions.append(kakariko_gorge_cave_entrance)

    kakariko_gorge_behind_gate = Region(
        "Kakariko Gorge Behind Gate", player, multiworld
    )
    regions["Kakariko Gorge Behind Gate"] = kakariko_gorge_behind_gate
    multiworld.regions.append(kakariko_gorge_behind_gate)

    eldin_lantern_cave = Region("Eldin Lantern Cave", player, multiworld)
    regions["Eldin Lantern Cave"] = eldin_lantern_cave
    multiworld.regions.append(eldin_lantern_cave)

    kakariko_gorge_keese_grotto = Region(
        "Kakariko Gorge Keese Grotto", player, multiworld
    )
    regions["Kakariko Gorge Keese Grotto"] = kakariko_gorge_keese_grotto
    multiworld.regions.append(kakariko_gorge_keese_grotto)

    eldin_field = Region("Eldin Field", player, multiworld)
    regions["Eldin Field"] = eldin_field
    multiworld.regions.append(eldin_field)

    eldin_field_near_castle_town = Region(
        "Eldin Field Near Castle Town", player, multiworld
    )
    regions["Eldin Field Near Castle Town"] = eldin_field_near_castle_town
    multiworld.regions.append(eldin_field_near_castle_town)

    eldin_field_lava_cave_ledge = Region(
        "Eldin Field Lava Cave Ledge", player, multiworld
    )
    regions["Eldin Field Lava Cave Ledge"] = eldin_field_lava_cave_ledge
    multiworld.regions.append(eldin_field_lava_cave_ledge)

    eldin_field_from_lava_cave_lower = Region(
        "Eldin Field From Lava Cave Lower", player, multiworld
    )
    regions["Eldin Field From Lava Cave Lower"] = eldin_field_from_lava_cave_lower
    multiworld.regions.append(eldin_field_from_lava_cave_lower)

    north_eldin_field = Region("North Eldin Field", player, multiworld)
    regions["North Eldin Field"] = north_eldin_field
    multiworld.regions.append(north_eldin_field)

    eldin_field_outside_hidden_village = Region(
        "Eldin Field Outside Hidden Village", player, multiworld
    )
    regions["Eldin Field Outside Hidden Village"] = eldin_field_outside_hidden_village
    multiworld.regions.append(eldin_field_outside_hidden_village)

    eldin_field_grotto_platform = Region(
        "Eldin Field Grotto Platform", player, multiworld
    )
    regions["Eldin Field Grotto Platform"] = eldin_field_grotto_platform
    multiworld.regions.append(eldin_field_grotto_platform)

    eldin_field_lava_cave_upper = Region(
        "Eldin Field Lava Cave Upper", player, multiworld
    )
    regions["Eldin Field Lava Cave Upper"] = eldin_field_lava_cave_upper
    multiworld.regions.append(eldin_field_lava_cave_upper)

    eldin_field_lava_cave_lower = Region(
        "Eldin Field Lava Cave Lower", player, multiworld
    )
    regions["Eldin Field Lava Cave Lower"] = eldin_field_lava_cave_lower
    multiworld.regions.append(eldin_field_lava_cave_lower)

    eldin_field_bomskit_grotto = Region(
        "Eldin Field Bomskit Grotto", player, multiworld
    )
    regions["Eldin Field Bomskit Grotto"] = eldin_field_bomskit_grotto
    multiworld.regions.append(eldin_field_bomskit_grotto)

    eldin_field_water_bomb_fish_grotto = Region(
        "Eldin Field Water Bomb Fish Grotto", player, multiworld
    )
    regions["Eldin Field Water Bomb Fish Grotto"] = eldin_field_water_bomb_fish_grotto
    multiworld.regions.append(eldin_field_water_bomb_fish_grotto)

    eldin_field_stalfos_grotto = Region(
        "Eldin Field Stalfos Grotto", player, multiworld
    )
    regions["Eldin Field Stalfos Grotto"] = eldin_field_stalfos_grotto
    multiworld.regions.append(eldin_field_stalfos_grotto)

    lower_kakariko_village = Region("Lower Kakariko Village", player, multiworld)
    regions["Lower Kakariko Village"] = lower_kakariko_village
    multiworld.regions.append(lower_kakariko_village)

    upper_kakariko_village = Region("Upper Kakariko Village", player, multiworld)
    regions["Upper Kakariko Village"] = upper_kakariko_village
    multiworld.regions.append(upper_kakariko_village)

    kakariko_top_of_watchtower = Region(
        "Kakariko Top of Watchtower", player, multiworld
    )
    regions["Kakariko Top of Watchtower"] = kakariko_top_of_watchtower
    multiworld.regions.append(kakariko_top_of_watchtower)

    kakariko_village_behind_gate = Region(
        "Kakariko Village Behind Gate", player, multiworld
    )
    regions["Kakariko Village Behind Gate"] = kakariko_village_behind_gate
    multiworld.regions.append(kakariko_village_behind_gate)

    kakariko_renados_sanctuary_front_left_door = Region(
        "Kakariko Renados Sanctuary Front Left Door", player, multiworld
    )
    regions["Kakariko Renados Sanctuary Front Left Door"] = (
        kakariko_renados_sanctuary_front_left_door
    )
    multiworld.regions.append(kakariko_renados_sanctuary_front_left_door)

    kakariko_renados_sanctuary_front_right_door = Region(
        "Kakariko Renados Sanctuary Front Right Door", player, multiworld
    )
    regions["Kakariko Renados Sanctuary Front Right Door"] = (
        kakariko_renados_sanctuary_front_right_door
    )
    multiworld.regions.append(kakariko_renados_sanctuary_front_right_door)

    kakariko_renados_sanctuary_back_left_door = Region(
        "Kakariko Renados Sanctuary Back Left Door", player, multiworld
    )
    regions["Kakariko Renados Sanctuary Back Left Door"] = (
        kakariko_renados_sanctuary_back_left_door
    )
    multiworld.regions.append(kakariko_renados_sanctuary_back_left_door)

    kakariko_renados_sanctuary_back_right_door = Region(
        "Kakariko Renados Sanctuary Back Right Door", player, multiworld
    )
    regions["Kakariko Renados Sanctuary Back Right Door"] = (
        kakariko_renados_sanctuary_back_right_door
    )
    multiworld.regions.append(kakariko_renados_sanctuary_back_right_door)

    kakariko_renados_sanctuary = Region(
        "Kakariko Renados Sanctuary", player, multiworld
    )
    regions["Kakariko Renados Sanctuary"] = kakariko_renados_sanctuary
    multiworld.regions.append(kakariko_renados_sanctuary)

    kakariko_renados_sanctuary_basement = Region(
        "Kakariko Renados Sanctuary Basement", player, multiworld
    )
    regions["Kakariko Renados Sanctuary Basement"] = kakariko_renados_sanctuary_basement
    multiworld.regions.append(kakariko_renados_sanctuary_basement)

    kakariko_malo_mart = Region("Kakariko Malo Mart", player, multiworld)
    regions["Kakariko Malo Mart"] = kakariko_malo_mart
    multiworld.regions.append(kakariko_malo_mart)

    kakariko_elde_inn_left_door = Region(
        "Kakariko Elde Inn Left Door", player, multiworld
    )
    regions["Kakariko Elde Inn Left Door"] = kakariko_elde_inn_left_door
    multiworld.regions.append(kakariko_elde_inn_left_door)

    kakariko_elde_inn_right_door = Region(
        "Kakariko Elde Inn Right Door", player, multiworld
    )
    regions["Kakariko Elde Inn Right Door"] = kakariko_elde_inn_right_door
    multiworld.regions.append(kakariko_elde_inn_right_door)

    kakariko_elde_inn = Region("Kakariko Elde Inn", player, multiworld)
    regions["Kakariko Elde Inn"] = kakariko_elde_inn
    multiworld.regions.append(kakariko_elde_inn)

    kakariko_bug_house_door = Region("Kakariko Bug House Door", player, multiworld)
    regions["Kakariko Bug House Door"] = kakariko_bug_house_door
    multiworld.regions.append(kakariko_bug_house_door)

    kakariko_bug_house_ceiling_hole = Region(
        "Kakariko Bug House Ceiling Hole", player, multiworld
    )
    regions["Kakariko Bug House Ceiling Hole"] = kakariko_bug_house_ceiling_hole
    multiworld.regions.append(kakariko_bug_house_ceiling_hole)

    kakariko_bug_house = Region("Kakariko Bug House", player, multiworld)
    regions["Kakariko Bug House"] = kakariko_bug_house
    multiworld.regions.append(kakariko_bug_house)

    kakariko_barnes_bomb_shop_lower = Region(
        "Kakariko Barnes Bomb Shop Lower", player, multiworld
    )
    regions["Kakariko Barnes Bomb Shop Lower"] = kakariko_barnes_bomb_shop_lower
    multiworld.regions.append(kakariko_barnes_bomb_shop_lower)

    kakariko_barnes_bomb_shop_upper = Region(
        "Kakariko Barnes Bomb Shop Upper", player, multiworld
    )
    regions["Kakariko Barnes Bomb Shop Upper"] = kakariko_barnes_bomb_shop_upper
    multiworld.regions.append(kakariko_barnes_bomb_shop_upper)

    kakariko_watchtower_lower_door = Region(
        "Kakariko Watchtower Lower Door", player, multiworld
    )
    regions["Kakariko Watchtower Lower Door"] = kakariko_watchtower_lower_door
    multiworld.regions.append(kakariko_watchtower_lower_door)

    kakariko_watchtower_dig_spot = Region(
        "Kakariko Watchtower Dig Spot", player, multiworld
    )
    regions["Kakariko Watchtower Dig Spot"] = kakariko_watchtower_dig_spot
    multiworld.regions.append(kakariko_watchtower_dig_spot)

    kakariko_watchtower_upper_door = Region(
        "Kakariko Watchtower Upper Door", player, multiworld
    )
    regions["Kakariko Watchtower Upper Door"] = kakariko_watchtower_upper_door
    multiworld.regions.append(kakariko_watchtower_upper_door)

    kakariko_watchtower = Region("Kakariko Watchtower", player, multiworld)
    regions["Kakariko Watchtower"] = kakariko_watchtower
    multiworld.regions.append(kakariko_watchtower)

    kakariko_graveyard = Region("Kakariko Graveyard", player, multiworld)
    regions["Kakariko Graveyard"] = kakariko_graveyard
    multiworld.regions.append(kakariko_graveyard)

    south_faron_woods = Region("South Faron Woods", player, multiworld)
    regions["South Faron Woods"] = south_faron_woods
    multiworld.regions.append(south_faron_woods)

    south_faron_woods_behind_gate = Region(
        "South Faron Woods Behind Gate", player, multiworld
    )
    regions["South Faron Woods Behind Gate"] = south_faron_woods_behind_gate
    multiworld.regions.append(south_faron_woods_behind_gate)

    south_faron_woods_coros_ledge = Region(
        "South Faron Woods Coros Ledge", player, multiworld
    )
    regions["South Faron Woods Coros Ledge"] = south_faron_woods_coros_ledge
    multiworld.regions.append(south_faron_woods_coros_ledge)

    south_faron_woods_owl_statue_area = Region(
        "South Faron Woods Owl Statue Area", player, multiworld
    )
    regions["South Faron Woods Owl Statue Area"] = south_faron_woods_owl_statue_area
    multiworld.regions.append(south_faron_woods_owl_statue_area)

    south_faron_woods_above_owl_statue = Region(
        "South Faron Woods Above Owl Statue", player, multiworld
    )
    regions["South Faron Woods Above Owl Statue"] = south_faron_woods_above_owl_statue
    multiworld.regions.append(south_faron_woods_above_owl_statue)

    faron_woods_coros_house_lower = Region(
        "Faron Woods Coros House Lower", player, multiworld
    )
    regions["Faron Woods Coros House Lower"] = faron_woods_coros_house_lower
    multiworld.regions.append(faron_woods_coros_house_lower)

    faron_woods_coros_house_upper = Region(
        "Faron Woods Coros House Upper", player, multiworld
    )
    regions["Faron Woods Coros House Upper"] = faron_woods_coros_house_upper
    multiworld.regions.append(faron_woods_coros_house_upper)

    faron_woods_cave_southern_entrance = Region(
        "Faron Woods Cave Southern Entrance", player, multiworld
    )
    regions["Faron Woods Cave Southern Entrance"] = faron_woods_cave_southern_entrance
    multiworld.regions.append(faron_woods_cave_southern_entrance)

    faron_woods_cave = Region("Faron Woods Cave", player, multiworld)
    regions["Faron Woods Cave"] = faron_woods_cave
    multiworld.regions.append(faron_woods_cave)

    mist_area_near_faron_woods_cave = Region(
        "Mist Area Near Faron Woods Cave", player, multiworld
    )
    regions["Mist Area Near Faron Woods Cave"] = mist_area_near_faron_woods_cave
    multiworld.regions.append(mist_area_near_faron_woods_cave)

    mist_area_inside_mist = Region("Mist Area Inside Mist", player, multiworld)
    regions["Mist Area Inside Mist"] = mist_area_inside_mist
    multiworld.regions.append(mist_area_inside_mist)

    mist_area_under_owl_statue_chest = Region(
        "Mist Area Under Owl Statue Chest", player, multiworld
    )
    regions["Mist Area Under Owl Statue Chest"] = mist_area_under_owl_statue_chest
    multiworld.regions.append(mist_area_under_owl_statue_chest)

    mist_area_near_owl_statue_chest = Region(
        "Mist Area Near Owl Statue Chest", player, multiworld
    )
    regions["Mist Area Near Owl Statue Chest"] = mist_area_near_owl_statue_chest
    multiworld.regions.append(mist_area_near_owl_statue_chest)

    mist_area_center_stump = Region("Mist Area Center Stump", player, multiworld)
    regions["Mist Area Center Stump"] = mist_area_center_stump
    multiworld.regions.append(mist_area_center_stump)

    mist_area_outside_faron_mist_cave = Region(
        "Mist Area Outside Faron Mist Cave", player, multiworld
    )
    regions["Mist Area Outside Faron Mist Cave"] = mist_area_outside_faron_mist_cave
    multiworld.regions.append(mist_area_outside_faron_mist_cave)

    mist_area_near_north_faron_woods = Region(
        "Mist Area Near North Faron Woods", player, multiworld
    )
    regions["Mist Area Near North Faron Woods"] = mist_area_near_north_faron_woods
    multiworld.regions.append(mist_area_near_north_faron_woods)

    faron_woods_cave_northern_entrance = Region(
        "Faron Woods Cave Northern Entrance", player, multiworld
    )
    regions["Faron Woods Cave Northern Entrance"] = faron_woods_cave_northern_entrance
    multiworld.regions.append(faron_woods_cave_northern_entrance)

    mist_area_faron_mist_cave = Region("Mist Area Faron Mist Cave", player, multiworld)
    regions["Mist Area Faron Mist Cave"] = mist_area_faron_mist_cave
    multiworld.regions.append(mist_area_faron_mist_cave)

    north_faron_woods = Region("North Faron Woods", player, multiworld)
    regions["North Faron Woods"] = north_faron_woods
    multiworld.regions.append(north_faron_woods)

    faron_field = Region("Faron Field", player, multiworld)
    regions["Faron Field"] = faron_field
    multiworld.regions.append(faron_field)

    faron_field_behind_boulder = Region(
        "Faron Field Behind Boulder", player, multiworld
    )
    regions["Faron Field Behind Boulder"] = faron_field_behind_boulder
    multiworld.regions.append(faron_field_behind_boulder)

    faron_field_corner_grotto = Region("Faron Field Corner Grotto", player, multiworld)
    regions["Faron Field Corner Grotto"] = faron_field_corner_grotto
    multiworld.regions.append(faron_field_corner_grotto)

    faron_field_fishing_grotto = Region(
        "Faron Field Fishing Grotto", player, multiworld
    )
    regions["Faron Field Fishing Grotto"] = faron_field_fishing_grotto
    multiworld.regions.append(faron_field_fishing_grotto)

    lost_woods = Region("Lost Woods", player, multiworld)
    regions["Lost Woods"] = lost_woods
    multiworld.regions.append(lost_woods)

    lost_woods_lower_battle_arena = Region(
        "Lost Woods Lower Battle Arena", player, multiworld
    )
    regions["Lost Woods Lower Battle Arena"] = lost_woods_lower_battle_arena
    multiworld.regions.append(lost_woods_lower_battle_arena)

    lost_woods_upper_battle_arena = Region(
        "Lost Woods Upper Battle Arena", player, multiworld
    )
    regions["Lost Woods Upper Battle Arena"] = lost_woods_upper_battle_arena
    multiworld.regions.append(lost_woods_upper_battle_arena)

    lost_woods_baba_serpent_grotto = Region(
        "Lost Woods Baba Serpent Grotto", player, multiworld
    )
    regions["Lost Woods Baba Serpent Grotto"] = lost_woods_baba_serpent_grotto
    multiworld.regions.append(lost_woods_baba_serpent_grotto)

    sacred_grove_before_block = Region("Sacred Grove Before Block", player, multiworld)
    regions["Sacred Grove Before Block"] = sacred_grove_before_block
    multiworld.regions.append(sacred_grove_before_block)

    sacred_grove_upper = Region("Sacred Grove Upper", player, multiworld)
    regions["Sacred Grove Upper"] = sacred_grove_upper
    multiworld.regions.append(sacred_grove_upper)

    sacred_grove_lower = Region("Sacred Grove Lower", player, multiworld)
    regions["Sacred Grove Lower"] = sacred_grove_lower
    multiworld.regions.append(sacred_grove_lower)

    sacred_grove_past = Region("Sacred Grove Past", player, multiworld)
    regions["Sacred Grove Past"] = sacred_grove_past
    multiworld.regions.append(sacred_grove_past)

    sacred_grove_past_behind_window = Region(
        "Sacred Grove Past Behind Window", player, multiworld
    )
    regions["Sacred Grove Past Behind Window"] = sacred_grove_past_behind_window
    multiworld.regions.append(sacred_grove_past_behind_window)

    gerudo_desert_cave_of_ordeals_floors_01_11 = Region(
        "Gerudo Desert Cave of Ordeals Floors 01-11", player, multiworld
    )
    regions["Gerudo Desert Cave of Ordeals Floors 01-11"] = (
        gerudo_desert_cave_of_ordeals_floors_01_11
    )
    multiworld.regions.append(gerudo_desert_cave_of_ordeals_floors_01_11)

    gerudo_desert_cave_of_ordeals_floors_12_21 = Region(
        "Gerudo Desert Cave of Ordeals Floors 12-21", player, multiworld
    )
    regions["Gerudo Desert Cave of Ordeals Floors 12-21"] = (
        gerudo_desert_cave_of_ordeals_floors_12_21
    )
    multiworld.regions.append(gerudo_desert_cave_of_ordeals_floors_12_21)

    gerudo_desert_cave_of_ordeals_floors_22_31 = Region(
        "Gerudo Desert Cave of Ordeals Floors 22-31", player, multiworld
    )
    regions["Gerudo Desert Cave of Ordeals Floors 22-31"] = (
        gerudo_desert_cave_of_ordeals_floors_22_31
    )
    multiworld.regions.append(gerudo_desert_cave_of_ordeals_floors_22_31)

    gerudo_desert_cave_of_ordeals_floors_32_41 = Region(
        "Gerudo Desert Cave of Ordeals Floors 32-41", player, multiworld
    )
    regions["Gerudo Desert Cave of Ordeals Floors 32-41"] = (
        gerudo_desert_cave_of_ordeals_floors_32_41
    )
    multiworld.regions.append(gerudo_desert_cave_of_ordeals_floors_32_41)

    gerudo_desert_cave_of_ordeals_floors_42_50 = Region(
        "Gerudo Desert Cave of Ordeals Floors 42-50", player, multiworld
    )
    regions["Gerudo Desert Cave of Ordeals Floors 42-50"] = (
        gerudo_desert_cave_of_ordeals_floors_42_50
    )
    multiworld.regions.append(gerudo_desert_cave_of_ordeals_floors_42_50)

    gerudo_desert = Region("Gerudo Desert", player, multiworld)
    regions["Gerudo Desert"] = gerudo_desert
    multiworld.regions.append(gerudo_desert)

    gerudo_desert_cave_of_ordeals_plateau = Region(
        "Gerudo Desert Cave of Ordeals Plateau", player, multiworld
    )
    regions["Gerudo Desert Cave of Ordeals Plateau"] = (
        gerudo_desert_cave_of_ordeals_plateau
    )
    multiworld.regions.append(gerudo_desert_cave_of_ordeals_plateau)

    gerudo_desert_basin = Region("Gerudo Desert Basin", player, multiworld)
    regions["Gerudo Desert Basin"] = gerudo_desert_basin
    multiworld.regions.append(gerudo_desert_basin)

    gerudo_desert_north_east_ledge = Region(
        "Gerudo Desert North East Ledge", player, multiworld
    )
    regions["Gerudo Desert North East Ledge"] = gerudo_desert_north_east_ledge
    multiworld.regions.append(gerudo_desert_north_east_ledge)

    gerudo_desert_outside_bulblin_camp = Region(
        "Gerudo Desert Outside Bulblin Camp", player, multiworld
    )
    regions["Gerudo Desert Outside Bulblin Camp"] = gerudo_desert_outside_bulblin_camp
    multiworld.regions.append(gerudo_desert_outside_bulblin_camp)

    gerudo_desert_skulltula_grotto = Region(
        "Gerudo Desert Skulltula Grotto", player, multiworld
    )
    regions["Gerudo Desert Skulltula Grotto"] = gerudo_desert_skulltula_grotto
    multiworld.regions.append(gerudo_desert_skulltula_grotto)

    gerudo_desert_chu_grotto = Region("Gerudo Desert Chu Grotto", player, multiworld)
    regions["Gerudo Desert Chu Grotto"] = gerudo_desert_chu_grotto
    multiworld.regions.append(gerudo_desert_chu_grotto)

    gerudo_desert_rock_grotto = Region("Gerudo Desert Rock Grotto", player, multiworld)
    regions["Gerudo Desert Rock Grotto"] = gerudo_desert_rock_grotto
    multiworld.regions.append(gerudo_desert_rock_grotto)

    bulblin_camp = Region("Bulblin Camp", player, multiworld)
    regions["Bulblin Camp"] = bulblin_camp
    multiworld.regions.append(bulblin_camp)

    outside_arbiters_grounds = Region("Outside Arbiters Grounds", player, multiworld)
    regions["Outside Arbiters Grounds"] = outside_arbiters_grounds
    multiworld.regions.append(outside_arbiters_grounds)

    mirror_chamber_lower = Region("Mirror Chamber Lower", player, multiworld)
    regions["Mirror Chamber Lower"] = mirror_chamber_lower
    multiworld.regions.append(mirror_chamber_lower)

    mirror_chamber_upper = Region("Mirror Chamber Upper", player, multiworld)
    regions["Mirror Chamber Upper"] = mirror_chamber_upper
    multiworld.regions.append(mirror_chamber_upper)

    mirror_chamber_portal = Region("Mirror of Twilight", player, multiworld)
    regions["Mirror of Twilight"] = mirror_chamber_portal
    multiworld.regions.append(mirror_chamber_portal)

    castle_town_west = Region("Castle Town West", player, multiworld)
    regions["Castle Town West"] = castle_town_west
    multiworld.regions.append(castle_town_west)

    castle_town_star_game = Region("Castle Town STAR Game", player, multiworld)
    regions["Castle Town STAR Game"] = castle_town_star_game
    multiworld.regions.append(castle_town_star_game)

    castle_town_center = Region("Castle Town Center", player, multiworld)
    regions["Castle Town Center"] = castle_town_center
    multiworld.regions.append(castle_town_center)

    castle_town_goron_house_left_door = Region(
        "Castle Town Goron House Left Door", player, multiworld
    )
    regions["Castle Town Goron House Left Door"] = castle_town_goron_house_left_door
    multiworld.regions.append(castle_town_goron_house_left_door)

    castle_town_goron_house_right_door = Region(
        "Castle Town Goron House Right Door", player, multiworld
    )
    regions["Castle Town Goron House Right Door"] = castle_town_goron_house_right_door
    multiworld.regions.append(castle_town_goron_house_right_door)

    castle_town_goron_house = Region("Castle Town Goron House", player, multiworld)
    regions["Castle Town Goron House"] = castle_town_goron_house
    multiworld.regions.append(castle_town_goron_house)

    castle_town_malo_mart = Region("Castle Town Malo Mart", player, multiworld)
    regions["Castle Town Malo Mart"] = castle_town_malo_mart
    multiworld.regions.append(castle_town_malo_mart)

    castle_town_north = Region("Castle Town North", player, multiworld)
    regions["Castle Town North"] = castle_town_north
    multiworld.regions.append(castle_town_north)

    castle_town_north_behind_first_door = Region(
        "Castle Town North Behind First Door", player, multiworld
    )
    regions["Castle Town North Behind First Door"] = castle_town_north_behind_first_door
    multiworld.regions.append(castle_town_north_behind_first_door)

    castle_town_north_inside_barrier = Region(
        "Castle Town North Inside Barrier", player, multiworld
    )
    regions["Castle Town North Inside Barrier"] = castle_town_north_inside_barrier
    multiworld.regions.append(castle_town_north_inside_barrier)

    castle_town_east = Region("Castle Town East", player, multiworld)
    regions["Castle Town East"] = castle_town_east
    multiworld.regions.append(castle_town_east)

    castle_town_doctors_office_balcony = Region(
        "Castle Town Doctors Office Balcony", player, multiworld
    )
    regions["Castle Town Doctors Office Balcony"] = castle_town_doctors_office_balcony
    multiworld.regions.append(castle_town_doctors_office_balcony)

    castle_town_doctors_office_left_door = Region(
        "Castle Town Doctors Office Left Door", player, multiworld
    )
    regions["Castle Town Doctors Office Left Door"] = (
        castle_town_doctors_office_left_door
    )
    multiworld.regions.append(castle_town_doctors_office_left_door)

    castle_town_doctors_office_right_door = Region(
        "Castle Town Doctors Office Right Door", player, multiworld
    )
    regions["Castle Town Doctors Office Right Door"] = (
        castle_town_doctors_office_right_door
    )
    multiworld.regions.append(castle_town_doctors_office_right_door)

    castle_town_doctors_office_entrance = Region(
        "Castle Town Doctors Office Entrance", player, multiworld
    )
    regions["Castle Town Doctors Office Entrance"] = castle_town_doctors_office_entrance
    multiworld.regions.append(castle_town_doctors_office_entrance)

    castle_town_doctors_office_lower = Region(
        "Castle Town Doctors Office Lower", player, multiworld
    )
    regions["Castle Town Doctors Office Lower"] = castle_town_doctors_office_lower
    multiworld.regions.append(castle_town_doctors_office_lower)

    castle_town_doctors_office_upper = Region(
        "Castle Town Doctors Office Upper", player, multiworld
    )
    regions["Castle Town Doctors Office Upper"] = castle_town_doctors_office_upper
    multiworld.regions.append(castle_town_doctors_office_upper)

    castle_town_south = Region("Castle Town South", player, multiworld)
    regions["Castle Town South"] = castle_town_south
    multiworld.regions.append(castle_town_south)

    castle_town_agithas_house = Region("Castle Town Agithas House", player, multiworld)
    regions["Castle Town Agithas House"] = castle_town_agithas_house
    multiworld.regions.append(castle_town_agithas_house)

    castle_town_seer_house = Region("Castle Town Seer House", player, multiworld)
    regions["Castle Town Seer House"] = castle_town_seer_house
    multiworld.regions.append(castle_town_seer_house)

    castle_town_jovanis_house = Region("Castle Town Jovanis House", player, multiworld)
    regions["Castle Town Jovanis House"] = castle_town_jovanis_house
    multiworld.regions.append(castle_town_jovanis_house)

    castle_town_telmas_bar = Region("Castle Town Telmas Bar", player, multiworld)
    regions["Castle Town Telmas Bar"] = castle_town_telmas_bar
    multiworld.regions.append(castle_town_telmas_bar)

    lanayru_field = Region("Lanayru Field", player, multiworld)
    regions["Lanayru Field"] = lanayru_field
    multiworld.regions.append(lanayru_field)

    lanayru_field_cave_entrance = Region(
        "Lanayru Field Cave Entrance", player, multiworld
    )
    regions["Lanayru Field Cave Entrance"] = lanayru_field_cave_entrance
    multiworld.regions.append(lanayru_field_cave_entrance)

    lanayru_field_behind_boulder = Region(
        "Lanayru Field Behind Boulder", player, multiworld
    )
    regions["Lanayru Field Behind Boulder"] = lanayru_field_behind_boulder
    multiworld.regions.append(lanayru_field_behind_boulder)

    hyrule_field_near_spinner_rails = Region(
        "Hyrule Field Near Spinner Rails", player, multiworld
    )
    regions["Hyrule Field Near Spinner Rails"] = hyrule_field_near_spinner_rails
    multiworld.regions.append(hyrule_field_near_spinner_rails)

    lanayru_ice_puzzle_cave = Region("Lanayru Ice Puzzle Cave", player, multiworld)
    regions["Lanayru Ice Puzzle Cave"] = lanayru_ice_puzzle_cave
    multiworld.regions.append(lanayru_ice_puzzle_cave)

    lanayru_field_chu_grotto = Region("Lanayru Field Chu Grotto", player, multiworld)
    regions["Lanayru Field Chu Grotto"] = lanayru_field_chu_grotto
    multiworld.regions.append(lanayru_field_chu_grotto)

    lanayru_field_skulltula_grotto = Region(
        "Lanayru Field Skulltula Grotto", player, multiworld
    )
    regions["Lanayru Field Skulltula Grotto"] = lanayru_field_skulltula_grotto
    multiworld.regions.append(lanayru_field_skulltula_grotto)

    lanayru_field_poe_grotto = Region("Lanayru Field Poe Grotto", player, multiworld)
    regions["Lanayru Field Poe Grotto"] = lanayru_field_poe_grotto
    multiworld.regions.append(lanayru_field_poe_grotto)

    outside_castle_town_west = Region("Outside Castle Town West", player, multiworld)
    regions["Outside Castle Town West"] = outside_castle_town_west
    multiworld.regions.append(outside_castle_town_west)

    outside_castle_town_west_grotto_ledge = Region(
        "Outside Castle Town West Grotto Ledge", player, multiworld
    )
    regions["Outside Castle Town West Grotto Ledge"] = (
        outside_castle_town_west_grotto_ledge
    )
    multiworld.regions.append(outside_castle_town_west_grotto_ledge)

    outside_castle_town_west_helmasaur_grotto = Region(
        "Outside Castle Town West Helmasaur Grotto", player, multiworld
    )
    regions["Outside Castle Town West Helmasaur Grotto"] = (
        outside_castle_town_west_helmasaur_grotto
    )
    multiworld.regions.append(outside_castle_town_west_helmasaur_grotto)

    outside_castle_town_east = Region("Outside Castle Town East", player, multiworld)
    regions["Outside Castle Town East"] = outside_castle_town_east
    multiworld.regions.append(outside_castle_town_east)

    outside_castle_town_south = Region("Outside Castle Town South", player, multiworld)
    regions["Outside Castle Town South"] = outside_castle_town_south
    multiworld.regions.append(outside_castle_town_south)

    outside_castle_town_south_inside_boulder = Region(
        "Outside Castle Town South Inside Boulder", player, multiworld
    )
    regions["Outside Castle Town South Inside Boulder"] = (
        outside_castle_town_south_inside_boulder
    )
    multiworld.regions.append(outside_castle_town_south_inside_boulder)

    outside_castle_town_south_tektite_grotto = Region(
        "Outside Castle Town South Tektite Grotto", player, multiworld
    )
    regions["Outside Castle Town South Tektite Grotto"] = (
        outside_castle_town_south_tektite_grotto
    )
    multiworld.regions.append(outside_castle_town_south_tektite_grotto)

    lake_hylia_bridge = Region("Lake Hylia Bridge", player, multiworld)
    regions["Lake Hylia Bridge"] = lake_hylia_bridge
    multiworld.regions.append(lake_hylia_bridge)

    lake_hylia_bridge_grotto_ledge = Region(
        "Lake Hylia Bridge Grotto Ledge", player, multiworld
    )
    regions["Lake Hylia Bridge Grotto Ledge"] = lake_hylia_bridge_grotto_ledge
    multiworld.regions.append(lake_hylia_bridge_grotto_ledge)

    lake_hylia_bridge_bubble_grotto = Region(
        "Lake Hylia Bridge Bubble Grotto", player, multiworld
    )
    regions["Lake Hylia Bridge Bubble Grotto"] = lake_hylia_bridge_bubble_grotto
    multiworld.regions.append(lake_hylia_bridge_bubble_grotto)

    lake_hylia = Region("Lake Hylia", player, multiworld)
    regions["Lake Hylia"] = lake_hylia
    multiworld.regions.append(lake_hylia)

    lake_hylia_cave_entrance = Region("Lake Hylia Cave Entrance", player, multiworld)
    regions["Lake Hylia Cave Entrance"] = lake_hylia_cave_entrance
    multiworld.regions.append(lake_hylia_cave_entrance)

    lake_hylia_lakebed_temple_entrance = Region(
        "Lake Hylia Lakebed Temple Entrance", player, multiworld
    )
    regions["Lake Hylia Lakebed Temple Entrance"] = lake_hylia_lakebed_temple_entrance
    multiworld.regions.append(lake_hylia_lakebed_temple_entrance)

    lake_hylia_lanayru_spring = Region("Lake Hylia Lanayru Spring", player, multiworld)
    regions["Lake Hylia Lanayru Spring"] = lake_hylia_lanayru_spring
    multiworld.regions.append(lake_hylia_lanayru_spring)

    lake_hylia_long_cave = Region("Lake Hylia Long Cave", player, multiworld)
    regions["Lake Hylia Long Cave"] = lake_hylia_long_cave
    multiworld.regions.append(lake_hylia_long_cave)

    lake_hylia_shell_blade_grotto = Region(
        "Lake Hylia Shell Blade Grotto", player, multiworld
    )
    regions["Lake Hylia Shell Blade Grotto"] = lake_hylia_shell_blade_grotto
    multiworld.regions.append(lake_hylia_shell_blade_grotto)

    lake_hylia_water_toadpoli_grotto = Region(
        "Lake Hylia Water Toadpoli Grotto", player, multiworld
    )
    regions["Lake Hylia Water Toadpoli Grotto"] = lake_hylia_water_toadpoli_grotto
    multiworld.regions.append(lake_hylia_water_toadpoli_grotto)

    upper_zoras_river = Region("Upper Zoras River", player, multiworld)
    regions["Upper Zoras River"] = upper_zoras_river
    multiworld.regions.append(upper_zoras_river)

    upper_zoras_river_izas_house = Region(
        "Upper Zoras River Izas House", player, multiworld
    )
    regions["Upper Zoras River Izas House"] = upper_zoras_river_izas_house
    multiworld.regions.append(upper_zoras_river_izas_house)

    fishing_hole = Region("Fishing Hole", player, multiworld)
    regions["Fishing Hole"] = fishing_hole
    multiworld.regions.append(fishing_hole)

    fishing_hole_house = Region("Fishing Hole House", player, multiworld)
    regions["Fishing Hole House"] = fishing_hole_house
    multiworld.regions.append(fishing_hole_house)

    zoras_domain = Region("Zoras Domain", player, multiworld)
    regions["Zoras Domain"] = zoras_domain
    multiworld.regions.append(zoras_domain)

    zoras_domain_west_ledge = Region("Zoras Domain West Ledge", player, multiworld)
    regions["Zoras Domain West Ledge"] = zoras_domain_west_ledge
    multiworld.regions.append(zoras_domain_west_ledge)

    zoras_throne_room = Region("Zoras Domain Throne Room", player, multiworld)
    regions["Zoras Domain Throne Room"] = zoras_throne_room
    multiworld.regions.append(zoras_throne_room)

    outside_links_house = Region("Outside Links House", player, multiworld)
    regions["Outside Links House"] = outside_links_house
    multiworld.regions.append(outside_links_house)

    ordon_links_house = Region("Ordon Links House", player, multiworld)
    regions["Ordon Links House"] = ordon_links_house
    multiworld.regions.append(ordon_links_house)

    ordon_village = Region("Ordon Village", player, multiworld)
    regions["Ordon Village"] = ordon_village
    multiworld.regions.append(ordon_village)

    ordon_seras_shop = Region("Ordon Seras Shop", player, multiworld)
    regions["Ordon Seras Shop"] = ordon_seras_shop
    multiworld.regions.append(ordon_seras_shop)

    ordon_shield_house = Region("Ordon Shield House", player, multiworld)
    regions["Ordon Shield House"] = ordon_shield_house
    multiworld.regions.append(ordon_shield_house)

    ordon_sword_house = Region("Ordon Sword House", player, multiworld)
    regions["Ordon Sword House"] = ordon_sword_house
    multiworld.regions.append(ordon_sword_house)

    ordon_bos_house_left_door = Region("Ordon Bos House Left Door", player, multiworld)
    regions["Ordon Bos House Left Door"] = ordon_bos_house_left_door
    multiworld.regions.append(ordon_bos_house_left_door)

    ordon_bos_house_right_door = Region(
        "Ordon Bos House Right Door", player, multiworld
    )
    regions["Ordon Bos House Right Door"] = ordon_bos_house_right_door
    multiworld.regions.append(ordon_bos_house_right_door)

    ordon_bos_house = Region("Ordon Bos House", player, multiworld)
    regions["Ordon Bos House"] = ordon_bos_house
    multiworld.regions.append(ordon_bos_house)

    ordon_ranch_entrance = Region("Ordon Ranch Entrance", player, multiworld)
    regions["Ordon Ranch Entrance"] = ordon_ranch_entrance
    multiworld.regions.append(ordon_ranch_entrance)

    ordon_ranch = Region("Ordon Ranch", player, multiworld)
    regions["Ordon Ranch"] = ordon_ranch
    multiworld.regions.append(ordon_ranch)

    ordon_ranch_stable = Region("Ordon Ranch Stable", player, multiworld)
    regions["Ordon Ranch Stable"] = ordon_ranch_stable
    multiworld.regions.append(ordon_ranch_stable)

    ordon_ranch_grotto = Region("Ordon Ranch Grotto", player, multiworld)
    regions["Ordon Ranch Grotto"] = ordon_ranch_grotto
    multiworld.regions.append(ordon_ranch_grotto)

    ordon_spring = Region("Ordon Spring", player, multiworld)
    regions["Ordon Spring"] = ordon_spring
    multiworld.regions.append(ordon_spring)

    ordon_bridge = Region("Ordon Bridge", player, multiworld)
    regions["Ordon Bridge"] = ordon_bridge
    multiworld.regions.append(ordon_bridge)

    snowpeak_climb_lower = Region("Snowpeak Climb Lower", player, multiworld)
    regions["Snowpeak Climb Lower"] = snowpeak_climb_lower
    multiworld.regions.append(snowpeak_climb_lower)

    snowpeak_climb_upper = Region("Snowpeak Climb Upper", player, multiworld)
    regions["Snowpeak Climb Upper"] = snowpeak_climb_upper
    multiworld.regions.append(snowpeak_climb_upper)

    snowpeak_ice_keese_grotto = Region("Snowpeak Ice Keese Grotto", player, multiworld)
    regions["Snowpeak Ice Keese Grotto"] = snowpeak_ice_keese_grotto
    multiworld.regions.append(snowpeak_ice_keese_grotto)

    snowpeak_freezard_grotto = Region("Snowpeak Freezard Grotto", player, multiworld)
    regions["Snowpeak Freezard Grotto"] = snowpeak_freezard_grotto
    multiworld.regions.append(snowpeak_freezard_grotto)

    snowpeak_summit_upper = Region("Snowpeak Summit Upper", player, multiworld)
    regions["Snowpeak Summit Upper"] = snowpeak_summit_upper
    multiworld.regions.append(snowpeak_summit_upper)

    snowpeak_summit_lower = Region("Snowpeak Summit Lower", player, multiworld)
    regions["Snowpeak Summit Lower"] = snowpeak_summit_lower
    multiworld.regions.append(snowpeak_summit_lower)

    # Connect Menu to starting region
    menu.connect(regions["Outside Links House"])

    return regions


def add_location_to_regions(
    multiworld: MultiWorld, player: int, region: str, location: str
):
    if location in LOCATION_TABLE:
        multiworld.get_region(region, player).locations.append(
            TPLocation(
                player,
                location,
                multiworld.get_region(region, player),
                LOCATION_TABLE[location],
            )
        )
    else:
        raise RuntimeError(f"{location=} is not in location table")


# def create_portal_location(world: MultiWorld, player: int):

#     portal_locations: list[tuple[str, str]] = [
#         ("Snowpeak Summit Upper", "Snowpeak Portal"),
#         ("Zoras Domain Throne Room", "Zoras Domain Portal"),
#         ("Upper Zoras River", "Upper Zoras River Portal"),
#         ("Lake Hylia", "Lake Hylia Portal"),
#         ("Outside Castle Town West", "Castle Town Portal"),
#         ("Gerudo Desert Cave of Ordeals Plateau", "Gerudo Desert Portal"),
#         ("Sacred Grove Lower", "Sacred Grove Portal"),
#         ("North Faron Woods", "North Faron Portal"),
#         ("South Faron Woods", "South Faron Portal"),
#         ("Lower Kakariko Village", "Kakariko Village Portal"),
#         ("Eldin Field", "Bridge of Eldin Portal"),
#         ("Kakariko Gorge", "Kakariko Gorge Portal"),
#         ("Death Mountain Volcano", "Death Mountain Portal"),
#         ("Mirror Chamber Upper", "Mirror Chamber Portal"),
#         ("Ordon Spring", "Ordon Spring Portal"),
#     ]

#     for region, location in portal_locations:
#         add_location_to_regions(world, player, region, location)
