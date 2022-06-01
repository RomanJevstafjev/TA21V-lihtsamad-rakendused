import psutil

ram_free_count = psutil.virtual_memory().available / (2**30)

disks_free_memory = 0

for disk in psutil.disk_partitions():
    if disk.fstype:
        disks_free_memory += psutil.disk_usage(disk.mountpoint).free  / (2**30)

with open("4_task_logs.txt", "a") as file:
    file.write(f"Ram free count: {ram_free_count} | Disks free memory: {disks_free_memory}\n")