class PersonCollection:
    def __init__(self):
        self.persons = []  

    def add_person(self, person):
        self.persons.append(person)

    def __iter__(self):
        return iter(self.persons)  

collection = PersonCollection()
collection.add_person("Alice")
collection.add_person("Bob")
collection.add_person("Charlie")

for person in collection:
    print(person)
