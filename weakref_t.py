import weakref

class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Object {self.name} is being deleted.")

def callback(ref):
    print(f"Callback: {ref} is no longer accessible.")

obj = MyClass('Object 2')

weak_ref = weakref.ref(obj, callback)

print(weak_ref()) 

del obj  

print(weak_ref())  
