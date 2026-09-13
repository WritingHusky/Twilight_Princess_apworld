# Setup Guide for Twilight Princess Archipelago

Welcome to Twilight Princess Archipelago! This guide will help you set up the randomizer and play your first multiworld.
Whether playing, generating, or hosting an Archipelago room with Twilight Princess, you must follow a few simple steps to
get started.

Unfortunately, Mac OS is not officially supported at this time.

## Requirements

You'll need the following components to be able to play/generate with Twilight Princess:

- Install [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) v0.6.1 or higher.\
   **Make sure to install the Generator if you intend to generate multiworlds.**
- The latest version of the [Twilight Princess APWorld](https://github.com/WritingHusky/Twilight_Princess_apworld/releases/latest).

### If you're playing Twilight Princess, you'll also need:

- Install [Dolphin Emulator](https://dolphin-emu.org/download/).\
   **We recommend using the latest release.**
- A Twilight Princess ISO (North American version), probably named "Legend of Zelda, The - Twilight Princess (USA).iso".

If you intend to play under Linux, you will need to consider the following information.

- Grab the `tar.gz` version of Archipelago, not the `AppImage`. The file name should be similar to the following on the
  release page: `Archipelago_X.X.X_linux-x86_64.tar.gz`.
- For Dolphin, you can use the flatpak package
  [available on Flathub](https://flathub.org/apps/org.DolphinEmu.dolphin-emu).

## Installation

All users should follow these steps:

1. Unzip the downloaded Twilight Princess APWorld zip file.
2. Double-click the `Twilight Princess.apworld` file. It should automatically install the APWorld after a little while. You will get a
   little dialog window telling you it has been installed successfully. \* Alternatively, copy the `Twilight Princess.apworld` to your Archipelago installation's `custom_worlds` folder (Windows default
   to: `%programdata%/Archipelago`).

If you're playing Twilight Princess, you'll need to download the "Archipelago Twilight Princess Files" from the [#twilight-princess](https://discord.com/channels/731205301247803413/1369050080887312506/1525200781698011287) channel in the [Archipelago Discord](https://discord.gg/archipelago). If you set Dolphin to use the GCI Folder method, you should be able to follow the README.txt in the zip you just downloaded to find the Save path. Place the 3 Files for your Region into the Folder where Dolphin makes its save files.

Note: If you played the Standalone Randomizer of Twilight Princess before, make sure to delete the `Randomizer-1.2.0.[region].gci`, because we use a custom File which can detect the Ganon kill to send AP the "Goal reached".

Note 2: If you started the Game before placing the Files in the Folder, you might have a Vanilla Save called `01-GZ2E-gczelda2.gci` which needs to be removed to make the `REL Loader v2` show up in the 3rd save slot in game.

## Setting Up a YAML

All players playing Twilight Princess must provide the room host with a YAML file containing the settings for their world.
The TP APWorld download includes a sample YAML file for Twilight Princess. The comments in that file explain each
setting's function.

Once you're happy with your settings, provide the room host with your YAML file and proceed to the next step.

Note: Please note the settings labled NON-DEFAULT CHOICE NOT REPRESENTED IN GAME, as these settings will alter logic however they will not be changed from default when playing the game.

## Generating a Multiworld

If you're generating a multiworld game that includes Twilight Princess, you'll need to do so locally as the online
generator does not yet support Twilight Princess. Follow these steps to generate a multiworld:

1. Gather all player's YAMLs. Place these YAMLs into the `Players` folder of your Archipelago installation. If the
   folder does not exist, then it must be created manually. The files here should not be compressed.
2. Modify any local host settings for generation, as desired.
3. Run `ArchipelagoGenerate.exe` (without `.exe` on Linux) or click `Generate` in the launcher. The generation output
   is placed in the `output` folder (usually named something like `AP_XXXXX.zip`). \* Please note that if any player in the game you want to generate plays a game that needs a ROM file to generate,
   you will need the corresponding ROM files. A ROM file is not required for Twilight Princess at this stage.
4. Unzip the `AP_XXXXX.zip` file. It should include a `.aptp` file for each player in the room playing Twilight Princess.
   Each file will be named `AP_XXXXX_P#_<name>.aptp`, where `#` corresponds to that player's slot number and `<name>` is
   their slot (player) name. The `.aptp` file currently contains a spoiler log and other debug information it can be safely ignored.
5. In the next section, use the archive file `AP_XXXXX.zip` to host a room or provide it to the room host.

## Hosting a Room

If you're generating the multiworld, follow the instructions in the previous section. Once you have the zip file
corresponding to your multiworld, follow
[these steps](https://archipelago.gg/tutorial/Archipelago/setup/en#hosting-an-archipelago-server) to host a room. Follow
the instructions for hosting on the website from a locally generated game or on a local machine.

## Connecting to a Room

You may have the `.aptp` file provided to you by the multiworld generator (you can ignore it.) You should also have the room's server
name and port number from the room's host.

Once you do, follow these steps to connect to the room:

**Your save data folder should have `Tpr-?-APTest_APT-aptest.gci`, `GZ2?01_REL_Loader_v2.gci`, and `RandomizerAP.??.gci`** (question marks replaced with the Region specific letters)

<img width="646" height="146" alt="grafik" src="https://github.com/user-attachments/assets/6f28b842-ade5-4018-8c4e-56f3f0cc30a7" />



1. Open Dolphin and use it to open Twilight Princess. (Ensure `Enable Emulated Memory Size Override` is disabled. See troubleshooting for more details)
2. Start the REL loader save file. The Game will restart and show a Screen like this:
<img width="1920" height="1080" alt="grafik" src="https://github.com/user-attachments/assets/0276c2d6-e740-4b7f-9dbe-98785cd0648c" />

3. Start a new save file and:
  - If your Slot Name you've set in the YAML is at most 8 Characters an doesn't have Special Characters, you can just name Link the same as your Slot Name.
  - If your Slot Name you've set in the YAML is at least 9 Characters or has Special Characters, leave the name as is for now (Will be changed next with a Command).
4. Start `ArchipelagoLauncher.exe` (without `.exe` on Linux) and choose `Twilight Princess Client`, which will open the text client. It should automatically connect to Dolphin.
5. Wait until you have control of Link. Cutscenes should be skipped and you should wear the Hero's Clothes.
6. If you skipped naming Link the same as your Slot Name, you can still do so by typing `/name [Your YAML name here]` to write that Name to Links' Name.
   For Example: If your Name is set to `ABC` in the YAML, you type `/name ABC` in the Client.
7. Connect to the room by entering the server name and port number at the top and pressing `Connect`. For rooms hosted on the website, this will be `archipelago.gg:<port>`, where `<port>` is the port number. If a game is hosted from the `ArchipelagoServer.exe` (without `.exe` on Linux), this will default to `38281` but may be changed in the `host.yaml`.

## PopTracker

There's a working PopTracker pack for TP at: https://github.com/Kizugaya/TPRAP_poptracker/releases/latest <br/>
You will need to install PopTracker itself at: https://github.com/black-sliver/PopTracker/releases/latest <br/>
If you have any issues with it, please DM `☆☬𝓚𝓲𝓻𝓲𝓽𝓸☬☆`/`kizugaya` on Discord or ping him in the [#twilight-princess](https://discord.com/channels/731205301247803413/1369050080887312506) channel in the [Archipelago Discord](https://discord.gg/archipelago). You can also open an Issue on GitHub on his Pack.

## Troubleshooting

- Ensure that you are running version v0.6.1 or higher of Archipelago, and the latest version of the world.
- If you do not see the client in the launcher, ensure the `Twilight Princess.apworld` file is in the correct folder (the `custom_worlds` folder of your Archipelago installation).
  It will only show up if you start the Launcher *after* installing the apworld.
- If the client says that seed version and client version do not match, it is recomended regenerate the seed with the current version.
  Differences in version can cause bugs which may make it unplayable.
- If the client throws an error along the lines of "could not read memory at < some-number >", dolphin has been disconnected.
  It should automaticly reconnect, so ensure that dolphin is open and running
- Ensure that you do not have any Dolphin cheats or codes enabled. Some cheats or codes can unexpectedly interfere with
  emulation and make troubleshooting errors difficult.
- If Dolphin is not connecting, ensure that `Enable Emulated Memory Size Override` in Dolphin (under `Options` >
  `Configuration` > `Advanced`) is **disabled**.
- If you run with a custom GC boot menu, you'll need to skip it by going to `Options` > `Configuration` > `GameCube`
  and checking `Skip Main Menu`.
- If Dolphin does load the RELoader save file and has a popup saying something like "Save file cannot be loaded",
  There may be a normal save file in your dolphin save folder, this will need to be removed in order for the randomizer to load.

## Frequently Asked Questions

### Setup
**Q:** "I can't find my GCI folder!" / "What do I do with the MemoryCardA.raw file?"<br/>
**A:** In Dolphin settings, under the GC tab, please set Slot A to 'GCI Folder'; once you do, press the [...] button to set/confirm the directory for it if you don't want to use the default one (default ends in `Card A`).

**Q:** "What goes in the GCI folder?"<br/>
**A:** `GZ2E01_REL_Loader_v2.gci`, `RandomizerAP.us.gci` and `Tpr-E-APTest_APT-aptest.gci`.

**Q:** "What does 'NON-DEFAULT CHOICE NOT REPRESENTED IN GAME' mean in the yaml?"<br/>
**A:** Because the seed is 'pre-generated' (this is the APTest file), certain options are baked into the seed at present and cannot be un-set by Archipelago. If the setting has logical implications, such as Hyrule Castle entry requirements, all items you will need to meet the logical requirement can be obtained without performing the restricted action. If the setting does not have logical implications, such as fast Iron Boots, then you simply have to operate on the honor system.

**Q:** "What do I do with the APTP patch file?"<br/>
**A:** As of APworld v0.3.0, this file is only useful for debugging slot data. It is not currently used to patch Twilight Princess or connect to Archipelago in any way.

**Q:** "I can't connect, the client says 'Invalid Slot'!"<br/>
**A:** The client will only connect once you are in-game, with your file name set to your slot name (you can set your file name with the `/name` command in the client if the file is loaded).

### In-Game

**Q:** "Everything's showing up as green rupees!"<br/>
**A:** This is normal as of APworld v0.3.0. On collecting the green rupee, Archipelago will send out the item at that location.

**Q:** "Everything's *not* showing up as green rupees!"<br/>
**A:** The REL Loader file must be run for each Dolphin session. Failing to do so will make the game think you're playing vanilla.

**Q:** "I'm getting items twice!"<br/>
**A:** The REL Loader file must only be run **once** per Dolphin session. Running more than once will cause you to receive items multiple times.

**Q:** "My check didn't send!"<br/>
**A:** If this check is "Palace of Twilight Zant Heart Container" or "Kakariko Village Malo Mart Hawkeye", these are known issues as of APworld v0.3.0

**Q:** "I received an item during Plumm's minigame but never got it!"<br/>
**A:** This is known. Currently the only workaround is Archipelago's item commands, either `!getitem` or the host's `/send`.<br/>
Note: If you give give yourself by either way extra Items, the Poptracker will think that you have an extra copy of that Item and may show things in logic that actually aren't.<br/>
For Example: You have 2 "Forest Temple Small Key"s, and get the 3rd while doing this Minigame, and then use one of the commands to give you another one so you have 3 in-game, then the PopTracker will think that you have 4 and show things in logic which aren't. you can still remove Item in the Tracker by right-clicking them.

**Q:** "I'm stuck in the Darknut room in Temple of Time!"<br/>
**A:** This is because the of the Open Door of Time setting (which is always on in AP). The only way to leave is to save and quit.

**Q:** "I'm stuck in the Gerudo Desert and don't have the Shadow Crystal to warp out!"<br/>
**A:** Same Answer as above: save and quit to get back to Lake Hylia

**Q:** "How do I move the statue in the basement of the Kakariko hut?"<br/>
**A:** You don't. If you are self-enforcing skip_city_in_the_sky_entrance: false, then you need seven Progressive Sky Books (the book itself and then six letters) before CitS is logically accessible. The Location "Shad Dominion Rod" doesn't exist here.

**Q:** "My victory didn't send!"<br/>
**A:** You're either not playing with the APTest Seed and generated a Seed yourself on the Standalone site (which is wrong), or you still have an old Randomizer file in your Dolphin Save Folder called `Randomizer-1.2.0.[region].gci` which has to be removed.

### PopTracker

**Q:** "What are these blue squares?"<br/>
**A:** For Twilight Princess's Poptracker, the blue squares indicate howling stone locations. There is a blue square both at the howling stone itself and at the golden wolf that howling stone spawns. The golden wolf will not be shown as logically-available until the howling stone is activated.

**Q:** "Why is a check marked red when I can get it?"<br/>
**A:** If you are in a dungeon, the answer is probably key logic; essentially, logic has to assume you have used small keys on every other accessible locked door first, to ensure that you can't lock yourself out of a necessary progression item. If you are not in a dungeon, or you're absolutely sure key logic isn't the problem here, then please tell us about it!

**Q:** "Why does the tracker only auto-tab *sometimes*?"<br/>
**A:** The Twilight Princess APworld can only track which "region" you're in to send to Poptracker. For some places, like Ordona Province, or dungeons, there's only one map for that region anyway, and Poptracker is able to auto-tab to that map. For the major regions (Faron, Eldin, and Lanaryu), as there are multiple possible maps, Poptracker cannot tell which one you're in specifically. For the partial auto-tabbing (the default), this means it does not shift maps at all. If you instead set it to full auto-tabbing, then entering any of these regions will set Poptracker to switch to the full map.
