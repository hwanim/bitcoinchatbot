import requests
from bs4 import BeautifulSoup as bs
import json
from microsoftbotframework import ReplyToActivity

def make_response(message):
    # input_image = #input message
    # path = #extract the path of picture in input_image
    if message["type"] == "message":
        ReplyToActivity(fill=message,text=get_bitcoinprice(btc_krw)).send()



bitcoin = 'btc_krw'

def get_bitcoinprice(bitcoin):
    req = requests.get('https://api.korbit.co.kr/v1/ticker?currency_pair={}'.format(bitcoin))
    return(req.json()['last'])
