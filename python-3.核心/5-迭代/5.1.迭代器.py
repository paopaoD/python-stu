# @Project   : Python
# @File      : 5.1.迭代器.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/15, 18:09
#
'''
    迭代器

'''

# 定义 技能 类
class Skill:
    pass

# 定义 技能迭代器 类
class SkillIterator:
    def __init__(self,target):
        self.__target = target    # 接收的是 技能管理器类 中 __iter__方法 传递过来的数据
        self.index = 0          # 从索引为0 开始返回数据

    # 获取列表内的数据
    def __next__(self):
        # 增加条件，如果索引超出范围，停止
        if self.index > len(self.__target)-1:
            raise StopIteration

        # 返回下一个数据   从第一个(索引为0)开始
        temp = self.__target[self.index]
        self.index += 1
        return temp


# 定义 技能管理器 类
class Skillmanager:
    def __init__(self):
        self.__skills = []

    def add_skill(self,skill):
        self.__skills.append(skill)

    def __iter__(self):
        # 创建一个 技能迭代器 对象，并传递需要迭代的数据
        return SkillIterator(self.__skills)


manager = Skillmanager()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())


for item in manager:
    print(item)

# for循环原理是：
iterator = manager.__iter__()

while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break





print("------------------------------- 练习 ------------------------------------")

# 练习：图形管理器 记录多个图形.
#       迭代图形管理器对象


# 图形 类
class Graph:
    def __init__(self,long,wide):
        self.long = long
        self.wide = wide


# 图形迭代器
class GraphIterator:
    def __init__(self,target):
        self.__target = target
        self.__index = 0

    # 获取列表内的下一个数据
    def __next__(self):
        if self.__index > len(self.__target)-1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


# 图形管理器 类
class GraphManager:
    def __init__(self):
        self.__graphics = []

    def add_graph(self,value):
        self.__graphics.append(value)

    # 可迭代对象
    def __iter__(self):
        return GraphIterator(self.__graphics)


g01 = Graph(5,6)
manager01 = GraphManager()
manager01.add_graph(g01)


# for item in manager01:
#     print(item.__dict__)
iterator01 = manager01.__iter__()
while True:
    try:
        item = iterator01.__next__()
        print(item.__dict__)
    except StopIteration:
        break


'''
class Graph:
    def __init__(self,long,wide):
        self.long = long
        self.wide = wide


class GraphIterator:
    def __init__(self,target):
        self.__target = target
        self.index = 0

    def __next__(self):
        if self.index > len(self.__target)-1:
            raise StopIteration
        temp = self.__target[self.index]
        self.index += 1
        return temp


class GraphManager:
    def __init__(self):
        self.__graphics = []

    def add_graphics(self,value):
        return self.__graphics.append(value)

    def __iter__(self):
        return GraphIterator(self.__graphics)


manager = GraphManager()
manager.add_graphics(Graph(5,6))


for item in manager:
    print(item)

iterator = manager.__iter__()

while True:
    try:
        item = iterator.__next__()
        print(item.__dict__)
    except StopIteration:
        break
'''




print("------------------------------- 练习 ------------------------------------")

# 练习：员工管理器 记录多个员工.
#       迭代员工管理器对象

#  员工
class Employee:
    def __init__(self,name):
        self.name = name

# 员工管理器
class EmployeeManager:
    def __init__(self):
        self.__employees = []

    # 管理员工
    def add_employee(self,employee):
        self.__employees.append(employee)

    def __iter__(self):
        return EmployeeIterator(self.__employees)

# 员工迭代器
class EmployeeIterator:
    def __init__(self,target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target)-1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp



manager = EmployeeManager()
manager.add_employee(Employee("zs"))
manager.add_employee(Employee("ls"))

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item.__dict__)
    except StopIteration:
        break





print("------------------------------- 练习 ------------------------------------")

# 练习：定义 MyRange 类  实现下列功能
#
# for item in range(10):
#     print(item)


class MyRange:
    def __init__(self,stop_value):
        self.stop_value = stop_value

    def __iter__(self):
        return MyRangeIterator(self.stop_value)


class MyRangeIterator:
    def __init__(self,end_value):
        self.__end_value = end_value
        self.__start_value = 0

    def __next__(self):
        # 开始值 等于 最后的传入值   停止
        if self.__start_value == self.__end_value:
            raise StopIteration
        temp = self.__start_value
        self.__start_value += 1
        return temp



for item in MyRange(10):
    print(item)



















