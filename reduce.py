from functools import reduce

# Flatten list
nested_lists = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]

flattened = reduce(lambda acc, curr: acc + curr, nested_lists)
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



dicts = [
    {'a': 2, 'b': 3},
    {'a': 5, 'c': 7},
    {'b': 4, 'c': 1, 'd': 8}
]
# Combine list of dicts by summing values of matching keys into single dict
def merge_dicts(acc, curr):
    for key, value in curr.items():
        acc[key] = acc.get(key, 0) + value
    return acc

merged_dict = reduce(merge_dicts, dicts, {})
print(merged_dict)  # {'a': 7, 'b': 7, 'c': 8, 'd': 8}
