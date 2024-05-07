import time

from memory_profiler import profile


class MyExampleClass:
    def __init__(self):
        self.data = [1] * (10 ** 6)

    def process_data(self):
        result = sum(self.data)
        return result

def my_example_function():
    obj = MyExampleClass()
    result = obj.process_data()
    #obj = None

def example_memory_leak():
    my_example_function()
    time.sleep(1)
    example_memory_leak()

def start_memory_leak_1():
    print("Example code with a memory leak running...")
    example_memory_leak()

