import pytest
from app.katas.filter import filter_projects_by_tech

def test_filter_projects():
    # Datos de prueba
    projects = [
        {"name": "Portfolio", "technologies": ["HTML", "CSS"]},
        {"name": "API", "technologies": ["Python", "FastAPI"]}
    ]
    
    # Caso 1: Tecnología existente
    result = filter_projects_by_tech(projects, "Python")
    assert len(result) == 1
    assert result[0]["name"] == "API"
    
    # Caso 2: Tecnología inexistente
    assert len(filter_projects_by_tech(projects, "Java")) == 0
    
    # Caso 3: Lista vacía
    assert len(filter_projects_by_tech([], "Python")) == 0
