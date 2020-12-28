from datetime import datetime
from flask import Flask,request, render_template, url_for, flash, redirect
from flask_cors import CORS
from pymongo import MongoClient
from forms import RegistrarProveedor, RegistrarDocumento, RegistrarEmpleado, RegistrarVenta
from forms import RegistrarCompra, RegistrarCliente, RegistrationForm, LoginForm
import pymongo
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e9d830bde37db8ca424cb0b55af9dac2'
CORS(app)

clienteMongo = MongoClient('mongodb://104.197.235.139',port=27017)
db = clienteMongo['erp']
comprasss = db['compras']
ventasss = db['ventas']
clientess = db['clientes']
usuarios = db['usuarios']

usuario = ""
juegos=[
    {
        'author':'Jairo Hernandez',
        'title': 'Intelaf',
        'content':'proveedor de computadoras',

    },
    {
        'author':'Guillermo Gonzales',
        'title': 'Nissan',
        'content':'Proveedor de vehiculos de transporte',
    }
]

documentos=[
    {
        'tipo':'Recibo',
        'titulo': 'Recibo de compra #23',
        'contenido':'Recibo por compra de 5 computadoras dell por un valor de Q4500.00 c/u',
        'encargado':'Juan Ramirez',
    },
    {
        'tipo':'Factura',
        'titulo': 'Factura compra de mobiliario',
        'contenido':'Compra de 2 escritorios valuados en Q1200.00 c/u',
        'encargado':'Pedro Sanchez',
    }
]

empleads = [
    {
        'nombre':'Cristiano Ronaldo',
        'puesto': 'Vendedor',
        'salario':'5000.00',
        'direccion':'Racon City',
        'telefono':'45323421',
    },
    {
        'nombre':'Mario',
        'puesto': 'Fontanero',
        'salario':'3000.00',
        'direccion':'Mushroom kingdom',
        'telefono':'34657890',
    }

]

ventas = [
    {
        'empresa':'Aceros de Guatemala',
        'cliente': 'Manuel Godinez',
        'venta':'3000.00',
        'descripcion':'Venta de 2 escritorios',
        'vendedor':'Rafael Pineda',
    },
    {
        'empresa':'Aceros de Guatemala',
        'cliente': 'Manuel Godinez',
        'venta':'10000.00',
        'descripcion':'Venta de 5 sillas gamer',
        'vendedor':'Pedro Santos',
    }

]
def ingresarVenta(empresa,cliente,venta,descripcion,vendedor):
    ventasss.insert_one({
            'empresa':empresa,
            'cliente': cliente,
            'venta':venta,
            'descripcion':descripcion,
            'vendedor':vendedor,
        })

def obtenerVentas():
    cursor = ventasss.find({})
    vents = []
    for documento in cursor:
        vents.append(
            {
                'empresa':documento['empresa'],
                'cliente':documento['cliente'],
                'venta':documento['venta'],
                'descripcion':documento['descripcion'],
                'vendedor':documento['vendedor']
            }
        )
    return vents

compras = [
    {
        'empresa':'Repuestos Michellin',
        'compra':'2000.00',
        'descripcion':'Llantas de repuesto para microbus',
    },
    {
        'empresa':'Librerias Progreso',
        'compra':'1000.00',
        'descripcion':'Papeleria y utiles',
    }
]

def ingresarCompra(empresa,compra,descripcion):
    comprasss.insert_one({
            'empresa':empresa,
            'compra':compra,
            'descripcion':descripcion,
        })

def obtenerCompras():
    cursor = comprasss.find({})
    comprs = []
    for documento in cursor:
        comprs.append(
            {
                'empresa':documento['empresa'],
                'compra':documento['compra'],
                'descripcion':documento['descripcion']
            }
        )
    return comprs

clientes = [
    {
        'nombre':'Adolfo Hitler',
        'empresa': 'Nazi',
        'nit':'1234423431-1',
        'direccion':'Berlin, Alemania',
        'telefono':'34241564',
    },
    {
        'nombre':'Lenin',
        'empresa': 'Partido Rojo',
        'nit':'2413452345-1',
        'direccion':'Leningrado, Rusia',
        'telefono':'55647899',
    }
]

def ingresoCliente(nombre,empresa,nit,direccion,telefono):
    clientess.insert_one({
            'nombre':nombre,
            'empresa':empresa,
            'nit':nit,
            'direccion':direccion,
            'telefono':telefono,
        })

def obtenerClientes():
    cursor = clientess.find({})
    clients = []
    for documento in cursor:
        clients.append(
            {
                'nombre':documento['nombre'],
                'empresa':documento['empresa'],
                'nit':documento['nit'],
                'direccion':documento['direccion'],
                'telefono':documento['telefono']
            }
        )
    return clients

