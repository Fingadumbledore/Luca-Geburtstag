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
        parsed = parse.urlparse(self.path)
        match self.path: 
            case '/': 
                self.path = '../../../frontend/sites/index.html'
            case '/matrix':
                self.path  = '../../../frontend/sites/matrix.html'
            case '/search':
                self.search(parsed.query)

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
      
    def search(self, q):
        # convert to sql query and execute
        print( "hier ist die query: " + q)
        # connect to db
        verbindung = sqlite3.connect("login.db")
        zeiger = verbindung.cursor()
        query = f"select * from user where search-type is  "
        zeiger.execute(query)
        inhalt = zeiger.fetchall()
        print(inhalt)
        verbindung.close()

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
