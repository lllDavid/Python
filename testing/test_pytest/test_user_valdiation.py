import pytest
from user_validation import validate_user  

@pytest.mark.parametrize("user", [
    # Valid user
    {"email": "test@example.com", "age": 25, "password": "Passw0rd123"},
    # Edge cases for age
    {"email": "edge@example.com", "age": 18, "password": "Abcdef12"},
    {"email": "edge2@example.com", "age": 99, "password": "Xyz12345"},
])
def test_valid_users(user):
    assert validate_user(user) is True


@pytest.mark.parametrize("user", [
    # Invalid emails
    {"email": "invalidemail", "age": 25, "password": "Passw0rd123"},
    {"email": "noatsign.com", "age": 25, "password": "Passw0rd123"},
    # Age out of range
    {"email": "test@example.com", "age": 17, "password": "Passw0rd123"},
    {"email": "test@example.com", "age": 100, "password": "Passw0rd123"},
    # Password too short
    {"email": "test@example.com", "age": 25, "password": "Ab12"},
    # Password missing numbers
    {"email": "test@example.com", "age": 25, "password": "Password"},
    # Password missing letters
    {"email": "test@example.com", "age": 25, "password": "12345678"},
])
def test_invalid_users(user):
    assert validate_user(user) is False