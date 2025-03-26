import gc
import random
import sys
from collections import Counter

def show_gc_objects(limit=10):
    """Displays summary and sample of objects tracked by GC."""
    gc.collect()  
    objects = gc.get_objects()
    
    print(f"\n[INFO] Total objects tracked by GC: {len(objects)}")
    
    type_counts = Counter(type(obj).__name__ for obj in objects)
    print("\n[INFO] Top 5 object types tracked by GC:")
    for obj_type, count in type_counts.most_common(5):
        print(f"  {obj_type}: {count}")

    print(f"\n[INFO] Sample of {limit} objects tracked by GC:")
    for obj in objects[:limit]:  
        print(f"  Object: {repr(obj)[:60]}... | Type: {type(obj).__name__} | Size: {sys.getsizeof(obj)} bytes")

def create_garbage():
    """Creates objects to increase GC load and inspects GC behavior."""
    print("\n[INFO] Creating some garbage objects...")
    garbage_objects = [random.sample(range(1, 1000), 50) for _ in range(5)]
    print(f"[INFO] Created {len(garbage_objects)} objects.")

    show_gc_objects()

if __name__ == "__main__":
    show_gc_objects()
    create_garbage()
    print("\n[INFO] Running garbage collection again...")
    gc.collect()
    show_gc_objects()
