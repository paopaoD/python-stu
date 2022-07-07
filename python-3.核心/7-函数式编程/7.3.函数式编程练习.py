# @Project   : Python
# @File      : 7.3.函数式编程练习.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/17, 15:32
#

list01 = [43,4,55,6,7,87,9]
# 需求1：在列表中查找所有偶数
# 需求2：在列表中查找所有大于10的数
# 需求3：在列表中查找所有范围在10--50之间的数

# 1，使用生成器函数实现以上3个需求
# 2， 体会函数式编程

#####  生成器函数:
''''''
def find_num01():
    for item in list01:
        if item % 2 ==0:
            yield item

for item in find_num01():
    print(item)


def find_num02():
    for item in list01:
        if item > 10:
            yield item

for item in find_num02():
    print(item)


def find_num03():
    for item in list01:
        if 10 < item < 50:
            yield item

for item in find_num03():
    print(item)


print()



######  函数式编程:

# 将不同的条件提取出来  单独定义函数
def condition01(item):
    return item % 2 ==0

def condition02(item):
    return item > 10

def condition03(item):
    return 10 < item < 50


# 将三个变化点定义的函数作为函数的参数进行传递
# 注入到此find_num函数中
def find_num(func_condition):
    for item in list01:
        # 调用父类，执行每个子类方法
        if func_condition(item):
            yield item

for item in find_num(condition02):
    print(item)



print("---------------")

# 练习：在list_helper.py中,定义通用的查找满足条件的**单个**对象
# 案例：查找名称是“葵花宝典”的技能
# 案例：查找编号是101 的技能
# 案例：查找持续时间大于0 的技能
#
class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio  # 攻击力倍数
        self.duration = duration    # 持续时间

    def __str__(self):
        return f"技能是：{self.name}，编号是{self.id}，攻击倍数" \
               f"是{self.atk_ratio}，持续时间是{self.duration}"

list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2),
]


def condition01(item):
    return item.name == "葵花宝典"

def condition02(item):
    return item.id == 101

def condition03(item):
    return item.duration > 0


# def find_all(func_condition):
#     for item in list_skill:
#         if func_condition(item):
#             return item        # 因为查找的是单个对象，所以使用return



from common.list_helper import *

# 调用模块中的类 以及 方法
result01 = ListHelper.find_all(list_skill,condition03)
print(result01)






























