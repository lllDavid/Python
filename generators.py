def square_numbers(n):
    for i in range(n):
        yield i ** 2
        
for square in square_numbers(5):
    print(square)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

gen = prime_numbers()
for _ in range(10):
    print(next(gen))
