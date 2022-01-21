from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
    return '<h1> Link 01 <h1>'

@app.route('/rota2')
def raiz2():
    return '<h1> Link 02 </h1>'

app.run()