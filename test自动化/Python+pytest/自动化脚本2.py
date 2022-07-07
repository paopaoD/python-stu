"""
前提条件：下载pytest
终端下载命令：pip install requirements.txt

"""
import time

import pytest
from selenium.webdriver.common.by import By
from webdriver_helper import get_webdriver


@pytest.fixture()
def driver():
    driver = get_webdriver()  # 启动浏览器
    driver.maximize_window()  # 浏览器最大化
    driver.get("http://101.34.221.219:8010/")  # 打开网址

    print("测试用例准备执行了")  # 前置的部分
    yield driver               # 生成器的写法，返回值

    print("测试用例执行结束了")  # 后置的部分
    driver.quit()


@pytest.fixture(scope="session")  #只登陆一次，不进行重复登录
def user_driver():
    """已经是登录状态的浏览器"""
    driver = get_webdriver()  # 启动浏览器

    driver.maximize_window()  # 浏览器最大化

    driver.get("http://101.34.221.219:8010/")  # 获取网址

    el = driver.find_element(By.LINK_TEXT, "登录")  #
    el.click()

    el = driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input"
    )
    el.send_keys("beifan")

    el = driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input"
    )
    el.send_keys("123123")

    el = driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button"
    )
    el.click()  # 登录成功

    msg = get_msg()

    assert msg == "登录成功"

    yield  driver

    driver.quit()

    time.sleep(0.5)


def get_msg(driver):
    time.sleep(2)  # 等待-0.5秒
    el = driver.find_element(By.XPATH, "//p[@class='prompt-msg']")
    return el.text


def alert(driver):
    time.sleep(2)
    driver.switch_to.alert.accept() # 弹窗点击确定


def test_login_ok(driver):
    """登陆成功"""
    el = driver.find_element(By.LINK_TEXT, "登录")  #
    el.click()             #点击左上角登录

    el = driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input"
    )
    el.send_keys("beifan")     # 输入账号

    el = driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input"
    )
    el.send_keys("123123")     # 输入密码

    el = driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button"
    )
    el.click()  # 登录成功

    msg = get_msg( driver)

    assert msg == '登录成功'


def test_login_fail(driver):
    """登录失败"""
    el = driver.find_element(By.LINK_TEXT, "登录")  #
    el.click()  # 3

    el = driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input"
    )  # 4
    el.send_keys("beifan")  # 5

    el = driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input"
    )
    el.send_keys("1231231")  # 7

    el = driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button"
    )
    el.click()  # 登录失败

    msg = get_msg(driver)

    assert msg == '密码错误'


def test_order_ok(user_driver):
    """测试下单成功"""

    time.sleep(0.5)  # 等待0.5s

    user_driver.get("http://101.34.221.219:8010/")  # 回到首页

    el = user_driver.find_element(By.PARTIAL_LINK_TEXT, "vivo")  # 选择商品
    el.click()

    user_driver.switch_to.window(user_driver.window_handles[-1])  # 窗口最新打开的切换

    time.sleep(0.5)  # 等待0.5s

    el = user_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[2]/div[2]/div/div[3]/div[2]/button[1]"
    )
    el.click()  # 立即购买

    alert(user_driver)  # 处理弹窗

    el = user_driver.find_element(By.XPATH,
                                  "/html/body/div[4]/div/div[4]/ul/li[1]/span"
    )
    el.click()  # 点击付款方式

    alert(user_driver)  # 处理弹窗

    el = user_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div/div[6]/div/form/div/button"
    )
    el.click()  # 点击提交订单

    msg = get_msg(user_driver)  # 获取系统提示

    assert msg == "操作成功"


@pytest.mark.xfail
def test_order_fail(user_driver):
    """测试下单失败"""

    user_driver.get("http://101.34.221.219:8010/")  # 回到首页

    el = user_driver.find_element(By.PARTIAL_LINK_TEXT, "北方手机")  # 选择商品
    el.click()
