def registrarPro(nombre,empresa,descripcion):
    juegos.append({'author':nombre,'title':empresa,'content':descripcion})

def regristroDoc(tipo,titulo,contenido,encargado):
    documentos.append({
        'tipo':tipo,
        'titulo': titulo,
        'contenido':contenido,
        'encargado':encargado,
    })

def registroEmp(nombre,puesto,salario,direccion,telefono):
    empleads.append({
        'nombre':nombre,
        'puesto': puesto,
        'salario':salario,
        'direccion':direccion,
        'telefono':telefono,
    })

def ingresarUsuario(nombre,password):
    usuarios.insert_one({
        'nombre': nombre,
        'password': password,
    })

def verficarExistencia(nombre,password):
    dato=usuarios.find_one(
        {"nombre":nombre,"password":password},
        {"_id" : 0}
    )
    return dato

@app.route('/registro_documento',methods=['GET','POST'])
def registro_documento():
    form = RegistrarDocumento()
    if form.validate_on_submit():
        regristroDoc(form.tipo.data,form.titulo.data,form.contenido.data,form.encargado.data)
        flash(f'Documento registrado', 'success')
        return redirect(url_for('docs'))
    return render_template('registro_doc.html', title='nuevo Doc', form=form)

@app.route('/registro_proveedor',methods=['GET','POST'])
def registro_proveedor():
    form = RegistrarProveedor()
    if form.validate_on_submit():
        registrarPro(form.tipo.data,form.titulo.data,form.contenido.data,form.encargado.data)
        flash(f'Proveedor registrado', 'success')
        return redirect(url_for('home'))
    return render_template('registro_pro.html', title='Nuevo Prov', form=form)

@app.route('/registro_empleado',methods=['GET','POST'])
def registro_empleado():
    form = RegistrarEmpleado()
    if form.validate_on_submit():
        registroEmp(form.nombre.data,form.puesto.data,form.salario.data,form.direccion.data,form.telefono.data)
        flash(f'Empleado registrado', 'success')
        return redirect(url_for('empleados'))
    return render_template('registro_empleado.html', title='Nuevo empleado', form=form)

@app.route('/registro_venta',methods=['GET','POST'])
def registro_venta():
    form = RegistrarVenta()
    if form.validate_on_submit():
        ingresarVenta(form.empresa.data,form.cliente.data,form.venta.data,form.descripcion.data,form.vendedor.data)
        flash(f'Venta registrada', 'success')
        return redirect(url_for('ventass'))
    return render_template('registro_venta.html', title='Nueva venta', form=form)

@app.route('/registro_compra',methods=['GET','POST'])
def registro_compra():
    form = RegistrarCompra()
    if form.validate_on_submit():
        ingresarCompra(form.empresa.data,form.compra.data,form.descripcion.data)
        flash(f'Compra registrada', 'success')
        return redirect(url_for('comprass'))
    return render_template('registro_compra.html', title='Nueva compra', form=form)

@app.route('/registro_cliente',methods=['GET','POST'])
def registro_cliente():
    form = RegistrarCliente()
    if form.validate_on_submit():
        ingresoCliente(form.nombre.data,form.empresa.data,form.nit.data,form.direccion.data,form.telefono.data)
        flash(f'Compra registrada', 'success')
        return redirect(url_for('home'))
    return render_template('registro_cliente.html', title='Nuevo cliente', form=form)

@app.route('/empleados', methods=['GET','POST'])
def empleados():
    return render_template('empleados.html', empleados=empleads)

@app.route('/docs', methods=['GET','POST'])
def docs():
    return render_template('docs.html', documentos=documentos)

@app.route('/ventass', methods=['GET','POST'])
def ventass():
    sales = obtenerVentas()
    return render_template('ventas.html', ventas=sales)

@app.route('/comprass', methods=['GET','POST'])
def comprass():
    compas = obtenerCompras()
    return render_template('compras.html', compras=compas)

@app.route('/',methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    cliens = obtenerClientes()
    return render_template('home.html', clientes=cliens)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        ingresarUsuario(form.username.data,form.password.data)
        flash(f'Cuenta creada para {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    global usuario
    if form.validate_on_submit():

        if form.username.data != '' and form.password.data != '':
            usuario_l = verficarExistencia(form.username.data,form.password.data)
            if usuario_l == None:
                flash(f'Usuario o contraseña incorrectas', 'danger')
            else:
                flash('Estas logueado!', 'success')
                usuario = form.usuario.data
                print("usuario logueado: "+usuario)
                return redirect(url_for('home'))
        else:
            flash('Login sin exito. Revisa tu usuario y contraseña', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    #app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=5000)