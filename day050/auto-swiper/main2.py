from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument(r'user-data-dir=C:\Users\gteac\AppData\Local\Google\Chrome\User Data\\')
chrome_driver_path = r"C:\Users\gteac\OneDrive\Documents\PycharmProjects\dev_tools\chromedriver_win32\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://tinder.com/app/recs")
driver.maximize_window()
time.sleep(10)
reject_button = driver.find_element(By.XPATH,
                                    '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
start_time = time.time()
end_time = start_time + 60

while time.time() < end_time:
    reject_button.click()
    time.sleep(5)

driver.quit()
