import time


# This code creates an infinite loop and appends items to a list, but the list keeps growing without ever being cleared.

# This code creates circular references between objects, preventing them from being garbage collected.

class Node:
    def __init__(self):
        self.next = None

node1 = Node()
node2 = Node()
node1.next = node2
node2.next = node1  # Circular reference

# node1 and node2 now reference each other, preventing them from being garbage collected.


def start_memory_leak_3():
    print("Example code with a memory leak running...")
    Node()

