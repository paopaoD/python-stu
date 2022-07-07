# @Project   : Python
# @File      : 2.5外部嵌套作用域.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/19, 16:03
#

'''

    外部嵌套作用域

'''


def fun01():
    # a 是fun01函数的内部作用域
    #   也是fun02函数的外部嵌套作用域
    a = 1

    def fun02():
        b = 2
        # 可以访问外部嵌套作用域
        # print(a)
        a = 2       # 相当于是创建了一个局部作用域变量
        print(a)    # 2



    fun02()
    print(a)    # 1
fun01()





def fun01():
    a = 1
    def fun02():
        b = 2
        # 不能修改外部嵌套作用域
        a = 2  # 相当于是创建了一个fun02局部作用域变量
        print(a)  # 2


    fun02()
    print(a)  # 1  fun01函数作用域的变量 a没有变
fun01()




#### 声明外部嵌套作用域  可以修改外部嵌套作用域变量0

def fun01():
    a = 1
    def fun02():
        b = 2
        # #### 定义外部嵌套作用域变量
        nonlocal a
        a = 2       # 可以修改外部嵌套作用域变量
        print(a)    # 2

    fun02()
    print(a)    # 2 外部嵌套作用域变量被修改
fun01()















































































