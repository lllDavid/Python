nums = [2, 1, 5, 66, 7, 12, 3]

for i in range(len(nums)):
    for j in range(len(nums) - i - 1):  
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)

def bubble_sort_recursive(nums, n=None):
    if n is None:
        n = len(nums)
    
    if n == 1:
        return nums
    
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    
    return bubble_sort_recursive(nums, n - 1)

nums = [2, 1, 5, 66, 7, 12, 3]
sorted_nums = bubble_sort_recursive(nums)
print(sorted_nums)
