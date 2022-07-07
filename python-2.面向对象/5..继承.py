# @Project   : Python
# @File      : 5..继承.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/8, 14:40
#

print("-------------------------继承 方法------------------------------")
'''
    继承：
        方法：
            代码：子类不用写，但是可以用父类的
            
            多个子类在概念上是一致的，所以就抽象出一个父类
            对个子类的共性，可以提取到父类中
            在实际开发过程中：
                    从设计角度讲：先有子类，再有父类
                    从代码角度讲：先有父类，再有子类
            
            定义父类：
                    动物(行为：叫)
            定义子类：
                    狗(行为：跑)
                    鸟(行为：飞)
'''


class Animal:
    def call(self):
        print("叫")


class Dog(Animal):
    def run(self):
        print("跑")

class Bird(Animal):
    def fly(self):
        print("飞")


A01 = Animal()
# 父类只能调用自己的行为成员，不能调用子类的行为成员
A01.call()

D01 = Dog()
# 子类不仅可以调用自己的行为成员，也可以调用父类行为成员
D01.call()
D01.run()

B01 = Bird()
# 子类不仅可以调用自己的行为成员，也可以调用父类行为成员
B01.call()
B01.fly()





print("-------------------------继承 内置函数------------------------------")

'''
    内置函数：
        isinstance(对象,类型)  判断一个对象是否属于一个类型
        issubclass(类型,类型)  判断一个类型是否属于另一个类型
'''

# isinstance 内置函数，判断一个对象是否属于一个类型
# "狗对象" 是 一个狗类型
print(isinstance(D01,Dog))      # True
# "狗对象" 不是 一个鸟类型
print(isinstance(D01,Bird))     # False
# "狗对象" 是 一个动物类型
print(isinstance(D01,Animal))   # True

# issubclass 内置函数，判断一个类型是否属于另一个类型
## 狗类型 不属于 鸟类型
print(issubclass(Dog,Bird))     # False
## 狗类型 属于 动物类型
print(issubclass(Dog,Animal))   # True
## 动物类型 不属于 鸟类型
print(issubclass(Animal,Bird))  # False





print("-------------------------继承 变量------------------------------")

'''
    继承：
        变量
        
'''

class Person:
    def __init__(self,name):
        self.name = name

# 子类若是没有构造函数，可以使用父类的
'''
class Student(Person):
    pass

s01 = Student()
print(s01.name)  
'''

# 子类若是具有构造函数，则必须先调用父类构造函数
class Student(Person):
    def __init__(self,name,score):
        # 子类若是具有构造函数，则必须先调用父类构造函数
        super().__init__(name)
        self.score = score

p01 = Person("李四")
print(p01.name)

p02 = Student("张三",100)
print(p02.name)
print(p02.score)



# 练习：定义父类：车(数据：品牌，速度)
#      定义子类：电动车(数据：电池容量，充电功率)

class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

class Electrocar(Car):
    def __init__(self,brand,speed,battery,power):
        # 父类中已经定义了品牌，速度   子类只需要调用即可
        super().__init__(brand,speed)
        self.battery = battery
        self.power = power

c01 = Car("宝马",200)
print(c01.brand)
print(c01.speed)


e01 = Electrocar("雅迪",60,10000,220)
print(e01.brand)
print(e01.speed)
print(e01.battery)
print(e01.power)




print("-------------------------继承 多态------------------------------")
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
        # 多态：调用父类，执行子类
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













'''
    类与类的关系
            1,泛化：子类与父类的关系，概念的复用，耦合度最高
                    做法：B类继承A类
                    
            2,关联(聚合/组合)：部分与整体的关系，功能的复用，变化影响一个方法
                    做法：在A类中包含B类成员
                    
            3,依赖：合作关系，一种相对松散的写作
                    做法：B类型作为A类中方法的参数，并不是A的成员
'''






















































