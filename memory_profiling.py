import tracemalloc

tracemalloc.start()

lst = [i for i in range(1000000)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("Top 10 lines with the most memory usage:")
for stat in top_stats[:10]:
    print(stat)
