import os
from pathlib import Path

from dotenv import load_dotenv

base_dir = Path(__file__).resolve().parent
db_path_dev = base_dir / "app" / "data" / "library.sqlite"
db_path_test = base_dir / "app" / "data" / "test_library.sqlite"
db_path_prod = base_dir / "app" / "data" / "library.sqlite"

load_dotenv(base_dir / ".env")


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path_dev}"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path_test}"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path_prod}"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
