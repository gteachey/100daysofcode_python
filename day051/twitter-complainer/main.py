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
driver.maximize_window()
speedtest_url = 'https://www.speedtest.net/'
twitter_url = 'https://www.twitter.com/'
driver.get(speedtest_url)
time.sleep(10)

speedtest_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
speedtest_button.click()
time.sleep(120)
download_speed_result = driver.find_element(By.XPATH,
                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload_speed_result = driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
d_speed = download_speed_result.text
u_speed = upload_speed_result.text
driver.get(twitter_url)
time.sleep(10)
twitter_text_box = driver.find_element(By.XPATH,
                                       '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
if float(d_speed) < 400.00:
    twitter_text_box.send_keys(
        f"@Ask_Spectrum We have issues! {d_speed}Mbps down and {u_speed}Mbps up right now, when I'm paying for 400Mbps! Please check the Charlotte area services!")
else:
    twitter_text_box.send_keys(
        f"@Ask_Spectrum Nice speeds! {d_speed}Mbps down and {u_speed}Mbps up. Thank you for the service you provide! ")

time.sleep(2)
twitter_tweet_btn = driver.find_element(By.XPATH,
                                        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
twitter_tweet_btn.click()
