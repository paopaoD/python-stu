

"""
程序窗口:uiautomation.WindowControl
按钮:uiautomation.ButtonControl
文本:uiautomation.TextControl
输入窗口:uiautomation.EditControl
文档控件:uiautomation.DocumentControl
单选控件:uiautomation.CheckBoxControl
复选控件:uiautomation.ComboBoxControl
日历控件:uiautomation.CalendarControl
"""
import time

import uiautomation as auto


# 打开微信
def open_wechat():
    # 点击任务栏
    desktop = auto.PaneControl(Name='任务栏')
    desktop.Click()

    # Win+D ,显示桌面
    desktop.SendKeys('{Win}d')

    wechat_win = auto.ListControl(Name="")

    a02 = wechat_win.GetChildren()
    print(a02)

    for item in a02:
        if item.Name == "微信":
            wechat_win.ListItemControl(Name="微信").DoubleClick()

def input_info():
    open_wechat()

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











# # 添加扫描项目
# def add_items(body, kind, value, name):  # 拍摄结构、扫描方式、参数、预期结果
#     print("开始")
#     # 随机左右眼
#     eye = random.choice(["IDrabtnOD", "IDrabtnOS"])
#     # 判断扫描项目界面是否打开
#     if uiautomation.RadioButtonControl(AutomationId="IDrabtnOS").Exists():
#         pass
#     else:
#         # 打开扫描项目界面
#         uiautomation.CheckBoxControl(AutomationId="IDaddscanchk").Click()
#     # 选择左右眼
#     uiautomation.RadioButtonControl(AutomationId=eye).Click()
#     # 选择拍摄结构
#     uiautomation.RadioButtonControl(AutomationId=body).Click()
#     # 选择扫描方式
#     uiautomation.RadioButtonControl(AutomationId=kind).Click()
#     # 选择扫描参数
#     uiautomation.RadioButtonControl(AutomationId=value).Click()
#     # 添加到扫描项
#     uiautomation.ButtonControl(AutomationId="IDbtnAddToScan").Click()
#     # 判断左右眼
#     if eye == "IDrabtnOD":
#         direction = "OD"
#     else:
#         direction = "OS"
#     # 获取期望添加的扫描项目
#     except_name = name + direction
#     print(except_name)
#
#     # 获取已添加扫描项列表视图
#     add_item = uiautomation.ListControl(AutomationId="IDlstBoxListView").GetFirstChildControl()
#     print(add_item)
#
#     # 获取实际添加的扫描项目名称
#     true_name = add_item.GetChildren()[0].Name + add_item.GetChildren()[1].Name
#     print(true_name)
#
#     assert true_name == except_name, '新加扫描项目实际与预期名称不一致'
#     # 逻辑修改后，添加扫描项后。相机会重新刷新
#     time.sleep(5)
#
# add_items("IDrabtnMacula", "IDrabtnCubicScan", "IDrabtn66mm", '黄斑,6x6mm Area Scan')
#
# # 点击捕获  拍摄照片
# def save():
#     """捕获，保存图片"""
#     if len(uiautomation.ListControl().GetChildren()) > 0:
#         # 点击捕获按钮
#         uiautomation.ButtonControl(AutomationId="IDbtnCapture").Click()
#         # 等待拍摄完成
#         time.sleep(3.5)
#         # 测试取消按钮
#         uiautomation.ButtonControl(AutomationId="IDbtnCancel").Click()
#         time.sleep(3.5)
#         # 新逻辑取消后会重新刷新相机，此处为等待刷新
#         uiautomation.ButtonControl(AutomationId="IDbtnCapture").Click()
#         # 重新拍摄
#         time.sleep(3.5)
#         # 等待拍摄完成
#         uiautomation.ButtonControl(AutomationId="IDbtnSave").Click()
#         # 测试保存按钮
#         time.sleep(5)
#         # 等待分析页面加载
#     else:
#         logging.info('扫描项列表添加不成功')
#
# save()



# def loginInput(username, password):  # 定义用户名密码测试输入函数
#     win.ButtonControl(searchDepth=2, AutomationId="IDbtnLoginClear").Click()  # 点击清除按钮
#     # win.EditControl(AutomationId="IDtxtLoginNameInput").SendKeys(username)  # 点击用户名输入框
#     win.EditControl(searchDepth=2, AutomationId="IDtxtLoginNameInput").Click()   # 点击用户名输入框
#     pyautogui.typewrite(username)   # 输入用户名
#     win.EditControl(searchDepth=2, AutomationId="IDcomLoginPasswordInput").Click()  # 点击密码输入框
#     pyautogui.typewrite(password)  # 输入密码
#     win.ButtonControl(searchDepth=2, AutomationId="IDbtnLoginLogin").Click()  # 点击登录按钮






# def scan_button(button_name):
#     a.RadioButtonControl(AutomationId=button_name).Click()
#     a.RadioButtonControl(AutomationId=button_name).Click()

# def Click():
#     a.WindowControl(AutomationID="Window").Click()
#     time.sleep(3)
#     a.WindowControl(AutomationID="MainPage").Click()
#     time.sleep(2)
#     a.ButtonControl(AutomationID="IDbtnHost").Click()
#     time.sleep(3)
#     a.ButtonControl(AutomationID="IDbtnHost").Click()
#     time.sleep(3)
#
#     a.ButtonControl(AutomationId="IDbtnSearch").Click()




# def test02(self):
#     """找到名称为有次的病人"""
#     uiautomation.EditControl(AutomationId="IDtxtSearchText").SendKeys('{Ctrl}a')  # 全选搜索框
#     uiautomation.EditControl(AutomationId="IDtxtSearchText").SendKeys('{Delete}')  # 删除
#     uiautomation.EditControl(AutomationId="IDtxtSearchText").SendKeys('有次')  # 在搜索框输入新建的病人名
#     uiautomation.ButtonControl(AutomationId="IDbtnSearch").Click()  # 点击搜索按钮
#     name = uiautomation.ListControl(AutomationId="IDlstBoxPatient").GetFirstChildControl().GetFirstChildControl().Name
#     assert name == '有次', '没有查询到名字为有次的病人'



