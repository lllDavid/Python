def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)

print(collatz(10))

def collatz_recursive(n):
    if n == 1:
        return
    elif n % 2 == 0:
        n = n // 2
        print(n)
    else:
        n = 3 * n + 1
        print(n)
    collatz_recursive(n)

print(collatz(10))

def fizzbuzz(n):
    for i in range(n):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizzbuzz(101)

def fizzbuzz_recursive(n, i=1):
    if i > n:
        return
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    fizzbuzz_recursive(n, i + 1)

fizzbuzz_recursive(101)

def fibonacci(n):
    a,b = 0,1
    print(a)
    for _ in range(n):
        c = a+b
        a = b
        b = c
        print(a)

fibonacci(10)

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

fibonacci(10)

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(binary_search(arr, target, 0, len(arr) - 1))  

def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

print(reverse_words("Hello reverse me"))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))

def decimal_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //=2
    bits.reverse()
    return ''.join(bits)

print(decimal_to_binary(10))

def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

print(are_rotations("abcd", "cdab"))
print(are_rotations("abcd", "acbd"))

def primes_up_to(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i in range(n+1) if sieve[i]]

print(primes_up_to(20))

target = 8
nums = [1,2,3,4,5,6]

def nums_2(target, nums):
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i,j]
            j = j + 1
        i = i +1 

print(nums_2(target,nums))

str1 = "bank"
str2 = "kanb"

def is_changeable(str1, str2):
    diff = []
    for i, j in zip(str1,str2):
        if i != j:
            diff.append([i,j])
    print(diff)
    print(len(diff))
    if len(diff) == 2:
        return True
    return False

print(is_changeable(str1,str2))

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  
print(are_anagrams("hello", "world"))    

nums = [1, 2, 3, 4, 5]

def max_num(nums: list):
    current_value = nums[0]
    for i in nums:
        if i > current_value:
            current_value = i 
    return current_value

print(max_num(nums))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(17))
print(is_prime(18))

def factorial(n):
    if n < 0:
        raise ValueError("Negative input not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))

from itertools import chain

items = ["A", "B", "C"]
items2 = ["D", "E", "F"]

def chain2(*iterables):
    chain(items, items2)
    for i in iterables:
        yield from i

for i in chain2(items, items2):
    print(i)

from itertools import permutations

items = ["A", "B", "C"]

perms = permutations(items)

for p in perms:
    print(p)

from itertools import combinations
items = [1, 2, 3]
result = combinations(items, 2)
print(list(result)) 

from itertools import groupby

numbers = [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5]

grouped = groupby(numbers)

for key, group in grouped:
    print(f"Key: {key}, Group: {list(group)}")

from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)
print(double(5))  

import functools

@functools.lru_cache(maxsize=None) 
def expensive_computation(x):
    print(f"Computing {x}...")
    return x * x

print(expensive_computation(4))  
print(expensive_computation(4)) 

from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)  

from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()
print(queue)  

from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter) 

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p.x, p.y) 

from collections import defaultdict

dd = defaultdict(int)
dd['apples'] += 1
dd['oranges'] += 2
print(dd) 

from collections import OrderedDict

od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
for key, value in od.items():
    print(key, value)

def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

print(flatten([1, [2, [3, 4], 5], 6]))

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Hello"))

def merge_sorted_lists(lst1, lst2):
    i, j = 0, 0
    merged = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    return merged

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))

def sum_list(lst):
    return reduce(lambda acc, x: acc + x, lst, 0)