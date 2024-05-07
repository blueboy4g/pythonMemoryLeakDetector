

def memory_leak():
    file = open("example.txt", "r")
    # no file.close() call which makes leak


def start_memory_leak_4():
    print("Example code with a memory leak running...")
    memory_leak()

