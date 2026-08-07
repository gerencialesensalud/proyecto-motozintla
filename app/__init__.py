from flask import Flask

# Dentro de app/principal/__init__.py
from app.principal import bp as principal_bp
from app.ardillasclub import bp as ardillas_bp

# Creamos la instancia global de la aplicación
def create_app():
	app = Flask(__name__, template_folder='template')

	# Registramos tus Blueprints organizados
	app.register_blueprint(principal_bp)
	app.register_blueprint(ardillas_bp, url_prefix='/club-ardillas')



	return app

