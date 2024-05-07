import threading

from MemoryLeakDetectionPrototype.adapters.objgraph_adapter import monitor_objects
from MemoryLeakDetectionPrototype.adapters.tracemalloc_adapter import monitor_memory
from MemoryLeakDetectionPrototype.config.memory_leak_config import Memory_Leak_Config


def start_tracemalloc():
    sec = Memory_Leak_Config.get_memory_leak_delay()
    memory_size = Memory_Leak_Config.get_memory_threshold()
    trigger_thresh = Memory_Leak_Config.get_trigger_threshold()
    monitor_memory(interval_seconds=sec, duration_seconds=10000, trigger_thresh=trigger_thresh, memory_size=memory_size)

def start_objgraph():
    sec = Memory_Leak_Config.get_memory_leak_delay()
    additional_logs = Memory_Leak_Config.get_additional_details()
    if additional_logs == 1:
        monitor_objects(interval_seconds=sec, duration_seconds=10000)

def analyze():
    tracemalloc_thread = threading.Thread(target=start_tracemalloc)
    objgraph_thread = threading.Thread(target=start_objgraph)
    tracemalloc_thread.start()
    objgraph_thread.start()
