import time

def compute_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

def benchmark_wall_clock():
    n = 10_000_000
    start = time.time()
    compute_sum(n)
    end = time.time()
    print(f"Wall clock time: {end - start:.4f} seconds")

def benchmark_perf_counter():
    n = 10_000_000
    start = time.perf_counter()
    compute_sum(n)
    end = time.perf_counter()
    print(f"High-resolution time (perf_counter): {end - start:.4f} seconds")

def benchmark_cpu_time():
    n = 10_000_000
    start = time.process_time()
    compute_sum(n)
    end = time.process_time()
    print(f"CPU time (process_time): {end - start:.4f} seconds")

benchmark_wall_clock()
benchmark_perf_counter()
benchmark_cpu_time()
