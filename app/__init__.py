from flask import Flask
from app.logger import setup_logger
from app.views import main
from pathlib import Path
from app.db import db


from config import config


logger = setup_logger(__name__)
template_path = Path(__file__).parent / "templates"


def create_app(config_name):
    app = Flask(__name__, template_folder=template_path)
    app.config.from_object(config[config_name])
    db.init_app(app)
    logger.info("App created using '%s' config %s", config_name, template_path)

    app.register_blueprint(main)
    return app
