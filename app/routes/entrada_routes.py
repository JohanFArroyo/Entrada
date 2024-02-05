from datetime import datetime       
from flask import Blueprint, render_template, request, redirect, url_for
from app.models.entrada import Entrada
from app import db

bp = Blueprint('entrada', __name__)

@bp.route('/')
def index():
    data = Entrada.query.all()
    return render_template('entrada/index.html', data=data)

@bp.route('/Entrada/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        aprendiz = request.form['idAprendiz']
        portatil = request.form['idPortatil']
        
        
        new_entrada = Entrada(fechaE=datetime.utcnow(), aprendiz=aprendiz, portatil=portatil)
        db.session.add(new_entrada)
        db.session.commit()
        
        return redirect(url_for('entrada.index'))

    return render_template('entrada/add.html')

@bp.route('/Entrada/delete/<int:id>')
def delete(id):
    entrada = Entrada.query.get_or_404(id)
    
    db.session.delete(entrada)
    db.session.commit()

    return redirect(url_for('entrada.index'))

@bp.route('/Entrada/exit/<int:id>', methods=['GET', 'POST'])
def exit(id):
    entrada = Entrada.query.get_or_404(id)


    if request.method == 'GET':
        entrada.fechaS = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('entrada.index'))

    return redirect(url_for('entrada.index'))
