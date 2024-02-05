from app import db

class Portatil(db.Model):
    __tablename__= "portatil"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(255), nullable=False)