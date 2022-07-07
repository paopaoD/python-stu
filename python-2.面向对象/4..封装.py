# @Project   : Python
# @File      : 4..封装.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/1, 11:44
#
'''
    封装
        定义：
            1,数据角度讲：
                        将多个变量封装到一个自定义类中
                    优势：
                        更符合人类的思考方式
                        可以将数据与对数据的操作封装到一起

            2,行为角度讲：
                        向类外提供必要的功能，隐藏实现的细节
                    优势：
                        以"模块化"的方式进行编程
                        (可以集中精力设计/组织/指挥多个类协同工作)

            3,设计角度讲：
                    1,分而治之
                        --将一个大的需求分解为许多类，每个类处理一个独立的功能
                        --拆分的好处：便于分工，便于复用，可扩展性强

                    2,变则疏之
                        --变化的地方独立封装，避免影响其他类

                    1,高 内 聚
                        --类中各个方法都在完成一项任务(一个类有且只有一个发生变化的原因)

                    1,低 耦 合
                        --类与类的关联性与依赖程度要低(每个类独立)，让一个类的改变，尽量不影响其他类

'''

print("------------------------双下划线  封装变量 过渡版01-----------------------")

'''
    # 使用 双下划线__ 私有化 封装变量 

'''


class Wife:
    def __init__(self,name,age,weight):
        self.name = name
        # 本质：障眼法(实际是将变量名改为：_类名__age )
        self.__age = age      # 加上双下划线，变成了私有变量
        self.__weight = weight      # 加上双下划线，变成了私有变量


w01 = Wife("公主",87,87)
print(w01.name)     # 公主
# print(w01.age)    # 打印报错，提示没有该对象

# 可以调用类名进行访问或者修改   不建议
print(w01._Wife__age)   # 87  实际是将变量名改为：_类名__age
w01._Wife__age = 100    # 直接修改了类中定义的私有变量    不建议

# __dict__ 以字典的方式  --->python内置变量，存储对象的实例变量
print(w01.__dict__)     #





class Wife:
    def __init__(self,name,age,weight):
        self.name = name
        # self.__age = age
        # 但将age变量藏起来之后，直接w01调用时，年龄直接传入的是__init__内的参数age
        # 所以这里需要调用设定年龄函数  将年龄传给value
        self.set_age(age)
        self.__weight = weight      # 将weight变量藏起来

    # 提供公开的读写方法  获取age变量
    def get_age(self):              #
        return self.__age

    # 定义函数，设定年龄
    def set_age(self,value):
        # 给要设定的年龄加上条件
        if 21 <= value <= 31:
            # 把新设定的年龄vaule 赋值给私有变量self.__age
            self.__age = value
        else:
            raise ValueError("输入错误")    # 如果输入范围外的  报错


# w01 = Wife("张三",34,55)
# print(w01.name)

# __dict__ 以字典的方式  --->python内置变量，存储对象的实例变量
# print(w01.__dict__) #
# # print(w01.age)  # age变量藏起来变为私有变量后，不能访问


w01 = Wife("张三",28,55)  # 录入的年龄是28

# 直接调用函数，修改年龄
w01.set_age(23)     #
# w01.set_age(45)     # 报错

# 读取修改后的年龄
print(w01.get_age())    # 23










print("------------------------property 属性 封装变量 过渡版02-----------------------")

'''  
    # 使用 property(读取方法，写入方法) 封装变量  
    
'''


class Enemy:
    def __init__(self,name,blood,attack):
        self.name = name
        # self.set_blood(blood)
        self.blood = blood
        # self.set_attack(attack)
        self.attack = attack

    # 定义 读取函数
    def get_blood_info(self):
        return self.__blood

    # 定义 写入函数，并增加条件
    def set_blood(self,vaule01):
        if 0 <= vaule01 <= 1001:
            self.__blood = vaule01
        else:
            raise  ValueError("血量错误")

    # property对象 拦截对 blood类变量 的读写操作 进入读写函数
    blood = property(get_blood_info,set_blood)     # 对外提供 可读可写


    # 定义读取攻击力函数
    def get_attack_info(self):
        return self.__attack

    # 定义修改攻击力函数，并增加条件
    def set_attack(self,vaule02):
        if 1 <= vaule02 <= 601:
            self.__attack = vaule02
        else:
            raise  ValueError("攻击力错误")

    # property对象 拦截对 attack类变量 的读写操作 进入读写函数
    attack = property(get_attack_info,set_attack)     # 对外提供 可读可写

    # attack = property(None,set_attack)              # 对外提供  只写
    # attack = property(set_attack,None)              # 对外提供  只读


