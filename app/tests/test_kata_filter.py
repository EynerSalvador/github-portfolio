from app.katas.kata_filter import filter_projects_by_tech

def test_filter_projects():
    projects = [
        {"name": "Portafolio", "technologies": ["HTML", "CSS"]},
        {"name": "API REST", "technologies": ["Python", "Flask"]}
    ]
    
    # Filtro exitoso
    assert len(filter_projects_by_tech(projects, "Python")) == 1
    
    # Filtro vacío
    assert len(filter_projects_by_tech(projects, "Java")) == 0
