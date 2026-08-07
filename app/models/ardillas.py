from app import db
from datetime import datetime

class Corredor(db.Model):
    __tablename__ = 'corredores_ardillas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    rama = db.Column(db.String(20), nullable=False)
    categoria = db.Column(db.String(20), nullable=False)
    
    # Almacenamiento binario para la imagen en PostgreSQL (BYTEA)
    comprobante_binario = db.Column(db.LargeBinary, nullable=False)
    comprobante_nombre = db.Column(db.String(100), nullable=False)
    comprobante_mimetype = db.Column(db.String(20), nullable=False)
    
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Corredor {self.nombre} - {self.categoria}>'

