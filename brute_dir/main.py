import requests
from concurrent.futures import ThreadPoolExecutor

def check_directory(target, dir):
    if not target.startswith('http://'):
        target = 'http://' + target
    
    url = f"{target.rstrip('/')}/{dir}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Found directory: {url} (Status: 200 OK)")
        elif response.status_code == 301:
            print(f"Found directory (Redirected): {url} (Status: 301 Moved Permanently)")
        elif response.status_code == 302:
            print(f"Found directory (Redirected): {url} (Status: 302 Found)")
        elif response.status_code == 403:
            print(f"Forbidden access to directory: {url} (Status: 403 Forbidden)")
        elif response.status_code == 404:
            print(f"Directory not found: {url} (Status: 404 Not Found)")
        else:
            print(f"URL: {url} returned status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error with URL {url}: {e}")

def brute_dir(target, wordlist):
    with open(wordlist, 'r') as file:
        dirs = file.readlines()

    with ThreadPoolExecutor(max_workers=100) as executor:  
        for dir in dirs:
            dir = dir.strip()
            executor.submit(check_directory, target, dir)

target = ""
wordlist = ""

brute_dir(target, wordlist)
