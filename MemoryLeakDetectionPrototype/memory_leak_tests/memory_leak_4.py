
# This code opens a file but forgets to close it, leading to a file handle leak.

def memory_leak():
    file = open("example.txt", "r")
    # File operations here, but no file.close() call


def start_memory_leak_4():
    print("Example code with a memory leak running...")
    memory_leak()

