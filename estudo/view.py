from estudo import app,db
from flask import render_template, url_for, request,redirect
from estudo.models import Contato
from estudo.forms import ContatoForm

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

@app.route("/ContatoNovo/", methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}

    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))

    return render_template("contatonovo.html",context = context, form = form)



@app.route("/Contato/", methods=['GET', 'POST'])
def novapage():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET', pesquisa)
        context.update({'pesquisa':pesquisa})
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        assunto = request.form['assunto']
        
        contato = Contato(
            nome = nome,
            email = email,
            assunto = assunto,
            mensagem = mensagem
        )

        db.session.add(contato)
        db.session.commit()



    return render_template("contato.html",context = context)