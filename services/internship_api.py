import requests
import time

API_URL = "https://internscan.vercel.app/in/api/active.json"

cached_jobs = []
last_updated = 0
CACHE_DURATION = 300  # 5 minutes

def get_internships():
    global cached_jobs, last_updated

    current_time = time.time()

    if cached_jobs and current_time - last_updated < CACHE_DURATION:
        return cached_jobs

    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()

    data = response.json()
    cached_jobs = data.get("jobs", [])
    last_updated = current_time

    return cached_jobs