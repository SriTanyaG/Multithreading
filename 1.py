import threading
import time
import random

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def threaded_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = []
    right = []

    def sort_left():
        nonlocal left
        left = threaded_merge_sort(arr[:mid])

    def sort_right():
        nonlocal right
        right = threaded_merge_sort(arr[mid:])

    t1 = threading.Thread(target=sort_left)
    t2 = threading.Thread(target=sort_right)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    return merge(left, right)

if __name__ == "__main__":
    arr = [random.randint(0, 10000) for _ in range(500)]

    start = time.perf_counter()
    merge_sort(arr.copy())
    print("Single-threaded time:", time.perf_counter() - start)

    start = time.perf_counter()
    threaded_merge_sort(arr.copy())
    print("Multi-threaded time:", time.perf_counter() - start)
