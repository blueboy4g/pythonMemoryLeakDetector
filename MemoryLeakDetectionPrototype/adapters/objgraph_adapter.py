import objgraph
import time


def monitor_objects(interval_seconds, duration_seconds, threshold=10):
    initial_counts = objgraph.typestats()
    start_time = time.time()

    while (time.time() - start_time) < duration_seconds:
        time.sleep(interval_seconds)
        current_counts = objgraph.typestats()
        print("Checking for leaks...")
        for obj_type, count in current_counts.items():
            initial_count = initial_counts.get(obj_type, 0)
            if count - initial_count > threshold:
                print(f"Potential leak detected: {obj_type} count increased by {count - initial_count}")

        # Update the initial_counts for the next interval
        initial_counts = current_counts

        # Optionally, show the most common types
        objgraph.show_most_common_types(limit=10)
