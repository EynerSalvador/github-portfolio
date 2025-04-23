from app.katas.kata_validation import validate_post

def test_validate_post_title_length():
    # Prueba que títulos cortos fallen
    assert validate_post("Hola", "Contenido") == False  # Menos de 5 caracteres
    assert validate_post("Python TDD", "Contenido") == True  # Válido
