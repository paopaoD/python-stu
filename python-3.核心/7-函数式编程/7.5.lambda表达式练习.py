# @Project   : Python
# @File      : 7.5.lambda表达式练习.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/18, 12:26
#



class Enemy:
    def __init__(self,name,blood,attack,phylactic):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.phylactic = phylactic

    #    定义行为变量
    def print_behavior_info(self):
        print(f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}。")

    def __str__(self):
        return f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}"


list01 = [
    Enemy("玄冥",5000,205,15),
    Enemy("灭霸",86,55,13),
    Enemy("成昆",0,100,10),
    Enemy("谢逊",300,15,8),
]

# 练习：定义敌人类  姓名，血量，基础攻击力，防御力
#      创建敌人列表，使用list_helper实现下列功能
#       1 查找姓名是"灭霸"的敌人对象
#       2 查找攻击力大于10所有敌人
#       3 查找活的敌人数量

from common.list_helper import *

#       1 查找姓名是"灭霸"的敌人对象
result01 = ListHelper.find_all(list01,lambda item:item.name =="灭霸")
print(result01)


print("----")
#       2 查找攻击力大于10所有敌人
result02 = ListHelper.find_num(list01,lambda item:item.attack >10)
for item in result02:
    print(item)


print("--***--")
########  2 查找攻击力大于10所有敌人的某几个(前2个  最后2个)
generater_result = ListHelper.find_num(list01,lambda item:item.attack >10)

# 将得到的生成器 转为 列表     ------>  惰性操作 ---> 立即操作
list_result = list(generater_result)
# 获取攻击力大于10所有敌人的前2个
for item in list_result[:2]:
    print(item)


print("----")
#       3 查找活的敌人数量
result03 = ListHelper.get_skill_count(list01,lambda item:item.blood>0)
print("活的敌人数量",result03)




print("---------------练习2 ------------------------")

# 练习2：在list_helper中增加判断是否存在某个对象的方法，返回值：True或False
#      1 判断敌人列表中是否存在“成昆”
#      2 判断敌人列表中是否存在攻击力小于5 或者防御力小于10的敌人
#

'''
def find():
    for item in list01:
        if item.name == "成昆":
            return True
    return False

def find02():
    for item in list01:
        if item.attack < 5 or item.phylactic < 10:
            return True
    return False

# 提取变化点
def condition01(item):
    return item.name == "成昆"

def condition02(item):
    return item.attack < 5 or item.phylactic < 10

# 提取不变点
def is_exists(list_target,func_condition):
    for item in list_target:
        if func_condition(item):
            return True
    return False
'''

from common.list_helper import *

#      1 判断敌人列表中是否存在“成昆”
exist01 = ListHelper.is_exists(list01,lambda item:item.name == "成昆")
print(exist01)


#      2 判断敌人列表中是否存在攻击力小于5 或者防御力小于10的敌人
exist02 = ListHelper.is_exists(list01,lambda item:item.attack < 5 or item.phylactic < 10)
print(exist02)





print("---------------练习 3------------------------")

class Enemy:
    def __init__(self,name,blood,attack,phylactic):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.phylactic = phylactic

    #    定义行为变量
    def print_behavior_info(self):
        print(f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}。")

    def __str__(self):
        return f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}"

list01 = [
    Enemy("玄冥",5000,205,15),
    Enemy("灭霸",86,55,13),
    Enemy("成昆",0,100,10),
    Enemy("谢逊",300,15,8),
]

# 练习：在list_helper中增加通用的求和方法
#   1，计算列表中索引敌人的总血量
#   2，计算列表中索引敌人的总攻击力
#   3，计算列表中索引敌人的总防御力

from common.list_helper import *


#   1，计算列表中索引敌人的总血量
sum_result01 = ListHelper.sum_condition(list01,lambda item:item.blood )
print(sum_result01)

