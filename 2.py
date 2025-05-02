import threading
import time
import random

MAX_THREADS = 4
thread_count = 0
thread_lock = threading.Lock()

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    more = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(more)

def threaded_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = []
    more = []

    def sort_less():
        nonlocal less
        less = threaded_quicksort([x for x in arr[1:] if x <= pivot])

    def sort_more():
        nonlocal more
        more = threaded_quicksort([x for x in arr[1:] if x > pivot])

    global thread_count
    with thread_lock:
        use_threads = thread_count < MAX_THREADS
        if use_threads:
            thread_count += 2

    if use_threads:
        t1 = threading.Thread(target=sort_less)
        t2 = threading.Thread(target=sort_more)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        with thread_lock:
            thread_count -= 2
    else:
        less = threaded_quicksort([x for x in arr[1:] if x <= pivot])
        more = threaded_quicksort([x for x in arr[1:] if x > pivot])

    return less + [pivot] + more

if __name__ == "__main__":
    arr = [random.randint(0, 10000) for _ in range(50000)]

    start = time.perf_counter()
    quicksort(arr.copy())
    print("Single-threaded time:", time.perf_counter() - start)

    start = time.perf_counter()
    threaded_quicksort(arr.copy())
    print("Multi-threaded time:", time.perf_counter() - start)
