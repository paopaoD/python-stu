'''
    类级别 的初始化、清除 分别在整个类的测试用例执行前后执行，并且只会执行1次
'''
import pytest

def setup_module():
    print('\n *** 初始化-模块 ***')


def teardown_module():
    print('\n ***   清除-模块 ***')

@pytest.mark.登录测试
class Test_错误密码3:

    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')

    @pytest.mark.smoke
    def test_C003001(self):
        print('\n用例C001001')
        assert 1 == 1

    def test_C003002(self):
        print('\n用例C001002')
        assert 2 == 2

    def test_C003003(self):
        print('\n用例C001003')
        assert 3 == 2


class Test_错误密码4:

    @pytest.mark.smoke
    def test_C004021(self):
        print('\n用例C001021')
        assert 1 == 1

    def test_C004022(self):
        print('\n用例C001022')
        assert 2 == 2