import asyncio
from copy import deepcopy
import time
import traceback
from typing import TYPE_CHECKING, Any, Dict, Optional

from MultiServer import mark_raw
import dolphin_memory_engine  # type: ignore

from .ClientUtils import VERSION
from .Items import ITEM_TABLE, LOOKUP_ID_TO_NAME
from .Locations import LOCATION_TABLE, TPLocation, TPLocationType
import Utils
from CommonClient import (
    ClientCommandProcessor,
    CommonContext,
    logger,
    server_loop,
    gui_enabled,
    get_base_parser,
)

from NetUtils import NetworkItem, ClientStatus

if TYPE_CHECKING:
    import kvui

CONNECTION_REFUSED_GAME_STATUS = "Dolphin failed to connect. Please load a ROM for Twilight Princess. Trying again in 5 seconds..."
CONNECTION_REFUSED_SAVE_STATUS = "Dolphin failed to connect. Please load into the save file. Trying again in 5 seconds..."
CONNECTION_LOST_STATUS = "Dolphin connection was lost. Please restart your emulator and make sure Twilight Princess is running."
CONNECTION_CONNECTED_STATUS = "Dolphin connected successfully."
CONNECTION_INITIAL_STATUS = "Dolphin connection has not been initiated."

# CURR_HEALTH_ADDR = 0x804061C2
# CURR_NODE_ADDR = 0x80406B38
# SLOT_NAME_ADDR = 0x80406374
# ITEM_WRITE_ADDR = 0x80406AB0
# EXPECTED_INDEX_ADDR = 0x80406734
# NODES_START_ADDR = 0x804063B0
# ACTIVE_NODE_ADDR = 0x80406B18

DEBUGGING = True


def set_address(
    regionCode=None,
    curr_health_addr=None,
    curr_node_addr=None,
    slot_name_addr=None,
    item_write_addr=None,
    expected_index_addr=None,
    nodes_start_addr=None,
    active_node_addr=None,
):
    global STRING_ENCODING
    if regionCode is None:
        regionCode = read_byte(0x80000003)
    saveFileAddr = 0x804061C0  # US by default
    STRING_ENCODING = "ascii"
    match (regionCode):
        case 0x50:  # ASCII for 'P', which is EU
            saveFileAddr = 0x80408160
            STRING_ENCODING = "ascii"
        case 0x4A:  # ASCII for 'J', which is JP
            saveFileAddr = 0x80400300
            STRING_ENCODING = "shift-jis"

    global CURR_HEALTH_ADDR, CURR_NODE_ADDR, SLOT_NAME_ADDR, ITEM_WRITE_ADDR, EXPECTED_INDEX_ADDR, NODES_START_ADDR, ACTIVE_NODE_ADDR, SAVE_FILE_ADDR

    CURR_HEALTH_ADDR = (
        curr_health_addr if curr_health_addr is not None else saveFileAddr + 0x2
    )
    CURR_NODE_ADDR = (
        curr_node_addr if curr_node_addr is not None else saveFileAddr + 0x978
    )
    SLOT_NAME_ADDR = (
        slot_name_addr if slot_name_addr is not None else saveFileAddr + 0x1B4
    )
    ITEM_WRITE_ADDR = (
        item_write_addr if item_write_addr is not None else saveFileAddr + 0x8F0
    )
    EXPECTED_INDEX_ADDR = (
        expected_index_addr if expected_index_addr is not None else saveFileAddr + 0x900
    )
    NODES_START_ADDR = (
        nodes_start_addr if nodes_start_addr is not None else saveFileAddr + 0x1F0
    )
    ACTIVE_NODE_ADDR = (
        active_node_addr if active_node_addr is not None else saveFileAddr + 0x958
    )
    SAVE_FILE_ADDR = saveFileAddr


# ...existing code...


class TPCommandProcessor(ClientCommandProcessor):
    """
    Command processor for the Twilight Princess client.

    This class handles all commands that are specific to the Twilight Princess client.
    """

    def __init__(self, ctx: CommonContext):
        """
        Initialize the command processor with the provided context.

        :param ctx: Context for the client.
        """
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        """Display the current Dolphin emulator connection status."""
        if isinstance(self.ctx, TPContext):
            assert isinstance(self.ctx.dolphin_status, str)

            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")

    def _cmd_debug(self) -> None:
        """Toggles Debug messages from showing"""
        global DEBUGGING
        DEBUGGING = not DEBUGGING

    @mark_raw
    def _cmd_name(self, name: str = "") -> None:
        """Change the name of the current save file"""

        if not isinstance(self.ctx, TPContext):
            return

        assert isinstance(name, str)

        if self.ctx.dolphin_status != CONNECTION_CONNECTED_STATUS:
            logger.info("Client must be connected to dolphin first")
            return

        if self.ctx.current_node == 0xFF:
            logger.info("Must be in game to change name")
            return

        if len(name) > 16:
            name = name[:16]

        # Pad the name with 0x00 characters to make it 16 characters long
        padded_name = name.ljust(16, "\x00")

        logger.info(f"Writing name {padded_name}")
        write_string(SLOT_NAME_ADDR, padded_name)
        return


