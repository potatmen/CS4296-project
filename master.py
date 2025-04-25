import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_request(ip, iterations):
    url = f"http://{ip}:5000/find_primes"
    data = {"iterations": iterations}
    resp = requests.post(url, json=data)
    return resp.json()

def test_workers(n, num_workers, worker_ips):
    iter_per_instance = n / num_workers
    print(f"Testing with {num_workers} workers")
    t0 = time.time()
    results = []
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        for i, ip in enumerate(worker_ips):
            futures.append(executor.submit(send_request, ip, iter_per_instance))
        for future in as_completed(futures):
            results.append(future.result())
    t1 = time.time()
    print(f"Total time: {t1-t0:.2f} seconds")
    print("Individual worker times:", [r['end'] - r['start'] for r in results])

if __name__ == '__main__':
    n = 100
    worker_ips = ["172.31.87.123"]
    test_workers(n, 1, worker_ips)
    #for num_workers in [1, 2, 4, 8]:
    #    # List your worker IPs here, for example:
    #    worker_ips = ["172.31.87.123"][:num_workers]
    #    test_workers(n, num_workers, worker_ips)