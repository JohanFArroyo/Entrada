import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    bcrypt = Bcrypt(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from .models.celador import Celador
        return Celador.query.get(int(user_id))

    from app.routes import aprendiz_routes, portatil_routes, celador_routes, entrada_routes, login_routes
    app.register_blueprint(aprendiz_routes.bp)
    app.register_blueprint(portatil_routes.bp)
    app.register_blueprint(celador_routes.bp)
    app.register_blueprint(entrada_routes.bp)
    app.register_blueprint(login_routes.login_bp)

    return app