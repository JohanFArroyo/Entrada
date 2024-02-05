from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import portatil_routes, aprendiz_routes, celador_routes, entrada_routes