import requests
import time
import numpy as np

URL = "http://localhost:8080/embed"
DATA = {"text": "Это тестовое предложение для замера скорости."}
N_REQUESTS = 100 

latencies = []

print(f"Starting benchmark: {N_REQUESTS} requests...")

for _ in range(N_REQUESTS):
    start_time = time.perf_counter()
    response = requests.post(URL, json=DATA)
    end_time = time.perf_counter()
    
    if response.status_code == 200:
        latencies.append((end_time - start_time) * 1000) 

p50 = np.percentile(latencies, 50)
p95 = np.percentile(latencies, 95)
p99 = np.percentile(latencies, 99)
rps = N_REQUESTS / (sum(latencies) / 1000)

print(f"Latency P50: {p50:.2f} ms")
print(f"Latency P95: {p95:.2f} ms")
print(f"Latency P99: {p99:.2f} ms")
print(f"Throughput (approx): {rps:.2f} RPS")