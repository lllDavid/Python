import threading
import time

def background_task():
    while True:
        print("Daemon thread running...")
        time.sleep(2)

daemon_thread = threading.Thread(target=background_task, daemon=True)

daemon_thread.start()

print("Main program will sleep for 5 seconds.")
time.sleep(5)
print("Main program is exiting now. Daemon thread will also exit.")
