from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions
import re
import pandas as pd

from selen import phone

df = pd.read_csv('tel.csv')
mess = "Hello, Devops team! Have a nice day"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.whatsapp.com")
# QR code is required
input("Press Enter after scanning QR code")
sleep(2)

driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/div[1]/button/span').click()
sleep(1)
for index, row in df.iterrows():
    name = row['name']
    phone = row['phone']
    search_box = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div/div/div[1]/p')
    #search_box.send_keys(re.sub(r"^0", '+972 ', phone))
    sleep(1)
    search_box.send_keys(Keys.CONTROL + 'a')
    search_box.send_keys(Keys.DELETE)
    sleep(1)
    search_box.send_keys(phone)
    search_box.send_keys(Keys.ENTER)
    #search_box.clear()
    sleep(1)

# Ready till this row
msg = driver.switch_to.active_element
msg.send_keys("test")
sleep(1)
msg.send_keys(Keys.ENTER)
sleep(5)

driver.quit()