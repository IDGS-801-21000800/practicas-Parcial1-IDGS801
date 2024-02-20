from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, RadioField

from wtforms import validators 

class buscar(Form):
    lectura = RadioField("lectura", choices=["ingles", "espannol"], validators=[
        validators.DataRequired(message='El campo es requerido')
    ])
    busqueda = StringField("busqueda", validators=[
        validators.DataRequired(message='El campo es requerido')
    ])