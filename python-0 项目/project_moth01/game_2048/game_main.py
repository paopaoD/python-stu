# @Project   : Python
# @File      : game_main.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/22, 12:09
#


# from game_ui import GameConsoleView
#
#
# # 测试
# if __name__ == "__main__":
#     view = GameConsoleView()
#     view.main()



import random
import time

import uiautomation as auto


# 添加扫描项目

def add_items(body, kind, value, name):  # 拍摄结构、扫描方式、参数、预期结果

    # 判断扫描项目界面是否打开
    if not auto.RadioButtonControl(AutomationId="IDrabtnOS").Exists():
        # 打开扫描项目界面
        auto.CheckBoxControl(AutomationId="IDaddscanchk").Click()

    # 随机左右眼
    eye = random.choice(["IDrabtnOD", "IDrabtnOS"])
    # 选择左右眼
    auto.RadioButtonControl(AutomationId=eye).Click()
    # 选择拍摄结构
    auto.RadioButtonControl(AutomationId=body).Click()
    # 选择扫描方式
    auto.RadioButtonControl(AutomationId=kind).Click()
    # 选择扫描参数
    auto.RadioButtonControl(AutomationId=value).Click()
    # 点击  添加到扫描项  按钮
    auto.ButtonControl(AutomationId="IDbtnAddToScan").Click()


    alert = auto.WindowControl(AutomationId="IDMessageBox").Exists()
    print(alert)
    if alert == True:
        auto.WindowControl(AutomationId="IDMessageBox").ButtonControl(AutomationId="Close").Click()

    but = auto.ButtonControl(AutomationId="Close").Exists()
    print(but)





    # if alert == True:
    #     auto.ButtonControl(AutomationId="Close").Click()


    # try:
    #     # 获取已添加扫描项列表视图
    #     add_item = auto.ListControl(AutomationId="IDlstBoxListView").GetFirstChildControl()
    #     # print(add_item)
    #     # 获取扫描项目 实际名称
    #     true_name = add_item.GetChildren()[0].Name + add_item.GetChildren()[1].Name
    #
    #     # 判断左右眼
    #     if eye == "IDrabtnOD":
    #         direction = "Od"
    #     else:
    #         direction = "Os"
    #     # 获取扫描项目 期望名称
    #     except_name = name + direction
    #
    #     assert true_name == except_name
    #
    # # 如果断言错误，则打印说明，但不中断测试流程
    # except:
    #
    #     raise AssertionError ("断言错误!项目期望名称和项目实际名称不一样。")




add_items("IDrabtnMacula", "IDrabtnCubicScan", "IDrabtn1212mm", '黄斑,12x12mm Area Scan')




































