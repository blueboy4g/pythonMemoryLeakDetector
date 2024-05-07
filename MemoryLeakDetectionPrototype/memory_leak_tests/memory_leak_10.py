# This code simulates a memory leak by continuously appending data to a list without releasing memory.

import time

def simulate_memory_leak():
    data = []
    while True:
        # Add a large amount of data to the list
        data.extend([0] * 1000)  # Adding 100,000 elements to the list
        # Pause for a short duration to simulate intermittent memory usage
        time.sleep(1)


def start_memory_leak_10():
    simulate_memory_leak()
    #print("Example code with a memory leak running...")
