from io import StringIO
from line_profiler import LineProfiler


def save_profiling_result(profile_type, func_name, stats_str):
    print(f"Saving {profile_type} profile for {func_name}:\n{stats_str}")
    return {"type": profile_type, "function": func_name, "stats": stats_str}

# Profiles a function’s execution using LineProfiler and saves the profiling results labeled by type.
def profile_function(profile_type="unoptimized"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            profiler = LineProfiler()
            profiler.add_function(func)
            result = profiler(func)(*args, **kwargs)

            stats_stream = StringIO()
            profiler.print_stats(stream=stats_stream)
            stats_str = stats_stream.getvalue()

            result_dict = save_profiling_result(profile_type, func.__name__, stats_str)

            return result, result_dict

        return wrapper
    return decorator


# Example unoptimized function
@profile_function(profile_type="unoptimized")
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Example optimized function
@profile_function(profile_type="optimized")
def fast_sum(n):
    return n * (n - 1) // 2

slow_sum(100000)
fast_sum(100000)