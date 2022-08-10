'''
    登录代码
'''
import pytest

from lib.webui import login_test

class Test_错误登录:

    def test_ui_001(self):      # 账号为空
        print("\n ---开始执行---")
        alertText = login_test(None,"88888888")
        assert alertText == "请输入用户名"

    def test_ui_002(self):
        print("\n ---开始执行---")
        alertText = login_test("byhy",None)
        assert alertText == "请输入密码"

    def test_ui_003(self):
        print("\n ---开始执行---")
        alertText = login_test("byh","88888888")
        assert alertText == "登录失败 : 用户名或者密码错误"



'''
    数据驱动
'''

# class Test_错误登录2:
#
#     @pytest.mark.parametrize('username,password,expectedalert',[
#         (None, "88888888",'请输入用户名'),
#         ('hyby', None,'请输入密码'),
#         ("byh", 8888888,"登录失败 : 用户名或者密码错误"),
#         ("byhy", 888888,"登录失败 : 用户名或者密码错误"),
#         ("byhy", 888888888,"登录失败 : 用户名或者密码错误")
#     ]
#                             )
#
#     def test_ui_001_005(self, username, password, expectedalert):
#         print("\n ---开始执行---")
#         alertText = login_test(username, password)
#         assert alertText == expectedalert



















