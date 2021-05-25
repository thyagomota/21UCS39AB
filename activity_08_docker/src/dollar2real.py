# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 08 - Extract the dollar to real exchange rate

import requests
from datetime import date
from bs4 import BeautifulSoup

EXCHANGE_RATE_URL = 'https://themoneyconverter.com/USD/BRL'

if __name__ == "__main__":
    req = requests.get(EXCHANGE_RATE_URL)
    soup = BeautifulSoup(req.content, 'html.parser')
    el = soup.find('output')
    exch_rate = el.text
    today = date.today().strftime("%Y-%m-%d")
    print(f"{exch_rate} in {today}")