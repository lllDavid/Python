from itertools import combinations

items = ['a', 'b', 'c', 'd']

pairs = list(combinations(items, 2))

for pair in pairs:
    print(pair)


numbers = [1, 2, 3, 4]


pairs = list(combinations(numbers, 2))

for pair in pairs:
    print(pair)
