from flask import Blueprint

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return "¡Bienvenido a la lista de tareas!"