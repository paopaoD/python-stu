# @Project   : Python
# @File      : fixture_case.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/23, 13:32
#

'''
#   使用 fixture 封装
'''

# setUp() 每个测试方法运行前执行一次(常用于初始化工作)

# tearDown() 每个测试方法结束后执行一次(常用于清理工作)

# setUpClass() 所有测试方法运行前执行一次，必须用@classmethod装饰器进行装饰

# tearDownClass() 所有测试方法结束后执行一次，必须用@classmethod装饰器进行装饰


import json
import requests


#***unittest框架***#

# 1，导入unittest模块
import unittest


# 2，创建一个扩展类的 类 unittest.TestCase    放置不同的接口代码
class TestCaseTwo(unittest.TestCase):
    response = None

    # 每个测试方法运行前执行一次(常用于初始化工作)
    def setUp(self):
        print("测试开始，清除数据")
        self.response = None

    '''
    # 或写为：
    @classmethod
    def setUpClass(cls) -> None:
        print("测试开始，清除数据")
        cls.response = None
    '''


    # 后台登录
    def test_backstageLogin(self):
        # 接口文档存放地址
        url = 'http://b.qdsgvision.com:40001/mock/388/system/backstageLogin'
        # 请求方法
        method = "post"
        # 参数
        params = {
            "account": "zxn001",  # 账号
            "password": "qdsg2020",  # 密码
            "phone": "",  #
        }

        # 发起请求
        self.response = requests.request(
            url=url,
            method=method,
            params=params
        )


    # 业务模板管理 新增
    def test_business_add(self):
        # 1,接口url
        interface_url = 'http://b.qdsgvision.com:40001/mock/460/devOps/application/business/add'  # 接口文档存放地址
        interface_method = "post"  # 请求方法
        interface_params = {
            "applicationId": "1111",    # number	必须		应用id,application的主键
            "name": "zs",               # string	必须		业务组名称
            "orgType": "10",            # number	必须		机构类型:10-学校,20-医院,30-政府部门,40-社会筛查机构
            "resourceList": "[1,2]",    # object[]	必须		资源集合 ,BusinessResourceQuery
            "resourceType": "1",        # number	必须		资源类型,0-登记表,1-结果记录表,2-结果记录表(复测),3-误差记录表,4-报表模板,5-视力标准模板
            "resourceId": "10001",       # number	必须		资源id
        }

        # 2,发起请求
        self.response = requests.request(
            url=interface_url,
            method=interface_method,
            params=interface_params
        )


    # 应用下拉框
    def test_listBySearch(self):
        # 接口文档存放地址
        url = 'http://b.qdsgvision.com:40001/mock/460/application/listBySearch'
        method = "get"  # 请求方法
        params = {
            "keyword": "",  #  String
            "": "",  #
        }  #

        # 2,发起请求
        self.response = requests.request(
            url=url,
            method=method,
            params=params
        )


    # tearDown() 每个测试方法结束后执行一遍(常用于清理工作)
    def tearDown(self):
        '''
            将三个接口用例代码后固定的逻辑(断言)提取出来  封装在 fixture
        '''
        text_result = self.response.text  # 接口返回的文本内容
        # print("接口返回值：", text_result)
        json_result = json.loads(text_result)
        assert json_result.get("success") == True, "接口异常"  # 断言
        print("测试结束")

















































































