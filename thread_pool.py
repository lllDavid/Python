from time import sleep, time
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_data(x):
    print(f"[{time():.2f}] Fetching {x}")
    sleep(1)
    return f"Data {x}"

numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(fetch_data, n): n for n in numbers}

    for future in as_completed(futures):
        try:
            result = future.result()
            print(f"[{time():.2f}] Result: {result}")
        except Exception as e:
            print(f"Error fetching data {futures[future]}: {e}")