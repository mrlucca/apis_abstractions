from typing import Tuple
from dolar_abstraction.consumer import dollar_generator


class GetDollar(object):
    def __init__(self):
        self.query_text: str = "{}/{}/{}"
        self.__year: str = None
        self.__day: str = None
        self.__month: str = None
        self.__dollar_value: str = None

    def __query_formater(self) -> str:
        return self.query_text.format(
            self.__year, 
            self.__month, 
            self.__day
        )

    def __get_year(self) -> None:
        print(f"Query: {self.__query_formater()} Exists: {True}")

    def __get_month(self) -> None:
        print(f"Query: {self.__query_formater()} Exists: {True}")

    def __get_day(self) -> None:
        print(f"Query: {self.__query_formater()} Exists: {True}")

    def __setattr__(self, name: str, value: str) -> None:
        if name == "year":
            self.__dict__["_GetDollar__year"] = value
            self.__get_year()
        elif name == "month":
            self.__dict__["_GetDollar__month"] = value
            self.__get_month()
        elif name == "day":
            self.__dict__["_GetDollar__day"] = value
            self.__get_day()
        else:
            self.__dict__[name] = value

    def __call__(self) -> str:
        self.__year = None
        self.__month = None
        self.__day = None
        return self.__dollar_value
