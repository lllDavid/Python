import math

def calculate_entropy(password) -> float:
    char_set_size = 0
    
    if any(c.islower() for c in password):  
        char_set_size += 26
    if any(c.isupper() for c in password):  
        char_set_size += 26
    if any(c.isdigit() for c in password):  
        char_set_size += 10
    if any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password):  
        char_set_size += 32

    password_length = len(password)
    
    entropy = password_length * math.log2(char_set_size)
    
    return entropy

password = "8e)?/?a/Quz%KdiVig#(^BCq9C>J-?"
entropy = calculate_entropy(password)
print(f"Entropy of the password '{password}' is: {entropy:.2f} bits")