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
    option_anywhere = 4
    default = 1

    @property
    def in_dungeon(self) -> bool:
        return self.value in (1, 2, 3)


# Logic Settings
class LogicRules(Choice):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
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
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
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
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
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
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
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
    Controls whether golden bug locations can contain progression items.
    """

    display_name = "Golden Bugs"
    default = True


class SkyCharactersShuffled(Toggle):
    """
    Controls whether sky characters locations can contain progression items.
    """

    display_name = "Sky Characters"
    default = True


class NpcItemsShuffled(Toggle):
    """
    Controls whether Gifts from NPCs can contain progression items.
    """

    display_name = "Gifts from NPCs"
    default = True


class ShopItemsShuffled(Toggle):
    """
    Controls whether Shop locations can contain progression items.
    """

    display_name = "Shop Items"
    default = True


class HiddenSkillsShuffled(Toggle):
    """
    Controls whether hidden skill locations can contain progression items.
    """

    display_name = "Hidden Skills"
    default = True


class PoeShuffled(Toggle):
    """
    Controls whether Poes can contain progression items.
    """

    display_name = "Poe Shuffled"
    default = True


class HeartPieceShuffled(Toggle):
    """
    Controls whether Heart Piece locations can contain progression items.
    """

    display_name = "Heart Pieces"
    default = True


class DungeonsShuffled(Toggle):
    """
    Controls whether dungeons locations can contain progression items.
    Cannot be disabled if Overworld shuffle is disabled
    """

    display_name = "Dungeons Shuffled"
    default = True


class OverWoldShuffled(Toggle):
    """
    Controls whether Overworld locations can contain progression items.
    Cannot be disabled if Dungeon shuffle is disabled
    """

    display_name = "Overworld Items"
    default = True


class EarlyShadowCrystal(Toggle):
    """
    When Enabled Shadow Crystal will be placed into Sphere 1 of the local world
    """

    display_name = "Early Shadow Crystal"
    default = False


# Dungeon Items
class SmallKeySettings(DungeonItem):
    """
    Controls how small keys are randomized.

    - **Start With Small Keys:** You will start the game with the small keys for all dungeons.
    - **Vanilla Small Keys:** Small keys will be kept in their vanilla location (non-randomized).
    - **Own Dungeon Small Keys:** Small keys will be randomized locally within their own dungeon.
    - **Any Dungeon Small Keys:** Small keys will be randomized locally within any dungeon.
    - **Anywhere:** Small keys can be found in any progression location, if dungeons are randomized.

    Note:
    Not shuffling Dungeons will overwrite this to vanilla, unless you selected start with
    """

    item_name_group = "Small Keys"
    display_name = "Randomize Small Keys"


class BigKeySettings(DungeonItem):
    """
    Controls how big keys are randomized.

    - **Start With Big Keys:** You will start the game with the big keys for all dungeons.
    - **Vanilla Big Keys:** Big keys will be kept in their vanilla location (non-randomized).
    - **Own Dungeon Big Keys:** Big keys will be randomized locally within their own dungeon.
    - **Any Dungeon Big Keys:** Big keys will be randomized locally within any dungeon.
    - **Anywhere:** Big keys can be found in any progression location.

    Note:
    Not shuffling Dungeons will overwrite this to vanilla, unless you selected start with
    """

    item_name_group = "Big Keys"
    display_name = "Randomize Big Keys"


class MapAndCompassSettings(DungeonItem):
    """
    Controls requirements for obtaining maps and compasses.

    Controls how dungeon maps and compasses are randomized.

    - **Start With Maps & Compasses:** You will start the game with the dungeon maps and compasses for all dungeons.
    - **Vanilla Maps & Compasses:** Dungeon maps and compasses will be kept in their vanilla location (non-randomized).
    - **Own Dungeon Maps & Compasses:** Dungeon maps and compasses will be randomized locally within their own dungeon.
    - **Any Dungeon Maps & Compasses:** Dungeon maps and compasses will be randomized locally within any dungeon.
    - **Anywhere:** Dungeon maps and compasses can be found anywhere, without restriction.

    Note:
    Not shuffling Dungeons will overwrite this to vanilla, unless you selected start with
    """

    item_name_group = "Maps and Compasses"
    display_name = "Randomize Maps & Compasses"


class DungeonRewardsProgression(Toggle):
    """
    NOT IMPLEMENTED YET
    Controls whether dungeon rewards are "forced" to have progression items.
    """

    display_name = "Dungeon Rewards are prgression"
    default = True


class SmallKeysOnBosses(Toggle):
    """
    NOT IMPLEMENTED YET
    Controls whether small keys can be on bosses.
    """

    display_name = "Small Keys on Bosses"
    default = False


# Timesavers
class SkipPrologue(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the prologue is skipped.
    """

    display_name = "Skip Prologue"
    default = True


