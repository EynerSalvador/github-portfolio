from db.database import db
from app.katas.kata_validation import validate_skill
from app.katas.kata_filter import filter_projects_by_tech

class Profile(db.Model):
    # ... (campos existentes)
    
    def validate_skill(self, skill: str) -> bool:
        """Usa la kata de validación."""
        allowed_skills = ["Python", "JavaScript", "HTML", "CSS"]
        return validate_skill(skill, allowed_skills)
    
    def get_projects_by_tech(self, tech: str) -> list:
        """Usa la kata de filtrado."""
        return filter_projects_by_tech(self.projects, tech)
