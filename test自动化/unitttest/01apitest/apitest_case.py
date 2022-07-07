# @Project   : Python
# @File      : apitest_case.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/23, 12:05
#

'''
    单个接口测试代码

'''

import json

import requests

#***原始代码***#    缺点：一个一个执行  效率慢

# 1,梳理接口文档
interface_url = ''              # 接口文档存放地址
interface_method = "post/get"   # 请求方法
interface_params = {
    "account":"zxn001",            # 账号
    "password":"qdsg2020",      # 密码
    "phone":"",         #
}                               # 请求参数

# 2,发起请求
response = requests.request(
    url=interface_url,
    method=interface_method,
    params=interface_params
)

# 3,对接口返回值进行判断
text_result = response.text # 接口返回的文本内容
print("接口返回值：",text_result)
json_result = json.loads(text_result)
assert json_result.get("success") == True,"接口异常"    # 断言
print("测试结束")






















































