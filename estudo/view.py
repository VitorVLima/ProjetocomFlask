from estudo import app
from flask import render_template, url_for

@app.route("/")
def homepage():
    usuario = "vitor vinicius"
    idade = 26
    cpf = "076466043-80"
    context = {
        'usuario': usuario,
        'idade': idade,
        'cpf': cpf
    }
    return render_template("index.html", context = context)

@app.route("/nova/")
def novapage():
    return "nova pagina"