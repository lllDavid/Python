import psutil
import time

def view_memory():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()

    print(f"--- System Memory ---")
    print(f"Total memory: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Available memory: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Used memory: {memory.used / (1024 ** 3):.2f} GB")
    print(f"Memory usage: {memory.percent}%")
    
    print(f"\n--- Swap Memory ---")
    print(f"Total swap: {swap.total / (1024 ** 3):.2f} GB")
    print(f"Used swap: {swap.used / (1024 ** 3):.2f} GB")
    print(f"Free swap: {swap.free / (1024 ** 3):.2f} GB")
    print(f"Swap usage: {swap.percent}%")

def real_time_monitoring(interval=5, duration=30):
    print(f"Starting real-time memory monitoring for {duration} seconds...\n")
    start_time = time.time()

    while time.time() - start_time < duration:
        view_memory()
        print("-" * 40)
        time.sleep(interval)

if __name__ == "__main__":
    real_time_monitoring()
    
