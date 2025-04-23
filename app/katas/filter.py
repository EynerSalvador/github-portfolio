def filter_projects_by_tech(projects: list, tech: str) -> list:
    """Filtra proyectos que usen una tecnología específica (Kata TDD)."""
    return [p for p in projects if tech in p.get("technologies", [])]
