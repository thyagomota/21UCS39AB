# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 10 - Extract the dollar to real exchange rate, saving it into a database.

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import mysql.connector
import os

EXCHANGE_RATE_URL = 'https://themoneyconverter.com/USD/BRL'

if __name__ == "__main__":

    # delete the following lines once you are satisfied with the db connection and before creating the docker image
    os.environ['DB_HOST']     = 'dollar2real.cvhpjdm21h9e.us-west-1.rds.amazonaws.com'
    os.environ['DB_NAME']     = 'dollar2real'
    os.environ['DB_USER']     = 'dollar2real'
    os.environ['DB_PASSWORD'] = '135791'

    # attempt to connect to MySQL
    db = mysql.connector.connect(
        host     = os.getenv('DB_HOST'),
        database = os.getenv('DB_NAME'),
        user     = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD')
    )
    cursor = db.cursor()

    # get quote and update db
    req = requests.get(EXCHANGE_RATE_URL)
    soup = BeautifulSoup(req.content, 'html.parser')
    el = soup.find('output')
    exch_rate = float(el.text.split(' ')[3])
    today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    sql = f"INSERT INTO quotes VALUES ('{today}', {exch_rate})"
    cursor.execute(sql)
    db.commit()
    db.close()