# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests
# from bs4 import BeautifulSoup

# def scrape_google_jobs():
#     def googleHasJobs(driver):
#         driver.get('https://www.google.com/about/careers/applications/jobs/results?q=%22Software%20Engineer%22&employment_type=INTERN')
#         try:
#             driver.find_element(By.XPATH, '//*[contains(text(), "No results")]')
#             return False
#         except:
#             return True

#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')
#     options.add_argument('log-level=3')

#     driver = webdriver.Chrome(options=options)
#     thing = googleHasJobs(driver)

#     return thing

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app.database import get_session
from app.models import Job

def scrape_google_jobs():
    url = 'https://careers.google.com/jobs/results/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    session = get_session()
    jobs = []
    new_data = False

    for job_posting in soup.find_all('div', class_='job-listing'):
        title = job_posting.find('h2').text
        location = job_posting.find('div', class_='location').text
        
        # Check if the job already exists in the database
        existing_job = session.query(Job).filter_by(title=title, platform='Google').first()
        
        if not existing_job:
            new_job = Job(title=title, location=location, platform='Google')
            session.add(new_job)
            jobs.append({'title': title, 'location': location})
            new_data = True
    
    if new_data:
        session.commit()

    return jobs
