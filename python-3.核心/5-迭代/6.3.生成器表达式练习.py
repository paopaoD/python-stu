# @Project   : Python
# @File      : 6.3.生成器表达式练习.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/16, 18:22
#



# 练习：

class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio  # 攻击力倍数
        self.duration = duration    # 持续时间

    def __str__(self):
        return f"技能{self.name}的编号是{self.id}，攻击倍数是{self.atk_ratio}，持续时间是{self.duration}"


list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2),
]


print("------------------------------- 练习 1------------------------------------")

# 练习1：获取攻击力倍数大于6的所有技能
# 要求：使用生成器函数/生成器表达式完成

def find_atk():
    for item in list_skill:
        if item.atk_ratio > 6:
            yield item

for item in find_atk():
    print(item.__dict__)


print("----------")
# 生成器表达式
for item in (item for item in list_skill if item.atk_ratio > 6):
    print(item.__dict__)


print("------------------------------- 练习 2------------------------------------")
# 练习2：获取持续时间在4--11之间的所有技能
# 要求：使用生成器函数/生成器表达式完成
def find_atk():
    for item in list_skill:
        if 4 < item.duration < 11:
            yield item

for item in find_atk():
    print(item.__dict__)

print("----------")
# 生成器表达式
for item in (item for item in list_skill if 4 < item.duration < 11):
    print(item.__dict__)



print("------------------------------- 练习 3------------------------------------")

# 练习3：获取技能编号是102的技能
# 要求：使用生成器函数/生成器表达式完成
def find_atk():
    for item in list_skill:
        if item.id == 102:
            yield item

for item in find_atk():
    print(item.__dict__)

print("----------")
# 生成器表达式
for item in (item for item in list_skill if item.id == 102):
    print(item.__dict__)




print("------------------------------- 练习 4------------------------------------")

# 练习4：获取技能名称大于4个字，并且持续时间小于6的技能
# 要求：使用生成器函数/生成器表达式完成
def find_atk():
    for item in list_skill:
        if len(item.name) > 4 and item.duration < 6:
            yield item

for item in find_atk():
    print(item.__dict__)

print("----------")
# 生成器表达式  ---> 此时不建议使用生成器表达式  过长
for item in (item for item in list_skill if len(item.name) > 4 and item.duration < 6):
    print(item.__dict__)


