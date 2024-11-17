import secrets
import string
from argon2 import PasswordHasher

def generate_random_password(length=20, salt_length=8):
    """Generates a random password with cryptographically secure randomness."""
    
    # Characters for password generation (expanded character set)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a cryptographically strong random password using secrets
    base_password = ''.join(secrets.choice(characters) for _ in range(length))
    
    # Optionally, you can add noise (more complex) by generating a few additional random characters
    # For added complexity, generate "noise" of the same length as base password, and shuffle the result.
    noise_length = 4
    noise = ''.join(secrets.choice(characters) for _ in range(noise_length))
    
    # Combine the base password with noise for added complexity
    password_with_noise = base_password + noise
    
    # Shuffle the final result to distribute noise evenly throughout the password
    password_list = list(password_with_noise)
    secrets.SystemRandom().shuffle(password_list)
    final_password = ''.join(password_list)[:length]
    
    return final_password

def hash_password(password):
    """Hashes the password using Argon2id and returns the hashed password."""
    # Create an Argon2 password hasher instance (using the default parameters)
    ph = PasswordHasher(
        time_cost=3,  # Number of iterations (time cost)
        memory_cost=2**16,  # Memory cost (in KB)
        parallelism=1  # Parallelism factor (number of threads)
    )
    
    # Hash the password using Argon2id
    hashed_password = ph.hash(password)
    
    return hashed_password

def verify_password(hashed_password, password):
    """Verifies the provided password matches the stored hash."""
    ph = PasswordHasher()
    
    try:
        # Verify the password against the stored hash
        ph.verify(hashed_password, password)
        return True
    except:
        return False

# Example Usage
if __name__ == "__main__":
    password_length = 20
    salt_length = 8
    
    # Step 1: Generate a strong random password
    password = generate_random_password(password_length, salt_length)
    print("Generated Password:", password)
    
    # Step 2: Hash the password using Argon2id
    hashed_password = hash_password(password)
    print("Hashed Password:", hashed_password)
    
    # Step 3: Verify the password (for example, during login)
    input_password = password  # Replace with actual user input during login
    is_valid = verify_password(hashed_password, input_password)
    print(f"Password valid: {is_valid}")
