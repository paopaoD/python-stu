# @Project   : Python
# @File      : skip_case.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/23, 13:36
#


import json
import requests
import unittest



'''
    skip
        
        @unittest.skip(reason): 强制跳过。reason是跳转原因
        
        @unittest.skipIf(condition,reason):condition为True的时候跳过
        
        @unittest.skipUnless(condition,reason):condition为False的时候跳过
        
        @unittest.expectedFailure:如果test失败了，这个测试不计入失败的用例数目
        
'''



# 创建一个扩展类的 类 unittest.TestCase    放置不同的接口代码


class TestBBSTopic(unittest.TestCase):
    response = None


    def setUp(self) -> None:    # setUp() 每个测试方法运行前执行一次(常用于初始化工作)
        print("测试开始，清除数据")
        self.response = None

    # 或写为：
    '''
    @classmethod
    def setUpClass(cls) -> None:
        print("测试开始，清除数据")
        cls.response = None
    '''


    def tearDown(self):
        # fixture
        # tearDown() 每个测试方法结束后执行一遍(常用于清理工作)
        text_result = self.response.text  # 接口返回的文本内容
        print("接口返回值：", text_result)
        json_result = json.loads(text_result)
        assert json_result.get("success") == True, "接口异常"  # 断言
        print("测试结束")


    # 这里定义的 版本号和  __init__.py 中的版本号一样，执行，
    @unittest.skipUnless(test_api_version == 2.0,"此用例针对2.0版本进行测试")
    def test_backstageLogin(self):    # 后台登录
        interface_url = 'http://b.qdsgvision.com:40001/mock/388/system/backstageLogin'  # 接口文档存放地址
        interface_method = "post"
        interface_params = {
            "account": "zxn001",
            "password": "qdsg2020",
            "phone": "",
        }

        # 1,发起请求
        self.response = requests.request(
            url=interface_url,
            method=interface_method,
            params=interface_params
        )


    # 这里定义的版本号和 __init__.py 中的版本号不一样  跳过  不执行
    @unittest.skipUnless(test_api_version == 1.0,"此用例针对1.0版本进行测试")
    def test_business_add(self):    # 业务模板管理 新增
        # 1,接口url
        interface_url = 'http://b.qdsgvision.com:40001/mock/460/devOps/application/business/add'  # 接口文档存放地址
        interface_method = "post"
        interface_params = {
            "applicationId": "1111",
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


    @unittest.skipUnless(test_api_version >= 2.0,"此用例针对大于等于2.0版本进行测试")
    def test_listBySearch(self):    # 应用下拉框
        # 1,梳理接口文档
        interface_url = 'http://b.qdsgvision.com:40001/mock/460/application/listBySearch'  # 接口文档存放地址
        interface_method = "get"  # 请求方法
        interface_params = {
            "keyword": "",  #  String
            "": "",  #

        }  #

        # 2,发起请求
        self.response = requests.request(
            url=interface_url,
            method=interface_method,
            params=interface_params
        )    # 应用下拉框






































































