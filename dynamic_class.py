# X = type("X", (), {},)

class_name = 'Person'

bases = (object,)

def init(self, name, age):
    self.name = name
    self.age = age

def greet(self):
    return f"Hello, my name is {self.name} and I am {self.age} years old."

attributes_dict = {
    '__init__': init,
    'greet': greet,
}

NewClass = type(class_name, bases, attributes_dict)

p = NewClass('Adam', 30)
print(p.greet()) 
print(type(p))