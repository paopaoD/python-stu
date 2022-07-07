# @Project   : Python
# @File      : 8..内置高阶函数.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/15, 16:27
#

'''
    内置高阶函数: 将函数作为参数或返回值的函数 就是高阶函数

        1,filter:根据条件筛选可迭代对象中的元素，返回值为新的可迭代对象

                filter(函数,可迭代对象)

        2,map:   使用可迭代对象中的每个元素调用函数，将返回值作为新的可
                    迭代对象元素，返回值为新可迭代对象

                map(函数,可迭代对象)

        3,max:  获取最大值

                max(可迭代对象,key= 函数)

        4,min:  获取最小值

                min(可迭代对象,key= 函数)

        5,sorted:
                -- 升序排列 ---> 内部返回新列表，使用时必须获取返回值

                sorted(可迭代对象,key= 函数)

                -- 降序排列

                sorted(可迭代对象,key= 函数,reverse = True)

'''




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

from common.list_helper import *


print('''-----------1,filter写法-----------''')
# 1,需求，获取所有死人
# lambda写法：
re = ListHelper.find_num(list01,lambda item:item.blood ==0)
for item in re:
    print(item)

# filter写法:相当于筛选敌人
re = filter(lambda item:item.blood ==0,list01)
for item in re:
    print(item)



print('''-----------2,map写法-------------''')
# 需求：获取所有敌人的姓名
# lambda写法：
re = ListHelper.select_info(list01,lambda item:item.name)
for item in re:
    print(item)

# map写法：返回的是某个元素
re = map(lambda item:item.name,list01)
for item in re:
    print(item)



print('''-----------2,max写法-------------''')
# 需求：获取血量最大的敌人
# lambda写法：
re = ListHelper.select_max(list01,lambda item:item.blood)
print(re)

# max写法：
re = max(list01,key=lambda item:item.blood)
print(re)


list03 = [2,5,6,9]
print(max(list03))  # 9


print('''-----------3,min写法-------------''')
# 需求：获取攻击力最小的敌人
# lambda写法：
re = ListHelper.select_min(list01,lambda item:item.attack)
print(re)


# min写法：
re = min(list01,key=lambda item:item.attack)
print(re)



list03 = [2,5,6,9]
print(min(list03))  # 2



print('''-----------2,sorted写法-------------''')
# 需求：将敌人列表 按攻击力升序排列

# lambda写法： --->  内部直接修改列表，使用时无需通过返回值获取数据
ListHelper.order_by(list01,lambda item:item.attack)
for item in list01:
    print(item)


# sortde写法：     ---> 内部返回新列表，使用时必须获取返回值
re = sorted(list01,key=lambda item:item.attack)
for item in re:
    print(item)

list02 = [5,8,3,4,9]
re = sorted(list02)
print(re)

# sorted 支持降序排列                             增加reverse
re = sorted(list01,key=lambda item:item.attack,reverse=True)
for item in re:
    print(item)







































