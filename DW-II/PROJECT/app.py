from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/produtos')
def page_produto():
    itens = [
        {'id': 1, 'nome': 'Celular', 'cod_barra': '1234567890', 'preco': 1200},
        {'id': 2, 'nome': 'Notebook', 'cod_barra': '0987654321', 'preco': 3500},
        {'id': 3, 'nome': 'Teclado', 'cod_barra': '12345455565', 'preco': 120},
        {'id': 4, 'nome': 'Monitor', 'cod_barra': '657899989909', 'preco': 800},
    ]
    return render_template("produtos.html", itens=itens)


