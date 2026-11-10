from services.internship_api import get_internships

jobs = get_internships()

print("Total internships:", len(jobs))

for job in jobs:
    print("-------------------")
    print("Company:", job.get("company"))
    print("Title:", job.get("title"))
    print("Location:", job.get("city_tag"))
    print("Apply:", job.get("url"))