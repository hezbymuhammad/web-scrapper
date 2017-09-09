from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://www.karir.com/search?page="
urls = [base_url + str(i) for i in range(80)]
browser = webdriver.Chrome()

for url in urls:
  browser.get(url)
  wait = WebDriverWait(browser, 10)

  results = browser.find_elements_by_class_name(
      'tdd-function-name')

  for result in results:
    print(result.get_attribute('innerHTML'))