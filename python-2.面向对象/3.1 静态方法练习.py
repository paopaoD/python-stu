# @Project   : Python
# @File      : 3.1 静态方法练习.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/31, 16:28
#

# 练习1：
list01 = [
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
]

# 在二维列表list01中，获取13位置，向左，3个元素
# 在二维列表list01中，获取22位置，向上，2个元素
# 在二维列表list01中，获取03位置，向下，2个元素

class Vector01:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @staticmethod
    # 定义函数   向左移动
    def left():
        return Vector01(0,-1)

    @staticmethod
    # 定义函数   向右移动
    def right():
        return Vector01(0,1)

    @staticmethod
    # 定义函数   向上移动
    def up():
        return Vector01(-1,0)

    @staticmethod
    # 定义函数   向下移动
    def down():
        return Vector01(-1,0)



class DoubleListHelper:
    @staticmethod
    def get_elements(list01,vect_pos,vect_dir,count):
        list02 = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = list01[vect_pos.x][vect_pos.y]
            list02.append(element)
        return list02

# 在二维列表list01中，获取13位置，向左，3个元素
result01 = DoubleListHelper.get_elements(list01,Vector01(1,3),Vector01.left(),3)
for item in result01:
    print(item)     # ['12', '11', '10']

# 在二维列表list01中，获取22位置，向上，2个元素
result02 = DoubleListHelper.get_elements(list01,Vector01(2,2),Vector01.up(),2)
for item in result02:
    print(item)     # ['12', '02']

# 在二维列表list01中，获取03位置，向下，2个元素
result03 = DoubleListHelper.get_elements(list01,Vector01(0,3),Vector01.down(),2)
for item in result03:
    print(item)     # ['23', '13']






print("------------------------练习2------------------------------------")





# 练习2：定义敌人类
#            数据：姓名，血量，基础攻击力，防御力
#            行为：打印个人信息
#       创建敌人列表(至少4个元素)，并画出内存图
#        查找姓名是"灭霸"的敌人对象
#        查找所有死亡的敌人
#        计算所有敌人的平均攻击力
#        删除防御力小于10的敌人
#        将所有敌人攻击力增加50


class Enemy:
    def __init__(self,name,blood,attack,phylactic):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.phylactic = phylactic

    #    定义行为变量
    def print_behavior_info(self):
        print(f"{self.name}的血量是{self.blood}，攻击力是{self.attack}，防御力是{self.phylactic}。")


list01 = [
    Enemy("玄冥",5000,205,15),
    Enemy("灭绝",86,55,13),
    Enemy("成昆",50,100,10),
    Enemy("谢逊",300,15,8),
]


print("----------------------查找姓名是'灭霸'的敌人对象--------------------")

def find_name():
    for item in list01:
        if item.name == "灭霸":
            return item

re01 = find_name()
print("01",re01)

# 如果没找到，返回值为None  可以判断不为空，再调用实例方法
if re01:
    re01.print_behavior_info()
else:
    print("没找到")



print("----------------------查找所有死亡的敌人--------------------")

def find02():
    list_result = []
    for item in list01:
        if item.blood == 0:
            list_result.append(item)
    return list_result

re02 = find02()
for item in re02:
    print("死亡的敌人:",item.name)

    item.print_behavior_info()




print("------------------计算所有敌人的平均攻击力------------------------")

def avg_attack():
    sum_attack = 0
    for item in list01:
        sum_attack += item.attack

    return sum_attack / len(list01)

re03 = avg_attack()
print("平均攻击力:",re03)



print("------------------删除防御力小于10的敌人------------------------")

def delete01():
    # 倒着删除
    for i in range(len(list01)-1,-1,-1):
        if list01[i].phylactic < 10:
            del list01[i]

delete01()
for item in list01:
    print("防御力大于10的敌人：",item.name)
    item.print_behavior_info()



print("--------------------所有敌人攻击力增加50----------------------")


def add_attack():
    for item in list01:
        item.attack += 50

add_attack()
for item in list01:
    item.print_behavior_info()



















