from data_provider import DataProvider
#from kis_connect import KisConnect
#from codes import KisConnect
from kis_connect import KisConnect


class KisDataProvider(DataProvider):
    """
    한국투자증권 rest API를 활용하여 krx의 실시간 거래 데이터를 제공하는 클래스

    """
    def __init__(self, ticker=""):

        self.connect = KisConnect()
        self.index = 0
        self.data = []
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

        self.index = now+1

        self.data = self.__get_data_from_server()
        
        if now >= len(self.data) :
            return None

        #self.logger.info(f'[DATA'@ {self.data[now]["candel_date_time_utc"]})
        return self.__create_candle_info(self.data[now])

        

    def initialize_kis_connect(self):

        self.index = 0
        pass

    def __create_candle_info(self, data):

        try :
            return            {
                "market": data["acml_tr_pbmn"],
                "date_time": data["stck_cntg_hour"],
                "opening_price": data["stck_oprc"],
                "high_price": data["stck_hgpr"],
                "low_price": data["stck_lwpr"],
                "closing_price": data["stck_prpr"],
                "acc_price": data["stck_prpr"],
                "acc_volume": data["cntg_vol"],
            }

        except KeyError:
            #self.logger.warning("invalid data for candle info")
            return None

        

    def __get_data_from_server(self):
        try:
            #ek.set_app_key(self.APP_KEY)
            #response = ek.get_timeseries(self.AVAILABLE_ASSET[self.asset], interval="minute", count=1)
            #return response.reset_index().to_dict(orient='records')
            return self.connect.getData()            
        except ValueError as error:
            #self.logger.error(f"Invalid parameter type of value: {error}")
            raise UserWarning("Parameter type or value is wrong") from error
        except Exception as error:
            #self.logger.error(f"Invalid data from server: {error}")
            raise UserWarning("Fail get data from sever") from error
    
