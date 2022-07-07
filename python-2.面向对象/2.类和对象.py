# @Project   : Python
# @File      : 2.类和对象.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/30, 17:37
#

print("----------------------------实例变量---------------------------")
'''
    实例成员/变量

            1,语法：
                定义：在__init__里面
                        对象.变量名   --->比如 self.name = name

                调用：对象.变量名

            2,说明：
                1,首次通过对象赋值为创建，再次赋值为修改
                    w01 = Wife()
                    w01.name = "张三"
                    w01.name = "李四"

                2,通常在构造函数(__init__)中创建
                    w01 = Wife("张三","女")
                    print(w01.name)

                3,每个对象存储一份，通过对象地址访问

            3,作用：描述所有对象的共有属性

'''

# 实例变量示例：
class Wife:
    # 数据成员
    def __init__(self, name, sex):
        # self 是调用当前方法的对象地址
        self.name = name        # ---> 实例变量
        self.sex = sex        # ---> 实例变量

    # 行为成员
    def play(self):
        print(self.name + "玩耍", f"他是{self.sex}生")


w01 = Wife("张三", "女")   #

w01.play()



# # 另一种创建类     ---> 不建议在类外添加实例成员 1
# class Wife:
#     pass
#
# s01 = Wife()
# s01.name = "张三"
# s01.sex = "男"
# print(s01.name)
# print(s01.sex)





print("----------------------------实例方法---------------------------")



'''
    实例方法
        1,语法：
            定义：def 类方法名(self,参数列表):
                    方法体
            
            调用：对象地址.实例方法名(参数列表)
                    不建议通过类名访问类方法
                 
        2,说明：
            --至少有一个形参，第一个参数绑定调用这个方法的对象，一般命名为'self'
            --无论创建多少对象，方法只有一份，并且被所有对象共享
        
        3,作用：表示对象行为

'''

# 实例方法示例：
class Wife:
    # 数据成员
    def __init__(self, name, sex):      # 定义的实例方法
        # self 是调用当前方法的对象地址
        self.name = name        # ---> 实例变量
        self.sex = sex        # ---> 实例变量

    # 行为成员
    def print_play_info(self):
        print(self.name + "玩耍", f"他是{self.sex}生")


w01 = Wife("张三", "女")
w02 = Wife("李四", "男")

# 不同的对象，调用的方法行为只有这一个
w01.print_play_info()      #
w02.print_play_info()      #


# # 可以通过类名调用访问实例方法 但必须要手动传递对象地址  ---> 不建议通过类名访问类方法 2
# # Wife.print_play_info()  # 报错
# Wife.print_play_info(w01)  #
# Wife.print_play_info(w02)  #




print("---------------------------类成员----------------------------")




'''
    类成员/类变量
            1，语法：
                定义： 在类里面，__init__外面  定义变量
                        class 类名：
                            变量名 = 表达式   --->比如 total_money = 1000000

                调用：类名.变量名

            2，说明：
                --存储在类中
                --只有一份，被所有对象共享

            3，作用：
                描述所有对象的共有数据  
                可以被所有对象共同操作的数据

'''

# 类对象示例：
class ICBC:
    '''
        工商银行
    '''
    # 表示总行的钱
    total_money = 1000000   # ---> 类变量
    def __init__(self,name,money):
        self.name = name        # ---> 实例变量/成员
        self.money = money      # ---> 实例变量/成员
        ICBC.total_money -= money   # ---> 类名.变量名

# 通过实例变量调用
a01 = ICBC("杭州支行",100000)
a02 = ICBC("上海支行",100000)

# 因为total_money是一个类变量，被所有对象共享，随着被调用的次数，类变量随之变化
print(f"总行还剩{ICBC.total_money}钱") # 总行还剩800000钱



print("---------------------------类方法------------------------")




'''
    类方法
        1,语法：
            定义：@classmethod
                def 类方法名(cls,参数列表):
                    方法体
            
            调用：类名.方法名(参数列表)
                 不建议通过对象访问类方法
                 
        2,说明：
            --至少有一个形参，第一个形参用于绑定类，一般命名为'cls'
            --使用@classmethod修饰的目的是调用类方法时可以隐式传递类
            --类方法中不能访问实例成员，实例方法中可以访问类成员
        
        3,作用：操作类变量
                可以操作所有对象共同的数据
    
'''

# 类方法实例：
class ICBC:
    '''
        工商银行
    '''
    # 表示总行的钱
    total_money = 1000000   # ---> 类变量

    # 因为类方法没有对象地址self，所以不能访问实例成员
    @classmethod             # ---> 类方法  可以操作类变量
    def print_total_money(cls):     #
        print(f"总行还剩{ICBC.total_money}钱")
        # cls 相当于是类 ICBC 所以也可以写成：
        # print(f"总行还剩{cls.total_money}钱")

    def __init__(self,name,money):
        self.name = name        # ---> 实例变量
        self.money = money      # ---> 实例变量

        ICBC.total_money -= money   # ---> 类名.变量名

# 通过实例变量调用
a01 = ICBC("杭州支行",100000)
a02 = ICBC("上海支行",100000)
print(f"总行还剩{ICBC.total_money}钱")

# 通过类名访问类方法，会将类名传入类方法
ICBC.print_total_money()

# # 通过对象地址访问类变量   ---> 不建议通过类名访问类方法 3
# print(a01.total_money)




'''
    总结不建议的写法：
            1,在类外添加实例成员
            2,通过类访问实例方法(特殊情况除外)
            3,通过实例访问类成员

'''



print("-----------------------------练习----------------------------------")





# 练习: 定义对象计数器
#       定义老婆类,创建3个老婆对象
#       可以通过类变量记录老婆对象个数
#       可以通过类变量打印老婆对象个数
#

class Wife:
    count = 0
    @classmethod    # 定义类方法，操作类变量
    def print_wife_num(cls):
        print(f"一共有{Wife.count}个老婆对象")

    def __init__(self,name):
        self.name =name

        Wife.count += 1

n01 = Wife("张三")
n02 = Wife("张四")
n03 = Wife("张五")

#
print(Wife.count)

# 通过类变量调用
Wife.print_wife_num()
# print(f"一共有{Wife.count}个老婆对象,他们是{n01.name},{n02.name},{n03.name}。")











class Wife:
    count = 0
    def __init__(self,name):
        self.name =name

        Wife.count += 1

    @classmethod    # 定义类方法，操作类变量
    def print_wife_num(cls):
        print(f"一共有{Wife.count}个老婆对象")



n01 = Wife("张三")
n02 = Wife("张四")
n03 = Wife("张五")

# 通过实例变量直接调用
print(Wife.count)

# 通过类变量调用
Wife.print_wife_num()