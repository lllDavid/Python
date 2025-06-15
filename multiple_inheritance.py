class BaseClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from {self.name}!"

class DerivedClass1(BaseClass):
    def __init__(self, name, age):
        super().__init__(name)  
        self.age = age

    def greet(self):
        return f"Hello, I am {self.name} and I am {self.age} years old."

class DerivedClass2(BaseClass):
    def __init__(self, name, city):
        super().__init__(name)
        self.city = city

    def greet(self):
        return f"Hello, I am {self.name} from {self.city}."

class CombinedClass(DerivedClass1, DerivedClass2):
    def __init__(self, name, age, city):
        DerivedClass1.__init__(self, name, age)  
        DerivedClass2.__init__(self, name, city)  

    def greet(self):
        return f"{DerivedClass1.greet(self)} And I live in {self.city}."

combined = CombinedClass("Alice", 30, "New York")
print(combined.greet())  
