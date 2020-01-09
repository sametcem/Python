from selenium import webdriver
import time

browser = webdriver.Firefox()
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712"

browser.get(url)
time.sleep(5)

elements = browser.find_elements_by_css_selector(".content")
for element in elements:
    print("*********************")
    print(element.text)

browser.close()
