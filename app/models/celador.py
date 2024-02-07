from app import db
from flask_login import UserMixin

class Celador(db.Model, UserMixin):
    __tablename__= "celador"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    contra = db.Column(db.String(255), nullable=False)
