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
