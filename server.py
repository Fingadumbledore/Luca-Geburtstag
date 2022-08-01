from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>index called</h1>\n<h2>hier muss ne datei hin, kein plaintext</h2>"
