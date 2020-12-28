from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrarProveedor(FlaskForm):
    nombre = StringField('Nombre',
                        validators=[DataRequired(), Length(min=3,max=30)])
    #De momento por acuerdo entre grupos las fechas son String
    #fecha = StringField('Fecha de muerte', validators=[DataRequired(),Length(min=0, max=10)])
    empresa = StringField('Empresa',
                        validators=[DataRequired(), Length(min=1,max=30)])
              
    #fecha = DateField('Start Date', format='%m/%d/%Y', validators=(validators.Optional(),))
    descripcion = StringField('descripcion', validators=[Length(min=0, max=140)])
    submit = SubmitField('Enviar')

class RegistrarDocumento(FlaskForm):
    tipo = StringField('tipo documento',
                        validators=[DataRequired(), Length(min=3,max=30)])

    titulo = StringField('titulo',
                        validators=[DataRequired(), Length(min=3,max=30)])
    
    contenido = StringField('contenido', validators=[Length(min=0, max=140)])

    encargado = StringField('descripcion', validators=[Length(min=3, max=40)])
    submit = SubmitField('Enviar')

class RegistrarEmpleado(FlaskForm):
    nombre = StringField('nombre',
                        validators=[DataRequired(), Length(min=3,max=30)])

    puesto = StringField('puesto',
                        validators=[DataRequired(), Length(min=3,max=30)])
    
    salario = StringField('salario', validators=[Length(min=0, max=8)])

    direccion = StringField('direccion', validators=[Length(min=3, max=40)])

    telefono = StringField('telefono', validators=[Length(min=8, max=8)])

    submit = SubmitField('Enviar')

class RegistrarVenta(FlaskForm):
    empresa = StringField('empresa',
                        validators=[DataRequired(), Length(min=3,max=30)])
    cliente = StringField('cliente',
                        validators=[DataRequired(), Length(min=3,max=30)])
    venta = StringField('monto de venta',
                        validators=[DataRequired(), Length(min=1,max=10)])
    descripcion = StringField('descripcion',
                        validators=[DataRequired(), Length(min=3,max=200)])
    vendedor = StringField('vendedor',
                        validators=[DataRequired(), Length(min=3,max=30)])
    submit = SubmitField('Enviar')

class RegistrarCompra(FlaskForm):
    empresa = StringField('empresa',
                        validators=[DataRequired(), Length(min=3,max=30)])
    compra = StringField('monto de compra',
                        validators=[DataRequired(), Length(min=3,max=30)])
    descripcion = StringField('descripcion',
                        validators=[DataRequired(), Length(min=1,max=200)])
    submit = SubmitField('Enviar')

class RegistrarCliente(FlaskForm):
    nombre = StringField('nombre',
                        validators=[DataRequired(), Length(min=3,max=30)])
    empresa = StringField('empresa',
                        validators=[DataRequired(), Length(min=3,max=30)])
    nit = StringField('nit',
                        validators=[DataRequired(), Length(min=4,max=15)])
    direccion = StringField('direccion',
                        validators=[DataRequired(), Length(min=3,max=50)])
    telefono = StringField('telefono',
                        validators=[DataRequired(), Length(min=8,max=8)])
    submit = SubmitField('Enviar')

class RegistrationForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')


class LoginForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')