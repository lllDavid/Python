class MyCollection:
    def __init__(self, data):
        self.data = data
        
    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self.data))
            return [self.data[i] for i in range(start, stop, step)]
        elif isinstance(key, int):
            return self.data[key]
        else:
            raise KeyError("Invalid key type")

obj = MyCollection([1, 2, 3, 4, 5])
print(obj[2])      
print(obj[1:4:2]) 

class Calculator:
    def __init__(self, value):
        self.value = value
        
    def __call__(self, *args, **kwargs):
        if args:
            return self.value + sum(args)
        return self.value

calc = Calculator(10)
print(calc(5, 10))  
print(calc())       