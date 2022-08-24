# @Project   : Python
# @File      : 5.1.0多态.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/22, 17:37
#

'''
    多态

    设计原则：
            1,开--闭原则
            2,类的单一职责
            3,依赖倒置(依赖抽象)  定义父类
            4,组合复用原则
            5,里氏替换原则(继承后的重写)
            6,迪米特法则(类与类交互的原则)
'''





print("------------------------- 多态 ------------------------------")
'''
需求：老张开车去东北
        坐飞机
        乘火车
        ...
'''

# 客户端代码
class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,vehicle,str_position):
        ######## 多态：调用父类，执行子类
        # 调用的是父类(交通工具)的运输方法，执行的是子类 (汽车/飞机)的运输方法
        # 相当于是子类方法覆盖了父类的方法，也叫覆写/重写
        vehicle.transport(str_position)


# 定义交通工具父类
class Vehicle:
    '''
        交通工具
    '''
    # 继承 隔离子类变化，将子类的共性提取到父类中
    def transport(self,str_position):
        # 因为父类太过于抽象，所以写不出方法体
        pass

# 子类代码  继承 交通工具父类
class Car(Vehicle):
    def transport(self,str_position):
        print("汽车开到",str_position)

class Airplan(Vehicle):
    def transport(self,str_position):
        print("飞机飞到",str_position)





p01 = Person("老张")
c01 = Car()
a01 = Airplan()

p01.go_to(c01,"东北")# 调用的是父类交通工具的运输方法，执行的是汽车的运输方法
p01.go_to(a01,"东北")# 调用的是父类交通工具的运输方法，执行的是飞机的运输方法



















































