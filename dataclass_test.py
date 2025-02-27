from dataclasses import dataclass, field
from datetime import datetime

# Dataclass with added complexity
@dataclass
class Car:
    make: str
    model: str
    year: int
    color: str
    price: float
    mileage: Optional[float] = field(default=0.0)  # Optional field to track mileage
    last_serviced: Optional[datetime] = field(default=None)  # Optional field to track last service date

    def calculate_depreciation(self, current_year: int) -> float:
        """Estimate depreciation based on car's age"""
        age = current_year - self.year
        depreciation_rate = 0.15  # 15% depreciation per year
        depreciation = self.price * (depreciation_rate ** age)
        return round(depreciation, 2)

    def calculate_discounted_price(self, discount_percentage: float) -> float:
        """Apply a discount on the car's price"""
        discounted_price = self.price - (self.price * discount_percentage / 100)
        return round(discounted_price, 2)

    def is_luxury_car(self) -> bool:
        """Check if the car is a luxury car based on its make"""
        luxury_brands = ["Mercedes", "BMW", "Audi", "Lexus", "Porsche"]
        return self.make.capitalize() in luxury_brands

    def validate(self):
        """Basic validation for the car's attributes"""
        if not self.make or not self.model or not self.year or not self.color or self.price <= 0:
            raise ValueError("Car details are invalid.")
        if self.year < 1886 or self.year > datetime.now().year:  # Cars didn't exist before 1886
            raise ValueError("Invalid year for the car.")
        if self.price <= 0:
            raise ValueError("Price must be positive.")

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.color}, Price: ${self.price}"

# Creating an instance of the Car class
car = Car("Mercedes", "A-Class", 2019, "White", 35000.00)
car.validate()

# Perform some actions on the car
print(car)
print(f"Depreciation for 2025: ${car.calculate_depreciation(2025)}")
print(f"Price after 10% discount: ${car.calculate_discounted_price(10)}")
print(f"Is it a luxury car? {'Yes' if car.is_luxury_car() else 'No'}")
