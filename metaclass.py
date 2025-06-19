import time

class ExampleMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if 'required_attr' not in attrs:
            raise AttributeError(f"{name} must have 'required_attr'")
        attrs['created_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

        for k, v in attrs.items():
            if callable(v) and k.startswith('process_'):
                attrs[k] = cls.wrap(v)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def wrap(f):
        def wrapped(*args, **kwargs):
            print(f"Calling {f.__name__}")
            result = f(*args, **kwargs)
            print(f"{f.__name__} returned {result}")
            return result
        return wrapped


class MyClass(metaclass=ExampleMetaClass):
    required_attr = True

    def process_task(self, x):
        return x * 2

obj = MyClass()
print(obj.created_at)
obj.process_task(5)
