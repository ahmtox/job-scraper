from selenium import webdriver
from selenium.webdriver.common.by import By

def googleHasJobs(driver):
  driver.get('https://www.google.com/about/careers/applications/jobs/results?q=%22Software%20Engineer%22&employment_type=INTERN')

  try:
    driver.find_element(By.XPATH, '//*[contains(text(), "No results")]')
    return False
  except:
    return True

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('log-level=3')

driver = webdriver.Chrome(options=options)
print(googleHasJobs(driver))