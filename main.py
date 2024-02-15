import math
from flask import Flask, render_template, request
from io import open
import Puntos
import Resistencia
import Diccionario

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("OperacBas.html")


@app.route("/diccionario", methods=["GET", "POST"])
def diccionario():
    cldiccionario = Diccionario.diccionario(request.form)
    archivo = open("diccionario.txt", "+a")
    res = ""

    if request.method=="POST":
        guardar = "\n {} | {}".format(cldiccionario.ingles.data, cldiccionario.espanol.data)
        print(guardar)
        archivo.write(guardar)
        archivo.close()
#        return render_template("diccionario.html", diccionario=cldiccionario)

    if request.method=="GET":
        leer = cldiccionario.lectura.data
        buscar = cldiccionario.busqueda.data
        palabras = archivo.readlines()
        print(leer)
        print(buscar)
        archivo.close()

    return render_template("diccionario.html", diccionario=cldiccionario, resultado=res)

@app.route("/resistencia", methods=["GET", "POST"])
def resistencia():
    resistencia = Resistencia.Resistencia(request.form)

    if request.method=="POST":
        color = dict(resistencia.banda1.choices).get(resistencia.banda1.data)
        colord = dict(resistencia.banda2.choices).get(resistencia.banda2.data)
        colort = dict(resistencia.banda3.choices).get(resistencia.banda3.data)
        tolerancia = resistencia.tolerancia.data
        valor = int(resistencia.banda1.data + resistencia.banda2.data) * int(resistencia.banda3.data)
        
        if tolerancia == "oro": 
            maximo = valor + (valor * 0.05)
            minimo = valor - (valor * 0.05)
            text = "5%"
        else :
            maximo = valor + (valor * 0.1)
            minimo = valor - (valor * 0.1)
            text = "10%"

    return render_template("resistencia.html", 
                                    resistencia=resistencia, 
                                    color=cambiarColor(color),
                                    colord=cambiarColor(colord),
                                    colort=cambiarColor(colort),
                                    tolerancia=cambiarColor(tolerancia),
                                    valor=valor, 
                                    maximo=maximo,
                                    minimo=minimo,
                                    text=text,

                                    vcolor=color,
                                    vcolord=colord,
                                    vcolort=colort,
                                    vresistencia=resistencia, 
                                    vtolerancia=tolerancia)

def cambiarColor(color):
    if color == "negro":
        return "black"
    if color == "cafe":
        return "brown"
    if color == "rojo":
        return "red"
    if color == "naranja":
        return "orange"
    if color == "amarillo":
        return "yellow"
    if color == "verde":
        return "green"
    
    if color == "azul":
        return "blue"
    if color == "violeta":
        return "violet"
    if color == "gris":
        return "gray"
    if color == "blanco":
        return "white"
    
    if color == "oro":
        return "gold"
    if color == "plata":
        return "silver"
    
    if color== "":
        return "black"

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    posA=Puntos.Punto(request.form)
    resultado=0
    
    if request.method=="POST":
        posAa=posA.posAa.data
        posAb=posA.posAb.data
        posBa=posA.posBa.data
        posBb=posA.posBb.data
        
        numero=((int(posBa)-int(posAa))**2)+((int(posBb)-int(posAb))**2)
        resultado= math.sqrt(float(numero))
        print("resultado {} --------- {}".format(resultado, numero))
    
    return render_template("Distancia.html", posa=posA, resultado=resultado)


@app.route("/operacion", methods=["GET", "POST"])
def operaciones():
    if request.method=="POST":
        operacion = request.form.get("operacion")
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        res = ""

        if operacion == "suma": 
            res="La suma {} + {} = {}".format(num1, num2, float(num1)+float(num2))
        if operacion == "rest": 
            res="La resta {} - {} = {}".format(num1, num2, float(num1)-float(num2))
        if operacion == "mult": 
            res="La multiplicación {} * {} = {}".format(num1, num2, float(num1)*float(num2))
        if operacion == "divi": 
            res="La división {} / {} = {}".format(num1, num2, float(num1)/float(num2))

        return render_template("Resultado.html",mensaje = res)

if __name__=="__main__":
    app.run(debug=True)