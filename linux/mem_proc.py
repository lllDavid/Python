import time

def get_cpu_stats():
    with open('/proc/stat', 'r') as file:
        stats = file.readlines()

    cpu_stats = {}
    for line in stats:
        if line.startswith('cpu '):
            cpu_info = line.split()
            cpu_stats['user'] = int(cpu_info[1])
            cpu_stats['nice'] = int(cpu_info[2])
            cpu_stats['system'] = int(cpu_info[3])
            cpu_stats['idle'] = int(cpu_info[4])
            cpu_stats['iowait'] = int(cpu_info[5])
            cpu_stats['irq'] = int(cpu_info[6])
            cpu_stats['softirq'] = int(cpu_info[7])
            cpu_stats['steal'] = int(cpu_info[8])
            cpu_stats['guest'] = int(cpu_info[9])
            cpu_stats['guest_nice'] = int(cpu_info[10])
    return cpu_stats

def get_system_uptime():
    with open('/proc/uptime', 'r') as file:
        uptime = file.readline().split()
    return float(uptime[0])

def calculate_cpu_usage(prev_cpu_stats, curr_cpu_stats):
    prev_total = sum(prev_cpu_stats.values())
    curr_total = sum(curr_cpu_stats.values())

    prev_idle = prev_cpu_stats['idle'] + prev_cpu_stats['iowait']
    curr_idle = curr_cpu_stats['idle'] + curr_cpu_stats['iowait']

    total_diff = curr_total - prev_total
    idle_diff = curr_idle - prev_idle

    if total_diff == 0:
        return 0.0

    cpu_usage = 100.0 * (1.0 - (idle_diff / total_diff))
    return cpu_usage

def display_stats():
    prev_cpu_stats = get_cpu_stats()
    prev_uptime = get_system_uptime()

    time.sleep(1)

    curr_cpu_stats = get_cpu_stats()
    curr_uptime = get_system_uptime()

    cpu_usage = calculate_cpu_usage(prev_cpu_stats, curr_cpu_stats)
    
    print(f"CPU Usage: {cpu_usage:.2f}%")
    print(f"System Uptime: {curr_uptime - prev_uptime:.2f} seconds")

if __name__ == "__main__":
    display_stats()
