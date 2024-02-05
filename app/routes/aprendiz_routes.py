from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.aprendiz import Aprendiz
from app import db

bp = Blueprint('aprendiz', __name__)

@bp.route('/Aprendiz')
def index():
    data = Aprendiz.query.all()
    return render_template('aprendiz/index.html', data=data)

@bp.route('/Aprendiz/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ficha = request.form['ficha']
        cedula = request.form['cedula']
        
        new_aprendiz = Aprendiz(nombre=nombre, ficha=ficha, cedula=cedula)
        db.session.add(new_aprendiz)
        db.session.commit()
        
        return redirect(url_for('aprendiz.index'))

    return render_template('aprendiz/add.html')

@bp.route('/Aprendiz/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    aprendiz = Aprendiz.query.get_or_404(id)

    if request.method == 'POST':
        aprendiz.nombre = request.form['nombre']
        aprendiz.ficha = request.form['ficha']
        aprendiz.cedula = request.form['cedula']
        db.session.commit()
        return redirect(url_for('aprendiz.index'))

    return render_template('aprendiz/edit.html', aprendiz=aprendiz)

@bp.route('/Aprendiz/delete/<int:id>')
def delete(id):
    aprendiz = Aprendiz.query.get_or_404(id)
    
    db.session.delete(aprendiz)
    db.session.commit()

    return redirect(url_for('aprendiz.index'))