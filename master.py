import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_request(ip, iterations):
    url = f"http://{ip}:5000/find_primes"
    data = {"iterations": iterations}
    resp = requests.post(url, json=data)
    return resp.json()

def test_workers(n, num_workers, worker_ips):
    iter_per_instance = n / num_workers
    results = []
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        for i, ip in enumerate(worker_ips):
            futures.append(executor.submit(send_request, ip, iter_per_instance))
        for future in as_completed(futures):
            results.append(future.result())
    
    total_time = max([r['end'] for r in results]) - min([r['start'] for r in results])
    print(f"Total time: {total_time:.2f} seconds")
    print("Individual worker times:", [r['end'] - r['start'] for r in results])
    return total_time


if __name__ == '__main__':
    
    args = input().split()
    power = int(args[0])
    file_name = args[1]
    with open('input.txt', 'r') as file:
        ip_addresses = file.readlines()
    ip_addresses = [ip.strip() for ip in ip_addresses]
    
    n = 10**power
    runs = 10
    time_arr = [0,0,0,0]
    for _ in range(runs):
        for i in range(4):
            num_workers = 2**i
            print("-----------------------------------------------")
            print(f"              LOGS FOR {num_workers} workers")

            worker_ips = ip_addresses[:num_workers]
            
            time_arr[i] += test_workers(n, num_workers, worker_ips)
            print("-----------------------------------------------\n")
    print("\n".join([f"avg time for {2**i} workers is: {k/runs}" for i,k in enumerate(time_arr)]))
    
    print("Performace boost coefficients")
    for i in range(1,4):
        print(f"From {2**(i - 1)} to {2**i} workers boost is {time_arr[i - 1] / time_arr[i]}")
    
