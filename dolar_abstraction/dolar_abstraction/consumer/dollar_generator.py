import os
import json
from datetime import datetime
from dolar_abstraction import provaiders

class DollarGenerator(object):
    def __init__(
        self, 
        base_data_path: str, 
        new_historical_data_path: str,
        historical_data_path: str 
    ) -> None:
        self.HISTORICAL_DATA_PATH: str = None
        self.raw_data: dict = dict()
        self.historical_data: dict = dict() 
        self.new_data: dict = dict()

    def __load_data(self) -> dict:
        with open(self.HISTORICAL_DATA_PATH, "r") as file:
            return json.load(file)

    def __write_data(self) -> None:
        with open(self.HISTORICAL_DATA_PATH, "w") as file:
            json.dump(self.data, file, indent=4)

    def __historical_data_exists(self) -> bool:
        return os.path.exists(self.HISTORICAL_DATA_PATH)

    def __get_new_data(self) -> dict:
        awesomeapi = provaiders.awesomeapi.AwesomeApi(date_to_search=date_to_search)
        if awesomeapi.is_active():
            data =  awesomeapi()
        self.new_data = data

    def __append_historical_data(self) -> bool:
        if historical_data_exists():
            self.historical_data = load_data()
        else:
            write_data(self.new_data)
            return historical_data_exists()

        new_data = json.loads(json.dumps(self.new_data))
        for year in new_data.keys():
            if not self.historical_data.get(year):
                self.historical_data[year] = {}

            for month in new_data[year].keys():
                if not self.historical_data[year].get(month):
                    self.historical_data[year][month] = {}

                for day in new_data[year][month].keys():
                    if not self.historical_data[year][month].get(day):
                        self.historical_data[year][month][day] = data[year][month][day]

        write_data(self.historical_data)

    def __call__(self) -> bool:
        self.historical_data = self.__load_data()
        self.__get_new_data()
        self.__append_historical_data()
