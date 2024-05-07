import time


# This code defines a generator that produces an infinite sequence, but it's not consumed completely, leading to memory leaks.

def generate_infinite_sequence():
    i = 0
    while True:
        yield i
        i += 1

# If the generator is not consumed completely, it holds references to objects that are never released from memory.


def start_memory_leak_7():
    generate_infinite_sequence()
    print("Example code with a memory leak running...")

