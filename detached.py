import sys
import subprocess
import time
from datetime import datetime
import os

LOG_FILE = "background_log.txt"

def run_in_background():
    DETACHED_PROCESS = 0x00000008
    process = subprocess.Popen(
        [sys.executable] + sys.argv + ['run'],
        creationflags=DETACHED_PROCESS
    )
    pid_msg = f"Background process started with PID {process.pid}"
    kill_msg = f"To kill: taskkill /PID {process.pid} /F"

    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()}: {pid_msg}\n")

    print(pid_msg)
    print(kill_msg)

def background_task():
    pid = os.getpid()
    while True:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()}: Background task alive (PID {pid})\n")
        time.sleep(10)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[-1] == 'run':
        background_task()
    else:
        print("Launching background process...")
        run_in_background()
