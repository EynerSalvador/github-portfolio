def filter_projects_by_tech(projects: list[dict], tech: str) -> list[dict]:
    """Filtra proyectos que usen cierta tecnología.
    
    Args:
        projects: Lista de diccionarios con clave 'technologies'.
        tech: Tecnología a filtrar (ej: 'Python').
    
    Returns:
        Lista filtrada o lista vacía si no hay coincidencias.
    """
    return [p for p in projects if tech in p.get('technologies', [])]
