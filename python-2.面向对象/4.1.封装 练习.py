# @Project   : Python
# @File      : 4.1.封装 练习.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/1, 16:52
#


#### 练习： 定义敌人类(姓名，攻击力(10~50之间)，血量 100~200之间)
#           创建一个敌人对象，可以修改数据，读取数据

print("---------------------------双下划线写法-------------------------------")

class Enemy:
    def __init__(self,name,blood,attack):
        self.name = name
        # self.__blood = blood  # 这样录入的数据会直接打印，不会经过下面的读写函数
        self.set_blood(blood)   # 这样录入的数据会首先赋值给vaule01，再给blood

        # self.__attack = attack # 这样录入的数据会直接打印，不会经过下面的读写函数
        self.set_attack(attack)  # 这样录入的数据会首先赋值给vaule02，再给attack


    # 定义读取血量函数
    def get_blood_info(self):
        return self.__blood

    # 定义 写入血量函数，并增加条件
    def set_blood(self,vaule01):
        if 0 <= vaule01 <= 1001:
            self.__blood = vaule01
        else:
            raise  ValueError("血量错误")


    # 定义读取攻击力函数
    def get_attack_info(self):
        return self.__attack

    # 定义 写入攻击力函数，并增加条件
    def set_attack(self,vaule02):
        if 1 <= vaule02 <= 601:
            self.__attack = vaule02
        else:
            raise  ValueError("攻击力错误")



# 录入的数据
re01 = Enemy("灭霸",1000,555)
print("录入的血量是：",re01.get_blood_info())
print("录入的攻击力是：",re01.get_attack_info())


# 修改血量  调用写入函数
re01.set_blood(777)
print("修改后的血量是：",re01.get_blood_info())

# 修改攻击力   调用写入攻击力函数
re01.set_attack(333)
print("修改后的攻击力是：",re01.get_attack_info())





print("---------------------------Property 封装写法-------------------------------")

class Enemy:
    def __init__(self,name,blood,attack):
        self.name = name

        self.blood = blood  # 此时的self.blood中的blood是封装的类变量blood

        self.attack = attack  #


    # 定义读取血量函数
    def get_blood_info(self):
        return self.__blood

    # 定义 写入血量函数，并增加条件
    def set_blood(self,value01):
        if 0 <= value01 <= 1001:
            self.__blood = value01
        else:
            raise  ValueError("血量错误")

    # property对象拦截封装
    blood = property(get_blood_info,set_blood)   # 对外提供 读 写

    # 定义读取攻击力函数
    def get_attack_info(self):
        return self.__attack

    # 定义 写入攻击力函数，并增加条件
    def set_attack(self,value02):
        if 1 <= value02 <= 601:
            self.__attack = value02
        else:
            raise ValueError("攻击力错误")

    # property对象拦截封装
    attack = property(get_attack_info,set_attack)   # 对外提供 读 写



# 写入数据
re01 = Enemy("张三",200,55)
print(re01.name,re01.blood,re01.attack)

# 修改血量数据
re01.blood = 199
print(re01.blood)

# 修改攻击力数据
re01.attack = 59
print(re01.attack)





print("--------------------------- @Property 封装写法-------------------------------")


class Enemy:
    def __init__(self,name,blood,attack):
        self.name = name
        self.blood = blood  #
        self.attack = attack  #

    # 定义行为成员函数
    def print_info(self):
        print(f"{self.name}的血量是{self.blood}，攻击力是{self.attack}")


    @property           # 读取血量数据
    def blood(self):
        return self.__blood

    @blood.setter           # 写入血量数据
    def blood(self,value01):
        if 0 <= value01 <= 1001:
            self.__blood = value01
        else:
            raise  ValueError("血量错误")


    @property           # 读取攻击力数据
    def attack(self):
        return self.__attack

    @attack.setter           # 写入攻击力数据
    def attack(self,value02):
        if 1 <= value02 <= 601:
            self.__attack = value02
        else:
            raise ValueError("攻击力错误")


# 写入数据
re01 = Enemy("张三",200,55)
re01.print_info()

# 修改血量数据
re01.blood = 199
print("血量：",re01.blood)

# 修改攻击力数据
re01.attack = 59
print("攻击力：",re01.attack)





print("--------------------------- 封装设计 -------------------------------")

# 练习：请用面向对象思想，描述一下场景
#       张无忌 教 赵敏 九阳神功
#       赵敏 教 张无忌 化妆
#       张无忌 上班 挣了 10000
#       赵敏 上班  挣了 6000
#   思考：变化点是数据的不同还是行为的不同

class Person:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    # 定义 教 行为函数
    def teach(self,name02,gongfu):
        print(f"{self.name}教会了{name02.name}{gongfu}")

    # 定义 挣 行为函数
    def get_money(self,money):
        print(f"{self.name}上班挣了{money}钱")


zwj = Person("张无忌")
zm = Person("赵敏")

#  张无忌 教 赵敏 九阳神功
zwj.teach(zm,"九阳神功")
#  赵敏 教 张无忌 化妆
zm.teach(zwj,"化妆")
# 张无忌 上班 挣了 10000
zwj.get_money(10000)
# 赵敏 上班  挣了 6000
zm.get_money(6000)




print("--------------------------- 封装设计02 -------------------------------")



# 练习：请用面向对象思想，描述一下场景
#       玩家(攻击力)攻击敌人(血量)，敌人受伤后(掉血)  还可能死亡(掉装备，加分)
#       敌人攻击玩家，玩家受伤后(掉血/碎屏)  还可能死亡(游戏结束)

class Player:
    def __init__(self,hp,atk):

        self.hp = hp
        self.atk = atk

    # 玩家攻击敌人
    def attack01(self,enemy):
        print("玩家攻击敌人")
        enemy.damage02(self.atk)


    #玩家受伤
    def damage01(self,value):
        print("玩家受伤")
        self.hp -= value
        if self.hp <=0:
            print("玩家死亡")
            print("游戏结束")



class Enemy:
    def __init__(self,blood,attack):
        self.blood = blood
        self.attack = attack


    #敌人受伤
    def damage02(self,value):
        print("敌人受伤")
        self.blood -= value
        if self.blood <=0:
            print("敌人死亡")
            print("掉装备")

    # 敌人攻击玩家
    def attack02(self,player):
        print("敌人攻击玩家")
        player.damage01(self.attack)



p01 = Player(100,50)
p02 = Enemy(100,10)


p02.attack02(p01)
p01.attack01(p02)
p01.attack01(p02)













