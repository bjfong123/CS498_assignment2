import requests
import uuid

# Verified External IPs from your script
US_URL = "http://35.224.230.41:8080"
EU_URL = "http://34.140.102.11:8080"

missed = 0
total = 100

for i in range(total):
    user = str(uuid.uuid4())
    # Register in US
    requests.post(f"{US_URL}/register", json={"username": user})
    
    # Check EU
    r = requests.get(f"{EU_URL}/list")
    
    # Check if the server actually sent back a success (200 OK)
    if r.status_code == 200:
        data = r.json() # This converts the response to a dictionary
        if user not in data.get("users", []):
            missed += 1
    else:
        # This will print the actual error (like 500) instead of crashing
        print(f"Iteration {i}: Server Error {r.status_code} - {r.text}")

print(f"Total Misses: {missed} out of {total}")