"""
    Python 高级
"""


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


# 1. 生成器函数
def find_all_did_eq_9001():
    for item in list_employees:
        if item.did == 9001:
            yield item


def find_single_name_wu_kong():
    for item in list_employees:
        if item.name == "孙悟空":
            return item

# 2.小结:
# # 1.函数有多个结果使用yield返回
# # 2.函数有单个结果使用return返回
# 3.函数使用raise发送错误消息


list_money = [54, 5, 65, 76, 78]

# 生成器函数
def find_all():
    for item in list_money:
        if item > 50:
            yield item

# 3.生成器本质
class Generator: # 生成器
    def __init__(self):
        self.index = -1

    # 可迭代对象：可以参与for循环
    def __iter__(self): # 可迭代对象
        return self
    def __next__(self):# 迭代器
        while True:
            if self.index == len(list_money) - 1:
                raise StopIteration()

            self.index += 1
            if list_money[self.index] > 50:
                return list_money[self.index]


for item in Generator():
    print(item)


# 4. 函数式编程
from common.iterable_tools import IterableHelper

dict_person = {
    "香酥":26,
    "赵云":25,
    "小雨":30,
}
sum_value = 0
for key in dict_person:
    sum_value += dict_person[key]
print(sum_value)

def condition02(key):
    return dict_person[key]

print(IterableHelper.sum(dict_person,condition02))
print(IterableHelper.sum(dict_person,lambda key:dict_person[key]))

# 在字典中查找值小于30的键名
for key in dict_person:
    if dict_person[key] < 30:
        print(key)

def condition01(key):
    return dict_person[key] < 30

for item in IterableHelper.find_all(dict_person,condition01):
    print(item)

print(list(IterableHelper.find_all(dict_person,condition01)))
print(IterableHelper.find_single(dict_person,condition01))

