# @Project   : Python
# @File      : 10..装饰器.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/20, 13:08
#

'''
    函数装饰器：decorators

            定义：在不改变原函数的调用以及内部代码情况下，为其添加新功能的函数

            语法：
                def 函数装饰器名称(func):
                    def 内嵌函数名(*args,**kwargs):
                        需要添加的新功能
                        return func(*args,**kwargs)
                    return 内嵌函数名

                @函数装饰器名称
                def 原函数名称(参数):
                    函数体

                原函数(参数)

            本质：使用 @函数装饰器名称 修饰原函数，相当于是 新增功能 + 已有功能

            装饰器链：一个函数可以被多个函数修饰，执行顺序为从近到远
'''

# 示例：已有两个功能函数
def enter_background():
    print("进入后台")

def delete_order():
    print("删除订单")


###### 需求：对以上两个功能增加 权限验证 新功能

#####  1        -->缺点：代码重复
def enter_background01():
    print("权限验证")       # 代码重复
    print("进入后台")


def delete_order02():
    print("权限验证")       # 代码重复
    print("删除订单")


enter_background()
delete_order()



print()
#####  2

# 将需要增加的新功能  单独定义函数
#                       -->缺点：增加新功能时，修改了原有功能代码，违反了开闭原则
def verify_permissions01():
    print("权限验证")


# 已有功能
def enter_background():
    verify_permissions01()
    print("进入后台")

# 已有功能
def delete_order():
    verify_permissions01()
    print("删除订单")


enter_background()
delete_order()




print()
#####  3   过渡     -->缺点：每次对拦截对已有功能的调用不科学

# 将新增的功能 做成闭包
def verify_permissions02(func):
    def wrapper():
        print("权限验证")
        func()

    return wrapper

# 已有功能
def enter_background():
    print("进入后台")

# 已有功能
def delete_order():
    print("删除订单")


# 拦截    -->缺点：每次对拦截对已有功能(enter_background)的调用不科学

# 将已有功能传入进新功能函数内  相当于调用wrapper() = 新增功能 + 已有功能
enter_background = verify_permissions02(enter_background)
delete_order = verify_permissions02(delete_order)


# 调用
enter_background()
delete_order()






print()
#####  3    装饰器 过渡
#                   -->缺点：如果已有功能参数不统一，没法包装
#
def verify_permissions03(func):
    def wrapper():
        print("权限验证")
        func()

    return wrapper


@verify_permissions03   # @新增功能函数名  装饰器
# 已有功能
def enter_background():
    print("进入后台")


@verify_permissions03   # @新增功能函数名  装饰器
# 已有功能
def delete_order():
    print("删除订单")






print()
#####  4    装饰器

#
def verify_permissions03(func):
    # *args将传入的多个实参 转为星号元组形参
    # **kwargs 把传入的关键字实参合并为字典
    def wrapper(*args,**kwargs):
        print("权限验证")
        func(*args,**kwargs)   # *args实参：将wrapper(*args)星号元组形参 拆分为多个实参
                                # **kwargs形参：将传入的关键字形参字典拆分

    return wrapper


@verify_permissions03
def enter_background(login_id,password):    # 接收func(*args)中拆分的实参
    print(login_id,password,"进入后台")


@verify_permissions03
def delete_order(id):   #
    print("删除订单",id)



enter_background(222,132,)   # 调用时  参数传入wrapper(*args,**kwargs)中
delete_order(101)           # 调用时  参数传入wrapper(*args,**kwargs)中





print("-------练习--------")

### 练习：再不改变原有功能(存取钱)的定义与调用情况下，
#           增加验证账号功能

def deposit(money):
    print(f"存了{money}钱")

def withdraw(log_id,pwd):
    print(f"账号为{log_id}，{pwd}的账户，存了钱")



# 定义验证账号功能函数
def verify_account(func):
    def wrapper(*args,**kwargs):
        print("验证账号")
        func(*args,**kwargs)

    return wrapper


@verify_account
def deposit01(money):
    print(f"存了{money}钱")

@verify_account
def withdraw01(log_id,pwd):
    print(f"账号为{log_id}，{pwd}的账户，存了钱")




deposit01(10000)
withdraw01("aaa",123456)


























