def validate_skill(skill: str, allowed_skills: list[str]) -> bool:
    """Valida si una habilidad está permitida.
    
    Args:
        skill: Habilidad a validar (ej: 'JavaScript').
        allowed_skills: Lista de habilidades permitidas.
    
    Returns:
        True si es válida, False si no.
    """
    return skill in allowed_skills
