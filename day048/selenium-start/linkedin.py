import time

import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# url = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0'
url = 'https://www.linkedin.com/jobs/search/?f_AL=true&geoId=90000152&keywords=Linux%20Software%20Engineer&location=Charlotte%20Metro'
username = 'gteachey@outlook.com'
user_passwword = 'Ilovelinux1230)'
service = Service(r'C:\Users\gteac\OneDrive\Documents\PycharmProjects\dev_tools\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url)

# /html/body/main/div/div/form[2]/section/p/button
# sign_in_button = driver.find_element(By.CLASS_NAME, '.authwall-join-form__form-toggle')
time.sleep(1)
try:
    sign_in_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in')
except selenium.common.exceptions.NoSuchElementException:
    sign_in_button = driver.find_element(By.CSS_SELECTOR, '#authwall-join-form__form-toggle form-toggle')
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(By.XPATH, '//*[@id="username"]')
email_field.send_keys(username)
login_password = driver.find_element(By.XPATH, '//*[@id="password"]')
login_password.send_keys(user_passwword)
sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()

time.sleep(5)
# job_search_text_input = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember32"]')
# job_search_text_input.clear()
# job_search_text_input.send_keys("Linux Software Engineer")
# time.sleep(2)
# try:
#     city_search_text = driver.find_element(By.XPATH, '//*[@id="location-typeahead-instance-ember32"]/div/input[2]')
# except:
#     city_search_text = driver.find_element(By.XPATH, '//*[@id="location-typeahead-instance-ember32"]/div/input[2]')
#
# city_search_text.clear()
# city_search_text.send_keys('Charlotte Metro')
# time.sleep(1)

# search_button = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]/button[1]')
# search_button.click()
postings = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

for job_post in postings:
    print('found a job')
    job_post.click()
    time.sleep(2)
    try:
        save_it = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
        save_it.click()
        time.sleep(2)
    except NoSuchElementException:
        print('//*[@id="ember1076"]')
