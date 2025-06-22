import re

def validate_user(user):
    """
    Validates user data compliance with rules:
    - 'email' must be a valid email format
    - 'age' must be between 18 and 99
    - 'password' must be at least 8 chars, contain letters and numbers
    """
    email = user.get("email", "")
    age = user.get("age", 0)
    password = user.get("password", "")

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        return False

    if not (18 <= age <= 99):
        return False

    if len(password) < 8:
        return False

    if not (re.search(r"[A-Za-z]", password) and re.search(r"\d", password)):
        return False

    return True