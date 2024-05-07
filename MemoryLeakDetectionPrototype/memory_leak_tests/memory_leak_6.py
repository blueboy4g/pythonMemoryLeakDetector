
cache = {}

def add_to_cache(key, value):
    cache[key] = value

def start_memory_leak_6():
    add_to_cache(1, 2)
    print("Example code with a memory leak running...")

