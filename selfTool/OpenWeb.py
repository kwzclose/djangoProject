
import ddddocr
import option as option
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import webbrowser ,sys
from selenium.webdriver.common.by import By

from time import sleep, time

class TestKeyWords(object):

    #初始化
    def __init__(self,browser_type):
        self.open_browser(browser_type)
    #调用浏览器
    def open_browser(self,browser_type):
        #定义全局变量
        global driver
        if browser_type == 'chrome':
            driver = webdriver.Chrome()
            driver.get('http://aflm.cf-finance.com/login?redirect=%2Findex')
            # sleep(2)
            #
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input').send_keys('wangze')
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input').send_keys('cf#2022')
            # orc = ddddocr.DdddOcr()
            # element = driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div[2]/img')
            # element.screenshot('sss.png')
            #
            # with open('sss.png', 'rb') as f:
            #     klk = orc.classification(f.read())
            # print("识别结果", klk)
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div[1]/input').send_keys(klk)
            #
            # sleep(3)
            # driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[4]/div/button').click()



        elif browser_type == 'firefox':
            driver = webdriver.Firefox()
        else:
            print('type error')

if __name__ == '__main__':
    TestKeyWords('chrome')
