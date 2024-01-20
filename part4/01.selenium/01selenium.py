import time as dlay
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import ui
import random

td = range(1, 15)

dv = webdriver.Firefox()

dv.get('https://www.google.com')

element = dv.find_element(By.NAME, 'q')

element.send_keys('gerrrr ger paow')
element.send_keys(Keys.ENTER)

dlay.sleep(random.choice(td))

dv.execute_script('window.scrollTo(0,300)')
dlay.sleep(0.91)
dv.execute_script('window.scrollTo(0,600)')
dlay.sleep(1.63)
dv.execute_script('window.scrollTo(0,600)')

dlay.sleep(8)
dv.close()
dv.quit()
