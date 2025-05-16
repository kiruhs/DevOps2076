from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions

driver = webdriver.Chrome()
# print(dir(driver))
driver.maximize_window()
url = 'https://ksp.co.il/web/cat/31635..271..61630'
driver.get(url)
sleep(3)

page_height = driver.execute_script("return document.body.scrollHeight")
# print(page_height)

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == page_height:
        break
    page_height = new_height
sleep(1)
try:
    driver.find_element(By.TAG_NAME, 'body').click()
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/main/div/div[3]/footer/div[3]/div[1]/div[3]/input')
    print("Element found")

except exceptions.NoSuchElementException:
    print("Element not found")

driver.get_screenshot_as_file('screen01.png')

brand = "Lenovo"
links = driver.find_elements(By.XPATH, f"//a[contains(text(), '{brand}')]")

# for item in links:
#     print(item.get_attribute("aria-label"))
print(f"We have {len(links)} products of {brand} on this page")
driver.quit()