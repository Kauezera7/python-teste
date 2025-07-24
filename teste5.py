from flask import Flask

# Cria a aplicação Flask
app = Flask(__name__)

# Rota principal "/"
@app.route('/')
def home():
    return "Hello, World!"

# Rota extra "/sobre"
@app.route('/sobre')
def sobre():
    return "Esta é uma aplicação de teste com Flask."

# Inicia o servidor local na porta 5000
if __name__ == '__main__':
    app.run(debug=True)
