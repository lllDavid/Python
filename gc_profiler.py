import gc
import random
import sys
from collections import Counter

def show_gc_objects(limit=10):
    gc.collect()  
    objects = gc.get_objects()
    
    print(f"\nTotal objects tracked by GC: {len(objects)}")
    
    type_counts = Counter(type(obj).__name__ for obj in objects)
    print("\nTop 5 object types tracked by GC:")
    for obj_type, count in type_counts.most_common(5):
        print(f"  {obj_type}: {count}")

    print(f"\nSample of {limit} objects tracked by GC:")
    for obj in objects[:limit]:  
        print(f"  Object: {repr(obj)[:60]}... | Type: {type(obj).__name__} | Size: {sys.getsizeof(obj)} bytes")

def create_garbage():
    print("\nCreating some garbage objects...")
    garbage_objects = [random.sample(range(1, 1000), 50) for _ in range(5)]
    print(f"Created {len(garbage_objects)} objects.")

    show_gc_objects()

if __name__ == "__main__":
    show_gc_objects()
    create_garbage()
    print("\nRunning garbage collection again...")
    gc.collect()
    show_gc_objects()