from flask import Flask
from .db.database import db  # Nota el punto al inicio

def create_app():
    app = Flask(__name__)
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicialización de extensiones
    db.init_app(app)
    
    # Registrar blueprints/rutas
    from app.katas.routes import bp as katas_bp
    app.register_blueprint(katas_bp, url_prefix='/api')
    
    return app
