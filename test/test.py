lst = [1, 2, 2, 3, 4, 4, 5, 6, 6]

def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

print(remove_duplicates(lst))  


text = "Hello abc hello 123 heLLo 223 xcb"

def count_words(text):
    word_counts = {}
    text = text.lower()
    subs = text.split()
    for word in subs:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

print(count_words(text))


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