w01 = Enemy("战三",500,25)
print(w01.blood,w01.attack) #







print("------------------------ @property属性 封装变量 最终版-----------------------")

'''
    属性 property     对实例变量的保护(拦截读写操作)
            
            1,定义：
                @property       ---> 负责读取
                def name(self):
                    return self.__name
                    
                @name.setter       ---> 负责写入
                def name(self,name):
                    self.__name = name
                    
            2,调用：
                对象.属性名 = 数据
                变量 = 对象.属性名

            3,说明：
                --通常两个公开的属性，保护一个私有的变量
                
                --@property只负责读取，@@name.setter 负责写入
                
                --只写：属性名 = property(None,写入方法名)--->也就是使用过渡版02
'''


class Enemy:
    def __init__(self,name,blood,attack):
        self.name = name
        self.blood = blood
        self.attack = attack


    @property               # 创建一个property对象，只负责拦截读取操作
    def blood(self):
        return self.__blood

    @blood.setter           # 只负责拦截读取操作
    def blood(self,vaule01):
        if 0 <= vaule01 <= 1001:
            self.__blood = vaule01
        else:
            raise  ValueError("血量错误")


    @property                # 创建一个property对象，只负责拦截读取操作
    def attack(self):
        return self.__attack

    @attack.setter           # 只负责拦截读取操作
    def attack(self,vaule02):
        if 1 <= vaule02 <= 601:
            self.__attack = vaule02
        else:
            raise  ValueError("攻击力错误")


# 写入数据
re01 = Enemy("张三",200,55)
print(re01.name,re01.blood,re01.attack)

# 修改血量数据
re01.blood = 199
print(re01.blood)

# 修改攻击力数据
re01.attack = 59
print(re01.attack)





print("--------------------------- 封装设计 -------------------------------")

# 练习：  请以面向对象的思想描述下列情景
#           小明在招商银行取钱

# 定义类


class Person:
    def __init__(self,name,money01):
        self.name = name
        self.money01 = money01

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def money01(self):
        return self.__money01

    @money01.setter
    def money01(self, value):
        self.__money01 = value

# 定义银行类
class Bank:
    def __init__(self,name,money02):
        self.name = name
        self.money02 = money02

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money02(self):
        return self.__money02

    @money02.setter
    def money02(self, value):
        self.__money02 = value

    # 定义取钱函数
    def get_money(self,person,value):
        self.money02 -= value
        person.money01 += value
        print(f"{person.name}在{self.name}取了{value}块钱,共有{person.money01}")


re01 = Person("小明",100)
re02 = Bank("招商",1000)

re02.get_money(re01,111)







print("--------------------------- __slots__ -------------------------------")

'''
__solts__ :限定类创建的对象，只能有固定的实力对象

        优点：可以防止用户因错写属性的名称而发生程序错误
        
        缺点：丧失了动态语言可以在运行时为对象添加变量的灵活性
'''

# 示例1：
class Student01:
    __slots__ = ("name")        # 可以防止用户因错写属性的名称而发生程序错误
    def __init__(self,name):
        self.name = name

re01 = Student01("zs")
print(re01.name)

# re01.nmae = "张三"          # 属性名称 name 写错，等于创建了新的变量
# print(re01.nmae)



# 示例2：
class Student02:
    __slots__ = ("__age")       #
    def __init__(self,age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

s01 = Student02(10)
print(s01.age)
s01.age = 11
print(s01.age)





























