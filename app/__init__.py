import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')

    # Carpeta instance siempre accesible desde Flask
    db_path = os.path.join(app.instance_path, "creditos.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Creación de la carpeta instance si no existe
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    db.init_app(app)

    with app.app_context():
        from . import models
        from . import routes  # Esto registra las rutas con @app.route :)
        db.create_all()

    return app
