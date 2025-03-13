import time

# O(1) - Constant Time
def get_first_element(lst):
    return lst[0]

# O(n) - Linear Time
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

# O(n^2) - Quadratic Time
def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

# O(log n) - Logarithmic Time
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# O(n!) - Factorial Time
def generate_permutations(s, step=0):
    if step == len(s):
        print("".join(s))
        return
    for i in range(step, len(s)):
        s[step], s[i] = s[i], s[step]
        generate_permutations(s, step + 1)
        s[step], s[i] = s[i], s[step]

arr = [1, 2, 3, 4, 5]
sorted_arr = [1, 3, 5, 7, 9]

print("O(1) - Get First Element:", get_first_element(arr))

print("O(n) - Linear Search (3 in arr):", linear_search(arr, 3))

print("O(n^2) - Print Pairs:")
print_pairs([1, 2, 3])

print("O(log n) - Binary Search (5 in sorted_arr):", binary_search(sorted_arr, 5))

print("O(n!) - Generate Permutations of 'ABC':")
generate_permutations(list("ABC"))
