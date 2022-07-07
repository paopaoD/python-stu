# @Project   : Gitproject
# @File      : test_yaml.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/7/5, 10:31
#

'''
    接口自动化框架 YAML 数据驱动的封装

        @pytest.mark.parametrize(args_name,args_vaule)
        args_name:参数名
        args_vaule:参数值(使用list列表,tuple元组,字典列表,字典元组等)在数据中有多少个值，
                    那么接口用例就会执行多少次。


'''


import pytest

class TestCase:

    # 基础用法
    @pytest.mark.parametrize("args",["1","2","3"])
    def test_api01(self,args):
        print(args)

    # 引用类型
    @pytest.mark.parametrize("args",[["zs",13],["ls",15]])
    def test_api02(self,args):
        print(args)

    # 解包
    @pytest.mark.parametrize("name,age",[["zs",13],["ls",15]])
    def test_api03(self,name,age):
        print(name,age)







if __name__ == '__main__':
    pytest.main(["-vs","test_yaml.py"])
























































