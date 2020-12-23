from flask import Flask,render_template,request,jsonify,flash,redirect, abort, send_from_directory, url_for
from flask_cors import CORS
import names

app = Flask(__name__)
CORS(app)

def obtenerNombre():
    nombre =names.get_first_name(gender='male') + " " + names.get_last_name()
    return nombre

@app.route('/api',methods=['GET'])
def elget():
    datos = {}
    contador = 1
    while (contador < 10):
        datos[contador] = {'id':contador, 'nombre':obtenerNombre()}
        contador +=1
    return jsonify(datos)
    #return jsonify(prueba)

@app.route('/cosas',methods=['GET'])
def cosas():
    return "cosas"

@app.route('/')
def hello():
    return '<h1>Api back</h1>'

if __name__ == '__main__':
    #app.run()
    app.run(debug=True,host='0.0.0.0',port=5000)
