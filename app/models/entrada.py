from app import db
from datetime import datetime

class Entrada(db.Model):
    __tablename__= "entrada"
    id = db.Column(db.Integer, primary_key=True)
    fechaE = db.Column(db.TIMESTAMP, nullable=True)
    fechaS = db.Column(db.TIMESTAMP, nullable=True)
    aprendiz = db.Column(db.Integer, db.ForeignKey('aprendiz.id'))
    modelo_principal = db.relationship('Aprendiz', backref='tus_modelos')
    portatil = db.Column(db.Integer, db.ForeignKey('portatil.id'))
    modelo_principal = db.relationship('Portatil', backref='tus_modelos')