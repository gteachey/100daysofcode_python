import time

from selenium import webdriver

# <div class="Mx(a) Fxs(0) Sq(60px) Sq(48px)--s Bd Bdrs(50%) Bdc($c-divider)"><button type="button" class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Pos(r) Pe(n) Bgc($c-yellow):a" draggable="false"><span class="Pos(r) Z(1) Expand"><svg class="Scale(.6) Expand" viewBox="0 0 24 24" width="24px" height="24px" focusable="false" aria-hidden="true" role="presentation"><path d="M12.119 4.599V3.307c0-1.216-.76-1.672-1.824-.988l-.608.304L6.04 5.13l-.456.304c-1.064.76-1.064 1.748 0 2.28l.38.38c.987.76 2.66 1.824 3.647 2.432l.532.304c.912.76 1.748.228 1.748-.912V8.246a5.125 5.125 0 0 1 5.167 5.167c0 2.888-2.28 5.092-5.167 5.092-3.04 0-5.32-2.28-5.32-5.168 0-.912-.76-1.671-1.747-1.671-1.064 0-1.824.76-1.824 1.671C3 18.125 6.951 22 11.815 22c4.787 0 8.738-3.8 8.738-8.663.076-4.711-3.875-8.51-8.662-8.51l.228-.228z" fill="#e9ebee"></path></svg><span class="Hidden">Rewind</span></span></button></div>
#
# < div
#
#
# class ="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-pink)" style="transform: scale(1); background-color: rgba(253, 84, 108, 0);" > < button type="button" class ="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgc($c-pink):a" draggable="false" > < span class ="Pos(r) Z(1) Expand" > < span class ="D(b) Expand" style="transform: scale(1); filter: none;" > < svg class ="Scale(.5) Expand" viewBox="0 0 24 24" width="24px" height="24px" focusable="false" aria-hidden="true" role="presentation" > < path class ="" d="M14.926 12.56v-1.14l5.282 5.288c1.056.977 1.056 2.441 0 3.499-.813 1.057-2.438 1.057-3.413 0L11.512 15h1.138l-5.363 5.125c-.975 1.058-2.438 1.058-3.495 0-1.056-.813-1.056-2.44 0-3.417l5.201-5.288v1.14L3.873 7.27c-1.137-.976-1.137-2.44 0-3.417a1.973 1.973 0 0 1 3.251 0l5.282 5.207H11.27l5.444-5.207c.975-1.139 2.438-1.139 3.413 0 1.057.814 1.057 2.44 0 3.417l-5.2 5.288z" fill="var(--fill--nope, none)" > < / path > < / svg > < span class ="Hidden" > Nope < / span > < / span > < / span > < / button > < / div >
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

exec_path = r'C:\Users\gteac\OneDrive\Documents\PycharmProjects\dev_tools\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(exec_path)
driver.maximize_window()
url = 'https://tinder.com/app/recs'
driver.get(url)

login = driver.find_element(By.XPATH,
                            '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
with_google = driver.find_element(By.XPATH, '*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
email = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email.send_keys("gt100daysofcode")
email.send_keys(Keys.ENTER)
T..h7RP  # tz;G[t27bC,y
time.sleep(2)
while True:
    try:
        swipe_left = driver.find_element(By.XPATH,
                                         '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[1]')
    except:
        swipe_left = driver.find_element(By.XPATH, '#')
