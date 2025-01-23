from flask import Blueprint

# Define a blueprint for the main routes
main = Blueprint("main", __name__)


@main.route("/")
def index():
    return "I am a Flask app", 200
