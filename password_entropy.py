import math

def calculate_entropy(password) -> float:
    char_set_size = 0
    
    if any(c.islower() for c in password):  # Lowercase
        char_set_size += 26
    if any(c.isupper() for c in password):  # Uppercase
        char_set_size += 26
    if any(c.isdigit() for c in password):  # Digits
        char_set_size += 10
    if any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password):  # Special characters
        char_set_size += 32

    password_length = len(password)
    
    entropy = password_length * math.log2(char_set_size)
    
    return entropy

password = "P@ssw0rd123"
entropy = calculate_entropy(password)
print(f"Entropy of the password '{password}' is: {entropy:.2f} bits")
