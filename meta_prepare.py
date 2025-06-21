class Meta(type):
    @staticmethod
    def __prepare__(name, bases, **kwargs):
        print(f"Preparing class namespace for {name}")
        from collections import OrderedDict
        return OrderedDict()

    def __new__(cls, name, bases, namespace, **kwargs):
        print(f"Creating class {name} with namespace keys: {list(namespace.keys())}")
        return super().__new__(cls, name, bases, dict(namespace))

class MyClass(metaclass=Meta):
    x = 10
    y = 20

print(MyClass.x, MyClass.y)
