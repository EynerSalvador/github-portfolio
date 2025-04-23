from flask import jsonify
from app import create_app
from app.katas.models import Profile, db

app = create_app()

@app.route('/api/profiles')
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([{
        'name': p.name,
        'skills': p.skills
    } for p in profiles])
