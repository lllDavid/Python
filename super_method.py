class Animal:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

class Dog(Animal):
    def __init__(self, race, age, height, weight):
        super().__init__(age, height, weight)
        self.race = race

    def __str__(self):
        return f"Age: {self.age}, Height: {self.height} cm, Weight: {self.weight} kg"
    
    def __repr__(self):
        return f"Dog(age={self.age}, race='{self.race}', height={self.height}, weight={self.weight})"
    
dog1 = Dog(9, 120, 100, "Bernhardiner")
print(dog1)