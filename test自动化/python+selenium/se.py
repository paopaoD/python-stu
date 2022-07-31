'''
    selenium
'''

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        sleep(2)

    def id(self):
        self.driver.find_element(By.ID,value="kw").send_keys("selenium")
        sleep(1)
        self.driver.find_element(By.ID,value="su").click()
        sleep(1)
        # self.driver.back()
        # self.driver.quit()

    def name(self):
        self.driver.find_element(By.NAME,value="wd").send_keys("selenium")
        sleep(1)
        self.driver.find_element(By.ID,value="su").click()
        sleep(1)
        # self.driver.back()
        # self.driver.quit()

    def tag_name(self):
        input = self.driver.find_element(By.TAG_NAME,value="input")
        print(input)

    def class_name(self):
        self.driver.find_element(By.CLASS_NAME,value="s_ipt").send_keys("selenium")
        self.driver.find_element(By.ID,value="su").click()
        sleep(2)
        self.driver.quit()

    def link_text(self):
        self.id()
        self.driver.find_element(By.LINK_TEXT,value="百度首页").click()
        sleep(2)
        self.driver.quit()

    def partial_link_text(self):
        self.id()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, value="百度").click()
        sleep(2)
        self.driver.quit()

    def css_selector(self):
        self.driver.find_element(By.CSS_SELECTOR, value="#kw").send_keys("selenium")
        self.driver.find_element(By.ID,value="su").click()
        sleep(2)
        self.driver.quit()


    def xpath(self):
        self.driver.find_element(By.XPATH, value="//*[@id='kw']").send_keys("selenium")
        self.driver.find_element(By.ID,value="su").click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.id()
    # case.link_text()
    # case.partial_link_text()
    # case.name()
    # case.css_selector()
    # case.class_name()
    # case.tag_name()
    case.xpath()














