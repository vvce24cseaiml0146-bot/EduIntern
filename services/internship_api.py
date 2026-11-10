import requests

API_URL = "https://internscan.vercel.app/in/api/active.json"

def get_internships():

    response = requests.get(API_URL, timeout=15)

    response.raise_for_status()

    data = response.json()

    internships = data.get("jobs", [])

    return internships