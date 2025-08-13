import threading
import time
import random

lock = threading.Lock()

shared_data = []

def print_numbers():
    for i in range(5):
        time.sleep(random.uniform(0.5, 1.5))  
        with lock:  
            shared_data.append(f"Number: {i}")
            print(f"Number Thread: {i}")

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(random.uniform(1, 2))  
        with lock:  
            shared_data.append(f"Letter: {letter}")
            print(f"Letter Thread: {letter}")

def thread_with_exception_handling(target_func, *args):
    try:
        target_func(*args)
    except Exception as e:
        print(f"Error in thread: {e}")

thread1 = threading.Thread(target=thread_with_exception_handling, args=(print_numbers,))
thread2 = threading.Thread(target=thread_with_exception_handling, args=(print_letters,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("\nBoth threads are done!")
print("Shared Data:")
with lock:
    for item in shared_data:
        print(item)

def print_with_timeout():
    try:
        thread1.join(timeout=5)  
        thread2.join(timeout=5) 
    except Exception as e:
        print(f"Error: {e}")

print_with_timeout()