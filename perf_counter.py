import time

start_time = time.time()
print([i for i in range(10000) if i > 9998])
end_time = time.time()
print(f"Time taken (time.time()): {end_time - start_time} seconds")

start_perf_counter = time.perf_counter()
print([i for i in range(10000) if i > 9998])
end_perf_counter = time.perf_counter()
print(f"Time taken (perf_counter): {end_perf_counter - start_perf_counter} seconds")


import time

def task():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

start_time = time.perf_counter()

result = task()

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"Result of the task: {result}")
print(f"Time taken: {elapsed_time:.6f} seconds")