#   2，计算列表中索引敌人的总攻击力
sum_result02 = ListHelper.sum_condition(list01,lambda item:item.attack )
print(sum_result02)

#   3，计算列表中索引敌人的总防御力
sum_result03 = ListHelper.sum_condition(list01,lambda item:item.phylactic)
print(sum_result03)






print("---------------练习 4------------------------")

class Enemy:
    def __init__(self,name,blood,attack,phylactic):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.phylactic = phylactic

    #    定义行为变量
    def print_behavior_info(self):
        print(f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}。")

    def __str__(self):
        return f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}"

list01 = [
    Enemy("玄冥",5000,205,15),
    Enemy("灭霸",86,55,13),
    Enemy("成昆",0,100,10),
    Enemy("谢逊",300,15,8),
]

# 练习：在list_helper中增加通用的筛选方法

# 1，获取敌人列表中所有敌人的名称
# 2，获取敌人列表中所有敌人的攻击力
# 1，获取敌人列表中所有敌人的名称和血量

from common.list_helper import *

# def select_info():
#     list_result = []
#     for item in list01:
#         list_result.append(item.name)
#     return list_result

# 1，获取敌人列表中所有敌人的名称

re01 = ListHelper.select_info(list01,lambda item:item.name)
print(re01)

# 2，获取敌人列表中所有敌人的攻击力
re02 = ListHelper.select_info(list01,lambda item:item.attack)
print(re02)

# 3，获取敌人列表中所有敌人的名称和血量
re03 = ListHelper.select_info(list01,lambda item:(item.name,item.blood))
print(re03)                                         # 元组的形式

# re03 = ListHelper.get_all_info(list01,lambda item:[item.name,item.blood])
# print(re03)                                         # 列表的形式
#
# re03 = ListHelper.get_all_info(list01,lambda item:{item.name:item.blood})
# print(re03)                                         # 字典的形式






print("---------------练习 5------------------------")

class Enemy:
    def __init__(self,name,blood,attack,phylactic):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.phylactic = phylactic

    #    定义行为变量
    def print_behavior_info(self):
        print(f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}。")

    def __str__(self):
        return f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}"

list01 = [
    Enemy("玄冥",5000,205,15),
    Enemy("灭霸",86,55,13),
    Enemy("成昆",0,100,10),
    Enemy("谢逊",300,15,8),
]

# 练习：在list_helper中增加通用的 **获取最大值 方法

# 1，获取敌人列表中 攻击力最大的敌人
# 2，获取敌人列表中 防御力最大的敌人
# 3，获取敌人列表中 血量最高的敌人

# 处理逻辑的推导代码
'''
def max():
    max_vaule = list01[0]
    for i in range(1,len(list01)):
        if max_vaule.attack < list01[i].attack:
            max_vaule = list01[i]
    return max_vaule

# 提取不同点
def handle01(item):
    return item.attack

def handle02(item):
    return item.phylactic

def handle03(item):
    return item.blood


# 提取相同点
def get_max(func_handle):
    max_vaule = list01[0]
    for i in range(1,len(list01)):
        # if max_vaule.attack < list01[i].attack:
        if func_handle(max_vaule) < func_handle(list01[i]):
            max_vaule = list01[i]
    return max_vaule

print(get_max(handle01))
'''

from common.list_helper import *


# 1，获取敌人列表中 攻击力最大的敌人
re01 = ListHelper.select_max(list01,lambda item:item.attack)
print(re01)

# 2，获取敌人列表中 防御力最大的敌人
re02 = ListHelper.select_max(list01,lambda item:item.phylactic)
print(re02)

# 3，获取敌人列表中 血量最高的敌人
re03 = ListHelper.select_max(list01,lambda item:item.blood)
print(re03)




print("---------------练习 6------------------------")

# 练习：在list_helper中增加通用的 **获取最小值 方法

# 1，获取敌人列表中 攻击力最小的敌人
re = ListHelper.select_min(list01,lambda item:item.attack)
print(re)






