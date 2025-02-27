from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def walk(self):
        pass
        
class Person(Human):
    def walk(self):
        print(f"{self.name} started to walk")
        
p1 = Person("David")
p1.walk()




