import pytest
from app import app, db  # Importa app y db
from app.models import Post

# Configuración para pruebas
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Crea tablas antes de las pruebas
        yield client
        with app.app_context():
            db.drop_all()  # Limpia la DB después

def test_create_post(client):
    """Prueba que se pueda crear un Post."""
    with app.app_context():
        post = Post(title="Prueba pytest", content="¡Funciona!")
        db.session.add(post)
        db.session.commit()
        assert post.id is not None  # Verifica que se guardó
