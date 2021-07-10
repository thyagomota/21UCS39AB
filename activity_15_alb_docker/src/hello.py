# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 13 - A Simple Hello App

from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        # only accept self.path = "/"
        if self.path != '/':
            return 

        # get the hostname and today's date/time
        hostname = socket.gethostname()
        today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        # generate a response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes('''
            <html>
                <head>
                    <title>Hello App</title>
                </head> 
                <body>
        ''', "utf-8"))
        self.wfile.write(bytes(f"Hello, and welcome to {hostname}<P>{today}", "utf-8"))
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