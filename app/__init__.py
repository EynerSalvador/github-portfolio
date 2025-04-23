from flask import Flask
from app.db.database import init_db

def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    init_db(app)
    return app
