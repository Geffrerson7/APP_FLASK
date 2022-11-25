from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .routes.libro import libros_ruta

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    app.register_blueprint(libros_ruta)
    return app
