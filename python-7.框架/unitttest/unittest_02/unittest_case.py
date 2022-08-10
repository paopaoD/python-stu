# @Project   : Python
# @File      : unittest_case.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/23, 11:10
#
'''
    python-8.自动化

        接口框架  unittest

'''


import json
import requests


#***unittest框架***#

# 1，导入unittest模块
import unittest



# 2，创建一个扩展类的 类 unittest.TestCase    放置不同的接口代码
class TestCaseOne(unittest.TestCase):

    # 后台登录
    def test_backstageLogin(self):
        interface_url = 'http://b.qdsgvision.com:40001/mock/388/system/backstageLogin'  # 接口文档存放地址
        interface_method = "post"  # 请求方法
        interface_params = {
            "account": "zxn001",  # 账号
            "password": "qdsg2020",  # 密码
            "phone": "",  #
        }

        # 2,发起请求
        response = requests.request(
            url=interface_url,
            method=interface_method,
            params=interface_params
        )

        # 3,对接口返回值进行判断
        text_result = response.text  # 接口返回的文本内容
        print("接口返回值：", text_result)
        json_result = json.loads(text_result)
        assert json_result.get("success") == True, "接口异常"  # 断言
        print("测试结束")


    # 后台用户账号详情
    def test_backstageUserInfo(self):
        # 1,接口url
        interface_url = 'http://b.qdsgvision.com:40001/mock/460/devOps/application/business/add'  # 接口文档存放地址
        interface_method = "post"  # 请求方法
        # interface_params = {
        #     "id": "",  # 账号
        #     "password": "",  # 密码
        #     "title": "",  # 名称
        # }  # 请求参数

        # 2,发起请求
        response = requests.request(
            url=interface_url,
            method=interface_method,
            # params=interface_params
        )

        # 3,对接口返回值进行判断
        text_result = response.text  # 接口返回的文本内容
        print("接口返回值：", text_result)
        json_result = json.loads(text_result)
        assert json_result.get("success") == True, "接口异常"  # 断言
        print("测试结束")


    # 登录账号所拥有权限
    def test_permissions(self):
        # 1,梳理接口文档
        interface_url = 'http://b.qdsgvision.com:40001/mock/388/permission/backstage/permissions'  # 接口文档存放地址
        interface_method = "get"  # 请求方法
        # interface_params = {
        #     "id": "",  # 账号
        #     "password": "",  # 密码
        #     "title": "",  # 名称
        # }  # 请求参数

        # 2,发起请求
        response = requests.request(
            url=interface_url,
            method=interface_method,
            # params=interface_params
        )

        # 3,对接口返回值进行判断
        text_result = response.text  # 接口返回的文本内容
        print("接口返回值：", text_result)
        json_result = json.loads(text_result)
        assert json_result.get("success") == True, "接口异常"  # 断言
        print("测试结束")







































