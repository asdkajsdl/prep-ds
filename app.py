from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/prep")
def miauu():
    return "<p>hola mundo!</p>"



@app.route("/ds/<string:prep1>/<string:prep2>")
def wauuu(prep1,prep2):
    return f"{prep1} vs {prep2}"