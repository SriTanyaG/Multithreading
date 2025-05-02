
# Python Threading Tasks

This repository contains Python scripts demonstrating the use of threading for performance comparison in three different scenarios:

1. **Threaded Merge Sort**
2. **Threaded Quick Sort**
3. **Concurrent File Downloads**

---

## Files

| File | Description |
|------|-------------|
| `1.py` | Implements multi-threaded and single-threaded merge sort with timing comparison |
| `2.py` | Implements multi-threaded and single-threaded quicksort with thread control |
| `3.py` | Downloads files using sequential and concurrent (threaded) methods and compares timing |
| `urls.txt` | Sample file containing direct download URLs (used by `3.py`) |

---

## Task Descriptions

### 1. Threaded Merge Sort

**Objective:**
Merge Sort is a divide-and-conquer algorithm that recursively splits an array into smaller sub-arrays, sorts them, and merges them back together in sorted order. 

**Approach:**
- The array is recursively split into two halves.
- For a multi-threaded approach, the recursive calls for splitting the array are run on separate threads up to a predefined depth (`MAX_DEPTH`). This allows us to parallelize the sorting of sub-arrays.
- The `merge` function combines two sorted sub-arrays into one sorted array.
- A depth limit is imposed on threading to avoid creating too many threads, which can actually lead to performance degradation due to overhead.

**Intuition:**
- Multi-threading should speed up sorting by concurrently sorting sub-arrays.
- However, threading introduces overhead, and Python’s GIL (Global Interpreter Lock) may prevent performance gains in CPU-bound tasks like sorting. This is why we limit the depth of threading.

**Code Explanation:**
- `merge_sort(arr)` implements the classic merge sort.
- `threaded_merge_sort(arr)` introduces the threading logic, where threads are used for sorting sub-arrays up to a certain depth (`MAX_DEPTH`).

### 2. Threaded Quick Sort

**Objective:**
Quick Sort is another divide-and-conquer algorithm that picks a "pivot" element, partitions the array into two sub-arrays (elements less than pivot, and elements greater than pivot), and recursively sorts the sub-arrays.

**Approach:**
- The pivot element is selected, and the array is split into two parts: one with elements smaller than the pivot and another with elements greater than the pivot.
- In the multi-threaded version, the recursive calls to sort the two sub-arrays are run concurrently in separate threads.
- A global thread counter (`thread_count`) is used to limit the number of threads. This prevents excessive thread creation, which could introduce overhead and degrade performance.

**Intuition:**
- Quick sort is often faster than merge sort due to its in-place sorting nature. By using threads to sort sub-arrays concurrently, we aim to reduce the total sorting time by parallelizing the task.
- As with merge sort, there’s overhead in creating too many threads, and thus we limit thread creation.

**Code Explanation:**
- `quicksort(arr)` implements the traditional quick sort.
- `threaded_quicksort(arr)` adds the threading mechanism, where sub-arrays are sorted concurrently if the thread count limit is not exceeded.

### 3. Concurrent File Downloader

**Objective:**
This task involves downloading multiple files concurrently using threads, which can significantly reduce the overall download time for multiple files compared to downloading them sequentially.

**Approach:**
- A list of file URLs is provided, and the program first downloads all the files sequentially.
- In the multi-threaded version, each file download is assigned to a separate thread, allowing multiple downloads to occur at the same time.
- The program measures the total time taken for both methods and prints the results.

**Intuition:**
- Since file downloading is an I/O-bound task (not CPU-bound), threading can improve performance by allowing multiple downloads to happen concurrently without waiting for each one to finish before starting the next.
- Python’s threading module works well for I/O-bound tasks like file downloading, where the threads spend time waiting for network responses.

**Code Explanation:**
- `download_file(url)` handles the actual file downloading using the `requests` library.
- `download_sequential(urls)` performs the file downloads one after another.
- `download_concurrent(urls)` spawns threads for each file download, allowing them to happen simultaneously.

---

## How to Run

### Prerequisites
- Python 3.x
- Internet connection for `3.py`
- `requests` library: install via `pip install requests`

---

### Run Each Script

```bash
python 1.py
python 2.py
python 3.py
```

Make sure `urls.txt` is present in the same directory for the downloader.

---

## Sample Input (for downloader)

Create a file named `urls.txt` with direct download URLs:

```
https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf
https://file-examples.com/wp-content/uploads/2017/02/file_example_XLS_10.xls
https://file-examples.com/wp-content/uploads/2017/10/file_example_JPG_1MB.jpg
```

---

## Sample Output

### File Downloader

```
Sequential download time: 6.5 seconds
Concurrent download time: 2.3 seconds
```

---

## Notes

- Threading is limited in Python for CPU-bound tasks due to the Global Interpreter Lock (GIL). This makes Python less efficient at running CPU-intensive tasks in parallel threads.
- For I/O-bound tasks like file downloading, threading provides a significant performance boost by allowing multiple downloads to occur concurrently.
