'''
    对象库层
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



def login_test(username,password):

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)      # 显示等待
    driver.get("http://127.0.0.1/mgr/sign.html")
    # driver.get("https://www.baidu.com/")
    # driver.maximize_window()

    if username is not None:
        driver.find_element(By.ID,value="username").send_keys(username)

    if password is not None:
        driver.find_element(By.ID, value="password").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, value="button[type='submit']").click()

    time.sleep(2)

    alertText = driver.switch_to.alert.text

    driver.quit()

    return alertText

# 这个改变是因人而异

# 我在这里看到了

