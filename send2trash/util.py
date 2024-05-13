# encoding: utf-8
# Copyright 2017 Virgil Dupras

# This software is licensed under the "BSD" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.hardcoded.net/licenses/bsd_license

from send2trash.compat import text_type, binary_type, iterable_type


def preprocess_paths(paths):
    if isinstance(paths, iterable_type) and not isinstance(paths, (text_type, binary_type)):
        paths = list(paths)
    elif not isinstance(paths, list):
        paths = [paths]
    # Convert items such as pathlib paths to strings
    paths = [path.__fspath__() if hasattr(path, "__fspath__") else path for path in paths]
    return paths

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


