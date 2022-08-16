'''
    初始化清除：
        模块级别 的初始化、清除 分别在整个模块的测试用例 执行前后执行，并且只会执行1次 。
'''
import pytest


def setup_module():
    print("\n *** 初始化-模块 ***")

def teardown_module():
    print("\n *** 清除-模块 ***")


class Test_错误密码1:

    @pytest.mark.smoke      # 标记 -->冒烟测试
    def test_C001001(self):
        print('\n用例C001001')
        # 通过断言 检测用例 (assert info == "用户名或密码错误")
        assert 1 == 1

    @pytest.mark.uitest      # 标记
    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2       #

    @pytest.mark.登录       # 标签  可以为中文
    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2


class Test_错误密码2:

    @pytest.mark.登录测试
    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1

    @pytest.mark.smoketest
    def test_C001022(self):
        print('\n用例C001022')
        assert 2 == 2


#   终端执行：-->首先 cd 到 用例所在的文件夹 内
# pytest cases -m  -sv
# pytest cases -m smoke -sv     执行标签 smoke 用例

# 或者：

if __name__ == '__main__':
    pytest.main(["-v","test_denglu.py"])















