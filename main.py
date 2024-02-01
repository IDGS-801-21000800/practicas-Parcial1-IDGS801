import math
from flask import Flask, render_template, request
import Puntos

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("OperacBas.html")

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