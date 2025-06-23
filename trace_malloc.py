import tracemalloc

tracemalloc.start()

snapshot_before = tracemalloc.take_snapshot()

def example_function():
    a = [i for i in range(10000)]  
    b = [i * 2 for i in range(5000)]
    return a, b

example_function()

snapshot_after = tracemalloc.take_snapshot()

current, peak = tracemalloc.get_traced_memory()

print(f"Current memory usage: {current / 10**6} MB")
print(f"Peak memory usage: {peak / 10**6} MB")

stats = snapshot_after.compare_to(snapshot_before, 'lineno')

print("\nTop 5 memory usage differences:")
for stat in stats[:5]:
    print(stat)

tracemalloc.stop()