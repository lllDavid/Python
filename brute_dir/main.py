import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

found_dirs = []
lock = Lock()

def check_directory(target, dir):
    if not target.startswith('http://'):
        target = 'http://' + target
    
    url = f"{target.rstrip('/')}/{dir}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Found directory: {url} (Status: 200 OK)")
            with lock:
                found_dirs.append(url)
        elif response.status_code == 301:
            print(f"Found directory (Redirected): {url} (Status: 301 Moved Permanently)")
            with lock:
                found_dirs.append(url)
        elif response.status_code == 302:
            print(f"Found directory (Redirected): {url} (Status: 302 Found)")
            with lock:
                found_dirs.append(url)
        elif response.status_code == 403:
            print(f"Forbidden access to directory: {url} (Status: 403 Forbidden)")
            with lock:
                found_dirs.append(url)
        elif response.status_code == 404:
            print(f"Directory not found: {url} (Status: 404 Not Found)")
        else:
            print(f"URL: {url} returned status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error with URL {url}: {e}")

def brute_dir(target, wordlist):
    with open(wordlist, 'r') as file:
        dirs = [line.strip() for line in file if line.strip()]

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_directory, target, dir) for dir in dirs]
        for _ in as_completed(futures):
            pass  

    print("\nSummary: Found directories:")
    for url in found_dirs:
        print(url)

target = ""
wordlist = ""

brute_dir(target, wordlist)
