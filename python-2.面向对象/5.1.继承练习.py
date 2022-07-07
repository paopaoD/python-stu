# @Project   : Python
# @File      : 5.1.继承练习.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/9, 15:52
#
print("-------------------------------练习1---------------------------------")
'''
    一个手雷炸了，可能伤害敌人/玩家的生命
                还可能伤害未知事物(鸭子，房子...)

    要求:增加新事物，不影响手雷

    体会：继承的作用
         多态的体现
         设计原则：开闭原则，单一职责，依赖倒置
'''

# 客户端代码
class Grenades: # 定义手雷
    def __init__(self,atk):
        self.atk = atk

    def explode(self,heart):
        # 加判断，判断变量传入的是否是 父类类型 受害者
        if not isinstance(heart,Damageable):
            raise ValueError("传入的不是Damageable的子类")
        else:
            print("手雷爆炸")
            # 调用 敌人/玩家 的父类  执行的还是子类的方法
            # 相当于是子类方法覆盖了父类的方法，也叫覆写/重写
            heart.get_attack(self.atk)


# 定义父类 受害者
class Damageable:
    '''
        受害者  父类
    '''
    def get_attack(self,value):
        # 如果子类 不重写，则异常
        raise NotImplementedError()

# 子类  敌人类
class Enemy(Damageable):
    def __init__(self,blood):
        self.blood = blood

    def get_attack(self,value):
        self.blood -= value
        print(f"敌人受到{value}伤害,剩余{self.blood}血量")

# 子类  玩家类
class Player(Damageable):
    def __init__(self,hp):
        self.hp = hp

    def get_attack(self,value):
        self.hp -= value
        print(f"敌人受到{value}伤害,剩余{self.hp}血量")

'''
g01 = Grenades(50)
e01 = Enemy(100)
p01 = Player(200)

g01.explode(e01)
g01.explode(e01)

g01.explode(p01)
'''



print("-------------------------------练习2---------------------------------")
'''
    定义图形管理器类
            1,管理所以图形
            2,提供计算所有图形总面积的方法
            
    具体图形：
            圆形面积
            矩形面积
    测试：
        创建1个圆形对象，1个矩形对象，添加到图形管理器中
        调用图形管理器的计算面积方法，输出结果
        
    要求：
        增加新图形，不修改图形管理器的代码
    
    体会：
        面向对象三大特征:封装/继承/多态
        面向对象设计原则：开闭/单一/倒置
'''

# 客户端代码  定义图形管理器
class GraphicsManager:
    def __init__(self):
        self.__graphics = []

    # 添加到图形管理器中
    def add_graphic(self,graphic):
        if not isinstance(graphic,Graph):
            raise ValueError("不是Graph子类")
        else:
            self.__graphics.append(graphic)

    # 计算总面积
    def get_total_area(self):
        total_area = 0
        # 遍历图形列表，累加每个图形的面积
        for item in self.__graphics:
            # 调用的是父类 图形方法   执行的是子类 圆形，矩形的方法  多态
            total_area += item.calculate_area()
        return total_area



# 定义父类  图形
class Graph:
    def calculate_area(self):
        '''
            计算面积
        '''
        # 如果子类不重写，则异常
        raise NotImplementedError()

# 定义子类 圆形
class Round(Graph):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

# 定义子类 矩形
class Rectangle(Graph):
    def __init__(self,long,wide):
        self.long = long
        self.wide = wide

    def calculate_area(self):
        return self.long * self.wide


# 测试
'''
g01 = GraphicsManager()
r01 = Round(10)
r02 = Rectangle(2,3)

g01.add_graphic(r02)
g01.add_graphic(r01)

print(g01.get_total_area())
'''






print("-------------------------------练习3---------------------------------")
'''
    定义员工管理器
            1,管理所有员工
            2,计算所有员工工资
    员工:
            程序员：底薪+项目分红
            销售：底薪 + 销售额 * 0.05
            ....
    要求：增加新岗位，员工管理器不变

'''
# 客户端代码  定义员工管理器
class EmployeeManager:
    def __init__(self):
        self.__employees = []

    # 管理所有员工
    def add_employee(self,employee):
        if not isinstance(employee,Employee):
            raise ValueError("不是Employee子类")
        else:
            self.__employees.append(employee)

    # 计算所有员工工资
    def get_total_salary(self):
        total_salary = 0
        for item in self.__employees:
            total_salary += item.calculate_salary()
        return total_salary


# 定义父类  员工
class Employee:
    # 底薪是共性 可以提取到父类中
    def __init__(self,basic):
        self.basic = basic  # 底薪

    # 计算薪资
    def calculate_salary(self):
        '''
            计算薪资
        '''
        return self.basic

# 定义子类 程序员
class Programmer(Employee):
    def __init__(self,basic,bonus):
        # 父类中已经定义了底薪   所以子类只需要调用即可
        super().__init__(basic)
        self.bonus = bonus  # 项目分红

    def calculate_salary(self):
        return self.basic + self.bonus

# 定义子类 销售
class Market(Employee):
    def __init__(self,basic,sale):
        # 父类中已经定义了底薪   所以子类只需要调用即可
        super().__init__(basic)
        self.sale = sale    # 销售额

    def calculate_salary(self):
        return self.basic + self.sale * 0.05


e01 = EmployeeManager()
p01 = Programmer(1000,1000)
m01 = Market(2000,300)

e01.add_employee(p01)
print(e01.get_total_salary())

e01.add_employee(m01)
print(e01.get_total_salary())












