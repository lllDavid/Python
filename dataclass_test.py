from dataclasses import dataclass

# Dataclass
@dataclass
class Car:
    make:str
    model:str
    year:str
    color:str
    price:float

c= Car("mercedes","a-class","2019","white",35_000.00)
print(c)

# Regular
class Car:
    def __init__(self, make:str, model:str, year:str, color:str, price:float):
        self.make = make
        self.model = model
        self.year = year 
        self.color = color
        self.price = price

c = Car("mercedes","a-class","2019","white",35_000.00)
print(c)