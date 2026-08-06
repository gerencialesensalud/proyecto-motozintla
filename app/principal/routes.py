from flask import render_template, Blueprint

# Creamos el Blueprint
principal_bp = Blueprint('principal', __name__)

# Usamos 'principal_bp' en lugar de 'app'
@principal_bp.route('/')
def inicio():
    datos_ciudad = {
        "nombre": "Motozintla de Mendoza",
        "eslogan": "La Hermosa Ventana de la Sierra Madre",
        "clima": "Templado / Húmedo",
        "altura": "1,300 msnm"
    }
    return render_template('inicio.html', ciudad=datos_ciudad)

