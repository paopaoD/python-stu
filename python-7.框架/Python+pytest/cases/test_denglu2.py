'''
    类级别 的初始化、清除 分别在整个类的测试用例执行前后执行，并且只会执行1次
'''
import pytest


@pytest.mark.登录测试       # 给整个类加上标签
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



class Test_错误密码4:

    @pytest.mark.smoke
    def test_C004021(self):
        print('\n用例C001021')
        assert 1 == 1

    def test_C004022(self):
        print('\n用例C001022')
        assert 2 == 2


#   终端执行：
# pytest cases -m  -sv
# pytest cases -m smoke -sv     执行标签 smoke 用例

if __name__ == '__main__':
    pytest.main(["-v","test_denglu2.py"])





