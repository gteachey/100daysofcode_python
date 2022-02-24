from instafollower import InstaFollower

CHROME_DRIVER_PATH = r'C:\Users\gteac\OneDrive\Documents\PycharmProjects\dev_tools\chromedriver_win32\chromedriver.exe'
INSTAGRAM_FOLLOW = 'joshinseisn'
USERNAME = 'gt100daysofcode'
PASSWORD = r'sHF6Kvnc}Wj[;M<d,!9c'

insta_follower = InstaFollower(path=CHROME_DRIVER_PATH)

insta_follower.login(username=USERNAME, password=PASSWORD)

insta_follower.find_followers(INSTAGRAM_FOLLOW)
insta_follower.follow()
