class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Persons:
    def __init__(self):
        self.persons = []

    def add_person(self, person):
        self.persons.append(person)

    def __iter__(self):
        return iter(self.persons)

    def get_names(self):
        return [person.name for person in self.persons]

    def get_ages(self):
        return [person.age for person in self.persons]

collection = Persons()
collection.add_person(Person("Alice", 30))
collection.add_person(Person("Bob", 25))
collection.add_person(Person("Charlie", 35))

for person in collection:
    print(person.name, person.age)