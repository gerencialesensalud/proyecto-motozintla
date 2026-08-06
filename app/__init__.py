from flask import Flask

app = Flask(__name__)

# Registramos el Blueprint de la subcarpeta
from app.principal.routes import principal_bp
app.register_blueprint(principal_bp)

