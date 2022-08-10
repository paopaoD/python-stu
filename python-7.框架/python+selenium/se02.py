'''
    se02
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
sleep(3)
driver.find_element(By.ID,value="kw").send_keys("selenium")
sleep(1)
driver.find_element(By.ID,value="su").click()
sleep(1)
# driver.find_element(By.LINK_TEXT,value="百度首页").click()
driver.find_element(By.XPATH,
                    value="//div[@id='3']/h3/a").click()
# '//*[@id="3"]/h3/a'
sleep(5)
driver.quit()

