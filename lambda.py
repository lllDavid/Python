# 1
sum_of_squares = lambda nums: sum(x**2 for x in nums)
print(sum_of_squares([1, 2, 3]))  

# 2
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
print(is_prime(7))  
print(is_prime(10))  

# 3
from functools import reduce

fibonacci = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n-2), [0, 1])

print(fibonacci(7))  
