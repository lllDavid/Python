nums = [2,3,6,4]
target = 9

def twoSum(nums, target):
    i = 0
    j = i +1
    while (i < len(nums)):
        j = i + 1 
        while(j < len(nums)):
            if (nums[i] + nums[j] == target):
                return [i,j]
            else:
                j = j + 1
        else:
            i = i + 1
print(twoSum(nums,target))

            