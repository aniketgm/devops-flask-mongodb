from flask import Flask
from flask import current_app as capp
from config import Config
from pymongo import MongoClient

# Get MongoDB Client
def get_mdb_client():
    return MongoClient(capp.config['DB_HOST'], capp.config['DB_PORT'])

# Get/Create a db from MongoDB client
def get_mdb():
    mdb_client = get_mdb_client() 
    return mdb_client[capp.config['DB_NAME']]

# Flask main app
def create_app(app_config=Config):
    # Create app and set configuration from object passed to 'create_app'. Default is 'Config'.
    app = Flask(__name__)
    app.config.from_object(app_config)

    # Register blueprint for main files
    from src.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Register blueprint for user files
    from src.user import bp as user_bp
    app.register_blueprint(user_bp) 

    return app

from src import models
