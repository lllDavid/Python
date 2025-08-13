import psutil
import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_bytes(bytes_value):
    return f"{bytes_value / (1024 ** 2):.2f} MB"

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    network_info = psutil.net_io_counters()
    disk_info = psutil.disk_usage('/')
    battery_info = psutil.sensors_battery()
    processes = len(psutil.pids())
    
    memory_usage = memory_info.percent
    bytes_sent = network_info.bytes_sent
    bytes_recv = network_info.bytes_recv
    disk_usage = disk_info.percent
    battery_percent = battery_info.percent if battery_info else "N/A"

    clear_terminal()
    print(f"CPU Usage: {cpu_usage:.2f}%")
    print(f"Memory Usage: {memory_usage:.2f}%")
    print(f"Network Sent: {format_bytes(bytes_sent)}, Received: {format_bytes(bytes_recv)}")
    print(f"Disk Usage: {disk_usage:.2f}%")
    print(f"Battery: {battery_percent}%")
    print(f"Processes: {processes}")

    time.sleep(1)