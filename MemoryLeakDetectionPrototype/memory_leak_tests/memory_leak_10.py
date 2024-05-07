import time

class Node:
    def __init__(self):
        self.next = None

node1 = Node()
node2 = Node()
node1.next = node2
node2.next = node1  # circular reference


def start_memory_leak_10():
    print("Example code with a memory leak running...")
    Node()

