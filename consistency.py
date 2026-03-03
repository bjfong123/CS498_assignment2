import requests
import uuid

US_URL = "http://136.115.61.59:8080"
EU_URL = "http://34.140.102.11:8080"

missed = 0
total = 100

for i in range(total):
    user = str(uuid.uuid4())
    requests.post(f"{US_URL}/register", json={"username": user})
    
    r = requests.get(f"{EU_URL}/list")
    
    if r.status_code == 200:
        data = r.json() 
        if user not in data.get("users", []):
            missed += 1
    else:
        print(f"Iteration {i}: Server Error {r.status_code} - {r.text}")

print(f"Total Misses: {missed} out of {total}")