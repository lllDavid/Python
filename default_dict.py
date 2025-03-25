from collections import defaultdict

counter = defaultdict(int)

counter['apple'] += 1
counter['banana'] += 2
counter['orange'] += 3

print(counter['grapes'])  

print(counter)  

from collections import defaultdict

grouped_numbers = defaultdict(list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    grouped_numbers[num % 3].append(num)

print(dict(grouped_numbers))
