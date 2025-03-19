import gc
import random

def show_gc_objects():
    gc.collect()  
    objects = gc.get_objects()  

    print(f"Total objects tracked by GC: {len(objects)}\n")

    print(f"Some objects tracked by the GC (showing first 10):")
    for obj in objects[:10]:  
        print(f"Object: {obj}, Type: {type(obj)}")

def create_garbage():
    print("Creating some objects...")
    garbage_objects = [random.sample(range(1, 1000), 50) for _ in range(5)]
    print(f"Created {len(garbage_objects)} objects.")
    
    show_gc_objects()

create_garbage()
