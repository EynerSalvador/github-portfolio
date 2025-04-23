
import pytest
from app.models import db, Post

def test_create_post():
    """Prueba que se pueda crear un Post en la DB."""
    post = Post(title="TDD en Python", content="Ejemplo de prueba")
    db.session.add(post)
    db.session.commit()
    assert post.id is not None  # Verifica que se guardó en la DB