class FaronTwilightCleared(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether Faron Twilight is cleared.
    """

    display_name = "Faron Twilight Cleared"
    default = True


class EldinTwilightCleared(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether Eldin Twilight is cleared.
    """

    display_name = "Eldin Twilight Cleared"
    default = True


class LanayruTwilightCleared(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether Lanayru Twilight is cleared.
    """

    display_name = "Lanayru Twilight Cleared"
    default = True


class SkipMdh(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the Midna's Darkest Hour is skipped.
    """

    display_name = "Skip Midna's Darkest Hour"
    default = True


class SkipMinorCutscenes(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the minor cutscenes are skipped.
    """

    display_name = "Skip Minor Cutscenes"
    default = True


class SkipMajorCutscenes(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the major cutscenes are skipped.
    """

    display_name = "Skip Major Cutscenes"
    default = True


class FastIronBoots(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the Iron Boots are fast.
    """

    display_name = "Fast Iron Boots"
    default = True


class QuickTransform(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the transform is quick.
    """

    display_name = "Quick Transform"
    default = True


class InstantMessageText(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the message text is instant.
    """

    display_name = "Instant Message Text"
    default = True


class OpenMap(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the map is open.
    Note: Logic for this not added yet. So logic assumes you cannot warp.
    """

    display_name = "Open Map"
    default = True


class IncreaseSpinnerSpeed(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the spinner speed is increased.
    """

    display_name = "Increase Spinner Speed"
    default = True


class OpenDoorOfTime(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the Door of Time is open.
    """

    display_name = "Open Door of Time"
    default = True


# Additional Settings
class TransformAnywhere(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the player can transform anywhere.
    """

    display_name = "Transform Anywhere"
    default = True


class IncreaseWalletCapacity(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the wallet capacity is increased.
    """

    display_name = "Increase Wallet Capacity"
    default = True


class BonksDoDamage(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
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
    option_many = 3
    option_mayhem = 7
    option_nightmare = 100
    default = 0


class DamageMagnification(Choice):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
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
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
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
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the Lakebed does not require water bombs.
    """

    display_name = "Lakebed Does not require water bombs"
    default = True


class SkipArbitersGroundsEntrance(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the Arbiters Grounds does not require defeating King Bublin.
    """

    display_name = "Arbiters Grounds Does not require Bublin Camp"
    default = True


class SkipSnowpeakEntrance(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the Snowpeak Entrance is skipped.
    """

    display_name = "Snowpeak Does not require Reekfish Scent"
    default = True


class SkipCityInTheSkyEntrance(Toggle):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls whether the City in The Sky does not require filled Skybook.
    """

    display_name = "City in The Sky Does not require filled Skybook"
    default = True


class GoronMinesEntrance(Choice):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls requirements for accessing the Goron Mines.
    """

    display_name = "Goron Mines Entrance"
    option_open = 0
    option_no_wrestling = 1
    option_closed = 2
    default = 0


class TotEntrance(Choice):
    """
    CHANGING FROM DEFAULT NOT IMPLEMENTED YET
    Controls requirements for accessing the Temple of Time.
    """

    display_name = "Temple of Time Entrance"
    option_open = 0
    option_open_grove = 1
    option_closed = 2
    default = 0


@dataclass
class TPOptions(PerGameCommonOptions):
    """
    A data class that encapsulates all configuration options for The Wind Waker.
    """

    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink

    # Item Pool Settings
    golden_bugs_shuffled: GoldenBugsShuffled
    sky_characters_shuffled: SkyCharactersShuffled
    npc_items_shuffled: NpcItemsShuffled
    shop_items_shuffled: ShopItemsShuffled
    hidden_skills_shuffled: HiddenSkillsShuffled
    poe_shuffled: PoeShuffled
    heart_piece_shuffled: HeartPieceShuffled
    overworld_shuffled: OverWoldShuffled
    dungeons_shuffled: DungeonsShuffled

    # Dungeon Items
    small_key_settings: SmallKeySettings
    big_key_settings: BigKeySettings
    map_and_compass_settings: MapAndCompassSettings
    dungeon_rewards_progression: DungeonRewardsProgression  # Not yet useful
    small_keys_on_bosses: SmallKeysOnBosses  # Not yet useful

    # Logic Settings
    logic_rules: LogicRules  #
    castle_requirements: CastleRequirements  #
    palace_requirements: PalaceRequirements  #
    faron_woods_logic: FaronWoodsLogic  #

    # Timesavers
    # skip_prologue: SkipPrologue  #
    # faron_twilight_cleared: FaronTwilightCleared  #
    # eldin_twilight_cleared: EldinTwilightCleared  #
    # lanayru_twilight_cleared: LanayruTwilightCleared  #
    # skip_mdh: SkipMdh  #
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
    # shops_display_shuffled: ShopsDisplayShuffled
    bonks_do_damage: BonksDoDamage  #
    trap_frequency: TrapFrequency
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

    early_shadow_crystal: EarlyShadowCrystal


tp_option_groups: list[OptionGroup] = [
    OptionGroup(
        "Item Pool / Location Settings",
        [
            GoldenBugsShuffled,
            SkyCharactersShuffled,
            NpcItemsShuffled,
            ShopItemsShuffled,
            HiddenSkillsShuffled,
            PoeShuffled,
            HeartPieceShuffled,
            OverWoldShuffled,
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
            DungeonRewardsProgression,
            SmallKeysOnBosses,
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
