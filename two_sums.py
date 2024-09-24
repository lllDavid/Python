def twoSum(numbers, target):
    complement = {}
    for i, num in enumerate(numbers):
        if target - num in complement:
            return [complement[target - num], i]
        complement[num] = i
numbers = [2,3,4,6]
target = 7
print(twoSum(numbers, target))
