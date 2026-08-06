from flask import Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return "¡Hola desde Motozintla, Chiapas!"

if __name__ == '__main__':
    app.run()

