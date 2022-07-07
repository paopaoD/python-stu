# @Project   : Python
# @File      : 1..概述.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/28, 18:10
#
'''
    面向对象：
        公式：程序 = 对象 + 交互

        优点：
            1,思想层面：
                可模拟显示情景，更接近于人类思维
                有利于竖立归纳，分析解决问题

            2,技术层面：
                高复用：对重复的代码进行封装，提高开发效率
                高扩展：增加新的功能，不修改以前的代码
                高维护：代码可读性好，逻辑清晰，结构规整


    类  和  对象：

            类： 抽象的概念    类别

                比如  人
                数据(变量)成员：身高/体重
                行为(函数/方法)成员：吃饭/睡觉

            对象：具体的事物/实例    个体    属于类的一种个体

                比如  张三
                数据成员：175/60kg
                行为成员：调用(类的行为成员)

        类和类的区别：     行为(函数/方法)不同
        对象和对象的区别：   数据不同

    语法:
        创建类：
            class 类名:            --->    类名所有单词首字母大写
                def __init__(self,参数):
                    # 数据成员
                    self.数据1 = 参数

                # 行为成员
                def 方法名称():
                    方法体

        创建对象：
            变量名 = 类名(参数)

'''


# 创建 类
class Wife:
    # 数据成员
    def __init__(self,name,sex):
        # self 是调用当前方法的对象地址
        self.name = name
        self.sex = sex

    # 行为成员
    def play(self):
        '''
            一起玩耍
        '''
        print(self.name + "玩耍",f"他是{self.sex}生")

# 创建 对象,实际是在调用__init__方法
w01 = Wife("张三","女")    # 自动将对象地址传入方法
# 调用对象的行为
w01.play()    # 自动将对象地址传入方法





# 练习：
# 1，创建学生类
# class Student:
#     def __init__(self,name,age,score,sex):
#         self.name = name
#         self.age = age
#         self.score = score
#         self.sex = sex
#
#     def print_self_info(self):
#         print(f"{self.name}的年龄是{self.age}，成绩{self.score}分，性别是{self.sex}")
#         # print("{}的年龄是{}，成绩{}分，性别是{}".format(self.name,self.age,self.score,self.sex))
#
# stu = Student("aaa",18,100,"女")
# stu.print_self_info()
#
# list_stu = []
# while True:
#     name = input("请输入学生姓名：")
#     if name == "":
#         break
#     age = input("请输入年龄：")
#     score = input("请输入成绩：")
#     sex = input("请输入性别：")
#     stu = Student(name,age,score,sex)
#     list_stu.append(stu)
#
# for stu in list_stu:
#     stu.print_self_info()
#
# info = list_stu[0]
# info.print_self_info()
#
# s01 = list_stu[0]
# s01.name = "小赵"
# s01.score = 98
# print(list_stu[0].name,list_stu[0].score)
#
# list_stu[0].print_self_info()



print("------------------------------")




class Student:
    def __init__(self,name,age,score,sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        print(f"{self.name}的年龄是{self.age}，成绩{self.score}分，性别是{self.sex}")
        # print("{}的年龄是{}，成绩{}分，性别是{}".format(self.name,self.age,self.score,self.sex))



list01 = [
    Student("赵敏",28,100,"女"),
    Student("苏大强",68,62,"男"),
    Student("明玉",30,95,"女"),
    Student("无忌",29,70,"男"),
    Student("张三丰",130,96,"男"),
]

# 练习1：定义函数，在list01中查找name是"苏大强"的对象
#       将名称与年龄打印在控制台中

def find_name():
    for item in list01:
        if item.name == "苏大强":
            return item
    # 如果没找到 返回空，而函数返回值默认就是空
    # return None

stu = find_name()
print(stu.name,stu.age)



# 练习2：定义函数，在list01中查找所有女同学
#       将名称与年龄打印在控制台中

def find02():
    result = []
    for item in list01:
        if item.sex == "女":

            result.append(item)
    return result

stu = find02()
for item in stu:
    # # 调用类里面的行为函数
    # item.print_self_info()
    print(item.name,item.age)




# 练习3：定义函数，在list01中查找年龄大于等于30岁的学生数量
#
def find03():
    count = 0
    for item in list01:
        if item.age >= 30:
            count +=1

    return count

re = find03()
print(re)
# for item in list_stu:
#     item.print_self_info()




# 练习4：定义函数，将list01中所有学生的成绩归零
#
def set01():
    for item in list01:
        # print(item.name)
        item.score = 0

set01()
for item in list01:
    # print(item.name,item.score)
    item.print_self_info()




# 练习5：定义函数，获取list01中所有学生的名字
#
def find04():
    list_stu = []
    for item in list01:
        list_stu.append(item.name)
    return list_stu

stu = find04()
print(stu)




# 练习6：定义函数，在list01中查找年龄最大的学生对象
#
def find05():
    max_stu = list01[0]
    for i in range(1,len(list01)-1):
        if max_stu.age < list01[i+1].age:
            max_stu = list01[i+1]

    return max_stu

stu = find05()
stu.print_self_info()

