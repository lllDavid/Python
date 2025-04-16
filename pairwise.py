from itertools import combinations

items = ['a', 'b', 'c', 'd']

pairs = list(combinations(items, 2))

for pair in pairs:
    print(pair)
