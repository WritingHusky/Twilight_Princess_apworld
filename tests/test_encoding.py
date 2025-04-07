from worlds.twilight_princess_apworld.Items import ITEM_TABLE
from ..Locations import LOCATION_TABLE
from . import TwilightPrincessWorldTestBase
from ..Randomizer.SettingsEncoder import check_list


class TestEncoding(TwilightPrincessWorldTestBase):
    def test_encoding(self) -> None:
        for location, data in LOCATION_TABLE.items():
            if not location in check_list and isinstance(data.code, int):
                self.logger.info(f"{location=} not in check_list")

        for check in check_list:
            if not check in LOCATION_TABLE:
                self.logger.info(f"{check=} not in location table")

    def test_gen_ids(self) -> None:
        if not self.run_generation_tests:
            return

        for location, data in LOCATION_TABLE.items():
            if isinstance(data.code, int):
                self.logger.info(f"{location}, {data.code}")

    def test_gen_item_ids(self) -> None:
        if not self.run_generation_tests:
            return

        for item, data in ITEM_TABLE.items():
            if isinstance(data.code, int):
                self.logger.info(f"{item}, {data.item_id}")
