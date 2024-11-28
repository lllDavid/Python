import secrets
import string
from argon2 import PasswordHasher

def generate_random_password(length=30, salt_length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    base_password = ''.join(secrets.choice(characters) for _ in range(length))

    noise_length = 4
    noise = ''.join(secrets.choice(characters) for _ in range(noise_length))
    
    password_with_noise = base_password + noise
    
    password_list = list(password_with_noise)
    secrets.SystemRandom().shuffle(password_list)
    final_password = ''.join(password_list)[:length]
    
    return final_password

def hash_password(password):
    ph = PasswordHasher(
        time_cost=3,  
        memory_cost=2**16,  
        parallelism=1  
    )

    hashed_password = ph.hash(password)
    
    return hashed_password

def verify_password(hashed_password, password):
    ph = PasswordHasher()
    
    try:
        ph.verify(hashed_password, password)
        return True
    except:
        return False

if __name__ == "__main__":
    password_length = 30
    salt_length = 8
    password = generate_random_password(password_length, salt_length)
    print("Generated Password:", password)
    
    hashed_password = hash_password(password)
    print("Hashed Password:", hashed_password)

    input_password = password  
    is_valid = verify_password(hashed_password, input_password)
    print(f"Password valid: {is_valid}")
