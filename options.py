from dataclasses import dataclass

from Options import (
    Choice,
    DeathLink,
    DefaultOnToggle,
    OptionGroup,
    OptionSet,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
)
from .Locations import DUNGEON_NAMES


class DungeonItem(Choice):
    value: int
    option_startwith = 0
    option_vanilla = 1
    option_own_dungeon = 2
    option_any_dungeon = 3
    option_keysy = 4
    default = 1

    @property
    def in_dungeon(self) -> bool:
        return self.value in (1, 2, 3)


# class Dungeons(DefaultOnToggle):
#     """This controls whether dungeons can contain progress items.

#     If off, dungeons will still be randomized, but will only contain optional items you don't need to beat the game.
#     """

#     display_name = "Dungeons"


# Logic Settings
class LogicRules(Choice):
    """
    Controls what types of tricks the logic can expect you to perform.

    - Glitchless: Only intended mechanics are required
    - Glitched: Some glitches may be required
    - No Logic: No logical requirements are enforced
    """

    display_name = "Logic Rules"
    option_glitchless = 0
    option_glitched = 1
    option_no_logic = 2
    default = 0


# Access Settings
class CastleRequirements(Choice):
    """
    Controls requirements for accessing Hyrule Castle.

    - Open: No requirements
    - Fused Shadows: Requires all Fused Shadows
    - Mirror Shards: Requires all Mirror Shards
    - All Dungeons: Requires completing all dungeons
    - Vanilla: Vanilla requirements
    """

    display_name = "Castle Requirements"
    option_open = 0
    option_fused_shadows = 1
    option_mirror_shards = 2
    option_all_dungeons = 3
    option_vanilla = 4
    default = 0


class PalaceRequirements(Choice):
    """
    Controls requirements for accessing Palace of Twilight.

    - Open: No requirements
    - Fused Shadows: Requires all Fused Shadows
    - Mirror Shards: Requires all Mirror Shards
    - Vanilla: Vanilla requirements
    """

    display_name = "Palace Requirements"
    option_open = 0
    option_fused_shadows = 1
    option_mirror_shards = 2
    option_vanilla = 3
    default = 0


class FaronWoodsLogic(Choice):
    """
    Controls logic for accessing Faron Woods.

    - Open: No special requirements
    - Closed: Requires normal progression
    """

    display_name = "Faron Woods Logic"
    option_open = 0
    option_closed = 1
    default = 0


# Item Pool Settings
class GoldenBugsShuffled(Toggle):
    """
    Controls whether golden bugs are in the item pool.
    """

    display_name = "Golden Bugs"
    default = False


class SkyCharactersShuffled(Toggle):
    """
    Controls whether sky characters are in the item pool.
    """

    display_name = "Sky Characters"
    default = False


class NpcItemsShuffled(Toggle):
    """
    Controls whether Gifts from NPCs are in the item pool.
    """

    display_name = "Gifts from NPCs"
    default = False


class ShopItemsShuffled(Toggle):
    """
    Controls whether shop items are in the item pool.
    """

    display_name = "Shop Items"
    default = False


class HiddenSkillsShuffled(Toggle):
    """
    Controls whether hidden skills are in the item pool.
    """

    display_name = "Hidden Skills"
    default = False


class PoeSettings(Toggle):
    """
    Controls weither poes are in the item pool.
    """

    display_name = "Poe Settings"
    default = False


class DungeonsShuffled(Toggle):
    """
    Controls whether items in dungeons are randomized.
    """

    display_name = "Dungeons Shuffled"
    default = False


class HeartPieceShuffled(Toggle):
    """
    Controls whether heart pieces are in the item pool.
    """

    display_name = "Heart Pieces"
    default = False


class OverWoldShuffled(Toggle):
    """
    Controls whether overworld items are in the item pool.
    """

    display_name = "Overworld Items"
    default = True


# Dungeon Items
class SmallKeySettings(DungeonItem):
    """
    Controls requirements for obtaining small keys.
    """

    item_name_group = "Small Keys"
    display_name = "Randomize Small Keys"
    default = 2


class BigKeySettings(DungeonItem):
    """
    Controls requirements for obtaining big keys.
    """

    item_name_group = "Big Keys"
    display_name = "Randomize Big Keys"
    default = 2


class MapAndCompassSettings(DungeonItem):
    """
    Controls requirements for obtaining maps and compasses.
    """

    item_name_group = "Maps and Compasses"
    display_name = "Randomize Maps & Compasses"
    default = 2


class DungeonRewardsProgression(Toggle):
    """
    Controls whether dungeon rewards are shuffled.
    """

    display_name = "Dungeon Rewards can be anywhere"
    default = False


class SmallKeysOnBosses(Toggle):
    """
    Controls whether small keys are on bosses.
    """

    display_name = "Small Keys on Bosses"
    default = False


