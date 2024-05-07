import time
import tracemalloc

import objgraph
from memory_profiler import profile

# from MemoryLeakDetectionPrototype.code_comparison.plag import plag
import plag.plag
import unique.unique

start_time = time.time()



# tracemalloc.start()

# initial_counts = objgraph.typestats()

loop=2000
i=1
while i <= loop:
    plag.plag.run()
    #unique.unique.run()
    i+=1

# unique.unique.run()
# time.sleep(2)

# plag.plag.run()


# current_counts = objgraph.typestats()
# print("Checking for leaks...")
# for obj_type, count in current_counts.items():
#     initial_count = initial_counts.get(obj_type, 0)
#     if count - initial_count > 2:
#         print(f"Potential leak detected: {obj_type} count increased by {count - initial_count}")
# Update the initial_counts for the next interval
# initial_counts = current_counts
# Optionally, show the most common types
# objgraph.show_most_common_types(limit=10)



# snapshot=tracemalloc.take_snapshot()
# top_stats =snapshot.statistics('lineno')
# print("[ Top 10 ]")
# for stat in top_stats[:10]:
#     print(stat)


end_time = time.time()
print("Runtime:", end_time - start_time, "seconds")
time.sleep(10)
