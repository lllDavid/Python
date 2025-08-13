import threading
import time

counter = 0

lock = threading.Lock()

def increment():
    global counter
    with lock:
        current_value = counter
        time.sleep(0.1)  
        counter = current_value + 1
        print(f"Counter incremented to {counter}")

def main():
    threads = []

    for i in range(5):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final counter value: {counter}")

if __name__ == "__main__":
    main()