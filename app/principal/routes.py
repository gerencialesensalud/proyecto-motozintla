from flask import render_template, Blueprint
# Importamos la función desde la subcarpeta exacta que definiste
# Tu Blueprint actual

bp = Blueprint('principal', __name__, 
              template_folder='../templates',
              static_folder='../static',
              static_url_path='/static')


@bp.route('/')
def inicio():
    datos_ciudad = {
        "nombre": "Motozintla de Mendoza",
        "eslogan": "La Hermosa Ventana de la Sierra Madre",
        "clima": "Templado / Húmedo",
        "altura": "1,300 msnm"
    }
    return render_template('inicio.html', ciudad=datos_ciudad)



