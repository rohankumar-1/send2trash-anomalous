import time
import math
import os

def runspike(interval=30, utilization=30):
    "Generate a utilization % for a duration of interval seconds"
    start_time = time.time()
    for i in range(0,int(interval)):
        print(f"About to do some arithmetic @ process: {os.getpid()}")
        while time.time()-start_time < utilization/100.0:
            a = math.sqrt(64*64*64*64*64)
        print(str(i) + " -> About to sleep")
        time.sleep(1-utilization/100.0)
        start_time += 1
