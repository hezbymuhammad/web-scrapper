from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://www.jobstreet.co.id/id/job-search/job-vacancy/"
urls = [base_url + str(i) for i in range(60)]
urls = [x + "/" for x in urls]

browser = webdriver.Chrome()

for url in urls:
  browser.get(url)
  wait = WebDriverWait(browser, 10)

  results = browser.find_elements_by_class_name(
      'position-title-link')

  for result in results:
    print(result.find_element_by_tag_name('h2').get_attribute('innerHTML'))
