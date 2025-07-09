import gc
import sys

class LargeObject:
    def __init__(self, size):
        self.data = [0] * size  

    def __del__(self):
        print(f"LargeObject of size {len(self.data)} is being deleted.")

def memory_management_example():
    obj = LargeObject(10**7)  
    print(f"Created a large object, size: {sys.getsizeof(obj)} bytes")

    total_size = sys.getsizeof(obj) + sys.getsizeof(obj.data)
    print(f"Total memory used by the object and its data: {total_size} bytes")

    print(f"Before collection, memory used by obj: {total_size} bytes")

    del obj
    print("Object deleted.")

    gc.collect()

    print("After collection, manually collected unused objects.")

if __name__ == "__main__":
    memory_management_example()