import psutil

total_disks_memory = 0
used_disks_memory = 0

for disk in psutil.disk_partitions():
    if disk.fstype:
        total_disks_memory += psutil.disk_usage(disk.mountpoint).total
        used_disks_memory  += psutil.disk_usage(disk.mountpoint).used

disks_memory_available_percentage = used_disks_memory / total_disks_memory * 100
ram_memory_available_percentage = psutil.virtual_memory().percent

if (disks_memory_available_percentage > 20 or ram_memory_available_percentage > 20):
    print("RAM or storage takes up more than 20%")
    print(f"Disks | Filled {disks_memory_available_percentage}%")
    print(f"RAM | Filled {ram_memory_available_percentage}%")