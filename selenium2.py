from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions

driver = webdriver.Chrome()
driver.maximize_window()
# url = 'https://ksp.co.il/web/cat/31635..271..61630'
# driver.get(url)
# sleep(3)
#
# driver.execute_script("window.open('https://www.youtube.com/watch?v=dOjvtkuhsdI')")
# sleep(3)
# for win_h in driver.window_handles:
#     driver.switch_to.window(win_h)
#     sleep(5)
# sub = driver.find_element(By.ID, 'owner-sub-count')
# print(sub.text)
# sleep(1)
# driver.execute_script("window.scrollTo(0,200);")
# driver.implicitly_wait(2)
# comments = driver.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[1]')
# print(f"There are {comments.text} comments for this video")

driver.get("https://vinothqaacademy.com/alert-and-popup/")
driver.find_element(By.NAME, 'alertbox').click()
sleep(2)
alert_obj = driver.switch_to.alert
msg = alert_obj.text
print(msg)
alert_obj.dismiss()
sleep(2)

driver.find_element(By.NAME, 'confirmalertbox').click()
confirm_obj = driver.switch_to.alert
msg2 = confirm_obj.text
print(msg2)
confirm_obj.dismiss()
sleep(2)

driver.find_element(By.NAME, 'promptalertbox1234').click()
prompt_obj = driver.switch_to.alert
msg3 = prompt_obj.text
print(msg3)
prompt_obj.send_keys("Yes")
sleep(1)
prompt_obj.accept()
sleep(2)


driver.quit()