from flask import Blueprint, jsonify
from app.katas.models import Profile
from app.db.database import db

bp = Blueprint('api', __name__)

@bp.route('/profiles')
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([{
        'name': p.name,
        'skills': p.skills,
        'projects': p.projects
    } for p in profiles])
