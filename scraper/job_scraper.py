import requests
from bs4 import BeautifulSoup

def get_latest_job_title():
    url = 'https://internfreak.co/jobs-and-internship-opportunities?page=1&limit=10'
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch data from the URL.")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    job_listings = soup.find_all('div', class_='job-listing')
    
    if not job_listings:
        return "No jobs found."
    
    latest_job = job_listings[0]  # Assuming the first job is the latest
    title = latest_job.find('h2').text.strip()  # Adjust based on actual HTML structure
    return title
