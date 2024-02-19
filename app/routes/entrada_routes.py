from datetime import datetime       
from sqlalchemy import func
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.entrada import Entrada
from app.models.aprendiz import Aprendiz
from app.models.portatil import Portatil
from app import db

bp = Blueprint('entrada', __name__)

@bp.route('/Entrada')
def index():
    data = Entrada.query.all()
    return render_template('entrada/index.html', data=data)

@bp.route('/Entrada/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        aprendiz = request.form['cedulaAprendiz']
        portatil = request.form['idPortatil']
        
        consulta = Aprendiz.query.filter_by(cedula=aprendiz).first()
        consulta1 = Portatil.query.filter_by(id=portatil).first()
        if not consulta:
            flash('Aprendiz no encontrado')
        elif not consulta1: 
            flash('Portatil no encontrado')
        elif consulta and consulta1:
            new_entrada = Entrada(fechaE=func.now(), aprendiz=consulta.id, portatil=portatil)
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
        entrada.fechaS = func.now()
        db.session.commit()
        return redirect(url_for('entrada.index'))

    return redirect(url_for('entrada.index'))


@bp.route('/Entrada/buscar', methods=['GET'])
def buscar():
    nombre = request.args.get('nombre')
    print("Nombre a buscar ",nombre)
    data = Entrada.query.join(Aprendiz).filter(Aprendiz.nombre.like(f"%{nombre}%")).all()
    return render_template('entrada/index.html',data=data)