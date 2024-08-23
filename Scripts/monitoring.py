import psutil
import tkinter as tk

def update_metrics():
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
    
    cpu_label.config(text=f"CPU Usage: {cpu_usage:.2f}%")
    memory_label.config(text=f"Memory Usage: {memory_usage:.2f}%")
    network_label.config(text=f"Network Sent: {bytes_sent / (1024 ** 2):.2f} MB, Received: {bytes_recv / (1024 ** 2):.2f} MB")
    disk_label.config(text=f"Disk Usage: {disk_usage:.2f}%")
    battery_label.config(text=f"Battery: {battery_percent}%")
    process_label.config(text=f"Processes: {processes}")

    root.after(1000, update_metrics)

root = tk.Tk()
root.title("Performance Monitor")

cpu_label = tk.Label(root, text="CPU Usage: 0.00%", font=("Arial", 12))
cpu_label.pack(pady=5)

memory_label = tk.Label(root, text="Memory Usage: 0.00%", font=("Arial", 12))
memory_label.pack(pady=5)

network_label = tk.Label(root, text="Network Stats: Sent: 0.00 MB, Received: 0.00 MB", font=("Arial", 12))
network_label.pack(pady=5)

disk_label = tk.Label(root, text="Disk Usage: 0.00%", font=("Arial", 12))
disk_label.pack(pady=5)

battery_label = tk.Label(root, text="Battery: N/A", font=("Arial", 12))
battery_label.pack(pady=5)

process_label = tk.Label(root, text="Processes: 0", font=("Arial", 12))
process_label.pack(pady=5)

update_metrics()

root.mainloop()
