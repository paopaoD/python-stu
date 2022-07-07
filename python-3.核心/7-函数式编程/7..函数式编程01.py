# @Project   : Python
# @File      : 7..函数式编程01.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/15, 16:26
#

'''
    函数式编程
            函数作为参数
                自定义高阶函数 ：common 内的 list_helper.py
                内置高阶函数
'''


def fun01():
    print("fun01执行！")

# 调用方法，执行方法体
re01 = fun01()
print(re01)

# 将函数赋值给变量
re02 = fun01
# 通过变量，调用函数
re02()

def fun02():
    print("fun02执行！")

# 将函数作为函数的参数进行传递
# 将一个函数的代码，注入到另一个函数中
def fun03(func):
    print("fun03执行！")
    func()       # 将fun01或fun02函数的代码 注入到fun03函数内部

fun03(fun01)
fun03(fun02)




'''
    函数式编程   思想

'''

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


####
# 需求1：获取攻击力倍数大于6的所有技能
def find_atk01():
    for item in list_skill:
        if item.atk_ratio > 6:
            yield item

# 需求2：获取持续时间在4--11之间的所有技能
def find_atk02():
    for item in list_skill:
        if 4 < item.duration < 11:
            yield item

# 需求3：获取技能名称大于4个字，并且持续时间小于6的技能
def find_atk03():
    for item in list_skill:
        if len(item.name) > 4 and item.duration < 6:
            yield item



print("-------------->  函数式编程思想：         ")
#####  函数式编程思想：


# 1 将三个需求的变化点分别提取出来，单独定义在 条件函数 中 --- 相当于是“封装” 分而治之
def condition01(item):
    return item.atk_ratio > 6

def condition02(item):
    return 4 < item.duration < 11

def condition03(item):
    return len(item.name) > 4 and item.duration < 6


# 2 再将相同的 定义函数，
# 将三个变化点定义的函数作为函数的参数进行传递
# 注入到此函数中                           --- 相当于是 “继承” 隔离变化
def find_atk(func_condition):
    '''
        通用的查找方法
    :param func_condition:查找条件，函数类型
                函数名(变量) --> 返回bool类型
    :return:
    '''
    for item in list_skill:
        # 不能调用具体的条件函数condition01/02/03，
        # 所以相当于是给三个条件函数 定义一个父类 -> func_condition ，
        # 调用父类，但是 执行时分别执行的是每个子类 条件函数的方法， --- 相当于是“多态”
        if func_condition(item):  # 将condition01/02/03函数的代码 注入到find_atk函数内部
            yield item


# 调用第一个需求   只需将定义的 条件函数 作为参数传入
for item in find_atk(condition01):
    print(item)

print("``````")
# 调用第二个需求
for item in find_atk(condition02):
    print(item.__dict__)

print("``````")
# 调用第三个需求
for item in find_atk(condition03):
    print(item.__dict__)


































