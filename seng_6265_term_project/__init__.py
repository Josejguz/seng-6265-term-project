from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
from config import config
import os

def create_app(config_name=None):

    load_dotenv()

    app = Flask(__name__)
    
    #Load Configuration
    app.config.from_object(config[config_name])

    app.secret_key = app.config['SECRET_KEY']

    # Initialize MongoDB connection
    client = MongoClient(app.config['MONGO_URI'])
    db = client.get_default_database()
    app.db = db

    # Register blueprints
    from .routes import register_blueprints
    register_blueprints(app)

    return app, db

#import models
from .models import User, Budget