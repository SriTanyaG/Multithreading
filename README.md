
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

- Uses Python’s `threading` module to run merge sort in parallel for subarrays.
- Limits thread creation using a depth-based condition.
- Compares execution time with a single-threaded merge sort.

### 2. Threaded Quick Sort

- Implements quicksort with optional concurrent sorting of partitions using threads.
- Controls thread creation to avoid too many active threads.
- Benchmarks against regular quicksort.

### 3. Concurrent File Downloader

- Accepts file URLs from a text file.
- Downloads files sequentially and concurrently using threads.
- Prints the time taken by each method.

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
## Notes

- Threading is limited in Python for CPU-bound tasks due to the Global Interpreter Lock (GIL).
- For file downloads (I/O-bound), threading shows clear performance benefits.
