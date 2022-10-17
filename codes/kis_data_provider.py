from .data_provider import DataProvider
class KisDataProvider(DataProvider):
    """
    한국투자증권 rest API를 활용하여 krx의 실시간 거래 데이터를 제공하는 클래스

    """
    def __init__(self, ticker=""):
        pass

    def get_info(self):
        pass

    def __create_candle_info(self, data):
        pass

    def __get_data_from_server(self):
        pass
    pass
