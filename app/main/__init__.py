from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
Migrate= Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    Migrate.init_app(app, db)
    flask_bcrypt.init_app(app)
    

    return app

