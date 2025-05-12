import concurrent.futures
import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    numbers = [30, 32, 34, 36, 38]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(fibonacci, numbers)

        for num, result in zip(numbers, results):
            print(f"Fibonacci({num}) = {result}")

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print(f"Execution time: {time.perf_counter() - start_time} seconds")
