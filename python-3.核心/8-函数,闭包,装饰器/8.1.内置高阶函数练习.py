# @Project   : Python
# @File      : 8.1.内置高阶函数练习.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/19, 15:11
#



# 练习：1，([1,1,1],[2,2],[3,3,3,3])
#         获取元组中长度最大的列表

tuple01 = ([1,1,1],[2,2],[3,3,3,3])

re = max(tuple01,key= lambda item:len(item))
print(re)


# 修改6.1内置生成器内的my_zip练习，
list02 = ["孙悟空","猪八戒","唐僧",]
list03 = [101,102,103,104,]

tuple02 = (["孙悟空","猪八戒","唐僧",],[101,102,103,104,])
# 获取长度最小的列表
m01 = min(tuple02,key=lambda item:len(item))
# 将两个列表组合成一个个元组
for item in zip(re,m01):
    print(item)




print("-------")


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
# 练习：
#      2，根据敌人列表，获取所有敌人的姓名与血量与攻击力
#      3，根据敌人列表，获取攻击力大于100的所有活人
#      4，根据防御力，对敌人列表进行降序排列


#      2，根据敌人列表，获取所有敌人的姓名与血量与攻击力
re = map(lambda item:(item.name,item.blood,item.attack),list01)
for item in re:
    print(item)


print("-------")
#      3，根据敌人列表，获取攻击力大于100的所有活人
re = filter(lambda item:item.attack >100 and item.blood >0,list01)
for item in re:
    print(item)


print("-------")
#      4，根据防御力，对敌人列表进行降序排列
re = sorted(list01,key=lambda item:item.phylactic,reverse=True)
for item in re:
    print(item)







































































