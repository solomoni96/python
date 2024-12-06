from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from app.config import Config

db = SQLAlchemy()

def app_init():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    # Register API resources
    from app.resources import Users, User
    api = Api(app)
    api.add_resource(Users, '/api/users/')
    api.add_resource(User, '/api/users/<int:id>')
    
    # Basic home route
    @app.route('/')
    def home():
        return "<h1>Flask REST API</h1>"
    
    return app
