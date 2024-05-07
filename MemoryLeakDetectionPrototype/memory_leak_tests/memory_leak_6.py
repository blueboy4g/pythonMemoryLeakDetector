
# This code caches objects in a dictionary indefinitely, leading to memory consumption growth over time.

cache = {}

def add_to_cache(key, value):
    cache[key] = value

# In a long-running application, if objects are continuously added to the cache without ever being removed, it can lead to memory leaks.

def start_memory_leak_6():
    add_to_cache(1, 2)
    print("Example code with a memory leak running...")

