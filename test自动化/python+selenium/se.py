'''
    selenium
'''

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        sleep(2)

    def test_id(self):
        self.driver.find_element(By.ID,value="kw").send_keys("selenium")
        sleep(1)
        self.driver.find_element(By.ID,value="su").click()
        sleep(1)
        self.driver.back()
        self.driver.quit()

    def test_name(self):
        self.driver.find_element(By.NAME,value="wd").send_keys("selenium")
        sleep(1)
        self.driver.find_element(By.ID,value="su").click()
        sleep(1)
        self.driver.back()
        self.driver.quit()

    def test_tag_name(self):
        self.driver.find_element(By.TAG_NAME,value="kw").send_keys("selenium")

    def test_class_name(self):
        self.driver.find_element(By.CLASS_NAME,value="kw").send_keys("selenium")

    def test_xpath(self):
        self.driver.find_element(By.XPATH, value="kw").send_keys("selenium")

    def test_link_text(self):
        self.driver.find_element(By.LINK_TEXT,value="kw").send_keys("selenium")

    def test_partial_link_text(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, value="kw").send_keys("selenium")

    def test_css_selector(self):
        self.driver.find_element(By.CSS_SELECTOR, value="kw").send_keys("selenium")


if __name__ == '__main__':
    cs = TestCase()
    cs.test_id()




















