# @Project   : Python
# @File      : ddt_case.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/23, 14:07
#

import json

import ddt
import requests
from parameterized import parameterized
from parametrize import parametrize

'''
    DDT + unittest  数据驱动机制
        
        作用：可以解决同一个接口多组测试数据的场景
'''


#***unittest框架***#

# 1，导入unittest模块
import unittest


# 2，创建一个扩展类的 类 unittest.TestCase    放置不同的接口代码
@ddt.ddt
class TestCaseThree(unittest.TestCase):
    response = None

    @classmethod
    def setUpClass(self):
        print("测试开始，清除数据")
        self.response = None


    # 导入ddt模块  将 某个 需要替换的数据 写为参数，比如 user_id
    @ddt.data("zxn001","12356","25847")
    def test_backstageLogin(self,user_id):    #   后台登录
        interface_url = 'http://b.qdsgvision.com:40001/mock/388/system/backstageLogin'  # 接口文档存放地址
        interface_method = "post"  # 请求方法
        interface_params = {
            "account": user_id,  # 账号
            "password": "qdsg2020",  # 密码
            "phone": "",  #
        }

        # 2,发起请求
        self.response = requests.request(
            url=interface_url,
            method=interface_method,
            params=interface_params
        )

        # 3,对接口返回值进行判断
        text_result = self.response.text  # 接口返回的文本内容
        print("接口返回值：", text_result)
        json_result = json.loads(text_result)
        assert json_result.get("success") == True, "接口异常"  # 断言
        print("测试结束")



    # 导入ddt模块  将 某些 需要替换的数据 写为字典参数，比如 data
    @ddt.data(
        {
            "applicationId": "1111",    # number	必须		应用id,application的主键
            "name": "zs",               # string	必须		业务组名称
            "orgType": "10",            # number	必须		机构类型:10-学校,20-医院,30-政府部门,40-社会筛查机构
            "resourceList": "[1,2]",    # object[]	必须		资源集合 ,BusinessResourceQuery
            "resourceType": "1",        # number	必须		资源类型,0-登记表,1-结果记录表,2-结果记录表(复测),3-误差记录表,4-报表模板,5-视力标准模板
            "resourceId": "10001",      # number	必须		资源id
        },
        {
            "applicationId": "1111",
            "name": "zs",
            "orgType": "10",
            "resourceList": "[1,2]",
            "resourceId": "10001",
        }
    )

    # 业务模板管理 新增
    def test_business_add(self,data):
        # 1,接口url
        interface_url = 'http://b.qdsgvision.com:40001/mock/460/devOps/application/business/add'  # 接口文档存放地址
        interface_method = "post"  # 请求方法
        interface_params = data

        # 2,发起请求
        self.response = requests.request(
            url=interface_url,
            method=interface_method,
            params=interface_params
        )


    def tearDown(self):
        # fixture
        # tearDown() 每个测试方法结束后执行一遍(常用于清理工作)
        text_result = self.response.text  # 接口返回的文本内容
        print("接口返回值：", text_result)
        json_result = json.loads(text_result)
        assert json_result.get("success") == True, "接口异常"  # 断言
        print("测试结束")



class ddt(parametrize):
    pass

class Ddt(parameterized):
    pass
