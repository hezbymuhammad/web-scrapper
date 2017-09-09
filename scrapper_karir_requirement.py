from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://karir.com/opportunities/"

# put opportunity ids here
ids = []

urls = [base_url + str(i) for i in range(10000)]
browser = webdriver.Chrome()

for url in urls:
    browser.get(url)
    wait = WebDriverWait(browser, 10)
    try:
        wrappers = browser.find_elements_by_class_name(
            'b-matte__content')
        requirements = wrappers[0].get_attribute('innerHTML')
        print(BeautifulSoup(requirements, "html.parser").text)
    except Exception:
        pass
