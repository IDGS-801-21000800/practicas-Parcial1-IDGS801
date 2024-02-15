from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, RadioField

from wtforms import validators 

class diccionario(Form):
    espanol=StringField("espanol", validators=[
        validators.DataRequired(message='El campo es requerido')
    ])
    ingles=StringField("ingles", validators=[
        validators.DataRequired(message='El campo es requerido')
    ])

    lectura = RadioField("lectura", choices=["ingles", "espannol"])
    busqueda = StringField("busqueda", validators=[
        validators.DataRequired(message='El campo es requerido')
    ])