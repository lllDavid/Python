from dataclasses import dataclass

@dataclass
class Human:
    name: str
    age: int
    birthyear: int
    height: float
    weight: float

    @classmethod
    def from_birthyear(cls, name: str, birthyear: int, height: float, weight: float):
        current_year = 2025
        age = current_year - birthyear
        return cls(name, age, birthyear, height, weight)

human = Human.from_birthyear(name="Alice", birthyear=1990, height=5.7, weight=140)
print(human)
