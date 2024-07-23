# import requests
# from bs4 import BeautifulSoup

# def get_latest_job_titles():
#     url = 'https://internfreak.co/jobs-and-internship-opportunities?page=1&limit=10'
#     response = requests.get(url)
    
#     if response.status_code != 200:
#         raise Exception("Failed to fetch data from the URL.")
    
#     soup = BeautifulSoup(response.text, 'html.parser')
#     job_listings = soup.find_all('div', class_='post-entry')
    
#     if not job_listings:
#         return "No jobs found."
    
#     job_titles = []
#     for job in job_listings:
#         title = job.find('h2', class_='heading').text.strip()
#         job_titles.append(title)
    
#     return job_titles

# # Example usage
# if __name__ == "__main__":
#     job_titles = get_latest_job_titles()
#     for idx, title in enumerate(job_titles, 1):
#         print(f"{idx}. {title}")


import requests
from bs4 import BeautifulSoup

def get_latest_job_titles():
    url = 'https://internfreak.co/jobs-and-internship-opportunities?page=1&limit=10'
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch data from the URL.")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    job_listings = soup.find_all('div', class_='post-entry')
    
    if not job_listings:
        return "No jobs found."
    
    job_titles = []
    for job in job_listings:
        title = job.find('h2', class_='heading').text.strip()
        job_titles.append(title)
    
    return job_titles

# Example usage
if __name__ == "__main__":
    job_titles = get_latest_job_titles()
    if isinstance(job_titles, list) and job_titles:
        print("Latest Job Titles:")
        for idx, title in enumerate(job_titles, 1):
            print(f"{idx}. {title}")
    else:
        print(job_titles)
