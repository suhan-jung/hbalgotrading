import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

APP_KEY = os.environ.get("KIS_SIMULATION_APP_KEY")
APP_SECRET = os.environ.get("KIS_SIMULATION_APP_SECRET_KEY")
print(APP_KEY)
print(APP_SECRET)
URL_BASE = "https://openapivts.koreainvestment.com:29443" #모의투자서비스

headers = {"content-type":"application/json"}
body = {"grant_type":"client_credentials",
        "appkey":APP_KEY, 
        "appsecret":APP_SECRET}

PATH = "oauth2/tokenP"

URL = f"{URL_BASE}/{PATH}"

res = requests.post(URL, headers=headers, data=json.dumps(body))
print(res.text)

ACCESS_TOKEN = res.json()["access_token"]
print(ACCESS_TOKEN)

datas = {
    "CANO": '00000000',
    "ACNT_PRDT_CD": "01",
    "OVRS_EXCG_CD": "SHAA",
    "PDNO": "00001",
    "ORD_QTY": "500",
    "OVRS_ORD_UNPR": "52.65",
    "ORD_SVR_DVSN_CD": "0"
}

