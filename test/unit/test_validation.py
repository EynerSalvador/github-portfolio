from app.katas.validation import validate_skill

def test_validate_skill():
    allowed = ["Python", "JavaScript", "HTML"]
    
    # Caso 1: Habilidad permitida
    assert validate_skill("Python", allowed) is True
    
    # Caso 2: Habilidad no permitida
    assert validate_skill("Java", allowed) is False
    
    # Caso 3: Habilidad vacía
    assert validate_skill("", allowed) is False
