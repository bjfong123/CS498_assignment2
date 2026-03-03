import requests 
import time

US_URL = "http://136.115.61.59:8080"
EU_URL = "http://34.140.102.11:8080"

def measure_latency(url, endpoint, method="GET",data=None):
    latencies = []
    for i in range(10):
        start = time.time()
        if method == "POST":
            requests.post(url + endpoint, json=data)
        else:
            requests.get(url + endpoint)
        end = time.time()
        latencies.append((end - start) * 1000)

        avg = sum(latencies) / len(latencies)
    return avg

us_reg_avg = measure_latency(US_URL, "/register", "POST", {"username": "latency_test_us"})
print(f"US /register Average Latency: {us_reg_avg:.2f} ms")

us_list_avg = measure_latency(US_URL, "/list")
print(f"US /list Average Latency: {us_list_avg:.2f} ms")

eu_reg_avg = measure_latency(EU_URL, "/register", "POST", {"username": "latency_test_eu"})
print(f"EU /register Average Latency: {eu_reg_avg:.2f} ms")

eu_list_avg = measure_latency(EU_URL, "/list")
print(f"EU /list Average Latency: {eu_list_avg:.2f} ms")