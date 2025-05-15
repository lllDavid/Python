def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(57))  
print(is_prime(29))  


import math

def is_prime_optimized(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:
            return False
    return True

print(is_prime_optimized(57))  
print(is_prime_optimized(29))  
