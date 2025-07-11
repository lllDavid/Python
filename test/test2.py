def two_sum_sorted(nums, target):
    sorted_nums = sorted((n, i) for i, n in enumerate(nums))
    l, r = 0, len(nums) - 1
    while l < r:
        total = sorted_nums[l][0] + sorted_nums[r][0]
        if total == target:
            return [sorted_nums[l][1], sorted_nums[r][1]]
        elif total < target:
            l += 1
        else:
            r -= 1

from itertools import combinations

def two_sum_combinations(nums, target):
    for i, j in combinations(range(len(nums)), 2):
        if nums[i] + nums[j] == target:
            return [i, j]
