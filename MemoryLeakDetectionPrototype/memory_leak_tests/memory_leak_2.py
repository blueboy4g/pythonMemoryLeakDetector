import time


# This code creates an infinite loop and appends items to a list, but the list keeps growing without ever being cleared.

def memory_leak():
    my_list = []
    while True:
        my_list.append("data")
        time.sleep(.1)


def start_memory_leak_2():
    print("Example code with a memory leak running...")
    memory_leak()

