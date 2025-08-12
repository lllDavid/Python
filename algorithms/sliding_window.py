def max_sum_subarray(nums, k):
    if k > len(nums):
        return None, []

    window_sum = sum(nums[:k])
    max_sum = window_sum
    start_index = 0

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            start_index = i - k + 1

    return max_sum, nums[start_index:start_index + k]

arr = [2, 1, 5, 1, 3, 2]
max_sum, subarr = max_sum_subarray(arr, 3)
print(max_sum)  
print(subarr)   