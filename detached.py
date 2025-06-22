import sys
import subprocess
import time
from datetime import datetime

LOG_FILE = "background_log.txt"

def run_in_background():
    DETACHED_PROCESS = 0x00000008
    subprocess.Popen([sys.executable] + sys.argv + ['run'], creationflags=DETACHED_PROCESS)

def background_task():
    while True:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()}: Background task alive\n")
        time.sleep(10)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[-1] == 'run':
        background_task()
    else:
        print("Launching background process...")
        run_in_background()
        print("Background process started. Exiting main program.")
