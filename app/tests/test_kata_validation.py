import pytest
from app.katas.kata_validation import validate_skill

def test_validate_skill():
    allowed = ["Python", "JavaScript", "HTML"]
    
    # Caso válido
    assert validate_skill("Python", allowed) is True
    
    # Caso inválido
    assert validate_skill("Java", allowed) is False
    
    # Edge case (empty)
    assert validate_skill("", allowed) is False
