import psutil

memory = psutil.virtual_memory()

memory_total_count = memory.total / (2**30)
memory_available_count = memory.available / (2**30)

print(f"Total: {memory_total_count} GB | Available: {memory_available_count} GB")