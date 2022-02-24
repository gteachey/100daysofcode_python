from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import lxml
import requests

CHROME_DRIVER_PATH = r'C:\Users\gteac\OneDrive\Documents\PycharmProjects\dev_tools\chromedriver_win32\chromedriver.exe'
# GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSf-ij-8VZV80X7hrql2qZXC0hVqTS4CEur-4JjulLeB1M24DA/viewform'
GOOGLE_FORM_URL = 'https://forms.gle/L6r9hWqfezBDE1e58'
ZILLOW_WEB_ADDRESS = 'https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417324103516%2C%22east%22%3A-122.23248561896484%2C%22south%22%3A37.6663930046388%2C%22north%22%3A37.884030820160305%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A870859%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

options = Options()
options.add_argument(r'user-data-dir=C:\Users\gteac\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--disable-web-security=true')
options.add_argument('--allow-running-insecure-content=true')
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
# driver.get(ZILLOW_WEB_ADDRESS)
#
# # with open('zillow.txt', 'r', encoding='') as file:
# #     driver = file.read(file)
# time.sleep(5)
# # print(driver.page_source)
# # with open('zillow.txt', 'w', encoding='utf-8') as file:
# #     file.write(driver.page_source)
# listings_title = driver.find_element(By.CSS_SELECTOR, 'a.list-card-link')
# listings_title.send_keys(Keys.END)
# time.sleep(3)
#
# listings_links = driver.find_elements(By.CSS_SELECTOR, 'a.list-card-link')
#
# links = []
# for i in listings_links:
#     try:
#         if '/b/' not in i.get_attribute('href') and i.get_attribute('href') not in links:
#             links.append(i.get_attribute('href'))
#             print(i.get_attribute('href'))
#     except AttributeError:
#         continue
# print(len(links))
# # print(links)
#
# listings_prices = driver.find_elements(By.CSS_SELECTOR, 'div.list-card-price')
# print(len(listings_prices))
# prices = []
# for i in listings_prices:
#     prices.append(i.text)
#
# listings_address = driver.find_elements(By.CSS_SELECTOR, 'address.list-card-addr')
# print(len(listings_address))
# addresses = []
# for i in listings_address:
#     addresses.append(i.text)
#
#
# driver.get(GOOGLE_FORM_URL)
# for i in range(0, len(listings_address)):
#     address = driver.find_element(By.XPATH, '//*[@aria-labelledby="i1"]')
#     address.send_keys(addresses[i])
#
#     price = driver.find_element(By.XPATH, '//*[@aria-labelledby="i5"]')
#     price.send_keys(prices[i])
#
#     link = driver.find_element(By.XPATH, '//*[@aria-labelledby="i9"]')
#     link.send_keys(links[i])
#
#     submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
#     submit_button.click()
#     time.sleep(2)
#     submit_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
#     submit_another.click()
#     time.sleep(2)

driver.get('https://docs.google.com/forms/d/1HoQTPD1ZupVCeToZNpCKHsKhxE4EUx4ns7phRclNItw/edit#responses')
time.sleep(20)
# create_spreadsheet = driver.find_element(By.XPATH, '//*[class="freebird-qp-icon-spreadsheet-green"')
# create_spreadsheet.click()
# time.sleep(2)
# confirm_button = driver.find_element(By.LINK_TEXT, 'Create')
# confirm_button.click()


# driver.quit()


# TODO: SELENIUM STUFF
# options = Options()
# options.add_argument(r'user-data-dir=C:\Users\gteac\AppData\Local\Google\Chrome\User Data\\')
# service = Service(executable_path=path)
# driver = webdriver.Chrome(service=service)
#
# driver.maximize_window()
# driver.get(ZILLOW_WEB_ADDRESS)
# time.sleep(5)
