import gc
import weakref

class Sample:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print(f"Object {self.name} is being garbage collected")

gc.disable()

obj = Sample("A")

weak_obj = weakref.ref(obj)

print("Before deleting obj:")
print("Weak reference exists:", weak_obj() is not None)

del obj

print("After deleting obj:")
print("Weak reference exists:", weak_obj() is not None)

gc.collect()

print("After garbage collection:")
print("Weak reference exists:", weak_obj() is not None)