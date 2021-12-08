from flask import Flask,request, make_response,redirect, render_template

# el nombre de la aplicacion es el nombre del archivo que se llama main.py
app = Flask(__name__)
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    #return "Hello world platzi, tu IP es {}".format(user_ip)
    return render_template('hello.html',user_ip=user_ip)