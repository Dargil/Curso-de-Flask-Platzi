from flask import Flask,request, make_response,redirect, render_template
from flask_bootstrap import  Bootstrap
# el nombre de la aplicacion es el nombre del archivo que se llama main.py
app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar video a productor']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip,
        'todos' : todos,
    }
    #return "Hello world platzi, tu IP es {}".format(user_ip)
    return render_template('hello.html', **context)