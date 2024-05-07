import time

def generate_infinite_sequence():
    i = 0
    while True:
        yield i
        i += 1


def start_memory_leak_7():
    generate_infinite_sequence()
    print("Example code with a memory leak running...")

