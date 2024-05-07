import time

def simulate_memory_leak():
    data = []
    while True:
        data.extend([0] * 1000)
        time.sleep(1)


def start_memory_leak_3():
    print("Example code with a memory leak running...")
    simulate_memory_leak()

