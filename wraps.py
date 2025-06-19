import hashlib
from functools import wraps

def log_function_call(func):
    @wraps(func)  
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def compute_hash(data):
    """Compute SHA-256 hash of the input string."""
    h = hashlib.sha256()
    h.update(data.encode('utf-8'))
    return h.hexdigest()

result = compute_hash("hello world")

print(f"Function name: {compute_hash.__name__}")
print(f"Function docstring: {compute_hash.__doc__}")