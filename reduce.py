from functools import reduce

nested_lists = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]

flattened = reduce(lambda acc, curr: acc + curr, nested_lists)
print(flattened)  


dicts = [
    {'a': 2, 'b': 3},
    {'a': 5, 'c': 7},
    {'b': 4, 'c': 1, 'd': 8}
]

def merge_dicts(acc, curr):
    for key, value in curr.items():
        acc[key] = acc.get(key, 0) + value
    return acc

merged_dict = reduce(merge_dicts, dicts, {})
print(merged_dict) 