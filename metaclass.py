# Define a metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Automatically add a custom init method to the class
        if 'initialize' not in dct:
            def initialize(self):
                print(f"Initializing {self.__class__.__name__}")
            dct['initialize'] = initialize
        return super().__new__(cls, name, bases, dct)

# Define a class using this metaclass
class MyClass(metaclass=MyMeta):
    pass

# Create an instance and call the initialize method
obj = MyClass()
obj.initialize()  # This will print: Initializing MyClass