# Timesavers
class SkipPrologue(Toggle):
    """
    Controls whether the prologue is skipped.
    """

    display_name = "Skip Prologue"
    default = False


class FaronTwilightCleared(Toggle):
    """
    Controls whether Faron Twilight is cleared.
    """

    display_name = "Faron Twilight Cleared"
    default = False


class EldinTwilightCleared(Toggle):
    """
    Controls whether Eldin Twilight is cleared.
    """

    display_name = "Eldin Twilight Cleared"
    default = False


class LanayruTwilightCleared(Toggle):
    """
    Controls whether Lanayru Twilight is cleared.
    """

    display_name = "Lanayru Twilight Cleared"
    default = False


class SkipMdh(Toggle):
    """
    Controls whether the Midna's Darkest Hour is skipped.
    """

    display_name = "Skip Midna's Darkest Hour"
    default = False


class SkipMinorCutscenes(Toggle):
    """
    Controls whether the minor cutscenes are skipped.
    """

    display_name = "Skip Minor Cutscenes"
    default = False


class SkipMajorCutscenes(Toggle):
    """
    Controls whether the major cutscenes are skipped.
    """

    display_name = "Skip Major Cutscenes"
    default = False


class FastIronBoots(Toggle):
    """
    Controls whether the Iron Boots are fast.
    """

    display_name = "Fast Iron Boots"
    default = False


class QuickTransform(Toggle):
    """
    Controls whether the transform is quick.
    """

    display_name = "Quick Transform"
    default = False


class InstantMessageText(Toggle):
    """
    Controls whether the message text is instant.
    """

    display_name = "Instant Message Text"
    default = False


class OpenMap(Toggle):
    """
    Controls whether the map is open.
    """

    display_name = "Open Map"
    default = False


class IncreaseSpinnerSpeed(Toggle):
    """
    Controls whether the spinner speed is increased.
    """

    display_name = "Increase Spinner Speed"
    default = False


class OpenDoorOfTime(Toggle):
    """
    Controls whether the Door of Time is open.
    """

    display_name = "Open Door of Time"
    default = False


# Additional Settings
class TransformAnywhere(Toggle):
    """
    Controls whether the player can transform anywhere.
    """

    display_name = "Transform Anywhere"
    default = False


class IncreaseWalletCapacity(Toggle):
    """
    Controls whether the wallet capacity is increased.
    """

    display_name = "Increase Wallet Capacity"
    default = False


class BonksDoDamage(Toggle):
    """
    Controls whether bonks do damage.
    """

    display_name = "Bonks Do Damage"
    default = False


class TrapFrequency(Choice):
    """
    Controls the frequency of traps in the game.
    """

    display_name = "Trap Frequency"
    option_no_traps = 0
    option_few = 1
    option_many = 2
    option_mayhem = 3
    option_nightmare = 4
    default = 0


class DamageMagnification(Choice):
    """
    Multiplies the damage the player takes.
    """

    display_name = "Damage Multiplier"
    option_vanilla = 0
    option_double = 1
    option_triple = 2
    option_quadruple = 3
    option_ohko = 4
    default = 0


class StartingToD(Choice):
    """
    Controls the starting time of day.
    """

    display_name = "Starting Time of Day"
    option_morning = 0
    option_noon = 1
    option_evening = 2
    option_night = 3
    default = 0


# Dungeon Entrance Settings
class SkipLakebedEntrance(Toggle):
    """
    Controls whether the Lakebed does not require water bombs.
    """

    display_name = "Lakebed Does not require water bombs"
    default = False


class SkipArbitersGroundsEntrance(Toggle):
    """
    Controls whether the Arbiter's Grounds does not require Bublin Key.
    """

    display_name = "Arbiter's Grounds Does not require Bublin Key"
    default = False


class SkipSnowpeakEntrance(Toggle):
    """
    Controls whether the Snowpeak Entrance is skipped.
    """

    display_name = "Snowpeak Does not require Reekfish Scent"
    default = False


class SkipCityInTheSkyEntrance(Toggle):
    """
    Controls whether the City in the Sky does not require filled Skybook.
    """

    display_name = "City in the Sky Does not require filled Skybook"
    default = False


class GoronMinesEntrance(Choice):
    """
    Controls requirements for accessing the Goron Mines.
    """

    display_name = "Goron Mines Entrance"
    option_closed = 0
    option_no_wrestling = 1
    option_open = 2
    default = 0


class TotEntrance(Choice):
    """
    Controls requirements for accessing the Temple of Time.
    """

    display_name = "Temple of Time Entrance"
    option_open = 0
    option_open_grove = 1
    option_closed = 2
    default = 0


# class BarrenDungeons(Toggle):
#     """
#     Controls whether dungeons can be barren.
#     """

#     display_name = "Barren Dungeons"
#     default = False


