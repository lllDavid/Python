import psutil
import os
import time

def get_process_info():
    """Retrieve information about all running processes."""
    process_info = []
    
    for proc in psutil.process_iter(['pid', 'name', 'status', 'memory_info', 'cpu_times']):
        try:
            proc_info = {
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'status': proc.info['status'],
                'memory_rss': proc.info['memory_info'].rss,  
                'memory_vms': proc.info['memory_info'].vms,  
                'cpu_user_time': proc.info['cpu_times'].user,  
                'cpu_system_time': proc.info['cpu_times'].system 
            }
            process_info.append(proc_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return process_info

def print_process_info(process_info):
    """Print process information in a readable format."""
    print(f"{'PID':<10}{'Name':<30}{'Status':<15}{'RSS Memory':<15}{'VMS Memory':<15}{'CPU Time (User)':<20}{'CPU Time (System)'}")
    print("="*105)
    
    for proc in process_info:
        print(f"{proc['pid']:<10}{proc['name']:<30}{proc['status']:<15}{proc['memory_rss']:<15}{proc['memory_vms']:<15}{proc['cpu_user_time']:<20}{proc['cpu_system_time']}")
    
def main():
    """Main function to retrieve and display process information."""
    while True:
        print("Gathering process information...\n")
        process_info = get_process_info()
        print_process_info(process_info)
        print("\n" + "="*80 + "\n")
        time.sleep(5)  

if __name__ == '__main__':
    main()

