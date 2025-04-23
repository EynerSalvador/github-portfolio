from app.katas.filter import filter_projects_by_tech
from app.katas.validation import validate_skill

class Profile(db.Model):
    # ... (campos existentes)
    
    def get_projects_by_tech(self, tech: str) -> list:
        """Filtra proyectos del perfil por tecnología."""
        return filter_projects_by_tech(self.projects or [], tech)
    
    def is_skill_valid(self, skill: str) -> bool:
        """Valida una habilidad contra las del perfil."""
        return validate_skill(skill, self.skills or [])
