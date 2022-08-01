from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import sqlite3
import urllib
import urllib.parse

PORT = 8000
date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
log = date

connection = sqlite3.connect("login.db")

# Datensatz-Cursor erzeugen
cursor = connection.cursor()


class Serve(BaseHTTPRequestHandler):
    def log_server(self, log):
        datei = open('server.log', 'a')
        datei.write('\n' + " " + log)
        log = date
        datei.close()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if self.path == '/':
            self.path = '../../../frontend/sites/index.html'
        elif self.path == '/matrix':
            self.path = '../../../frontend/sites/matrix.html'
        elif parsed.path == '/search':
            self.path = '../../../frontend/results.html'
            .send_reponse(200)
            self.send_header('Content-Type: application/json')
            self.end_headers()
            self.wfile.write(self.search(parsed.query))
        elif self.path == '/login':
            self.login()
        else:
            self.path = '../../../frontend/troll.html'
            return

        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            log = date + " 200"
            # datei.write('\n' + " " + date)
        except:
            file_to_open = "File not found"
            self.send_response(400)
            log = date + " " + file_to_open
        finally:
            self.log_server(log)

        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def json_from(self, ls: list):
        json = "["
        for item in ls:
            json += "\n\t{"
            json += "\n\t\tItemId: "
            json += str(item[0])

            json += ",\n\t\tItemName: "
            json += str(item[1])
            json += ",\n\t\tItemBeschreibung: "
            json += str(item[2]) + "\n\t"
            json += "},\n"
        json += "]"
        print(json)
        return json

    def search(self, q):
        verbindung = sqlite3.connect("login.db")
        zeiger = verbindung.cursor()
        obj = urllib.parse.parse_qs(q)

        try:
            query = f"select * from Item where {obj['search-type'][0]} is '{obj['query'][0]}';"
            print(query)
            zeiger.execute(query)
            inhalt = zeiger.fetchall()
            print(inhalt)
            verbindung.close()
            return self.json_from(inhalt)

        except KeyError as e:
            print("error: " + str(type(e)))

    def login():
        print("moin")


try:
    httpd = HTTPServer(('0.0.0.0', PORT), Serve)
    log = log + "server is now running on 127.0.0.1:" + str(PORT)
    # log_server(log)
    print("server is now running on http://127.0.0.1:" + str(PORT))

    httpd.serve_forever()
except KeyboardInterrupt:
    pass
    # Server beenden, und Datein speichern/in Sammlung schieben
    httpd.server_close()
    print("\nServer stopped.")
    print("saving files")
