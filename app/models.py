from app.db.database import db

class Profile(db.Model):
    """Modelo para perfiles del portfolio"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    skills = db.Column(db.JSON)  # Ej: ["Python", "JavaScript"]
    projects = db.Column(db.JSON) # Ej: [{"name": "Proyecto X", "tech": ["React"]}]

    def __repr__(self):
        return f'<Profile {self.email}>'
