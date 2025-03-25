names = ["David", "Tim", "Mark", "Sven", "Daniel" ]

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

print(d)

from collections import defaultdict

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

print(d)