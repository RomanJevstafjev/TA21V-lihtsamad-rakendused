import psutil

memory_total_count: int = 0
memory_free_count: int = 0

for disk in psutil.disk_partitions():
    if disk.fstype:
        memory_total_count += psutil.disk_usage(disk.mountpoint).total  / (2**30)
        memory_free_count  += psutil.disk_usage(disk.mountpoint).free  / (2**30)

print(f"Total: {memory_total_count} GB | Free: {memory_free_count} GB")