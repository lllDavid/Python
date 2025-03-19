class MyMeta(type):
    def __new__(cls, name, bases, dct):
        if 'initialize' not in dct:
            def initialize(self):
                print(f"Initializing {self.__class__.__name__}")
            dct['initialize'] = initialize
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()
obj.initialize()  
