from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Car:
    make: str
    model: str
    year: int
    color: str
    price: float
    mileage: Optional[float] = field(default=0.0) 
    last_serviced: Optional[datetime] = field(default=None) 

    def calculate_depreciation(self, current_year: int) -> float:
        age = current_year - self.year
        depreciation_rate = 0.15  
        depreciation = self.price * (depreciation_rate ** age)
        return round(depreciation, 2)

    def calculate_discounted_price(self, discount_percentage: float) -> float:
        discounted_price = self.price - (self.price * discount_percentage / 100)
        return round(discounted_price, 2)

    def is_luxury_car(self) -> bool:
        luxury_brands = ["Mercedes", "BMW", "Audi", "Lexus", "Porsche"]
        return self.make.capitalize() in luxury_brands

    def validate(self):
        if not self.make or not self.model or not self.year or not self.color or self.price <= 0:
            raise ValueError("Car details are invalid.")
        if self.year < 1886 or self.year > datetime.now().year:  
            raise ValueError("Invalid year for the car.")
        if self.price <= 0:
            raise ValueError("Price must be positive.")

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.color}, Price: ${self.price}"

car = Car("Mercedes", "A-Class", 2019, "White", 35000.00)
car.validate()

print(car)
print(f"Depreciation for 2025: ${car.calculate_depreciation(2025)}")
print(f"Price after 10% discount: ${car.calculate_discounted_price(10)}")
print(f"Is it a luxury car? {'Yes' if car.is_luxury_car() else 'No'}")
