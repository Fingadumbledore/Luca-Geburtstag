from flask import Flask, render_template, jsonify, request, session, url_for
import sqlite3
import time
#from flask_login import login_required, current_user

app = Flask(__name__, template_folder='templates/')
con = sqlite3.connect("login.db")
cur = con.cursor()
date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
log = date


def log_server(self, log):
    datei = open('server.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()


"""
@app.route("/")
def index():
    return render_template("index.html")"""


def json_from(ls: list):
    # json = "["
    # for item in ls:
    #     json += "\n\t{"
    #     json += "\n\t\tItemId: "
    #     json += str(item[0])
    #     json += ",\n\t\tItemName: "
    #     json += str(item[1])
    #     json += ",\n\t\tItemBeschreibung: "
    #     json += str(item[2]) + "\n\t"
    #     json += "},\n"
    # json += "]"
    # print(json)
    # return json
    lis = []
    for item in ls:
        x = jsonify(
            Itemid=str(item[0]),
            ItemName=str(item[1]),
            ItemBeschreibung=str(item[2])
        ).response[0]
        lis.append(x)

    return lis


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=['GET'])
def search():
    return render_template("results.html")


@app.route("/search", methods=['POST'])
def post_search():
    con = sqlite3.connect("login.db")
    cur = con.cursor()

    n1 = request.args['search-type']
    n2 = request.args['query']

    q = f"select * from Item where {n1} is \'{n2}\'"
    cur.execute(q)
    content = cur.fetchall()
    js = json_from(content)
    for i in range(len(js)):
        js[i] = js[i].decode("utf-8")
        print(js[i])
    return jsonify(str(js))


@app.route("/login", methods=['POST'])
def login():
    print("login")
    
    con = sqlite3.connect("login.db")
    cur = con.cursor()
    username = request.form['uname']
    password = request.form['psw']

        # das nicht benutzen, weil es sql-injections nicht erlaubt
    cur.execute('select * from user where username = %s and password = %s',(username, password))

                    
    account = cur.fetchone()

    if account:
        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']
        return render_template("login.html")
    else:
        return "{ \"message\": \"Login failed\"'}"

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route("/matrix")
#@login_required
def matrix():
    return render_template('matrix.html')


@app.route("/raetsel")
def raetsel():
    return render_template('raetsel.html')


@app.route("/rot")
def rot():
    return render_template('rot.html')

@app.route("/werbung")
def werbung():
    return render_template('werbung.html')


@app.route("/hilfe")
def hilfe():
    return render_template('selbsthilfe.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('troll.html'), 404


def create_app(config_filename):
    app.register_error_handler(404, page_not_found)
    return app
