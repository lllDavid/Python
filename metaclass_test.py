class UppercaseClassNameMeta(type):
    def __new__(cls, name, bases, dct):
        if not name.isupper():
            raise ValueError(f"Class name '{name}' must be uppercase")
        return super().__new__(cls, name, bases, dct)

class VALIDCLASS(metaclass=UppercaseClassNameMeta):
    pass

class InstanceCounterMeta(type):
    def __new__(cls, name, bases, dct):
        dct['_instance_count'] = 0
        
        original_init = dct.get('__init__', lambda self: None)
        
        def new_init(self, *args, **kwargs):
            self.__class__._instance_count += 1  
            original_init(self, *args, **kwargs)
        
        dct['__init__'] = new_init
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=InstanceCounterMeta):
    def __init__(self, name):
        self.name = name

obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

print(MyClass._instance_count)  
 
