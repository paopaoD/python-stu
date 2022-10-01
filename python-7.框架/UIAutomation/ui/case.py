import time

import uiautomation as auto
from model import DesktopView



def input_info():
    a = DesktopView()
    a.open_wechat()

    wechat_win = auto.WindowControl(Name="微信",ClassName="WeChatMainWndForPC")

    # 点击左上角 聊天 模式
    p01 = wechat_win.ButtonControl(Name="聊天")
    p01.Click()

    # 遍历回话列表
    p02 = wechat_win.ListControl(Name="会话")

    # 获取列表内数据
    P01 = p02.GetChildren()

    # 遍历列表
    for people in P01[1:15]:
        print(people.Name)
        if people.Name == "文件传输助手":
            # 如果符合，就点击输入
            wechat_win.ListItemControl(Name=people.Name).Click()

            time.sleep(2)

            wechat_win.EditControl(Name="输入")

            wechat_win.SendKeys("优美胜于丑陋（Python 以编写优美的代码为目标）\n")

            time.sleep(2)
            # wechat_win.SendKeys('{Enter}')

            wechat_win.SendKeys("这是我用自动化写的代码")
            # wechat_win.SendKeys('{Enter}')

    # 测试鼠标移动到微信中心
    wechat_win.MoveCursorToMyCenter()