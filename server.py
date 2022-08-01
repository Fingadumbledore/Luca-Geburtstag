from flask import Flask, render_template, jsonify, request
import sqlite3
import urllib
import urllib.parse

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

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
    for item in ls:
        x = jsonify(
            Itemid=str(item[0]),
            ItemName=str(item[1]),
            ItemBeschreibung=str(item[2])
        )
        print(x)


@app.route("/search")
def search():
#    verbindung = sqlite3.connect("login.db")
#    zeiger = verbindung.cursor()
#    obj = urllib.parse.parse_qs()
#
#    try:
#        query = f"select * from Item where {obj['search-type'][0]} is '{obj['query'][0]}';"
#        print(query)
#        zeiger.execute(query)
#        inhalt = zeiger.fetchall()
#        print(inhalt)
#        verbindung.close()
#        json_from(inhalt)
#
#    except KeyError as e:
#        print("error: " + str(type(e)))

    print(request.args)
    n1 = request.args['search-type']
    n2 = request.args['query']


    return render_template("results.html")
 

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/matrix")
def matrix():
    return render_template(matrix.html)
