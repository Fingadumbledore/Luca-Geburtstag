from flask import Flask, render_template, jsonify, request, session
import sqlite3
import time
# from flask_login import login_required, current_user

app = Flask(__name__, template_folder='templates/')
con = sqlite3.connect("login.db")
cur = con.cursor()
date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time()))
log = date
app.config['SECRET_KEY'] = 'sicher'


def log_server(log):
    datei = open('server.log', 'a')
    datei.write('\n' + " " + log)
    log = date
    datei.close()


def json_from(ls: list):
    lis = []
    for item in ls:
        x = jsonify(
            Itemid=str(item[0]),
            ItemName=str(item[1]),
            ItemBeschreibung=str(item[2])
        ).response[0]
        lis.append(x)

    log_server(lis)
    return lis


@app.route("/")
def index():
    log_server("called /")
    return render_template("index.html")


@app.route("/search", methods=['GET'])
def search():
    log_server("called /search with GET")
    return render_template("results.html")


@app.route("/search", methods=['POST'])
def post_search():
    log_server("called /search with POST")
    con = sqlite3.connect("login.db")
    cur = con.cursor()

    n1 = request.args['search-type']
    n2 = request.args['query']

    q = f"select * from Item where {n1} is \'{n2}\'"
    cur.execute(q)
    content = cur.fetchall()
    log_server(f"executed {q}")
    js = json_from(content)
    for i in range(len(js)):
        js[i] = js[i].decode("utf-8")
        print(js[i])
        log_server(f"recieved {js[i]} from query")
    return jsonify(js)


@app.route("/login", methods=['POST'])
def login():
    log_server("called /login with POST")
    print("login")

    con = sqlite3.connect("login.db")
    cur = con.cursor()
    username = request.form['uname']
    password = request.form['psw']
    l = f"select * from user where username = \'{username}\' and password =\'{password}\';"
    # das nicht benutzen, weil es sql-injections nicht erlaubt
    #cur.execute(f'select * from user where username = %s and password = %s',
     #           (username, password))
    cur.execute(l)
    account = cur.fetchone()

    if account:
        session['loggedin'] = True
       # session['username'] = account['username']
        return render_template("login.html")
    else:
        return "{ \"message\": \"Login failed\"'}"


@app.route('/logout')
def logout():
    log_server("called /logout")
    return render_template('logout.html')


@app.route("/matrix")
# @login_required
def matrix():
    log_server("called /matrix")
    return render_template('matrix.html')


@app.route("/raetsel")
def raetsel():
    log_server("called /raetsel")
    return render_template('raetsel.html')


@app.route("/rot")
def rot():
    log_server("called /rot")
    return render_template('rot.html')


@app.route("/werbung")
def werbung():
    log_server("called /werbung")
    return render_template('werbung.html')


@app.route("/hilfe")
def hilfe():
    log_server("called /hilfe")
    return render_template('selbsthilfe.html')


@app.route("/datenschutz")
def datenschutz():
    log_server("called /datenschutz")
    return render_template('Datenschutz.html')


@app.errorhandler(404)
def page_not_found(e):
    log_server("called non-existing page")
    # note that we set the 404 status explicitly
    return render_template('troll.html'), 404


def create_app(config_filename):
    app.register_error_handler(404, page_not_found)
    log_server("created app")
    return app
