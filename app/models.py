from db.database import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    skills = db.Column(db.JSON)  # Ej: ["Python", "HTML"]
    projects = db.Column(db.JSON)  # Ej: [{"name": "Portafolio", "url": "/"}]
