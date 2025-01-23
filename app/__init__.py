from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .logger import setup_logger
from app.main.views import main


from config import config

db = SQLAlchemy()
logger = setup_logger(__name__)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    logger.info("App created using '%s' config", config_name)

    app.register_blueprint(main)
    return app
