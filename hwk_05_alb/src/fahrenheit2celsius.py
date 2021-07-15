# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Homework 05 - Fahrenheit to Celsius Web App

from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
from urllib import parse
from urllib.parse import unquote

class MyHandler(BaseHTTPRequestHandler):

    # extracts query parameters from the request path (if any available)
    def do_query_parameters(self):
        #print(self.path)
        raw_params = parse.urlparse(unquote(self.path)).query.split('&')
        query_params = {}
        print(raw_params)
        if len(raw_params) > 0 and len(raw_params[0]) > 0:
            query_params['fahrenheit'] = float(raw_params[0].split('=')[1])
        return query_params

    def do_GET(self):

        # get the hostname and today's date/time
        hostname = socket.gethostname()
        today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        # generate a response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # get the parameter (if any)
        query_params = self.do_query_parameters()
        if 'fahrenheit' not in query_params:
            self.wfile.write(bytes('''
                <html>
                    <head>
                        <title>Temperature Conversion App</title>
                    </head> 
                    <body>fahrenheit parameter is required!</body>
                </html>
            ''', "utf-8"))
        else:
            # convert temperature
            celsius = (query_params['fahrenheit'] - 32) * 5 / 9.
            celsius_string = "{:.2f}".format(celsius)

            self.wfile.write(bytes('''
                <html>
                    <head>
                        <title>Temperature Conversion App</title>
                    </head> 
                    <body>
            ''', "utf-8"))
            self.wfile.write(bytes(f"{query_params['fahrenheit']}F = {celsius_string}C<p><p>{hostname}<P>{today}", "utf-8"))
            self.wfile.write(bytes(''' 
                    </body>
                </html>
            ''', "utf-8"))

if __name__ == "__main__":

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