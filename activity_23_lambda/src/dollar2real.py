# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 23 - Extract the dollar to real exchange rate

import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

EXCHANGE_RATE_URL = 'https://themoneyconverter.com/USD/BRL'

def lambda_handler(event, context):
    req = requests.get(EXCHANGE_RATE_URL)
    soup = BeautifulSoup(req.content, 'html.parser')
    el = soup.find('output')
    exch_rate = el.text
    today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    out = f"{exch_rate} in {today}"

    return {
        'statusCode': 200,
        'body': json.dumps(out)
    }
