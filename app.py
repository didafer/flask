from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', lista=range(15))

@app.route('/<nome>')
def ola_com_nome(nome):
    return render_template('index.html', nome_pessoa = nome)

#pip install flask
##pip install python-dotenv