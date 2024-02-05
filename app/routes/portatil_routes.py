from flask import Blueprint, render_template, request, redirect, url_for
from app.models.portatil import Portatil
from app import db

bp = Blueprint('portatil', __name__)

@bp.route('/Portatil')
def index():
    data = Portatil.query.all()
    return render_template('portatil/index.html', data=data)

@bp.route('/Portatil/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        color = request.form['color']
        
        new_portatil = Portatil(nombre=nombre, color=color)
        db.session.add(new_portatil)
        db.session.commit()
        
        return redirect(url_for('portatil.index'))

    return render_template('portatil/add.html')

@bp.route('/Portatil/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    portatil = Portatil.query.get_or_404(id)

    if request.method == 'POST':
        portatil.nombre = request.form['nombre']
        portatil.color = request.form['color']
        db.session.commit()
        return redirect(url_for('portatil.index'))

    return render_template('portatil/edit.html', portatil=portatil)

@bp.route('/Portatil/delete/<int:id>')
def delete(id):
    portatil = Portatil.query.get_or_404(id)
    
    db.session.delete(portatil)
    db.session.commit()

    return redirect(url_for('portatil.index'))