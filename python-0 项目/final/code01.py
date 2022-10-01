"""

"""
from pathlib import Path


class MyClass(object):
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        # 默认：判断地址
        # return id(self) == id(other)
        # 重写:判断内容
        return self.data == other.data


m1 = MyClass(10)
m2 = MyClass(10)
print(m1 is m2)  # 判断内存地址  False
print(m1 == m2)  # 根据__eq__判断  False/True

list01 = [10]  # list
list02 = [10]
print(list01 is list02)  # False
print(list01 == list02)  # True

# 结论:重写__eq__根据内容比较,不重写根据地址比较

# 140727239287280 不是 140727238810848
print(4 is not None)  # True
# print(id(4))
# print(id(None))

# 相对路径
p1 = Path("../../month01/day06", "homework", "exercise01.py")
print(p1)
print(p1.exists())

# 绝对路径
p2 = Path.cwd().joinpath("../../month01/day06", "homework", "exercise01.py")
print(p2)
print(p2.exists())