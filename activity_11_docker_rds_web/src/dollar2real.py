# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 11 - Extract the dollar to real exchange rate, saving it into a database. All quotes are then displayed using a dynamically generated web page. 

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import mysql.connector
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

EXCHANGE_RATE_URL = 'https://themoneyconverter.com/USD/BRL'

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        # only accept self.path = "/"
        if self.path != '/':
            return 

        # get quote and update db
        req = requests.get(EXCHANGE_RATE_URL)
        soup = BeautifulSoup(req.content, 'html.parser')
        el = soup.find('output')
        exch_rate = float(el.text.split(' ')[3])
        today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        sql = f"INSERT INTO quotes VALUES ('{today}', {exch_rate})"
        cursor = self.db.cursor()
        cursor.execute(sql)
        db.commit()

        # generate a response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes('''
            <html>
            <head>
                <title>Dollar to Real</title>
                <style>
                    body {
                        font:18px/1.4 Verdana,Arial; 
                        background: #fff; 
                        height:100%; 
                        margin:25px 0; 
                        padding:0;
                        text-align: center
                    }

                    p {
                        margin-top:0
                    }

                    table { 
                        border: 1px solid black; 
                        margin: 0 auto; 
                        border-collapse: separate;
                        box-sizing: border-box;
                        table-layout: fixed;
                        width: 900px;
                    }

                    th, td { 
                        border: 1px solid black;
                        text-align: center; 
                    }

                    thead { 
                        background: #008CBA; 
                        color: #fff; 
                    }

                    tbody { 
                        background: #fff; 
                        color: #000; 
                    }
                </style>
            </head> 
        ''', "utf-8"))
        self.wfile.write(bytes('''
            <body>
                <table class="table table-striped table-bordered table-sm">  
                    <thead class="thead-dark">  
                        <tr>  
                            <th>Date</th>  
                            <th>Time</th>  
                            <th>Exchange Rate</th>  
                        </tr>  
                    </thead>  
                    <tbody class="tbody-light">  
        ''', "utf-8"))
        sql = "SELECT `datetime`, quote FROM quotes ORDER BY `datetime` DESC"
        cursor = self.db.cursor(buffered = True)
        cursor.execute(sql)
        for date_time, quote in cursor:
            date = date_time.date()
            time = date_time.time()
            self.wfile.write(bytes(f"<tr><td>{date}</td><td>{time}</td><td>{quote}</td></tr>", "utf-8")) 
        self.wfile.write(bytes('''
                    </tbody>  
                </table>  
            </body>  
        </html>
        ''', "utf-8"))

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

    # attempt to start a web server
    my_handler = MyHandler 
    my_handler.db = db
    webServer = HTTPServer(('0.0.0.0', 8000), my_handler)
    print("Ready to serve!")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
    db.close()