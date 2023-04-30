from flask import Flask
from config import Config


def create_app():
    # Create the Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import and register the blueprints
    from app.home.routes import home
    app.register_blueprint(home)

    return app
