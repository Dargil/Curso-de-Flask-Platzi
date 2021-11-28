from flask import Flask

# el nombre de la aplicacion es el nombre del archivo que se llama main.py
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world flask"
