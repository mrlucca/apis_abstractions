  
import os 
import json
from datetime import datetime, timedelta


class GetDollarError(Exception):
    ...


class DollarFileNotExists(GetDollarError):
    ...


class GetDollarPrice(object):
    def __init__(
        self, historical_data_path: str 
    ) -> None: 
        self.HISTORICAL_DATA_PATH: str = historical_data_path
        self.dollar_values: dict = None

    def __historical_data_exists(self) -> bool:
        return os.path.exists(self.HISTORICAL_DATA_PATH)

    def get_dollar_data(self) -> None or Exception:
        global dollar_values

        if not os.path.exists(USD_JSON_PATH):
            raise GetDollarError("Dollar folder not exixts!")

        with open(USD_JSON_PATH, 'r') as json_file:
            dollar_values = json.load(json_file)


    def value_exists(
        self, day: str, month: str, year: str,
    ) -> bool:
        if not dollar_values.get(year):
            return False
        if not dollar_values[year].get(month):
            return False
        if not dollar_values[year][month].get(day):
            return False
        return True


    def get_recursive_dollar_price(
        self, date: datetime, recursive: bool = True
    ) -> float or Exception:
        exists = False
        count = 0
        while not exists and count < MAX_RECURSIVE_INTERATION:
            day, month, year = str(date.day), str(date.month), str(date.year)
            print(f"Try {count} of get dollar value", end=" |> ")
            print(f"get price in: [ {day}/{month}/{year} ]")
            exists = value_exists(day=day,month=month,year=year)
            if not recursive: break
            date = date - timedelta(days=1)
            count += 1

        if exists:
            return dollar_values[year][month][day]
        else:
            raise GetDollarError("Dollar value not exists")

    def __call__(self) -> float or Exception:
        if self.__historical_data_exists():
            raise DollarFileNotExists()
        