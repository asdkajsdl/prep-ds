from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"""
    <p>hola prep!</p>
    <a href='{url_for("wauuu", prep1="lele", prep2='lele')}'> ruta simple </a>
    <a href="{ url_for('otra') }">Ruta simple</a>
    <a href="{ url_for('miauu') }">Ruta simple</a>

    """


@app.route("/prep")
def miauu():
    return "<p>hola prep!</p>"



@app.route("/ds/<string:prep1>/<string:prep2>")
def wauuu(prep1,prep2):
    return f"{prep1} vs {prep2}"

@app.route('/prepp')
def index():
    return render_template('wauuu')

@app.route('/ds')
def otra():
    return render_template('lalalala')

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone()
   registros = res["cant"]
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"


