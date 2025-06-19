import re
from itertools import combinations

items = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]

item_pairs = list(combinations(items, 2))
number_pairs = list(combinations(numbers, 2))

print("Item pairs:")
for pair in item_pairs:
    print(pair)

print("\nNumber pairs:")
for pair in number_pairs:
    print(pair)

text = "abcd 1234"
pattern = r'([a-z]{2}|[0-9]{2})'

matches = re.finditer(pattern, text)

print("\nRegex matches:")
for match in matches:
    print(match.group(), match.start(), match.end())
