from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# url = 'https://en.wikipedia.org/wiki/Main_Page'
execu_path = r'C:\Users\gteac\OneDrive\Documents\PycharmProjects\dev_tools\chromedriver_win32\chromedriver.exe'
service = Service(execu_path)
driver = webdriver.Chrome(service=service)

# driver.get(url)
# num_of_articles = driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
# print(num_of_articles.text)
# num_of_articles.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

# search = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
# search = driver.find_element(By.NAME, "search")
# print(search.text)
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
url = 'http://secure-retreat-92358.herokuapp.com/'
driver.get(url)

fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Joe")
lName = driver.find_element(By.NAME, "lName")
lName.send_keys("Black")
email = driver.find_element(By.NAME, "email")
email.send_keys('meetjoeblack@movies.com')
button = driver.find_element(By.XPATH, '/html/body/form/button')
button.click()

# driver.close()
