import os
import json
import requests
from dotenv import load_dotenv


def get_token(app_key, secret_key, url_base):
    headers = {"content-type":"application/json"}
    body = {"grant_type":"client_credentials",
            "appkey":app_key,
            "appsecret":secret_key}

    path = "oauth2/tokenP"

    url = f"{url_base}/{path}"

    res = requests.post(url, headers=headers, data=json.dumps(body))
    print(res.text)

    return res.json()["access_token"]

def send_order(app_key, secret_key, token, url_base):
    path = "uapi/domestic-futureoption/v1/trading/order"
    url = f"{url_base}/{path}"

    headers = {
        "content-type":"application/json",
        "authorization":f"Bearer {token}",
        "appkey":app_key,
        "appsecret":secret_key,
        "tr_id":"VTTO1101U",
        "custtype":"P",
    }
    datas = {
        "ORD_PRCS_DVSN_CD": "02",
        "CANO": "60019179",
        "ACNT_PRDT_CD": "03",
        "SLL_BUY_DVSN_CD": "02",
        "SHTN_PDNO": "167T03",
        "ORD_QTY": "1",
        "UNIT_PRICE": "111.00",
        "NMPR_TYPE_CD": "01",
        "KRX_NMPR_CNDT_CD": "0",
        "ORD_DVSN_CD": "01"
    }

    res = requests.post(url, headers=headers, data=json.dumps(datas))
    print(res.json())
    return res

def get_trade_tick(url_base, token, app_key, secret_key):
    path = "uapi/domestic-futureoption/v1/quotations/inquire-price"
    querystring = {
        "fid_cond_mrkt_div_code": "CF", #시장분류코드
        "fid_input_iscd": "167T03"
        }
    headers = {
        "content-type":"application/json",
        "authorization":f"Bearer {token}",
        "appkey":app_key,
        "appsecret":secret_key,
        "tr_id":"FHMIF10000000",
    }
    url = f"{url_base}/{path}"
    res = requests.get(url, headers=headers, params=querystring)
    print(res.json())
    return res

def main():
    load_dotenv()
    app_key = os.environ.get("KIS_SIMULATION_APP_KEY")
    secret_key = os.environ.get("KIS_SIMULATION_APP_SECRET_KEY")

    # print(APP_KEY)
    # print(APP_SECRET)
    url_base = "https://openapivts.koreainvestment.com:29443" #모의투자서비스

    token = get_token(app_key,secret_key,url_base)
    # res = send_order(app_key, secret_key, token, url_base
    res = get_trade_tick(url_base, token, app_key, secret_key)
    # print(type(res))
    print(res.json()["output1"]["futs_prpr"])

if __name__ == '__main__':
    main()