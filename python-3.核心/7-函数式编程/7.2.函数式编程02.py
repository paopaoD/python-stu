# @Project   : Python
# @File      : 7.2.函数式编程02.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/17, 16:06
#
'''
    将不变的部分，提取出来，放到另一个模块中
    使用时，直接导入

'''

# 导入列表助手模块中 列表助手类
from common.list_helper import *


class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio  # 攻击力倍数
        self.duration = duration    # 持续时间

    def __str__(self):
        return f"技能是：{self.name}，编号是{self.id}，攻击倍数是{self.atk_ratio}，持续时间是{self.duration}"

list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2),
]


## 函数式编程思想：

def condition01(item):
    return item.atk_ratio > 6

def condition02(item):
    return 4 < item.duration < 11

def condition03(item):
    return len(item.name) > 4 and item.duration < 6


# 将不变的点 统一放到共同的模块list_helper中
'''
def find_atk(func_condition):
    for item in list_skill:
        if func_condition(item):  
            yield item
'''



generate01 = ListHelper.find_num(list_skill,condition01)

for item in generate01:
    print(item.__dict__)



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
        return f"技能是：{self.name}，编号是{self.id}，攻击倍数是{self.atk_ratio}，持续时间是{self.duration}"

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








































































