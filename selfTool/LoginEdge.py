import ddddocr
import option as option
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.by import By

from time import sleep, time

class  LoginUp:
       optionN = webdriver.EdgeOptions()
       optionN.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
       optionN.add_experimental_option("detach", True)
       selusername='lixuemei'
       '''
        YANGFAN-CX
         chencong1
         jiangliangliang
         ningbin
         YSHZ
         ZHUJIANI
         BTSQ
       '''



       driver = webdriver.Edge(options=optionN)
       driver.maximize_window()
       driver.get('http://aflm.cf-finance.com/login?redirect=%2Findex')
       sleep(1)

       driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input').send_keys(selusername)
       driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input').send_keys('cf#2022')
       orc = ddddocr.DdddOcr()
       element = driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div[2]/img')
       element.screenshot('sss.png')

       with open('sss.png', 'rb') as f:
            klk = orc.classification(f.read())
       print("识别结果", klk)
       driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div[1]/input').send_keys(klk)


       driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[4]/div/button').click()














