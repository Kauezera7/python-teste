from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "KSKSKSK TESTE !"


@app.route('/sobre')
def sobre():
    return "oi AMOR EU ESTOU AQUI"


if __name__ == '__main__':
    app.run(debug=True)
