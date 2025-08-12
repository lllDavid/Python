def backtrack(nums, start, path, result):
    result.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(nums, i + 1, path, result)
        path.pop()

nums = [1, 2, 3]
result = []
backtrack(nums, 0, [], result)
print(result)