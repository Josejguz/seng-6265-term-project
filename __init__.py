from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def create_app(config_name=None):
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY', '7nWCfr63Pntd1kgOCGDLQG5E0HcpVjvjrHxEjhwslrcey')

    # Initialize MongoDB connection
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client.budget_app

    # Register blueprints
    from .routes.home import home_bp
    from .routes.auth import auth_bp
    from .routes.budget import budget_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(budget_bp, url_prefix='/budget')

    return app, db