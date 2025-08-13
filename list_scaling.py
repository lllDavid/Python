import random
import sys
import time

def test_memory_for_list(size):
    start_time = time.time()
    
    my_list = [random.randint(1, 100) for _ in range(size)]
    
    list_size = sys.getsizeof(my_list)  
    total_size = list_size + sum(sys.getsizeof(item) for item in my_list)  
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print(f"\nTime to create the list of size {size}: {elapsed_time:.6f} seconds")
    print(f"List size in memory (list object itself): {list_size} bytes")
    print(f"Total size (list + items): {total_size} bytes")
    print(f"Total size (in MB): {total_size / (1024 * 1024):.2f} MB")

sizes = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
for size in sizes:
    test_memory_for_list(size)