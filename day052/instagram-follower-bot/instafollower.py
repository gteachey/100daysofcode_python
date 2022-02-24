from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

INSTAGRAM_URL = 'https://www.instagram.com/accounts/login/'


class InstaFollower:
    def __init__(self, path):
        options = Options()
        options.add_argument(r'user-data-dir=C:\Users\gteac\AppData\Local\Google\Chrome\User Data\\')
        service = Service(executable_path=path)
        self.driver = webdriver.Chrome(service=service)

    def login(self, username, password):
        self.driver.maximize_window()
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        user_name = self.driver.find_element(By.NAME, "username")
        user_name.send_keys(username)
        pass_word = self.driver.find_element(By.NAME, "password")
        pass_word.send_keys(password)
        pass_word.send_keys(Keys.ENTER)
        time.sleep(15)
        confirm = self.driver.find_element(By.XPATH,
                                           '//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        confirm.click()
        time.sleep(7)
        try:
            notifications_off = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        except NoSuchElementException:
            time.sleep(5)
            notifications_off = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[1]')
        notifications_off.click()
        time.sleep(1)

    def find_followers(self, insta_account):
        search = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(insta_account)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        account = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        account.click()
        time.sleep(5)

    def follow(self):
        get_followers = self.driver.find_elements(By.XPATH, '//li/div/div/button')
        num = 0
        while num < len(get_followers):
            while num < len(get_followers):
                print(len(get_followers))
                follower = get_followers[num]
                while get_followers[num].text == "Follow":
                    # Sometimes clicking Follow didn't do anything.
                    # Repeat click until it works
                    # Added the try block for if/when following another user has users
                    # I'm already following previously in it.
                    try:
                        follower.click()
                    except ElementClickInterceptedException:
                        cancel_button = self.driver.find_element(By.XPATH,
                                                                 '/html/body/div[7]/div/div/div/div[3]/button[2]')
                        cancel_button.click()
                    time.sleep(2)
                    get_followers = self.driver.find_elements(By.XPATH, '//li/div/div/button')
                num += 1
