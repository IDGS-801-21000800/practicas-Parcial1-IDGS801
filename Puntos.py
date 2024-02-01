from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField
#from wtforms import StringField, TelField, IntegerField
class Punto(Form):
    posAa=IntegerField("puntoax")
    posAb=IntegerField("puntoay")
    posBa=IntegerField("puntobx")
    posBb=IntegerField("puntoby")