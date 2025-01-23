from flask_migrate import Migrate

from app import create_app, db

app = create_app("development")
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
