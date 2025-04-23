from app.katas.validation import validate_skill

def test_validate_skill():
    assert validate_skill("Python", ["Python", "Java"]) is True
    assert validate_skill("Ruby", ["Python"]) is False
