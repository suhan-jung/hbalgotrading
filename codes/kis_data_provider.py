from .data_provider import DataProvider
class KisDataProvider(DataProvider):
    """
    한국투자증권 rest API를 활용하여 krx의 실시간 거래 데이터를 제공하는 클래스

    """
    def __init__(self, ticker=""):
        pass

    def get_info(self):
        '''
        Returns: 거래 정보 딕셔너리
        {
            "market": 거래 시장 종류 BTC
            "date_time": 정보의 기준 시간
            "opening_price": 시작 거래 가격
            "high_price": 최고 거래 가격
            "low_price": 최저 거래 가격
            "closing_price": 마지막 거래 가격
            "acc_price": 단위 시간내 누적 거래 금액
            "acc_volume": 단위 시간내 누적 거래 양
        }

        '''

        now = self.index

        if now >= len(self.data) :
            return None

        self.index = now+1

        self.logger.info(f'[DATA'@ {self.data[now]["candel_date_time_utc"]}'')
        return self.__create_candle_info(self.data[now])

        

    def initialize_kis_connect(self):

        self.index = 0
        pass

    def __create_candle_info(self, data):

        try :
            return            {
                "market": data["marget"],
                "date_time": data["candle_date_time_kst"],
                "opening_price": data["opening_price"],
                "high_price": data["high_price"],
                "low_price": data["low_price"],
                "closing_price": data["closing_price"],
                "acc_price": data["candle_acc_trade_price"],
                "acc_volume": data["candle_acc_trade_volume"],
            }
        except KeyError:
            self.logger.warning("invalid data for candle info")
            return None

        

    def __get_data_from_server(self):
        pass
    pass
