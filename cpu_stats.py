from psutil import cpu_percent, cpu_freq

cpu_usage = cpu_percent(interval=1, percpu=True)
for core, value in enumerate(cpu_usage):
    print(f"Core: {core}, Usage: {value} %")

cpu_freq = cpu_freq()
print(f"\nCPU Frequency: {cpu_freq.current} MHz (Current), {cpu_freq.min} MHz (Min), {cpu_freq.max} MHz (Max)")