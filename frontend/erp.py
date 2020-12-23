from flask import Flask,render_template,request,jsonify,flash,redirect, abort, send_from_directory, url_for
from flask_cors import CORS
import requests
import json
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

app = Flask(__name__)
CORS(app)

def obtenerDatos():
    salida = "salidass"
    solicitud = requests.get('http://backenderp:5000/api', verify=False)
    datos = solicitud.json()
    print("datos")
    return datos 

@app.route('/info')
def info():
    datios = obtenerDatos()
    print("estoy en info")
    return datios
    #return '<h1>datio del backend '+datios+'</h1>'#datios


@app.route('/')
def hello():
    return '<h1>Soy el servidor de erp</h1>'

if __name__ == '__main__':
    #app.run()
    app.run(debug=True,host='0.0.0.0',port=5000)
