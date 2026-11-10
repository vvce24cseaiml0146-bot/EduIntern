# EduIntern – Internship Discovery Platform

## Project Overview
EduIntern is a web-based platform that helps students discover internship opportunities from different companies in one place.

Students can search for internships, filter opportunities by location, and apply through the company's official application portal.

## Technologies Used
- Python 3.12
- NiceGUI
- Requests
- External Internship API
- Git and GitHub
- Render Cloud Platform

## Features
- Fetches internship listings using an external API.
- Displays internship opportunities.
- Search internships by company or job title.
- Filter internships by location.
- Apply Now redirects students to external application portals.
- API caching to reduce repeated API requests.

## Performance Optimization
A five-minute in-memory caching mechanism was implemented to reduce repeated API calls.

The first API request fetches internship data from the external API. Subsequent requests can use cached data until the cache expires.

## Load Testing
A basic load test was performed using Python ThreadPoolExecutor.

- Number of concurrent requests: 5
- Successful HTTP responses: 5
- HTTP status code: 200 for all requests
- Average response time: Approximately 1.48 seconds

## Cloud Deployment
The application was deployed using Render.

Live Application: https://eduintern.onrender.com

Source Code: https://github.com/vvce24cseaiml0146-bot/EduIntern

## Scalability
The application uses API caching to reduce repeated external API requests.

The current application runs on Render's Free instance. Multiple-instance horizontal scaling and automatic scaling have not been enabled.

Future improvements include:
- Deploying multiple application instances.
- Using a load balancer.
- Implementing shared caching.
- Supporting more internship data sources.