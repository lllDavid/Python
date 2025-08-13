from dataclasses import dataclass

@dataclass
class Human:
    name: str
    age: int
    birthyear: int
    height: float
    weight: float

    @classmethod
    def from_birthyear(cls, name, birthyear, height, weight):
        age = 2025 - birthyear
        return cls(name, age, birthyear, height, weight)

@dataclass
class Patient(Human):
    patient_id: str = None

    @classmethod
    def from_birthyear(cls, name, birthyear, height, weight, patient_id=None):
        instance = super().from_birthyear(name, birthyear, height, weight)
        instance.patient_id = patient_id
        return instance

patient = Patient.from_birthyear("Alice", 1990, 5.7, 140, patient_id="P1001")
print(patient)