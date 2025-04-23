def validate_skill(skill: str, allowed_skills: list) -> bool:
    """Valida si una habilidad está en la lista permitida (Kata TDD)."""
    return skill in allowed_skills
