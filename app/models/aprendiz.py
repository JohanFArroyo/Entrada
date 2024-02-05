from app import db

class Aprendiz(db.Model):
    __tablename__ = "aprendiz"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    ficha = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.String(255), nullable=False)