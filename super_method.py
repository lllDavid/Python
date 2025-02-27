class Animal:
    def __init__(self, age, height, weight, species):
        self.age = age
        self.height = height
        self.weight = weight
        self.species = species

    def calculate_bmi(self):
        return self.weight / (self.height / 100) ** 2

    def is_overweight(self):
        bmi = self.calculate_bmi()
        return bmi > 30  # Example threshold for overweight

    def life_expectancy(self):
        # Placeholder logic: average life expectancy based on species
        life_expectancy_map = {
            'dog': 12,
            'cat': 15,
        }
        return life_expectancy_map.get(self.species.lower(), 10)

    def __str__(self):
        return f"{self.species.capitalize()} - Age: {self.age}, Height: {self.height} cm, Weight: {self.weight} kg, Life Expectancy: {self.life_expectancy()} years"
    
    def __repr__(self):
        return f"Animal(age={self.age}, height={self.height}, weight={self.weight}, species='{self.species}')"


class Dog(Animal):
    def __init__(self, race, age, height, weight):
        super().__init__(age, height, weight, species="dog")
        self.race = race
        self.is_training = False

    def start_training(self):
        self.is_training = True
        print(f"{self.race} has started training!")

    def stop_training(self):
        self.is_training = False
        print(f"{self.race} has stopped training.")

    def __str__(self):
        training_status = "Training" if self.is_training else "Not Training"
        return f"Dog - Race: {self.race}, Age: {self.age}, Height: {self.height} cm, Weight: {self.weight} kg, Training Status: {training_status}, BMI: {self.calculate_bmi():.2f}"
    
    def __repr__(self):
        return f"Dog(race='{self.race}', age={self.age}, height={self.height}, weight={self.weight}, training={self.is_training})"


dog1 = Dog("Bernhardiner", 9, 120, 100)
dog2 = Dog("Labrador", 5, 60, 35)

print(dog1)
dog1.start_training()
print(dog1)

dog1.stop_training()
print(dog2)

print(f"Is {dog1.race} overweight? {'Yes' if dog1.is_overweight() else 'No'}")
print(f"{dog2.race}'s Life Expectancy: {dog2.life_expectancy()} years")
