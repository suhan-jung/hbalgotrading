import os
import eikon as ek
from dotenv import load_dotenv
from .data_provider import DataProvider
from .log_manager import LogManager

load_dotenv()

class EikonDataProvider(DataProvider):
    """
    Refinitiv Eikon Data API를 활용하여 krx의 실시간 거래 데이터를 제공하는 클래스

    """
    AVAILABLE_ASSET = {"LKTB": "10TBc1", "KTB": "KTBc1"}

    def __init__(self, asset="LKTB"):
        if asset not in self.AVAILABLE_ASSET:
            raise UserWarning(f"not supported asset: {asset}")

        self.logger = LogManager.get_logger(__class__.__name__)
        self.APP_KEY = os.environ.get("EIKON_API_KEY", "eikon_api_key")
        self.asset = asset

    def get_info(self):
        """실시간 거래 정보 전달한다

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
        """
        data = self.__get_data_from_server()
        return self.__create_candle_info(data[0])

    def __create_candle_info(self, data):
        try:
            return {
                "market": self.asset,
                "date_time": data["Date"],
                "opening_price": float(data["OPEN"]),
                "high_price": float(data["HIGH"]),
                "low_price": float(data["LOW"]),
                "closing_price": float(data["CLOSE"]),
                "acc_price": float(0),
                "acc_volume": float(data["VOLUME"]),
            }
        except KeyError as err:
            self.logger.warning(f"invalid data for candle info: {err}")
            return None

    def __get_data_from_server(self):
        try:
            ek.set_app_key(self.APP_KEY)
            response = ek.get_timeseries(self.AVAILABLE_ASSET[self.asset], interval="minute", count=1)
            response.index = response.index.tz_localize('UTC').tz_convert('Asia/Seoul').tz_localize(None).strftime('%Y-%m-%dT%X')
            return response.reset_index().to_dict(orient='records')
        except ValueError as error:
            self.logger.error(f"Invalid parameter type of value: {error}")
            raise UserWarning("Parameter type or value is wrong") from error
        except Exception as error:
            self.logger.error(f"Invalid data from server: {error}")
            raise UserWarning("Fail get data from sever") from error
