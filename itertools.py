import itertools

colors = ["red", "green", "blue"]
cycler = itertools.cycle(colors)
for i in range(6):
    print(next(cycler))

import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = itertools.chain(list1, list2)
for item in combined:
    print(item)

import itertools

items = ['A', 'B', 'C']
combs = itertools.combinations(items, 2)
for comb in combs:
    print(comb)

import itertools

items = ['A', 'B', 'C']
perms = itertools.permutations(items, 2)
for perm in perms:
    print(perm)

import itertools

list1 = [1, 2]
list2 = ['A', 'B']
prod = itertools.product(list1, list2)
for p in prod:
    print(p)

import itertools

pairs = [(1, 2), (3, 4), (5, 6)]
result = itertools.starmap(lambda x, y: x + y, pairs)
for r in result:
    print(r)

import itertools

numbers = [1, 2, 3, 4, 5, 6]
filtered = itertools.filterfalse(lambda x: x % 2 != 0, numbers)
for num in filtered:
    print(num)