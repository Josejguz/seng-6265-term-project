from flask import Blueprint
from .home import home_bp
from .auth import auth_bp
from .budget import budget_bp

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(budget_bp, url_prefix='/budget') 