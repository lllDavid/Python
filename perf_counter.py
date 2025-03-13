import time

start_time = time.time()
print([i for i in range(10000) if i > 9998])
end_time = time.time()
print(f"Time taken (time.time()): {end_time - start_time} seconds")

start_perf_counter = time.perf_counter()
print([i for i in range(10000) if i > 9998])
end_perf_counter = time.perf_counter()
print(f"Time taken (perf_counter): {end_perf_counter - start_perf_counter} seconds")
