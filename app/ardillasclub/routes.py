import io
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
#from app import db
#from app.models.ardillas import Corredor
from app.ardillasclub.carrera1.logica import simular_carrera1

bp = Blueprint('ardillas', __name__,
              template_folder='../templates',
              static_folder='../static',
              static_url_path='/static')

# Extensiones permitidas para los pagos
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 1. PORTAL PRINCIPAL DEL CLUB ARDILLAS
@bp.route('/')
def index():
    return render_template('ardillasclub/index.html')

# 2. VISTA DE LA INFORMACIÓN DE LA CARRERA 10K Y CUENTA REGRESIVA
@bp.route('/carrera-info')
def carrera_info():
    return render_template('ardillasclub/ardillas_carrera.html')

# 3. TU VISTA ORIGINAL: SIMULACIÓN Y PODIO DE LA CARRERA
@bp.route('/carrera1')
def carrera_uno():
    datos_podio = simular_carrera1()
    return render_template('ardillasclub/podio.html', podio=datos_podio)

# 4. FORMULARIO DE REGISTRO PARA LOS CORREDORES (GUARDA EN POSTGRESQL)
@bp.route('/registro', methods=['GET', 'POST'])
def registro_corredor():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        telefono = request.form.get('telefono', '').strip()
        edad = request.form.get('edad')
        rama = request.form.get('rama')
        categoria = request.form.get('categoria')
        file = request.files.get('comprobante')
        
        # Validación estricta en el servidor
        if not (nombre and telefono and edad and rama and categoria and file):
            flash('Todos los campos son estrictamente obligatorios.', 'error')
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            try:
                # Lee los bytes del archivo para la columna LargeBinary (BYTEA)
                datos_binarios = file.read()
                
                nuevo_corredor = Corredor(
                    nombre=nombre,
                    telefono=telefono,
                    edad=int(edad),
                    rama=rama,
                    categoria=categoria,
                    comprobante_binario=datos_binarios,
                    comprobante_nombre=file.filename,
                    comprobante_mimetype=file.content_type
                )
                
                db.session.add(nuevo_corredor)
                db.session.commit()
                
                flash('¡Inscripción y comprobante guardados con éxito en la base de datos!', 'success')
                return redirect(url_for('ardillas.index'))
                
            except Exception as e:
                db.session.rollback()
                flash('Error crítico al escribir en la base de datos PostgreSQL.', 'error')
                return redirect(request.url)
        else:
            flash('Formato de imagen no permitido (solo JPG, JPEG o PNG).', 'error')
            return redirect(request.url)

    return render_template('ardillasclub/registro.html')

# 5. RUTA PARA EXTRAER Y VER EL COMPROBANTE DESDE POSTGRESQL
@bp.route('/comprobante/<int:corredor_id>')
def ver_comprobante(corredor_id):
    corredor = Corredor.query.get_or_404(corredor_id)
    return send_file(
        io.BytesIO(corredor.comprobante_binario),
        mimetype=corredor.comprobante_mimetype,
        as_attachment=False,
        download_name=corredor.comprobante_nombre
    )