@dataclass
class TPOptions(PerGameCommonOptions):
    """
    A data class that encapsulates all configuration options for The Wind Waker.
    """

    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink

    # Logic Settings
    logic_rules: LogicRules  #
    castle_requirements: CastleRequirements  #
    palace_requirements: PalaceRequirements  #
    faron_woods_logic: FaronWoodsLogic  #

    # Item Pool Settings
    golden_bugs_shuffled: GoldenBugsShuffled  #
    sky_characters_shuffled: SkyCharactersShuffled  #
    npc_items_shuffled: NpcItemsShuffled  #
    shop_items_shuffled: ShopItemsShuffled  #
    hidden_skills_shuffled: HiddenSkillsShuffled  #
    poe_shuffled: PoeSettings  #
    overworld_shuffled: OverWoldShuffled  #
    heart_piece_shuffled: HeartPieceShuffled  #
    dungeons_shuffled: DungeonsShuffled  #

    # item_scarcity: ItemScarcity

    # Dungeon Items
    small_key_settings: SmallKeySettings  #
    big_key_settings: BigKeySettings  #
    map_and_compass_settings: MapAndCompassSettings  #
    dungeon_rewards_progression: DungeonRewardsProgression
    small_keys_on_bosses: SmallKeysOnBosses

    # Timesavers
    skip_prologue: SkipPrologue  #
    faron_twilight_cleared: FaronTwilightCleared  #
    eldin_twilight_cleared: EldinTwilightCleared  #
    lanayru_twilight_cleared: LanayruTwilightCleared  #
    skip_mdh: SkipMdh  #
    # skip_minor_cutscenes: SkipMinorCutscenes
    # skip_major_cutscenes: SkipMajorCutscenes
    # fast_iron_boots: FastIronBoots
    # quick_transform: QuickTransform
    # barren_dungeons: BarrenDungeons  #
    # instant_message_text: InstantMessageText
    open_map: OpenMap  #
    # increase_spinner_speed: IncreaseSpinnerSpeed
    # open_door_of_time: OpenDoorOfTime
    increase_wallet: IncreaseWalletCapacity  #

    # Additional Settings
    transform_anywhere: TransformAnywhere  #
    # increase_wallet_capacity: IncreaseWalletCapacity
    # shops_display_shuffled: ShopsDisplayShuffled
    bonks_do_damage: BonksDoDamage  #
    # trap_frequency: TrapFrequency
    damage_magnification: DamageMagnification  #
    # starting_tod: StartingToD
    # hint_distribution: HintDistribution

    # Dungeon Entrance Settings
    skip_lakebed_entrance: SkipLakebedEntrance  #
    skip_arbiters_grounds_entrance: SkipArbitersGroundsEntrance  #
    skip_snowpeak_entrance: SkipSnowpeakEntrance  #
    skip_city_in_the_sky_entrance: SkipCityInTheSkyEntrance  #
    goron_mines_entrance: GoronMinesEntrance  #
    tot_entrance: TotEntrance  #


tp_option_groups: list[OptionGroup] = [
    OptionGroup(
        "Item Pool Settings",
        [
            GoldenBugsShuffled,
            SkyCharactersShuffled,
            NpcItemsShuffled,
            ShopItemsShuffled,
            HiddenSkillsShuffled,
            PoeSettings,
            OverWoldShuffled,
            HeartPieceShuffled,
            DungeonsShuffled,
        ],
        start_collapsed=True,
    ),
    OptionGroup(
        "Logic Settings",
        [
            LogicRules,
            CastleRequirements,
            PalaceRequirements,
            FaronWoodsLogic,
        ],
        start_collapsed=True,
    ),
    OptionGroup(
        "Dungeon Items",
        [
            SmallKeySettings,
            BigKeySettings,
            MapAndCompassSettings,
        ],
        start_collapsed=True,
    ),
    OptionGroup(
        "Timesavers",
        [
            SkipPrologue,
            FaronTwilightCleared,
            EldinTwilightCleared,
            LanayruTwilightCleared,
            SkipMdh,
            SkipMinorCutscenes,
            SkipMajorCutscenes,
            FastIronBoots,
            QuickTransform,
            # UnrequiredDungeonAreBarren,
            InstantMessageText,
            OpenMap,
            IncreaseSpinnerSpeed,
            OpenDoorOfTime,
        ],
        start_collapsed=True,
    ),
    OptionGroup(
        "Additional Settings",
        [
            TransformAnywhere,
            IncreaseWalletCapacity,
            # ShopsDisplayShuffled,
            BonksDoDamage,
            TrapFrequency,
            DamageMagnification,
            StartingToD,
            # HintDistribution,
        ],
        start_collapsed=True,
    ),
    OptionGroup(
        "Dungeon Entrance Settings",
        [
            SkipLakebedEntrance,
            SkipArbitersGroundsEntrance,
            SkipSnowpeakEntrance,
            SkipCityInTheSkyEntrance,
            GoronMinesEntrance,
            TotEntrance,
        ],
        start_collapsed=True,
    ),
]
