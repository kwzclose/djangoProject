import ddddocr
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

URL = 'http://aflm.cf-finance.com/login?redirect=%2Findex'
USERNAME = 'wangze'
PASSWORD = 'cf#2022'
SCREENSHOT_PATH = 'sss.png'
contract_number = 'CON230700040'

# linum 这个字段中[1]代表选择了下拉列表中的第几个角色
linum = '//li[1]'
project_number = ''


class LoginUp:
    def __init__(self):
        self.driver = self.setup_driver()
        self.ocr = ddddocr.DdddOcr()

    @staticmethod
    def setup_driver():
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=option)
        driver.maximize_window()
        return driver

    def login(self):
        self.driver.get(URL)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input').send_keys(USERNAME)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input').send_keys(PASSWORD)
        self.handle_captcha()
        self.handle_Select()

    def handle_captcha(self):
        element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div[2]/img')
        element.screenshot(SCREENSHOT_PATH)
        with open(SCREENSHOT_PATH, 'rb') as f:
            captcha_text = self.ocr.classification(f.read())
        print("识别结果", captcha_text)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div[1]/input').send_keys(captcha_text)
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()

    def handle_Select(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//div/div[2]/div/div/input").click()
        # 超级用户第一个选项
        self.driver.find_element(By.XPATH, linum).click()
        # 超级用户第三个选项
        # driver.find_element(By.XPATH, "//li[3]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'确 定')]").click()

        # 进入页面，在订单管理页面进行查询操作
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//span[contains(., '订单管理')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(., '案件查询')]").click()
        self.driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/section/div/form/div[3]/div/div/input').send_keys(contract_number)
        self.driver.find_element(By.XPATH, '//div[@id="app"]/div/div[2]/section/div/form/div[2]/div/div/input').send_keys(project_number)
        self.driver.find_element(By.XPATH, "//span[contains(.,'搜索')]").click()


if __name__ == "__main__":
    login = LoginUp()
    login.login()
