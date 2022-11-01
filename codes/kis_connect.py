import json
import requests
import dotenv
import os 
from datetime import datetime

class KisConnect:

    def __init__(self):
        dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv(dotenv_file)

        self.apikey = os.environ.get('apikey')
        self.apisecret = os.environ.get('apisecret')

        self.token = ""
        self.token_expired = ""

        self.data = []

    def getAuth(self):

        body  = { 'grant_type': "client_credentials", 'appkey' : self.apikey, 'appsecret' : self.apisecret }
        url = "https://openapi.koreainvestment.com:9443"
        url2 = "/oauth2/tokenP"

        r = requests.post( url + url2 , data = json.dumps(body) )

        dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv(dotenv_file)

        print ( r.status_code,  r.json() )
        #dotenv.setkey(dotenv_file,'access_token',r.json()["access_token"]  )
        #dotenv.setkey(dotenv_file,'token_expired',r.json()["access_token_token_expired"]  )
        #dotenv.setkey(dotenv_file,'token_type',r.json()["token_type"]  )

        self.token = r.json()["access_token"].replace("\r","").replace("\n","")
        self.token_expired = r.json()["access_token_token_expired"].replace("\r","").replace("\n","")
        
        f = open( r"../KISAUTH.ini" , "wt")

        f.write( r.json()["access_token"] + '\n' )
        f.write( r.json()["access_token_token_expired"] + '\n' )
        f.write( r.json()["token_type"] + '\n' )
        
    def loadAuth(self):
        
        if self.token == "" :
            f = open( r"../KISAUTH.ini" , "rt")
            idx = 0

            for s in f :
                if idx == 0 :
                    self.token = s.replace("\r","").replace("\n","")

                if idx == 1 :
                    self.token_expired = s.replace("\r","").replace("\n","")

                idx +=1 

        s = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if s > self.token_expired :
            self.getAuth()

        return self.token

    def getData(self, cont = "") :

        url = "https://openapi.koreainvestment.com:9443"
        url2 = "/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice"


        body  = { 'grant_type': "client_credentials", 'appkey' : self.apikey, 'appsecret' : self.apisecret }
 

        params =  {
            "fid_cond_mrkt_div_code": "J",
            "fid_etc_cls_code": "",
            "fid_input_hour_1": "100000",
            "fid_input_iscd": "000660",
            "fid_pw_data_incu_yn": "Y"
        }

        access_token = self.loadAuth()

        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "authorization": f"Bearer {access_token}",    
            "appKey": self.apikey,
            "appSecret": self.apisecret,      
            "tr_id" : "FHKST03010200",
            "tr_cont": cont,
            "custtype": "P",
            "seq_no": ""
            
        }

        r = requests.get( url + url2 , params = params, headers = headers )

        #print(r.json())
        #print(r.header())
        return r.json()['output2']