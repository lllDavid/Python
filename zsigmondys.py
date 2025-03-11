import math

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def check_zsigmondy(a, b, n):
    if a == b:
        print(f"Zsigmondy's theorem does not apply when a = b.")
        return

    expression = a**n - b**n
    print(f"Checking for a = {a}, b = {b}, n = {n}:")

    factors_n = set(prime_factors(abs(expression)))
    print(f"Prime factors of {a}^{n} - {b}^{n}: {factors_n}")

    for k in range(1, n):
        expression_k = a**k - b**k
        factors_k = set(prime_factors(abs(expression_k)))
        print(f"Prime factors of {a}^{k} - {b}^{k}: {factors_k}")

        common_factors = factors_n.intersection(factors_k)
        if common_factors:
            print(f"Common factors found between {a}^{n} - {b}^{n} and {a}^{k} - {b}^{k}: {common_factors}")
            return
    
    print(f"Zsigmondy's theorem holds for a = {a}, b = {b}, n = {n}.")

check_zsigmondy(2, 1, 5)
