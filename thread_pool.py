from concurrent.futures import ThreadPoolExecutor
import time

def fetch_data(x):
    print(f"Fetching {x}")
    time.sleep(1)
    return f"Data {x}"

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(fetch_data, [1, 2, 3, 4, 5])

for res in results:
    print(res)
