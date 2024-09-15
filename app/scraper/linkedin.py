import requests
from bs4 import BeautifulSoup

def scrape_linkedin_jobs():
    url = 'https://www.linkedin.com/jobs'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    jobs = []
    for job_posting in soup.find_all('div', class_='job-card'):
        title = job_posting.find('h3').text
        company = job_posting.find('h4').text
        jobs.append({'title': title, 'company': company})
    
    return jobs