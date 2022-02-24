from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

execu_path = r'C:\Users\gteac\OneDrive\Documents\PycharmProjects\dev_tools\chromedriver_win32\chromedriver.exe'
service = Service(execu_path)
driver = webdriver.Chrome(service=service)

driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, 'cookie')
moni = driver.find_elements(By.XPATH, '//*[@id="store"]/div/b')

while True:
    cookie = driver.find_element(By.ID, 'cookie')
    moni = driver.find_elements(By.XPATH, '//*[@id="store"]/div/b')
    num = 0
    clean_moni = []
    for mon in moni:
        if mon.text:
            clean_moni.append(mon)
    timeout = 5  # [seconds]

    timeout_start = time.time()

    while time.time() < timeout_start + timeout:
        num += 1
        cookie.click()

    money = int(driver.find_element(By.ID, 'money').text.replace(",", ""))
    store_item_price = int(clean_moni[0].text.split('-')[1].strip().replace(",", ""))
    if money > store_item_price:  # start off by checking there's enough money to buy the first item in the store
        for num in range(0, len(clean_moni) - 1):
            store_item_price = int(clean_moni[num].text.split('-')[1].strip().replace(",", ""))
            if money > store_item_price:  # compare money against the store item prices
                choice = clean_moni[num]  # save the webelement if it's cheaper than money
        parent = choice.find_element(By.XPATH, './..')  # find the parent of this web element we saved.
        parent.click()  # buy it with a click!
    sleep(1)
# //*[@id="bigCookie"]
