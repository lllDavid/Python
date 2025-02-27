def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  

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