class TPContext(CommonContext):
    """
    The context for Twilight Princess client.

    This class manages all interactions with the Dolphin emulator and the Archipelago server for Twilight Princess.
    """

    command_processor = TPCommandProcessor
    game: str = "Twilight Princess"
    items_handling: int = 0b111

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        """
        Initialize the context with the provided server address and password.

        :param server_address: The address of the Archipelago server.
        :param password: The password for the server.
        """
        super().__init__(server_address, password)
        self.items_received_2: list[tuple[NetworkItem, int]] = []
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = CONNECTION_INITIAL_STATUS
        self.awaiting_dolphin: bool = False
        self.last_received_index: int = -1
        self.has_send_death: bool = False
        self.current_node: int = 0xFF

    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        """
        Disconnect from the server and stop the Dolphin synchronization task.

        :param allow_autoreconnect: Whether to allow the client to automatically reconnect to the server.
        """
        self.auth = None
        await super().disconnect(allow_autoreconnect)

    async def server_auth(self, password_requested: bool = False) -> None:
        """
        Authenticate with the Archipelago server.

        :param password_requested: Whether the server requires a password. Defaults to `False`.
        """
        assert isinstance(password_requested, bool)

        if password_requested and not self.password:
            await super().server_auth(password_requested)
        if not self.auth:
            if self.awaiting_dolphin:
                return
            self.awaiting_dolphin = True
            logger.info("Awaiting connection to Dolphin to get player information.")
            return
        await self.send_connect()

    def on_package(self, cmd: str, args: dict[str, Any]) -> None:
        """
        Handle incoming packages from the server.

        :param cmd: The command received from the server.
        :param args: The command arguments.
        """
        if cmd == "Connected":
            self.items_received_2 = []
            self.last_received_index = -1
            if args["slot_data"] is not None and "DeathLink" in args["slot_data"]:
                assert isinstance(
                    args["slot_data"]["DeathLink"], int
                ), f"{args["slot_data"]["DeathLink"]=}"
                Utils.async_start(
                    self.update_death_link(bool(args["slot_data"]["DeathLink"]))
                )
                if DEBUGGING:
                    logger.info(
                        f"Debug: Seting deathlink to {bool(args["slot_data"]["DeathLink"])}"
                    )
            if args["slot_data"] is not None and (
                not args["slot_data"]["World Version"]
                or args["slot_data"]["World Version"] != VERSION
            ):
                logger.warning(
                    f"""Error: Client version does not match version of generated seed. 
                            Things may not work as intended,
                            Seed version:{args["slot_data"]["World Version"]} client version:{VERSION}"""
                )
            # Request the connected slot's dictionary (used as a set) of visited stages.
        elif cmd == "ReceivedItems":
            if args["index"] >= self.last_received_index:
                self.last_received_index = args["index"]
                for item in args["items"]:
                    self.items_received_2.append((item, self.last_received_index))
                    self.last_received_index += 1
            self.items_received_2.sort(key=lambda v: v[1])
        elif cmd == "Retrieved":
            requested_keys_dict = args["keys"]
            # Read the connected slot's dictionary (used as a set) of visited stages.
            if self.slot is not None:
                # self.slot.visited_stages = requested_keys_dict
                pass

    def on_deathlink(self, data: dict[str, Any]) -> None:
        """
        Handle a DeathLink event.

        :param data: The data associated with the DeathLink event.
        """
        if DEBUGGING:
            logger.info("Debug: on deathlink trigger")

        super().on_deathlink(data)
        _give_death(self)

    def make_gui(self) -> type["kvui.GameManager"]:
        """
        Initialize the GUI for Twilight Princess client.

        :return: The client's GUI.
        """
        ui = super().make_gui()
        ui.base_title = "Archipelago Twilight Princess Client"
        return ui


def read_byte(console_address: int) -> int:
    """
    Read a byte from Dolphin memory.

    :param console_address: Address to read from.
    :return: The value read from memory.
    """
    assert isinstance(console_address, int)
    result = dolphin_memory_engine.read_byte(console_address)
    assert isinstance(result, int)
    return result


