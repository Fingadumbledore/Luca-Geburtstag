from flask import Flask, render_template, request, send_file
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>index called</h1>\n<h2>hier muss ne datei hin, kein plaintext</h2>"


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/login")
def login():
    return render_template("login.html")
