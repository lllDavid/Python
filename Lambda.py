#1)
double = lambda x: x * 2
doubledNumber = double(5)
print(doubledNumber)

#2)
def doubleNumbers(wert):
    double = lambda x : x * 2
    doubledNumber = double(wert)
    print(doubledNumber)
doubleNumbers((int(input("Geben sie eine Zahl zum verdoppeln ein: "))))

#3)
from itertools import groupby

words = ['apple', 'ant', 'banana', 'bat', 'cat', 'car']

grouped_words = {key: list(group) for key, group in groupby(sorted(words), key=lambda x: x[0])}

print(grouped_words)

#4)
add_message = lambda func: lambda *args, **kwargs: ("Executing:", func(*args, **kwargs))

@add_message
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
