from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_dict

db = SQLAlchemy()

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    # Inicializar la base de datos
    db.init_app(app)

    # Importar blueprints/routes
    from app.routes import data_routes

    # Registrar blueprints
    app.register_blueprint(data_routes)

    return app

