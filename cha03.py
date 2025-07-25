from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/sobre')
def sobre():
    return "Esta é uma aplicação de teste com Flask."


if __name__ == '__main__':
    app.run(debug=True)
