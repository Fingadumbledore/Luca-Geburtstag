from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import socketserver
import time
from urllib import parse

PORT = 8000

class Serve(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '../../frontend/sites/index.html'
        try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(400)
            print(file_to_open)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
        
        parsed = parse.urlparse(self.path)
        if parsed.path == '/search':
            # convert to sql query and execute
            print( "hier ist die query: " + parsed.query)

""""
    def do_POST(self):

        try:
            self.send_responses(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
            self.wfile(bytes('{"time": "' + date + '"}',"utf-8"))
        except:
                self.send_response(400)
                print("POST error")
"""

httpd = HTTPServer(('0.0.0.0', PORT), Serve)
print("server is now running on " + str(PORT))
httpd.serve_forever()