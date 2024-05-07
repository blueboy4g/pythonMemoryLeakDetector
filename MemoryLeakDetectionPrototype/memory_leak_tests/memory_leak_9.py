cache = {}

def memoized_function(argument):
    if argument not in cache:
        result = argument * 2
        cache[argument] = result
    return cache[argument]

def start_memory_leak_9():
    memoized_function(2)
    print("Example code with a memory leak running...")
