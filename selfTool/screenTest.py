import ddddocr
import option as option
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.by import By

from time import sleep, time

orc = ddddocr.DdddOcr()

driver = webdriver.Chrome()
driver.get('http://aflm.cf-finance.com/login?redirect=%2Findex')
sleep(2)
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input').send_keys('wangze')
driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input').send_keys('cf#2022')

element = driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div[2]/img')
element.screenshot('sss.png')

with open('sss.png', 'rb') as f:
        klk = orc.classification(f.read())
print("识别结果", klk)
driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div[1]/input').send_keys(klk)
driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[4]/div/button').click()
time.sleep(10)





