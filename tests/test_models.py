from app.models import Profile
from app import create_app
from app.db.database import db

def test_profile_creation():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        profile = Profile(name="Test", skills=["Python"])
        db.session.add(profile)
        db.session.commit()
        
        assert Profile.query.first().name == "Test"
