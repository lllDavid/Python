nums = [2, 1, 5, 66, 7, 12, 3]

for i in range(len(nums)):
    for j in range(len(nums) - i - 1):  
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
