# @Project   : Python
# @File      : 5.1.1 多继承.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/10, 18:30
#
'''
    多继承:
        一个子类继承两个，或两个以上的基类，父类中的属性和方法同时
        同名方法的解析顺序(MRO,Method Resolution Order)

    类自身---> 父类继承列表(从左到右)--->再找上层父类
'''

class A:
    def m01(self):
        print("A - m01")

class B(A):
    def m01(self):  # def m02(self): # 如果B类中没有m01方法，那就调用C的
        print("B - m01")

class C(A):
    def m01(self):  # def m03(self): # 如果B，C类中都没有m01方法，才会调用A的
        print("C - m01")

# 多继承，不仅继承了B,C  还继承了它们的上层父类A
class D(B,C):
    def m02(self):
        self.m01()


d01 = D()
d01.m02()   # 调用D类方法时，首先调用B类中方法

# d01.m02()   # 如果B类中没有该m01方法，那就调用C的
# d01.m02()   # 如果B，C类中都没有m01方法，才会调用A的




















































































