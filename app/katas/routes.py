from flask import Blueprint, jsonify
from ..models import Profile
from ..db.database import db  # Cambiado a import relativo

bp = Blueprint('api', __name__)

@bp.route('/profiles')
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([{
        'name': p.name,
        'skills': p.skills,
        'projects': p.projects
    } for p in profiles])
