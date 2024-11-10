import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '7nWCfr63Pntd1kgOCGDLQG5E0HcpVjvjrHxEjhwslrcey')
    MONGO_URI = os.getenv('MONGO_URI')
    
class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/budget_app')

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/budget_app_test')
    WTFR_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/budget_app')

config = {
    'development': DevelopmentConfig, 
    'testing': TestingConfig, 
    'production': ProductionConfig,
    'default': DevelopmentConfig
}