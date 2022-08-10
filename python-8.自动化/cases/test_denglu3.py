'''
    方法级别  的初始化、清除 分别在类的每个测试方法执行前后执行，并且每个用例分别执行1次
'''
import pytest


def setup_module():
    print('\n *** 初始化-模块 ***')


def teardown_module():
    print('\n ***   清除-模块 ***')


class Test_错误密码5:

    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')

    def setup_method(self):
        print('\n --- 初始化-方法  ---')

    def teardown_method(self):
        print('\n --- 清除  -方法 ---')

    @pytest.mark.smoke
    def test_C005001(self):
        print('\n用例C001001')
        assert 1 == 1

    def test_C005002(self):
        print('\n用例C001002')
        assert 2 == 2

    def test_C005003(self):
        print('\n用例C001003')
        assert 3 == 2


class Test_错误密码6:

    @pytest.mark.smoke
    def test_C006021(self):
        print('\n用例C001021')
        assert 1 == 1

    def test_C006022(self):
        print('\n用例C001022')
        assert 2 == 2