from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField

class Resistencia(Form): 
    banda1 = SelectField("banda1", choices=[
        ("0", "negro"),
        ("1", "cafe"),
        ("2", "rojo"),
        ("3", "naranja"),
        ("4", "amarillo"),
        ("5", "verde"),
        ("6", "azul"),
        ("7", "violeta"),
        ("8", "gris"),
        ("9", "blanco")])
    banda2 = SelectField("banda2", choices=[
        ("0", "negro"),
        ("1", "cafe"),
        ("2", "rojo"),
        ("3", "naranja"),
        ("4", "amarillo"),
        ("5", "verde"),
        ("6", "azul"),
        ("7", "violeta"),
        ("8", "gris"),
        ("9", "blanco")])
    banda3 = SelectField("banda3", choices=[
        ("1", "negro"),
        ("10", "cafe"),
        ("100", "rojo"),
        ("1000", "naranja"),
        ("10000", "amarillo"),
        ("100000", "verde"),
        ("1000000", "azul"),
        ("10000000", "violetaa"),
        ("100000000", "gris"),
        ("1000000000", "blanco")])
    
    tolerancia = RadioField("tolerancia", choices=["oro", "plata"])