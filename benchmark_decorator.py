from statistics import mean
from time import perf_counter

# Measure and print the average execution time of a function over a given number of repetitions
def time_function(repetitions=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            execution_times = []
            for _ in range(repetitions):
                start_time = perf_counter()
                func(*args, **kwargs)
                end_time = perf_counter()
                execution_times.append(end_time - start_time)
            avg_time = mean(execution_times)
            print(f"Avg. execution time over {repetitions} repetitions: {avg_time} seconds")
            return avg_time 
        return wrapper
    return decorator


# Example
@time_function(repetitions=10)
def example_function():
    sum(range(1000000))

example_function()