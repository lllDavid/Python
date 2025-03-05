class Person:
    __slots__ = ['name', 'age']  
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person('Alice', 30)
person2 = Person('Bob', 25)

print(person1.name, person1.age)
print(person2.name, person2.age)

print(hasattr(person1, '__dict__'))  