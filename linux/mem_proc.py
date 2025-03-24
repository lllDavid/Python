import psutil
import time
import logging
import os

log_file = "sys_stats.log"
if os.path.exists(log_file):
    os.remove(log_file)

logging.basicConfig(filename=log_file, level=logging.INFO)

def log():
    logging.info(f"CPU Usage: {psutil.cpu_percent()}%")
    logging.info(f"Memory Usage: {psutil.virtual_memory().percent}%")
    logging.info(f"Swap Memory Usage: {psutil.swap_memory().percent}%")
    
    uptime = time.time() - psutil.boot_time()
    logging.info(f"System Uptime: {time.strftime('%H:%M:%S', time.gmtime(uptime))}")

    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            disk_usage = psutil.disk_usage(partition.mountpoint)
            logging.info(f"Disk Usage ({partition.device}): {disk_usage.percent}%")
        except PermissionError:
            continue

    net_io = psutil.net_io_counters()
    logging.info(f"Bytes Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
    logging.info(f"Bytes Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB")
    
    try:
        cpu_temp = psutil.sensors_temperatures()
        if 'coretemp' in cpu_temp:
            for entry in cpu_temp['coretemp']:
                logging.info(f"CPU Temperature ({entry.label}): {entry.current}°C")
    except AttributeError:
        logging.info("CPU Temperature: Not Supported")

def display():
    while True:
        try:
            print(f"CPU Usage: {psutil.cpu_percent()}%")
            print(f"Memory Usage: {psutil.virtual_memory().percent}%")
            print(f"Swap Memory Usage: {psutil.swap_memory().percent}%")
            
            uptime = time.time() - psutil.boot_time()
            print(f"System Uptime: {time.strftime('%H:%M:%S', time.gmtime(uptime))}")
            
            partitions = psutil.disk_partitions()
            for partition in partitions:
                try:
                    disk_usage = psutil.disk_usage(partition.mountpoint)
                    print(f"Disk Usage ({partition.device}): {disk_usage.percent}%")
                except PermissionError:
                    continue

            net_io = psutil.net_io_counters()
            print(f"Bytes Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
            print(f"Bytes Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB")

            try:
                cpu_temp = psutil.sensors_temperatures()
                if 'coretemp' in cpu_temp:
                    for entry in cpu_temp['coretemp']:
                        print(f"CPU Temperature ({entry.label}): {entry.current}°C")
            except AttributeError:
                print("CPU Temperature: Not Supported")

            print("\n" + "-"*50 + "\n")

            log()

            time.sleep(2)
        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
            break

display()
