from app import db


class Celador(db.Model):
    __tablename__= "celador"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    contra = db.Column(db.String(255), nullable=False)
