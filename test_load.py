import requests
import time
from concurrent.futures import ThreadPoolExecutor

URL = "https://eduintern.onrender.com"

def test_user(user):
    start = time.time()

    try:
        response = requests.get(URL, timeout=60)
        duration = time.time() - start

        return {
            "User": user,
            "Status": response.status_code,
            "Response Time": round(duration, 3)
        }

    except requests.RequestException as error:
        return {
            "User": user,
            "Status": "Failed",
            "Response Time": str(error)
        }

print("Starting load test...")

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(test_user, range(1, 6)))

for result in results:
    print(result)

print("Load test completed!")