# Descriptor that enforces a minimum value constraint on an attribute
class Descriptor:
    def __init__(self, name, min_value=0):
        self.name = name
        self.min_value = min_value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        if self.name in instance.__dict__:
            del instance.__dict__[self.name]

class Class:
    attr = Descriptor('attr', min_value=5)
'''
o = Class()
o.attr = 10 # Valid
print(o.attr)
o.attr = 3 # Error
print(o.attr)
'''


# Descriptor that enforces a certain expected type
class ImmutableTyped:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if self.name in instance.__dict__:
            raise AttributeError(f"{self.name} is immutable and already set")
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be of type {self.expected_type.__name__}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"{self.name} is immutable and cannot be deleted")

class Person:
    ssn = ImmutableTyped('ssn', str)  

p = Person()
p.ssn = "123-45-6789" # Valid
print(p.ssn)

p = Person()
p.ssn = 123456789  #TypeError: ssn must be of type str
print(p.ssn)

p = Person()
p.ssn = "123-45-6789"
p.ssn = "987-65-4321"  #AttributeError: ssn is immutable and already set
print(p.ssn)

p = Person()
del p.ssn  #AttributeError: ssn is immutable and cannot be deleted
print(p.ssn) 