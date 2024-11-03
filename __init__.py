from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def create_app(config_name=None):

    load_dotenv()
    app = Flask(__name__)
    
    #Load Configuration
    if config_name == 'development':
        app.config.from_object('config.DevelopmentConfig')
    elif config_name == 'testing':
        app.config.from_object('config.TestingConfig')
    elif config_name == 'production':
        app.config.from_object('config.ProductionConfig')

    app.secret_key = app.config['SECRET_KEY']

    # Initialize MongoDB connection
    client = MongoClient(app.config['MONGO_URI'])
    db = client.budget_app

    # Register blueprints
    from .routes import register_blueprints
    register_blueprints(app)

    return app, db

#import models
from .models import User, Budget