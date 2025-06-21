# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial", factorial(5))  

# Binary Search
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
print("Binary Search", binary_search(arr, target, 0, len(arr) - 1))  

# Fibonacci
def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print("Fibonacci", fibonacci(10))

# Fizzbuzz
def fizzbuzz(n):
    if n == 101:
        return 
    elif n % 15 == 0:
        print("Fizzbuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)

    fizzbuzz(n+1)

fizzbuzz(1)


# Collatz
def collatz(n):
    if n == 1:
        print(n)
        return
    print(n)
    
    if n % 2 == 0:
        collatz(n // 2)  
    else:
        collatz(3 * n + 1)  

collatz(6)  

# Example for actual use, Simulated directory tree, numbers = bytes
file_system = {
    'folder1': {
        'file1.txt': 1200,
        'file2.txt': 800,
        'subfolder1': {
            'file3.txt': 600
        }
    },
    'folder2': {
        'file4.txt': 1500
    },
    'file5.txt': 200
}

def get_total_size(node):
    if isinstance(node, int): 
        return node
    total = 0
    for child in node.values():
        total += get_total_size(child) 
    return total

total_size = get_total_size(file_system)
print("Total Size", total_size)