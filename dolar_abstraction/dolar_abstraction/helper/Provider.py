from datetime import datetime
from abc import ABC, abstractmethod
from typing import List


class Provider(ABC):
    def __init__(self, date_to_search: datetime) -> None:
        self.values: list = None
        self.date_to_search = date_to_search
        self.final_data = dict()

    @abstractmethod
    def get_raw_dollar_data(self) -> any:

    @abstractmethod
    def transform_raw_data(self, raw_value: any) -> List[dict]: 
        """ 
        :params
            raw_value -> base value for trasnfor in: List of dicts
        format return:
        [
            {
                "date": timestemp, "value": DOLLAR_VALUE(FLOAT)
            }
        ]

        """
        ...

    @abstractmethod
    def is_active(self) -> bool: ...

    def __call__(self) -> dict:
        raw_value = self.get_raw_dollar_data()
        self.values = self.transform_raw_data(raw_value=raw_value)
        for value in self.values:
            date = value.get("date")
            value = value.get("value")
            if date and value is not None:
                if not self.final_data.get(date.year):
                    self.final_data[date.year] = {}
                if not self.final_data[date.year].get(date.month):
                    self.final_data[date.year][date.month] = {}
                self.final_data[date.year][date.month][date.day] = value

        return self.final_data
