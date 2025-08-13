class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = value

    @property
    def area(self):
        return 3.14 * self._radius * self._radius

circle = Circle(5)
print(circle.radius)  
print(circle.area)    

circle.radius = 10    
print(circle.area)


class Square:
    def __init__(self, side_length):
        self._side_length = side_length

    @property
    def area(self):
        return self._side_length ** 2

square = Square(4)
print(square.area)


class Item:
    def __init__(self, name):
        self.name = name

    @property
    def read_only_name(self):
        return "ABC"
    
item = Item("Laptop")
print(item.name)
item.read_only_name = "Phone"