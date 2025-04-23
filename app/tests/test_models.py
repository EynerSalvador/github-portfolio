from app.models import Profile

def test_profile_skill_validation():
    profile = Profile(skills=["Python"])
    assert profile.validate_skill("Python") is True
    assert profile.validate_skill("Java") is False

def test_profile_project_filtering():
    profile = Profile(projects=[{"name": "API", "technologies": ["Python"]}])
    assert len(profile.get_projects_by_tech("Python")) == 1
