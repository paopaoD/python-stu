# @Project   : Python
# @File      : 7.4.lambda表达式.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/17, 21:10
#

'''
    lambda ： 匿名函数
        作用：作为参数传递时，语法简洁优雅，代码可读性强
                随时创建和销毁，减少程序耦合度

        语法：
            变量 = lambda 形参：函数体
                注意：自带return
            调用：
                变量(实参)

        说明：
            形参没有可以不填
            函数体只能有一条语句，且不支持赋值语句


'''


###### lmmbda 示例:

# 无参数 --> lmmbda
def fun01():
    return 100

a = lambda : 100
re = a()
print(re)



# 多参数 --> lmmbda
def fun02(p1,p2):
    return p1 > p2

b = lambda p1,p2:p1 > p2
re = b(1,2)
print(re)



# 无返回值函数 --> lmmbda
def fun03(p1):
    print("参数是：",p1)

re = lambda p1:print("参数是：",p1)
re(100)



# 函数体只能有一条语句，且不支持赋值语句
def fun04(p1):
    p1 = 2

# d = lambda p1:p1 = 2



print("----------------------------lmmbda 示例:----------------------------------")

# 将相同点放入list-helper文件中
from common.list_helper import *

list01 = [43,4,5,5,6,7,87,9]

# 函数式编程写法:
'''
def condition01(item):
    return item % 2 ==0

def condition02(item):
    return item > 10

def condition03(item):
    return 10 < item < 50

for item in ListHelper.find_num(list01,condition02):
    print(item)
'''

# lambda表达式：
for item in ListHelper.find_num(list01,lambda item:item > 10):
    print(item)

for item in ListHelper.find_num(list01,lambda item:10<item<50):
    print(item)



print("------------------------lmmbda 练习:-------------------------")

# 练习：将下列 def定义的函数，改为使用lambda定义

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

# # def定义的函数
# def condition01(item):
#     return item.name == "葵花宝典"
#
# def condition02(item):
#     return item.id == 101
#
# def condition03(item):
#     return item.duration > 0


from common.list_helper import *


# lambda表达式：

# 1：查找名称是“葵花宝典”的技能
result01 = ListHelper.find_all(list_skill,lambda item:item.name == "葵花宝典")
print(result01)

# 2：查找编号是101 的技能
result01 = ListHelper.find_all(list_skill,lambda item:item.id == 101)
print(result01)

# 3：查找持续时间大于0 的技能
result01 = ListHelper.find_all(list_skill,lambda item:item.duration > 0)
print(result01)



print()

# 需求1：计算技能列表中 技能名称大于4个字的技能数量
# 需求2：计算技能列表中 技能持续时间小于等于5的技能数量

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

from common.list_helper import *


result02 = ListHelper.get_skill_count(list_skill,lambda item:len(item.name)>4)
print(result02)


result02 = ListHelper.get_skill_count(list_skill,lambda item:item.duration <=5)
print(result02)













