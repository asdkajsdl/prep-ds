from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/prep")
def miauu():
    return "<p>hola mundo!</p>"



@app.route("/ds")
def wauuu():
    return "<p>argentina!</p>"