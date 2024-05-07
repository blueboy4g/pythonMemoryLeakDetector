import time


# This code creates global variables that reference large objects, preventing them from being garbage collected.

large_object = [0] * 1000000  # Large list
# Large_object is a global variable, preventing it from being garbage collected even if it's no longer needed.


def start_memory_leak_5():
    print("Example code with a memory leak running...")

