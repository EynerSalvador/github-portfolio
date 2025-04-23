from flask import Flask
from .db.database import db  # Import relativo

from app.katas.models import Profile
from app.db.database import db

def create_app():
    app = Flask(__init__)
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicialización de extensiones
    db.init_app(app)
    
    # Registrar blueprints/rutas (¡CAMBIADO A IMPORT RELATIVO!)
    from .katas.routes import bp as katas_bp  # Nota el punto inicial
    app.register_blueprint(katas_bp, url_prefix='/api')
    
    return app
