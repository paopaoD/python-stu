# @Project   : Python
# @File      : module01.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/13, 15:00
#

# 定义：当前模块内的那些成员可以被 from 模块 import * 导入
__all__ = ["fun01","MyClass04","_fun03"]


print("123")


def fun01():
    print("234")


class MyClass02:
    def fun02(self):
        print("12345")




# 前面加下划线   表示隐藏该成员方法
def _fun03():
    print("模块03中的")


class MyClass04:
    @staticmethod
    def fun04():
        print("模块03中的_03")





print(__name__)