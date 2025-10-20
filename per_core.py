#!/usr/bin/env python3
import psutil
import time

def get_per_core_details():
    cpu_percentages = psutil.cpu_percent(interval=0.5, percpu=True)
    processes = list(psutil.process_iter(['pid', 'cpu_num', 'cpu_percent', 'num_threads']))
    
    cores_info = {}
    for i, cpu in enumerate(cpu_percentages):
        cores_info[i] = {'cpu_usage': cpu, 'processes': 0, 'threads': 0}

    for proc in processes:
        try:
            core = proc.info['cpu_num']
            if core is not None and core in cores_info:
                cores_info[core]['processes'] += 1
                cores_info[core]['threads'] += proc.info['num_threads']
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return cores_info

def display_in_place():
    while True:
        cores_info = get_per_core_details()
        output_lines = []
        for core, info in cores_info.items():
            line = f"Core {core}: CPU {info['cpu_usage']:.1f}% | Procs {info['processes']} | Threads {info['threads']}"
            output_lines.append(line)
        print(" | ".join(output_lines), end="\r", flush=True)
        time.sleep(1)

if __name__ == "__main__":
    display_in_place()
