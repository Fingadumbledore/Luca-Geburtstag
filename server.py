from flask import Flask, render_template, jsonify, request, session, redirect
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
    log = date + log
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

    log_server(str(lis))
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
        log_server(f"recieved {js[i]} from query")
    print(dict(js))
    return jsonify(dict(js))

@app.route("/login", methods=['POST'])
def login():
    log_server("called /login with POST")
    

    con = sqlite3.connect("login.db")
    cur = con.cursor()
    username = request.form['uname']
    password = request.form['psw']
    l = f"select * from user where username = \'{username}\' and password =\'{password}\';"

    cur.execute(l)
    account = cur.fetchone()

    if account:
        session['loggedin'] = True
       # session['username'] = account['username']
        return redirect('/matrix')
    else:
        return "{ \"message\": \"Login failed\"'}"


@app.route('/logout')
def logout():
    
    if session:
        log_server("called /logout")
        return render_template('logout.html')
        session['loggedin'] = False
    else: 
         return render_template('troll.html')
         log_server("called /logout without being logged in")


@app.route("/matrix")
# @login_required
def matrix():
    
    if session:
        log_server("called /matrix")
        return render_template('matrix.html')
    else: 
         return render_template('troll.html')
         log_server("called /matrix without being logged in")


@app.route("/raetsel")
def raetsel():
    
    if session:
     log_server("called /raetsel")
     return render_template('raetsel.html')
    else: 
         return render_template('troll.html')
         log_server("called /raetsel without being logged in")


@app.route("/rot")
def rot():
    
    if session:
        log_server("called /rot")
        return render_template('rot.html')
    else: 
         return render_template('troll.html')
         log_server("called /rot without being logged in")


@app.route("/werbung")
def werbung():
    
    if session:
        log_server("called /werbung")
        return render_template('werbung.html')
    else: 
         return render_template('troll.html')
         log_server("called /werbung without being logged in")


@app.route("/hilfe")
def hilfe():
    
  
        log_server("called /hilfe")
        return render_template('selbsthilfe.html')
   

@app.route("/datenschutz")
def datenschutz():
    
    if session:
        log_server("called /datenschutz")
        return render_template('Datenschutz.html')
    else: 
         return render_template('troll.html')
         log_server("called /datenschutz without being logged in")

@app.route("/spiel")
def spiel():
    
    if session:
        log_server("called /spiel")
        return render_template('spiel.html')
    else: 
         return render_template('troll.html')
         log_server("called /spiel without being logged in")


@app.errorhandler(404)
def page_not_found(e):
    log_server("called non-existing page")
    # note that we set the 404 status explicitly
    return render_template('troll.html'), 404


def create_app(config_filename):
    app.register_error_handler(404, page_not_found)
    log_server("created app")
    return app
