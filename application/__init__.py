import flask
import flask_sqlalchemy
import flask_praetorian
import flask_cors
import flask_migrate
import pandas as pd
import numpy as np
from flasgger import Swagger
from sqlalchemy import MetaData
# from .models import User
# from flask_session import Session
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_redis import FlaskRedis

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

# Globally accessible libraries
db = flask_sqlalchemy.SQLAlchemy(metadata=metadata)
guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()
migrate = flask_migrate.Migrate()
swag = Swagger(
    template={
        "swagger": "2.0",
        "info": {
            "title": "Simulator APP",
            "version": "1.0",
        },
        "consumes": [
            "application/json",
        ],
        "produces": [
            "application/json",
        ],
    },
)
# sess = Session()
# db = SQLAlchemy()
# r = FlaskRedis()

def create_app():
    """Initialize the core application."""
    app = flask.Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app,db, render_as_batch=True)
    from .models import User
    guard.init_app(app, User)
    swag.init_app(app)
    # sess.init_app(app)
    # r.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes

        return app