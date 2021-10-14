from time import time


def time_check(fn):
    def timed_fn(arr):
        start = time()
        compare_operations = fn(arr)
        end = time()

        return {"time": end - start, "compare_operations": compare_operations}
    return timed_fn
