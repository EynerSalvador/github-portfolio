import pytest
from app.db.database import db, init_app
from app.katas.models import Profile
from flask import Flask

@pytest.fixture
def app():
    """Fixture para pruebas con base de datos en memoria"""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    init_app(app)
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_profile_creation(app):
    """Prueba la creación de perfiles"""
    with app.app_context():
        # Crear y guardar perfil
        profile = Profile(
            name="Ejemplo",
            email="test@example.com",
            skills=["Python"],
            projects=[{"name": "Proyecto Test"}]
        )
        db.session.add(profile)
        db.session.commit()
        
        # Verificar
        saved = Profile.query.first()
        assert saved.email == "test@example.com"
        assert "Python" in saved.skills
