def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(factorial(5))


def factorial2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial2(n - 1)

print(factorial2(5))
