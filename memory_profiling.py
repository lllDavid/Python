import tracemalloc
import time

def allocate_memory():
    lst1 = [i for i in range(1000000)]
    time.sleep(0.5)
    lst2 = [str(i) for i in range(500000)]
    time.sleep(0.5)
    return lst1, lst2

def display_top(snapshot, key_type='lineno', limit=5):
    top_stats = snapshot.statistics(key_type)
    print(f"Top lines by memory usage ({key_type}):")
    for stat in top_stats[:limit]:
        frame = stat.traceback[0]
        print(f"{frame.filename}:{frame.lineno}: {stat.size / 1024:.1f} KiB - {stat.count} blocks")

tracemalloc.start()

print("Starting memory allocation...")
snapshot1 = tracemalloc.take_snapshot()

lst1, lst2 = allocate_memory()

snapshot2 = tracemalloc.take_snapshot()

print("\nMemory usage after allocations:")
display_top(snapshot2, limit=5)

print("\nMemory differences since snapshot1:")
stats_diff = snapshot2.compare_to(snapshot1, 'lineno')
for stat in stats_diff[:5]:
    frame = stat.traceback[0]
    size_diff = stat.size_diff / 1024
    count_diff = stat.count_diff
    print(f"{frame.filename}:{frame.lineno}: {size_diff:+.1f} KiB ({count_diff:+} blocks)")

tracemalloc.stop()