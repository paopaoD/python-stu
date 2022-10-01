import time

import pyautogui
import uiautomation as auto
# from lib import DesktopController
#
# # # 前置条件，每个用例执行前
# # def setup_module():
# #     result = DesktopController()
# #     result.open_wechat()
#
#
# # 桌面操作
# class DesktopView:
#
#     def open_wechat(self):
#
#         result = DesktopController()
#         result.open_wechat()
#
#         wechat_win = auto.WindowControl(Name="微信",ClassName="WeChatMainWndForPC")
#
#         # 点击左上角 聊天 模式
#         p01 = wechat_win.ButtonControl(Name="聊天")
#         p01.Click()
#
#         # 遍历回话列表
#         p02 = wechat_win.ListControl(Name="会话")
#
#         # 获取列表内数据
#         P01 = p02.GetChildren()
#
#         # 遍历列表
#         for people in P01[1:15]:
#             print(people.Name)
#             if people.Name == "文件传输助手":
#                 # 如果符合，就点击输入
#                 wechat_win.ListItemControl(Name=people.Name).Click()
#
#                 time.sleep(2)
#
#                 wechat_win.EditControl(Name="输入")
#
#                 wechat_win.SendKeys("优美胜于丑陋（Python 以编写优美的代码为目标）\n")
#
#                 time.sleep(2)
#                 # wechat_win.SendKeys('{Enter}')
#
#                 wechat_win.SendKeys("这是我用自动化写的代码")
#                 # wechat_win.SendKeys('{Enter}')
#
#         # 测试鼠标移动到微信中心
#         wechat_win.MoveCursorToMyCenter()




# if __name__ == '__main__':
#     re = DesktopView()
#     re.print_info()


class TestLoginMethod:

    # 打开 OCT2020 80k 软件
    @staticmethod
    def open_octa():
        # 点击任务栏
        desktop = auto.PaneControl(Name='任务栏')
        desktop.Click()

        # Win+D ,显示桌面
        desktop.SendKeys('{Win}d')

        # 获取桌面
        octa_win = auto.ListControl(Name="")

        # 获取桌面应用列表
        a02 = octa_win.GetChildren()
        # print(a02)    # 打印子列表内容

        for item in a02:
            if item.Name == "OCT2020 80k":
                octa_win.ListItemControl(Name=item.Name).DoubleClick()

        time.sleep(25)

    # 登录页面
    @staticmethod
    def Test_login(username, password):
        # 获取登录框
        win = auto.WindowControl(name="WinLogin")
        # 点击清除按钮
        win.ButtonControl(searchDepth=2, AutomationId="IDbtnLoginClear").Click()

        # 点击用户名输入框
        win.EditControl(searchDepth=2, AutomationId="IDtxtLoginNameInput").Click()
        if username is not None:
            pyautogui.typewrite(username)   # 输入用户名
        # 点击密码输入框
        win.EditControl(searchDepth=2, AutomationId="IDcomLoginPasswordInput").Click()
        if password is not None:
            pyautogui.typewrite(password)  # 输入密码

        # 点击登录按钮
        win.ButtonControl(searchDepth=2, AutomationId="IDbtnLoginLogin").Click()

        # alertText = auto.TextControl(searchDepth=2, AutomationId="IDtxtloginTips").Name
        #
        # return alertText

    # 关闭登录页面
    @staticmethod
    def close_octa():
        # 登录框
        octa_win = auto.WindowControl(name="WinLogin")
        # 点击取消按钮
        octa_win.ButtonControl(searchDepth=2, AutomationId="IDbtnLoginCancel").Click()


class TestPatientMethod:
    # 打开 并成功登录
    @staticmethod
    def open_and_login(username,password):
            # 点击任务栏
            desktop = auto.PaneControl(Name='任务栏')
            desktop.Click()

            # Win+D ,显示桌面
            desktop.SendKeys('{Win}d')
            # 获取桌面
            octa_win = auto.ListControl(Name="")
            # 获取桌面应用列表
            a02 = octa_win.GetChildren()
            # 遍历桌面应用 找到OCT2020 80k 打开
            for item in a02:
                if item.Name == "OCT2020 80k":
                    octa_win.ListItemControl(Name=item.Name).DoubleClick()

            time.sleep(25)
            # 获取登录框
            win = auto.WindowControl(name="WinLogin")
            # 点击清除按钮
            win.ButtonControl(searchDepth=2, AutomationId="IDbtnLoginClear").Click()

            # 点击用户名输入框
            win.EditControl(searchDepth=2, AutomationId="IDtxtLoginNameInput").Click()
            pyautogui.typewrite(username)  # 输入用户名
            # 点击密码输入框
            win.EditControl(searchDepth=2, AutomationId="IDcomLoginPasswordInput").Click()
            pyautogui.typewrite(password)  # 输入密码

            # 点击登录按钮
            win.ButtonControl(searchDepth=2, AutomationId="IDbtnLoginLogin").Click()

    # 定义添加用户界面清空信息函数
    @staticmethod
    def add_clean():
        # 点击添加按钮
        auto.CheckBoxControl(AutomationId="IDchkAddCancel").Click()
        # 点击清除按钮
        auto.CheckBoxControl(searchDepth=5, AutomationId="IDchkClearUp").Click()
        # 点击选择日期
        auto.EditControl(AutomationId="PART_TextBox").Click()
        pyautogui.hotkey('ctrl', 'a')  # 全选
        pyautogui.hotkey('backspace')  # 删除

    # 定义随机选择性别函数
    @staticmethod
    def select_male():
        for num in range(2):
            if num:
                auto.ComboBoxControl(AutomationId="IDcombobSex").Select(itemName='男')
            else:
                auto.ComboBoxControl(AutomationId="IDcombobSex").Select(itemName='女')

    # 成功登录 到 患者页面
    @staticmethod
    def patient_test(patient_name,malenum,doctor_name,bornday,medicaltxt):

        TestPatientMethod.open_and_login("admin","admin@123")

        time.sleep(5)


        patient_win = auto.CustomControl(ClassName="PatientCon")
        # CustomControl
        # PatientCon
        # PatientQueue


        # 点击添加按钮
        patient_win.CheckBoxControl(AutomationId="IDchkAddCancel").Click()

        # 添加患者姓名
        patient_win.EditControl(AutomationId="IDtxtNameInput").SendKeys(patient_name)

        # 选择性别
        if malenum is not None:
            TestPatientMethod.select_male()

        # 添加医生姓名
        auto.EditControl(AutomationId="IDtxtDoctorInput").SendKeys(doctor_name)

        # 添加出生日期
        auto.EditControl(AutomationId="PART_TextBox").SendKeys(bornday)

        # 添加病例号
        auto.EditControl(AutomationId="IDtxtCaseNumberInput").SendKeys(medicaltxt)

        # 点击确认
        auto.CheckBoxControl(AutomationId="IDchkConfirm").Click()

        alertText = auto.TextControl(searchDepth=2, AutomationId="IDtxtloginTips").Name

        return alertText



re = TestPatientMethod()

re.patient_test("","男","zs",'1996/10/14','10086')