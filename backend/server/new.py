from flask import Flask, render_template

app = Flask(__name__, template_folder='frontend/sites/')


@app.route("/")
def index():
    return app.send_static_file('../../../frontend/static/index.html')


@app.route("/matrix")
def matrix():
    return render_template("<h1>matrix</h1>")


@app.route("/search")
def search():
    return "<h1>test</h1>"


@app.route("/login")
def login_r():
    return login()


def login():
    return render_template("<h1>asd</h1>")