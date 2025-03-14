from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(15), nullable=True)
    direccion = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Cliente {self.nombre}>'
