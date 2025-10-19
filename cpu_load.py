#!/usr/bin/env python3

import time
import sys
import multiprocessing
import psutil

TEMP_LIMIT = 80.0  


def work():
    while True:
        _ = 12345 * 54321


def start():
    procs = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=work)
        p.daemon = True
        p.start()
        procs.append(p)
    return procs


def stop(procs):
    for p in procs:
        if p.is_alive():
            p.terminate()
    for p in procs:
        p.join(timeout=1)


if __name__ == "__main__":
    processes = start()

    count = 0
    last_temp_read = 0
    temp_c = 0.0
    sensor_path = "/sys/class/hwmon/hwmon2/temp1_input" 

    psutil.cpu_percent(percpu=True)

    with open(sensor_path, "r") as temp_file:
        while True:
            count += 1

            if time.time() - last_temp_read >= 0.5:
                temp_file.seek(0)
                raw_temp = temp_file.read().strip()
                try:
                    temp_c = int(raw_temp) / 1000.0
                except ValueError:
                    temp_c = 0.0
                last_temp_read = time.time()

                cpu_usages = psutil.cpu_percent(percpu=True)
                total_cpu = psutil.cpu_percent()

                output = [
                    f"Count:           {count}",
                    f"Temperature:     {temp_c:.1f} °C",
                    f"CPU Load Procs:  {len(processes)}",
                    f"CPU Cores:       {multiprocessing.cpu_count()}",
                    f"Total CPU Usage: {total_cpu:.1f} %",
                ]
                for i, usage in enumerate(cpu_usages):
                    output.append(f"  Core {i}: {usage:.1f} %")

                sys.stdout.write("\n".join(output) + f"\n\033[{len(output)}A")
                sys.stdout.flush()

                if temp_c >= TEMP_LIMIT:
                    stop(processes)
                    print(f"\nTemperature limit reached ({temp_c:.1f} °C). Processes stopped.")
                    break

            time.sleep(0.1)