def read_short(console_address: int) -> int:
    """
    Read a short from Dolphin memory.

    :param console_address: Address to read from.
    :return: The value read from memory.
    """
    assert isinstance(console_address, int)
    result = int.from_bytes(
        dolphin_memory_engine.read_bytes(console_address, 2), byteorder="big"
    )
    assert isinstance(result, int)
    return result


def read_string(console_address: int, strlen: int) -> str:
    """
    Read a string from Dolphin memory.

    :param console_address: Address to read from.
    :param strlen: Length of the string to read.
    :return: The string read from memory.
    """
    assert isinstance(console_address, int)
    assert isinstance(strlen, int)
    result = (
        dolphin_memory_engine.read_bytes(console_address, strlen)
        .split(b"\0", 1)[0]
        .decode(STRING_ENCODING)
    )
    assert isinstance(result, str)
    return result


def write_byte(console_address: int, value: int) -> None:
    """
    Write a byte to Dolphin memory.

    :param console_address: Address to write to.
    :param value: Value to write.
    """
    assert isinstance(console_address, int)
    assert isinstance(value, int)

    dolphin_memory_engine.write_bytes(
        console_address, value.to_bytes(1, byteorder="big")
    )


def write_short(console_address: int, value: int) -> None:
    """
    Write a short to Dolphin memory.

    :param console_address: Address to write to.
    :param value: Value to write.
    """
    assert isinstance(console_address, int)
    assert isinstance(value, int)

    dolphin_memory_engine.write_bytes(
        console_address, value.to_bytes(2, byteorder="big")
    )


def write_string(console_address: int, string: str) -> None:
    """
    Write a string to Dolphin memory.

    :param console_address: Address to write to.
    :param string: String to write.
    """
    assert isinstance(console_address, int)
    assert isinstance(string, str)

    if len(string) > 16:
        raise ValueError("String length must be 16 characters or less.")

    dolphin_memory_engine.write_bytes(
        console_address, string.encode(STRING_ENCODING) + b"\0"
    )


def _give_death(ctx: TPContext) -> None:
    """
    Trigger the player's death in-game by setting their current health to zero.

    :param ctx: Twilight Princess client context.
    """
    if DEBUGGING:
        logger.info("Debug: Trying to kill player")

    if (
        ctx.slot is not None
        and dolphin_memory_engine.is_hooked()
        and ctx.dolphin_status == CONNECTION_CONNECTED_STATUS
    ):
        ctx.has_send_death = True
        write_short(CURR_HEALTH_ADDR, 0)
        if DEBUGGING:
            logger.info("Debug: Health set to 0")


async def _give_item(ctx: TPContext, item_name: str) -> None:
    """
    Give an item to the player in-game.

    :param ctx: Twilight Princess client context.
    :param item_name: Name of the item to give.
    :return: Whether the item was successfully given.
    """
    assert isinstance(item_name, str)

    if not await check_ingame(ctx) or read_byte(CURR_NODE_ADDR) == 0xFF:
        return False

    if item_name not in ITEM_TABLE:
        logger.info(
            f"Error: Cannot give item {item_name} as it is not in the item table"
        )

    assert isinstance(ITEM_TABLE[item_name].item_id, int)

    # Items are written into a stack, this allows for more then one item to be given at a time.
    # However items will still be collected one at a time
    # By nature of stack, items may not be collected in oreder recieved
    i = 0
    while True:
        if i > 7:
            if DEBUGGING:
                logger.info("Debug: Item Stack full so an item cannot be given")
            return False

        item_stack_addr = ITEM_WRITE_ADDR + i
        assert isinstance(item_stack_addr, int)

        if read_byte(item_stack_addr) == 0x00:
            item_stack_addr = ITEM_WRITE_ADDR + i
            write_byte(item_stack_addr, ITEM_TABLE[item_name].item_id)
            return True

        i += 1
    # assert item_stack_addr >= ITEM_WRITE_ADDR and item_stack_addr <= ITEM_WRITE_ADDR + 7


