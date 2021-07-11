# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Lab 02 - The Perry Rhodan Annual Marathon

from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
from urllib import parse
from urllib.parse import unquote
import mysql.connector
import os

class MyHandler(BaseHTTPRequestHandler):

    # handles "/" path requests
    def main(self): 
        pass

    # handles "/submit" path requests
    def submit(self, query_params):
        pass

    # handles "/admin" path requests 
    def admin(self): 
        pass

    # extracts query parameters from the request path (if any available)
    def do_query_parameters(self):
        raw_params = parse.urlparse(unquote(self.path)).query.split('&')
        query_params = {}
        print(raw_params)
        if len(raw_params) > 1:
            query_params['email'] = raw_params[0].split('=')[1]
            query_params['first'] = raw_params[1].split('=')[1]
            query_params['last']  = raw_params[2].split('=')[1]
            query_params['birth'] = raw_params[3].split('=')[1]
            query_params['event'] = raw_params[4].split('=')[1]
            query_params['time']  = raw_params[5].split('=')[1]
        return query_params

    # handles all requests
    def do_GET(self):

        # validates the given path
        path = parse.urlparse(self.path).path
        if path != '/' and path != '/submit' and path != '/admin':
            return 

        # generates the response headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # gets the hostname and today's date/time
        self.hostname = socket.gethostname()
        self.today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        
        # decides which specific method to call based on self.path
        if path == '/submit':
            query_params = self.do_query_parameters()
            self.submit(query_params)
        elif path == '/admin':
            self.admin()
        else:
            self.main()

if __name__ == "__main__":

    # delete the following lines once you are satisfied with the db connection 
    # make sure to create those variables in your EC2 instances using the user-data.sh script
    # os.environ['DB_HOST']     = ''
    # os.environ['DB_NAME']     = 'perryrhodan'
    # os.environ['DB_USER']     = 'perryrhodan'
    # os.environ['DB_PASSWORD'] = '135791'    

    # attempt to connect to MySQL
    db = mysql.connector.connect(
        host     = os.getenv('DB_HOST'),
        database = os.getenv('DB_NAME'),
        user     = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD')
    )

    # attempt to start a web server
    my_handler = MyHandler
    webServer = HTTPServer(('0.0.0.0', 8000), my_handler)
    print("Ready to serve!")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")