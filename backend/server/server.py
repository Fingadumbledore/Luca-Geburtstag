from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import socketserver
import time
import logging
import sqlite3
from urllib import parse

PORT = 8000
date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
log = date
 
connection = sqlite3.connect("login.db")

# Datensatz-Cursor erzeugen
cursor = connection.cursor()

class Serve(BaseHTTPRequestHandler):

      



    def log_server(self, log):
        datei = open('server.log','a')
        datei.write('\n' + " " + log )
        log = date
        datei.close()

    def do_GET(self):
        if self.path == '/':
            self.path = '../../../frontend/sites/index.html'
        if self.path == '/matrix':
            self.path  = '../../../frontend/sites/matrix.html'

        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            log = date + " 200"
            # datei.write('\n' + " " + date)
        except:
            file_to_open = "File not found"
            self.send_response(400)
            log = date + " " +file_to_open
        finally:
            
            self.log_server(log)
            #datei.write('\n' + " " + log)
            #logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
            #logging.error(file_to_open)

        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

        parsed = parse.urlparse(self.path)

        if parsed.path == '/search':

            # convert to sql query and execute
            print( "hier ist die query: " + parsed.query)
            verbindung = sqlite3.connect("login.db")
            zeiger = verbindung.cursor()
            zeiger.execute(parsed.query)
            inhalt = zeiger.fetchall()
            print(inhalt)
            verbindung.close()
            
            

    def do_POST(self):

        try:
            self.send_responses(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile(bytes('{"time": "' + date + '"}',"utf-8"))
        except:
                self.send_response(400)
                #print("POST error")
try:
    httpd = HTTPServer(('0.0.0.0', PORT), Serve)
    log = log + "server is now running on 127.0.0.1:" + str(PORT)
    #log_server(log)
    print("server is now running on http://127.0.0.1:" + str(PORT))

    httpd.serve_forever()
except KeyboardInterrupt:
        pass
    #Server beenden, und Datein speichern/in Sammlung schieben
        httpd.server_close()
        print("\nServer stopped.")
        print("saving files")
        