async def give_items(ctx: TPContext) -> None:
    """
    Give the player all outstanding items they have yet to receive.

    :param ctx: Twilight Princess client context.
    """
    if (
        await check_ingame(ctx)
        and dolphin_memory_engine.read_byte(CURR_NODE_ADDR) != 0xFF
    ):
        # Read the expected index of the player, which is the index of the latest item they've received.
        expected_idx = read_short(EXPECTED_INDEX_ADDR)

        # Loop through items to give.
        for item, idx in ctx.items_received_2:
            assert item.item in LOOKUP_ID_TO_NAME, f"{item=}"

            # If the item's index is greater than the player's expected index, give the player the item.
            if expected_idx <= idx:
                if DEBUGGING:
                    logger.info(f"Debug: getting item: {LOOKUP_ID_TO_NAME[item.item]}")
                # Attempt to give the item and increment the expected index.
                while not await _give_item(ctx, LOOKUP_ID_TO_NAME[item.item]):
                    await asyncio.sleep(0.1)

                # Increment the expected index.
                write_short(EXPECTED_INDEX_ADDR, idx + 1)


async def check_locations(ctx: TPContext) -> None:
    """
    Iterate through all locations and check whether the player has checked each location.
    If the location is in the active node check memory rather than save data

    Update the server with all newly checked locations since the last update. If the player has completed the goal,
    notify the server.

    :param ctx: Twilight Princess client context.
    """
    current_node = read_byte(CURR_NODE_ADDR)

    locations_read = set()

    # node_start_addr = (current_node * 0x20) + NODES_START_ADDR

    for location, data in LOCATION_TABLE.items():

        # There might be a better way but this works for now
        # Also this data is a flag so node handling is not needed
        if location == "Hyrule Castle Ganondorf":
            addr = SAVE_FILE_ADDR + data.offset
            byte = read_byte(addr)
            checked = (byte & data.bit) != 0
            if checked:
                if not ctx.finished_game:
                    logger.info("Game finishing")
                # It sends multiple times incase the server does not acknoledge.
                # Upon completion check locations will stop running
                await ctx.send_msgs(
                    [{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]
                )
                ctx.finished_game = True
            continue

        # If there is not a valid apid dont bother checking that location
        # apids not given when logic only location
        if not isinstance(data.code, int):
            continue

        # Debug functionality
        if DEBUGGING and (
            not isinstance(data.bit, int) or not isinstance(data.offset, int)
        ):
            logger.info(f"Debug: location:{location} has weird formating")
            continue

        # Depening on locatin type find the memory address for the flag
        # Checks the active memory for the current node
        match (data.type):
            case TPLocationType.Region:
                region = data.region.value
                assert (
                    isinstance(region, int) and data.offset < 0x20
                ), f"Location {location=} has bad region {region} {data=}"
                if region == current_node:
                    addr = ACTIVE_NODE_ADDR + data.offset
                else:
                    addr = (region * 32) + NODES_START_ADDR + data.offset
            case TPLocationType.Flag:
                addr = SAVE_FILE_ADDR + data.offset
            case TPLocationType.Event:
                if DEBUGGING:
                    logger.info(f"Debug: {location}, is an event with an apid")
                continue

        byte = read_byte(addr)
        checked = (byte & data.bit) != 0
        if checked:
            locations_read.add(TPLocation.get_apid(data.code))

    # Incase the stage changed during location checking
    asyncio.sleep(0.1)
    if current_node != read_byte(CURR_NODE_ADDR):
        if DEBUGGING:
            logger.info("Debug: Stage changed during location checks skiping checks")
        return

    new_locations_checked = locations_read.difference(ctx.locations_checked)
    if new_locations_checked:
        if DEBUGGING:
            logger.info(f"Debug: Sending location checks: {new_locations_checked}")
        await ctx.send_msgs(
            [{"cmd": "LocationChecks", "locations": new_locations_checked}]
        )
        # This might be needed if the clinet doesn't sync, it might also brick if msg is sent but nothing happens
        ctx.locations_checked.update(new_locations_checked)


async def check_alive() -> bool:
    """
    Check if the player is currently alive in-game.

    :return: `True` if the player is alive, otherwise `False`.
    """
    cur_health = read_short(CURR_HEALTH_ADDR)
    return cur_health > 0


async def check_death(ctx: TPContext) -> None:
    """
    Check if the player is currently dead in-game.
    If DeathLink is on, notify the server of the player's death.

    :return: `True` if the player is dead, otherwise `False`.
    """
    if ctx.slot is not None and await check_ingame(ctx):
        cur_health = read_short(CURR_HEALTH_ADDR)
        if cur_health == 0:
            if not ctx.has_send_death and time.time() >= ctx.last_death_link + 5:
                if DEBUGGING:
                    logger.info(
                        "Debug: Sending Death to other players will not send death until player is alive"
                    )
                ctx.has_send_death = True
                await ctx.send_death(ctx.player_names[ctx.slot] + " ran out of hearts.")
        else:
            if DEBUGGING and ctx.has_send_death:
                logger.info("Debug: Player is now alive")
            ctx.has_send_death = False


async def check_ingame(ctx: TPContext) -> bool:
    """
    Check if the player is currently in-game.
    If the player switches to hyrule field wait 3s to see if the node updates to the menu
    (This check will occur only once per load to the field, but I will slow the client from working)

    :return: `True` if the player is in-game, otherwise `False`.
    """
    current_node = read_byte(CURR_NODE_ADDR)
    if current_node == ctx.current_node:
        return current_node != 0xFF

    # If Node changed check for chnge to hyrule field
    if current_node != 0x06:
        ctx.current_node = current_node
        return current_node != 0xFF

    await asyncio.sleep(3)
    new_node = read_byte(CURR_NODE_ADDR)

    if new_node == 0x06:
        ctx.current_node = 0x06
        return True
    else:
        ctx.current_node = new_node
        return new_node != 0xFF


async def dolphin_sync_task(ctx: TPContext) -> None:
    """
    The task loop for managing the connection to Dolphin.

    While connected, read the emulator's memory to look for any relevant changes made by the player in the game.

    :param ctx: Twilight Princess client context.
    """
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    while not ctx.exit_event.is_set():
        try:
            if (
                dolphin_memory_engine.is_hooked()
                and ctx.dolphin_status == CONNECTION_CONNECTED_STATUS
            ):

                if not await check_ingame(ctx):
                    await asyncio.sleep(0.1)
                    continue
                if ctx.slot is not None:
                    if "DeathLink" in ctx.tags:
                        await check_death(ctx)
                    await give_items(ctx)
                    await check_locations(ctx)
                else:
                    if not ctx.auth:
                        ctx.auth = read_string(SLOT_NAME_ADDR, 0x40)
                    if ctx.awaiting_dolphin:
                        await ctx.server_auth()
                await asyncio.sleep(0.1)
            else:
                if ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
                    logger.info("Connection to Dolphin lost, reconnecting...")
                    ctx.dolphin_status = CONNECTION_LOST_STATUS
                logger.info("Attempting to connect to Dolphin...")
                dolphin_memory_engine.hook()
                if dolphin_memory_engine.is_hooked():
                    try:
                        if not (
                            dolphin_memory_engine.read_bytes(0x80000000, 3) == b"GZ2"
                            and dolphin_memory_engine.read_byte(0x80000003)
                            in [
                                ord("E"),
                                ord("P"),
                                ord("J"),
                            ]
                        ):
                            logger.info(CONNECTION_REFUSED_GAME_STATUS)
                            ctx.dolphin_status = CONNECTION_REFUSED_GAME_STATUS
                            dolphin_memory_engine.un_hook()
                            await asyncio.sleep(5)
                        else:
                            logger.info(CONNECTION_CONNECTED_STATUS)
                            ctx.dolphin_status = CONNECTION_CONNECTED_STATUS
                            ctx.locations_checked = set()
                            set_address()
                    except NameError as e:
                        logger.error(f"Global address not set: {e}")
                        set_address(regionCode=ord("E"))
                    except Exception as e:
                        logger.error(f"Unexpected error: {e}")
                        raise e
                else:
                    logger.info(
                        "Connection to Dolphin failed, attempting again in 5 seconds..."
                    )
                    ctx.dolphin_status = CONNECTION_LOST_STATUS
                    await ctx.disconnect()
                    await asyncio.sleep(5)
                    continue
        except Exception:
            dolphin_memory_engine.un_hook()
            logger.info(
                "Connection to Dolphin failed due to error, attempting again in 5 seconds..."
            )
            logger.error(traceback.format_exc())

            ctx.dolphin_status = CONNECTION_LOST_STATUS
            await ctx.disconnect()
            await asyncio.sleep(5)
            continue


def main(connect: Optional[str] = None, password: Optional[str] = None) -> None:
    """
    Run the main async loop for the Twilight Princess client.

    :param connect: Address of the Archipelago server.
    :param password: Password for server authentication.
    """
    Utils.init_logging("Twilight Princess Client")

    async def _main(connect: Optional[str], password: Optional[str]) -> None:
        ctx = TPContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        ctx.dolphin_sync_task = asyncio.create_task(
            dolphin_sync_task(ctx), name="DolphinSync"
        )

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.dolphin_sync_task:
            await asyncio.sleep(3)
            await ctx.dolphin_sync_task

    import colorama  # type: ignore

    colorama.init()
    asyncio.run(_main(connect, password))
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser()
    args = parser.parse_args()
    main(args.connect, args.password)
