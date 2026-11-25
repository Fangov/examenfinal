from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre=request.form["nombre"]
        edad=int(request.form["edad"])
        cantidad=int(request.form["cantidad"])

        precio_tarro=9000
        total_sin_descuento = cantidad * precio_tarro
        if edad < 18:
            porcentaje = 0
        elif edad <=30:
            porcentaje = 15
        else:
            porcentaje = 25

        descuento = total_sin_descuento * porcentaje //100
        total_a_pagar= total_sin_descuento - descuento


        return render_template(
            "ejercicio1.html",
            nombre=nombre,
            porcentaje=porcentaje,
            descuento=descuento,
            total_sin_descuento=total_sin_descuento,
            total_a_pagar=total_a_pagar
        )

    return render_template("ejercicio1.html")

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        usuario=request.form["usuario"]
        clave=request.form["clave"]

        if usuario=="fabian" and clave=="admin":
            mensaje="Bienvenido Señor Administrador"
        elif usuario=="pepe" and clave=="user":
            mensaje="Bienvenido usuario Pepe"
        else:
            mensaje="Usuario o contraseña incorrecto"

        return render_template("resultado_acceso.html",mensaje=mensaje)
    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run()