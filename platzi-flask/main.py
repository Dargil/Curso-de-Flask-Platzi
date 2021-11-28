from flask import Flask,request

# el nombre de la aplicacion es el nombre del archivo que se llama main.py
app = Flask(__name__)

@app.route('/')
def hello():
    user_ip = request.remote_addr
    return "Hello world platzi, tu IP es {}".format(user_ip)
