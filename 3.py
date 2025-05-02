import threading
import requests
import time

def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(r.content)

def download_sequential(urls):
    for url in urls:
        download_file(url)

def download_concurrent(urls):
    threads = []
    for url in urls:
        t = threading.Thread(target=download_file, args=(url,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def read_urls(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

if __name__ == "__main__":
    urls = read_urls("urls.txt")

    start = time.perf_counter()
    download_sequential(urls)
    print("Sequential download time:", time.perf_counter() - start)

    start = time.perf_counter()
    download_concurrent(urls)
    print("Concurrent download time:", time.perf_counter() - start)
