from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions
import csv
driver = webdriver.Chrome()
url = 'https://www.globes.co.il/portal/instrument.aspx?instrumentId=356621&mode=trades'
driver.maximize_window()
driver.get(url)
sleep(2)
driver.find_element(By.XPATH, '//*[@id="htmlHead"]/body/div[8]/div/button').click()
sleep(1)
data = []
deals = driver.find_element(By.XPATH, '//*[@id="divTrade"]/table[2]/tbody')
for row in deals.find_elements(By.TAG_NAME, 'tr'):
    cols = row.find_elements(By.TAG_NAME, 'td')
    data.append({f"col{i+1}": cols[i].text for i in range(len(cols))})

data0 = []
titles = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[3]/div[7]/div[2]/div[2]/table[2]/tbody/tr[2]/td/div/table[1]/tbody')
for row in titles.find_elements(By.TAG_NAME, 'tr'):
    cols = row.find_elements(By.TAG_NAME, 'th')
    data0.append({f"col{i+1}": cols[i].text for i in range(len(cols))})


for rows in data:
    data0.append(rows)

with open("test2.csv", 'w', newline='', encoding='utf-8') as file:
    fieldnames = [f"col{i+1}" for i in range(len(cols))]
    csv_wr = csv.DictWriter(file, fieldnames=fieldnames)
    csv_wr.writeheader()
    csv_wr.writerows(data0)

driver.quit()