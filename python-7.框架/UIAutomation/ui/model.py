import time

import pyautogui
import uiautomation as auto

# class TestLoginMethod:
#     #
#     def open_wechat(self):
#         # 点击任务栏
#         desktop = auto.PaneControl(Name='任务栏')
#         desktop.Click()
#
#         # Win+D ,显示桌面
#         desktop.SendKeys('{Win}d')
#
#         # 获取桌面
#         wechat_win = auto.ListControl(Name="")
#
#         # 获取桌面应用列表
#         a02 = wechat_win.GetChildren()
#         print(a02)
#
#         for item in a02:
#             if item.Name == "腾讯QQ":
#                 wechat_win.ListItemControl(Name=item.Name).DoubleClick()
#
#         time.sleep(3)
#
#
#     def Test_login(self,username,password):
#         # 登录框
#         win = auto.WindowControl(Name="QQ",ClassName="TXGuiFoundation")
#         # # 点击清除按钮
#         # win.ButtonControl(searchDepth=2, AutomationId="IDbtnLoginClear").Click()
#
#         # # 点击用户名输入框
#         # win.EditControl(Name="QQ号码").Click()
#         #
#         # if username is not None:
#         #     win.EditControl(Name="").SendKeys(username)  # 输入用户名
#         #
#         # # 点击密码输入框
#         # win.EditControl(Name="密码").Click()
#         # if password is not None:
#         #     win.SendKeys(password)  # 输入密码
#
#         # 点击登录按钮
#         win.ButtonControl(searchDepth=2, Name="登录").Click()
#
#         alertText = auto.TextControl(searchDepth=2, AutomationId="IDtxtloginTips").Name
#
#         print(alertText)
#         # return alertText
#
#
# re = DesktopView()
# re.open_wechat()
# re.Test_login("123225","123")




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

            alertText = auto.TextControl(searchDepth=2, AutomationId="IDtxtloginTips").Name

            if alertText:       # 防止因为输入法错误导致输入的用户名密码错误
                # 点击清除按钮
                win.ButtonControl(searchDepth=2, AutomationId="IDbtnLoginClear").Click()

                # 点击用户名输入框
                win.EditControl(searchDepth=2, AutomationId="IDtxtLoginNameInput").Click()
                pyautogui.typewrite(username)  # 输入用户名
                pyautogui.hotkey('enter')

                time.sleep(1)
                # 点击密码输入框
                win.EditControl(searchDepth=2, AutomationId="IDcomLoginPasswordInput").Click()
                pyautogui.typewrite(password)  # 输入密码
                pyautogui.hotkey('enter')

                # 点击登录按钮
                win.ButtonControl(searchDepth=2, AutomationId="IDbtnLoginLogin").Click()

                time.sleep(2)

                # 点击添加按钮
                auto.CheckBoxControl(AutomationId="IDchkAddCancel").Click()

    # 定义添加用户界面清空信息函数
    @staticmethod
    def add_clean():

        # 点击清除按钮
        auto.CheckBoxControl(searchDepth=5, AutomationId="IDchkClearUp").Click()
        # 点击选择日期
        # auto.EditControl(AutomationId="PART_TextBox").Click()
        #
        # pyautogui.hotkey('ctrl', 'a')  # 全选
        # pyautogui.hotkey('backspace')  # 删除

        # 点击取消按钮
        auto.CheckBoxControl(AutomationId="IDchkAddCancel").Click()

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
        # 点击清除按钮
        auto.CheckBoxControl(searchDepth=5, AutomationId="IDchkClearUp").Click()
        time.sleep(2)
        # 获取登录后的页面
        auto.CustomControl(ClassName="PatientCon")
        # 点击添加按钮
        # auto.CheckBoxControl(AutomationId="IDchkAddCancel").Click()
        # 添加患者姓名
        if patient_name is not None:
            auto.EditControl(AutomationId="IDtxtNameInput").SendKeys(patient_name)

        # 选择性别
        if malenum is not None:
            TestPatientMethod.select_male()

        # 添加医生姓名
        if doctor_name is not None:
            auto.EditControl(AutomationId="IDtxtDoctorInput").SendKeys(doctor_name)

        # 添加出生日期
        if bornday is not None:
            auto.EditControl(AutomationId="PART_TextBox").SendKeys(bornday)

        # 添加病例号
        if medicaltxt is not None:
            auto.EditControl(AutomationId="IDtxtCaseNumberInput").SendKeys(medicaltxt)

        # 点击确认
        auto.CheckBoxControl(AutomationId="IDchkConfirm").Click()

        # self.assertEqual('姓名必须填写', auto.TextControl(AutomationId="IDtxtblockTips").Name)
        alertText = auto.TextControl(AutomationId="IDtxtblockTips").Name

        return alertText


re = TestPatientMethod
re.open_and_login("admin", "admin@123")
alertText = re.patient_test(None,"男","zs",'1996/10/14','10086')
print(alertText)