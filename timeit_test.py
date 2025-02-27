import timeit
import random

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

size = 10**5  
nums_linear = [random.randint(1, size) for _ in range(size)] 
nums_binary = sorted(nums_linear)  

target = random.choice(nums_linear)

linear_time = timeit.timeit('linear_search(nums_linear, target)', globals=globals(), number=100)

binary_time = timeit.timeit('binary_search(nums_binary, target)', globals=globals(), number=100)

print(f"Linear Search Time: {linear_time:.6f} seconds")
print(f"Binary Search Time: {binary_time:.6f} seconds")
