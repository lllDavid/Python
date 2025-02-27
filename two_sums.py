nums = [2,3,4,5,8]
t = 9

def sums(nums,t):
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == t:
                return [i,j]
            j = j + 1
        i = i + 1

print(sums(nums,t))

def two_sum(nums, target):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                result.append((i, j))
    return result

print(two_sum(nums, t))

def two_sum2(nums, target):
    result = []
    seen = {}  
    
    for i, num in enumerate(nums):
        complement = target - num  
        if complement in seen:
            result.append((seen[complement], i))  
        seen[num] = i
    
    return result
