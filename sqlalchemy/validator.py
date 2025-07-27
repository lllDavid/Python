from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import re

DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

class InvalidInputError(Exception):
    pass

def validate_input(expected_type, pattern=None):
    def decorator(func):
        def wrapper(value, *args, **kwargs):
            if not isinstance(value, expected_type):
                raise InvalidInputError(f"Input '{value}' is not of type {expected_type.__name__}")
            if pattern and isinstance(value, str):
                if not re.match(pattern, value):
                    raise InvalidInputError(f"Input '{value}' does not match required pattern.")
            return func(value, *args, **kwargs)
        return wrapper
    return decorator

@validate_input(str, r"^[a-zA-Z0-9_]+$")
def get_user_by_name(name: str):
    session = SessionLocal()
    try:
        sql = text("SELECT * FROM users WHERE name = :name")
        result = session.execute(sql, {"name": name}).fetchone()
        return result
    finally:
        session.close()

if __name__ == "__main__":
    try:
        user = get_user_by_name("Alice")
        if user:
            print(user)
        else:
            print("User not found.")
    except InvalidInputError as e:
        print(f"Validation failed: {e}")

if __name__ == "__main__":
    test_inputs = [
        123,
        "Alice!",
        "Bob Smith",
        "",
        "'; DROP TABLE users;--",
        "admin' OR '1'='1",
        "Robert'); DROP TABLE students;--",
        "Alice",
    ]

    for input_val in test_inputs:
        try:
            user = get_user_by_name(input_val)
            if user:
                print(f"User found: {user}")
            else:
                print(f"No user found with name '{input_val}'")
        except InvalidInputError as e:
            print(f"Validation failed for input '{input_val}': {e}")