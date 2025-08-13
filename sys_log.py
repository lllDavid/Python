def get_cpu_usage():
    cpu_usage = []

    with open('/proc/stat', 'r') as f:
        lines = f.readlines()

    total_cpu = [int(x) for x in lines[0].split()[2:6]]
    cpu_usage.extend(total_cpu)

    for i in range(1, len(lines)):
        line = lines[i].split()
        if len(line) >= 5 and line[0].startswith('cpu'):
            cpu_usage.extend([int(line[1]), int(line[3]), int(line[4])])

        if len(cpu_usage) >= 21:  
            break

    return cpu_usage

def calculate_usage(cpu_usage):
    total_user = cpu_usage[0]
    total_system = cpu_usage[1]
    total_idle = cpu_usage[2]
    total_cpu_usage = (100 * (total_user + total_system)) // (total_user + total_system + total_idle)
    
    print("--- Current CPU Load ---")
    print(f"Total CPU Load: {total_cpu_usage} %")
    
    for i in range(6):
        j = i * 3 + 3
        k = i * 3 + 4
        l = i * 3 + 5
        if j < len(cpu_usage) and k < len(cpu_usage) and l < len(cpu_usage):  
            core_usage = (100 * (cpu_usage[j] + cpu_usage[k])) // (cpu_usage[j] + cpu_usage[k] + cpu_usage[l])
            print(f"Core {i} Load: {core_usage} %")
        else:
            print(f"Core {i} Load: Data unavailable")

if __name__ == "__main__":
    cpu_usage = get_cpu_usage()
    calculate_usage(cpu_usage)