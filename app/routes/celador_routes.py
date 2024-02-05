from flask import Blueprint, render_template, request, redirect, url_for
from app.models.celador import Celador
from app import db
from flask_bcrypt import Bcrypt

bp = Blueprint('celador', __name__)

@bp.route('/Celador')
def index():
    data = Celador.query.all()
    return render_template('celador/index.html', data=data)

@bp.route('/Celador/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        correo =  request.form['correo']
        contra =  request.form['contra']
        bcrypt = Bcrypt()
        
        password =bcrypt.generate_password_hash(contra).decode('utf-8')
        
        new_celador = Celador(nombre=nombre, cedula=cedula, correo=correo, contra=password)
        db.session.add(new_celador)
        db.session.commit()
        
        return redirect(url_for('celador.index'))

    return render_template('celador/add.html')

@bp.route('/Celador/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    celador = Celador.query.get_or_404(id)

    if request.method == 'POST':
        celador.nombre = request.form['nombre']
        celador.cedula = request.form['cedula']
        celador.correo = request.form['correo']
        db.session.commit()
        return redirect(url_for('celador.index'))

    return render_template('celador/edit.html', celador=celador)

@bp.route('/Celador/delete/<int:id>')
def delete(id):
    celador = Celador.query.get_or_404(id)
    
    db.session.delete(celador)
    db.session.commit()

    return redirect(url_for('celador.index'))