import ddddocr
import option as option
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import webbrowser ,sys
from selenium.webdriver.common.by import By

from time import sleep, time

class  LoginUp:

       try:
             option = webdriver.ChromeOptions()
             option.add_experimental_option("detach", True)
             selusername='wangze'

             driver = webdriver.Chrome(options=option)
             driver.maximize_window()
             driver.get('https://ls.cf-finance.com/hlsprod/login.screen')
             sleep(1)

             driver.find_element(By.ID, 'ext-gen3').send_keys(selusername)
             driver.find_element(By.ID, 'ext-gen4').send_keys('qwerty123456')

             driver.find_element(By.ID, 'ext-gen6').click()
             driver.find_element(By.XPATH, '//*[@id ="ext-gen16"]').click()
             # driver.find_element(By.ID, 'ext-gen22').click()


             orc = ddddocr.DdddOcr()
             element = driver.find_element(By.ID, 'code')
             element.screenshot('ssso.png')

             with open('ssso.png', 'rb') as f:
                  klk = orc.classification(f.read())
             print("识别结果", klk)
             driver.find_element(By.ID, 'ext-gen10').send_keys(klk)


             driver.find_element(By.ID, 'btn_1').click()


       except Exception as  e:
             print("流程过程中没有抓取到页面的元素")
             # print(e)



       finally:
            pass
             # print("流程结束")
             # driver.close()







