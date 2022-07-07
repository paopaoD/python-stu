#
# @Project   :Python
# @File         :自动化脚本.py
# @Time       :2022/5/13,21:44
#

# 对于大部分的定位策略，
# 其底层，是使用CSS或者XPath实现
# 对于CSS和XPath的底层，是通过什么实现的？
# 通过js
#
# import keyword
# print(keyword.kwlist)  #可以查看那些字符不能使用
#
# 终端下载驱动：pip install webdriver-helper
import time

from selenium.webdriver.common.by import By
from webdriver_helper import get_webdriver



def get_msg():
    '''
        系统提示
    :return:
    '''
    time.sleep(0.5) # 等待-0.5秒
    el = driver.find_element(By.XPATH, "//p[@class='prompt-msg']")
    return el.text


def alert():
    '''
         处理弹窗
    :return:
    '''
    time.sleep(2)
    driver.switch_to.alert.accept() # 弹窗点击确定


driver = get_webdriver()                         # 启动浏览器

driver.maximize_window()                        # 浏览器最大化

driver.get("http://101.34.221.219:8010/")      # 获取网址


el = driver.find_element(By.LINK_TEXT, "登录")
el.click()                                      #点击左上角登录按钮

el = driver.find_element(
    By.XPATH,
    "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input")

el.send_keys("beifan")                          # 输入账号


el = driver.find_element(
    By.XPATH,
    "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input"
)
el.send_keys("123123")                           # 输入密码


el = driver.find_element(
    By.XPATH,
    "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button"
)

el.click()                                        # 点击登录

msg = get_msg()                                # 系统提示登录成功


assert msg == "登录成功"                         #设置断言：登录成功。查看是否和系统提示的相同

time.sleep(0.5)                               #等待0.5s

driver.get("http://101.34.221.219:8010/")    # 回到首页

el = driver.find_element(By.PARTIAL_LINK_TEXT, "vivo") # 选择商品
el.click()

driver.switch_to.window(driver.window_handles[-1]) # 窗口最新打开的切换

time.sleep(0.5)                           #等待0.5s

el = driver.find_element(
    By.XPATH,
    "/html/body/div[4]/div[2]/div[2]/div/div[3]/div[2]/button[1]"
)
el.click()                              # 立即购买

alert()                                 # 处理弹窗

el = driver.find_element(
    By.XPATH,
    "/html/body/div[4]/div/div[4]/ul/li[1]/span"
)
el.click()                         #点击付款方式

alert()                             #处理弹窗

el = driver.find_element(
    By.XPATH,
    "/html/body/div[4]/div/div[6]/div/form/div/button"
)
el.click()                          #点击提交订单

msg = get_msg()                    # 获取系统提示
assert msg == "操作成功"

alert()                               #处理弹窗


driver.quit()                       #关闭浏览器












