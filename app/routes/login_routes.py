from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from app.models.celador import Celador

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contra = request.form['contra']
        
        user = Celador.query.filter_by(correo=correo).first()
        bcrypt = Bcrypt()
        
        if user and bcrypt.check_password_hash(user.contra,contra):
            login_user(user)
            return redirect(url_for('login.dashboard'))
        flash('Invalid credentials. Please try again.', 'danger')
    
    if current_user.is_authenticated:
        return redirect(url_for('login.dashboard'))
    return render_template("login/login.html")

@login_bp.route('/dashboard')
@login_required
def dashboard():
    return redirect(url_for('entrada.index'))

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login.login'))