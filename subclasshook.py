from abc import ABC, abstractmethod

class Shape(ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        if hasattr(subclass, 'area') and callable(subclass.area):
            return True
        return NotImplemented

    @abstractmethod
    def area(self):
        pass

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class NotAShape:
    pass

print(issubclass(Circle, Shape))      
print(issubclass(Rectangle, Shape))   
print(issubclass(NotAShape, Shape))  