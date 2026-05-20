from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Olá'

@app.route('/Inicio')
def FunçãoInicio():
    return render_template('index.html')

@app.route('/Cardapio')
def FunçãoCardapio():
    return render_template('cardapio.html')

@app.route('/Cliente')
def FunçãoCliente():
    return render_template('cliente.html')

@app.route('/Contato')
def FunçãoContato():
    return render_template('contato.html')

@app.route('/Lanche')
def FunçãoLanche():
    return render_template('lanche.html')

@app.route('/Pedidos')
def FunçãoPedidos():
    return render_template('Pedidos.html')

@app.route("/cliente/<nome>/<cidade>")
def cliente(nome, cidade):

    if cidade.lower() == "natal":
        mensagem = "Entrega disponível!"
    else:
        mensagem = "Entrega indisponível."

    return render_template(
        "cliente.html",
        nome=nome,
        cidade=cidade,
        mensagem=mensagem
    )

app.run(debug=True)