print("---------------练习 7------------------------")

class Enemy:
    def __init__(self,name,blood,attack,phylactic):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.phylactic = phylactic

    #    定义行为变量
    def print_behavior_info(self):
        print(f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}。")

    def __str__(self):
        return f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}"

list01 = [
    Enemy("玄冥",5000,205,15),
    Enemy("灭霸",86,55,20),
    Enemy("成昆",0,100,10),
    Enemy("谢逊",300,15,16),
]

# 练习：在list_helper中增加通用的 **升序排列 方法

# 1，将敌人列表 按攻击力升序排列
# 2，将敌人列表中 按防御力升序排列
# 3，将敌人列表中 按血量升序排列

# # 处理逻辑的推导过程代码
'''
def select_max_info():
    for i in range(len(list01)-1):
        for c in range(i,len(list01)):
            if list01[i].attack > list01[c].attack:
                list01[i],list01[c] = list01[c],list01[i]
    

select_max_info()
for item in list01:
    print(item)
'''

# 1，将敌人列表 按攻击力升序排列
ListHelper.order_by(list01,lambda item:item.attack)
for item in list01:
    print(item)

# 2，将敌人列表中 按防御力升序排列
ListHelper.order_by(list01,lambda item:item.phylactic)
for item in list01:
    print(item)

# 3，将敌人列表中 按血量升序排列
ListHelper.order_by(list01,lambda item:item.blood)
for item in list01:
    print(item)



print("---------------练习 8------------------------")

# 练习：在list_helper中增加通用的 **降序排列 方法

# 1，将敌人列表 按攻击力降序排列
re = ListHelper.order_by_desc(list01,lambda item:item.attack)
for item in list01:
    print(item)






print("---------------练习 9------------------------")

class Enemy:
    def __init__(self,name,blood,attack,phylactic):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.phylactic = phylactic

    #    定义行为变量
    def print_behavior_info(self):
        print(f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}。")

    # 将对象转换为字符串
    def __str__(self):
        return f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}"

list01 = [
    Enemy("玄冥",5000,205,15),
    Enemy("灭霸",86,55,20),
    Enemy("成昆",0,100,10),
    Enemy("谢逊",300,15,16),
]

# 练习：在list_helper中增加通用的 **根据指定条件删除元素 方法

# 1，将敌人列表 删除所有死人
# 2，将敌人列表中 删除攻击力小于50的所有敌人
# 3，将敌人列表中 删除防御力大于100的所有敌人

# 推导代码
"""
def delete():
    for i in range(len(list01)-1,-1,-1):
        if list01[i].blood ==0:
            del list01[i]

re = delete()
for item in list01:
    print(item)
    

def handle01(item):
    return item.blood ==0

def handle02(item):
    return item.attack <50

def handle03(item):
    return item.phylactic >100


def delete01(func_condition):
    # 使用正向索引，倒叙删除
    for i in range(len(list01)-1,-1,-1):
        # if handle01(item):
        if func_condition(list01[i]):
            del list01[i]
"""


from common.list_helper import *

# 1，将敌人列表 删除所有死人
re01 = ListHelper.deletea_all(list01,lambda item:item.blood == 0)
for item in list01:
    print(item)

print()
# 2，将敌人列表中 删除攻击力小于50的所有敌人
re02 = ListHelper.deletea_all(list01,lambda item:item.attack <50)
for item in list01:
    print(item)

print()
# 3，将敌人列表中 删除防御力大于100的所有敌人
re03 = ListHelper.deletea_all(list01,lambda item:item.phylactic >100)
for item in list01:
    print(item)



# print(".....")
# def delete01():
#     # 使用正向索引，倒叙删除
#     for i in range(-1,-len(list01),-1,):
#         if list01[i].attack < 100:
#             del list01[i]
#
# delete01()
# for item in list01:
#     print(item)

































