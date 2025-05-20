from collections import Counter

data = ['cat', 'dog', 'cat', 'bird', 'dog', 'dog']
counter = Counter(data)
print(counter)

text = "abracadabra"
char_counter = Counter(text)
print(char_counter)

top_two = counter.most_common(2)
print(top_two)

counter.update(['cat', 'elephant', 'dog'])
print(counter)

counter.subtract(['dog', 'dog', 'bird'])
print(counter)

counter_dict = dict(counter)
print(counter_dict)

elements_list = list(counter.elements())
print(elements_list)

counter.clear()
print(counter)
