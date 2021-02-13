from dolar_abstraction.helper import Provider


class AwesomeApi(Provider):
    def get_raw_dollar_data(self):
        ...

    def transform_raw_data(self): ...