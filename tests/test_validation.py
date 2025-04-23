from app.katas.validation import validate_skill  # Import absoluto

def test_validate_skill():
    assert validate_skill("Python", ["Python", "JS"]) is True
    assert validate_skill("Ruby", ["Python"]) is False
