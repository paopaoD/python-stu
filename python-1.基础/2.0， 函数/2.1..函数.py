# @Project   : Python
# @File      : 2.1..函数.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/25, 15:44
#
'''
    函数 function
        1,定义: 1,用于封装一个特定的功能，表示一个功能或者行为
                2,函数是可以重复调用执行的语句块

                作用：提高代码的可重用性和可维护性（代码层次结构更清晰）

                语法： def 函数名(形式参数):
                           函数体

        2,说明： def关键字： 全称define：‘定义’
                函数名：    对函数体中语句的描述，规则与变量相同
                形式参数：  方法定义者要求调用者提供的信息
                函数体：    完成该功能的语句


        3,函数的第一行语句建议使用文档字符串描述函数的功能


            调用函数：
                    1,语法：函数名(实际参数)
                    2,说明：根据形参传递内容



'''




# 练习1：将下列代码定义到函数中，再调用一次
# for i in range(4):
#     for n in range(3):
#         print("*#",end="")
#     print()


def num_count(r_count,c_count,char):
    '''
            打印星星  4行 3列
    :param r_count: 行数
    :param c_count: 列数
    :param char:    打印的字符
    :return:
    '''
    for i in range(r_count):
        for n in range(c_count):
            print(char,end="")
        print()

num_count(5,4,"*")






# 练习：定义在控制台中打印一维列表的函数
#   例如：[1,2,3] --> 1 2 3  每个元素一行

def print_list(list_target):    # list_target
    '''
        打印列表
    :param list_target:目标列表
    :return:
    '''
    for item in list_target:
        print(item)


list01 = [1,2,3]
print_list(list01)  # 列表内的元素可以随意改变





# 定义在控制台中打印二维列表的函数
# list01 = [
#     [1,2,3,8],
#     [11,55,44,9],
#     [44,58]
# ]

# 打印成
# 1 2 3 8
# 11 55 44 9
# 44 58

def print_hanshu(list_target):
    '''
        打印二维列表
    :param list_target: 目标列表
    :return:
    '''
    for item in list_target:
        for nums in item:
            print(nums,end=" ")
        print()


list01 = [
    [1,2,3,8],
    [11,55,44,9],
    [44,58]
]

print_hanshu(list01)



print("----------------------------------------")



'''

    可变/不可变类型在传参时的区别：
    
            不可变： 数值型(整数，浮点数，复数)，
                    字符串 str
                    None 空值，
                    元组 tuple
                    布尔 bool
                    固定集合 forzenset
            
            可变：  列表 list
                   字典 dict
                   集合 set
                   
            传参说明：
                    不可变类型的数据在传参时，函数内部不会改变原数据的值
                    可变类型的数据传参时，函数内部可以改变原数据

'''



# 在方法区中存储函数代码，不执行函数体
def fun01(a):
    # 改变的fun01栈帧中 变量a的指向
    a = 100

a = 1
# 因为调用函数，所以开辟一块内存空间，叫做栈帧，用于存
#               储在函数内部定义的变量(包括参数)
fun01(a)
# 函数执行完毕后，栈帧立即释放(其中定义的变量也会销毁)
print(a)   # 1



def fun02(a):
    # 改变的是传入的可变对象
    a[0]=100

list01 = [1,2]
fun02(list01)

print(list01)   # [100, 2]



# 例如：计算list01[1]打印的值
def fun03(a):
    a[1] = [200]


list01 = [1,[2,3]]
fun03(list01)

print(list01[1]) # [200]




































