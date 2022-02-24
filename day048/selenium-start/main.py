from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'C:\Users\gteac\OneDrive\Documents\PycharmProjects\dev_tools\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)
# url = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CYMYK6/ref=dp_fod_1?pd_rd_i=B075CYMYK6&psc=1"
# driver.get(url)

# <input id="attach-base-product-price" type="hidden" value="99.95"/>
# <span aria-hidden="true">$99.95</span>


# price = driver.find_element(By.XPATH, "//span[@data-a-color='price']/span[@aria-hidden='true']")
# price = driver.find_element(By.XPATH, "//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]")
# print(price.text.strip('$'))

url = "http://www.python.org"
driver.get(url)
# search_bar = driver.find_element(By.NAME, 'q')
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, 'python-logo')
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)


#     driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

upcoming_events = {}
events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
dates = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')

num = 0
for num in range(0, len(dates)):
    date = dates[num].get_attribute('datetime').split('T')[0]
    event = events[num].text
    upcoming_events[num] = {'time': date, 'name': event}

print(upcoming_events)

driver.close()
