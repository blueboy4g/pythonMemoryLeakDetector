import tracemalloc
import time
from collections import defaultdict

potential_leaks = defaultdict(int)
suspected_leaks = defaultdict(int)
potential_leaks = []

def start_memory_tracking():
    tracemalloc.start()

def take_snapshot():
    return tracemalloc.take_snapshot()


def already_in_list(stat, potential_leaks):
    for item in potential_leaks:
        # print(item["stat"])
        # print(stat)
        if item["stat"] == stat:
            #print("ON LIST")
            return True
    return False


def analyze_snapshots(old_snapshot, new_snapshot, trigger_thresh, memory_size):

    top_stats = new_snapshot.compare_to(old_snapshot, 'lineno')
    print("Potential Memory Leak Report:")
    purge_list = []
    for stat in top_stats[:50]:
        purge_list.append(stat.traceback)
        if stat.size_diff >= memory_size:
            #print(stat.traceback)
            if already_in_list(stat.traceback, potential_leaks):
                for item in potential_leaks:
                    if item["stat"] == stat.traceback:
                        item["count"] = int(item["count"]) + 1
                        # print("adding")
                        # print(item)
                        if item["count"] >= trigger_thresh:
                            print("ALERT " + str(item))
            else:
                potential_leaks.append({"stat": stat.traceback, "count": 0})

    #print(potential_leaks)
    # clear the list
    potential_leaks_new = []
    for item in potential_leaks:
        if item["stat"] in purge_list:
            potential_leaks_new.append(item)
    #print(purge_list)
    potential_leaks.clear()
    for item in potential_leaks_new:
        potential_leaks.append(item)
    #print(len(potential_leaks))
    print(potential_leaks)


def monitor_memory(interval_seconds, duration_seconds, trigger_thresh, memory_size):
    start_memory_tracking()
    initial_snapshot = take_snapshot()

    start_time = time.time()
    while (time.time() - start_time) < duration_seconds:
        time.sleep(interval_seconds)
        new_snapshot = take_snapshot()
        analyze_snapshots(initial_snapshot, new_snapshot, trigger_thresh, memory_size)
        initial_snapshot = new_snapshot

