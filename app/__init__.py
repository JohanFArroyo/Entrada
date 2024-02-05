from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    bcrypt = Bcrypt(app)
    db.init_app(app)

    from app.routes import aprendiz_routes, portatil_routes, celador_routes, entrada_routes
    app.register_blueprint(aprendiz_routes.bp)
    app.register_blueprint(portatil_routes.bp)
    app.register_blueprint(celador_routes.bp)
    app.register_blueprint(entrada_routes.bp)

    return app