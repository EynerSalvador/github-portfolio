from flask import Flask
from app.db.database import db

def create_app():
    app = Flask(__name__)
    
    # Configuración de la DB (SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicialización
    db.init_app(app)
    
    # Crear tablas (esto puede moverse a un script aparte si prefieres)
    with app.app_context():
        db.create_all()
    
    return app
