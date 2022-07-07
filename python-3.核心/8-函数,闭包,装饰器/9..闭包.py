# @Project   : Python
# @File      : 9..闭包.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/15, 16:27
#

'''
    闭包:
        三要素：
            --必须有一个内嵌函数
            --内嵌函数必须引用外部函数中的变量
            --外部函数返回值必须是内嵌函数

        语法：
            --定义：
                def 外部函数名(参数)
                    外部变量
                    def 内部函数名()
                        使用外部变量
                    return 内部函数名

            --调用：
                变量 = 外部函数名(参数)
                变量(参数)


        定义：在一个函数内部的函数，同时内部函数有引用了外部函数的变量
        本质：闭包试讲内部函数和外部函数的执行环境绑在了一起
        优点：内部函数可以使用外部变量
        缺点：外部变量一直存在与内存中，不会在调用结束后释放，占用内存

'''

# 示例：
def fun01():
    a = 1
    def fun02():
        print(a)

    return fun02


# 调用外部函数  返回值是内嵌函数
result = fun01()
# 调用函数  ---> 相当于 fun02()
result() # 可以访问外部变量a


# 闭包应用：逻辑连续，当内部函数被调用时，不脱离当前的逻辑

# 举例
# 获得压岁钱
def give_gife_money(money):
    print(f"得到了{money}元")
    # 购买东西  价格
    def child_buy(target,price):
        nonlocal money
        if money >= price:
            money -= price
            print(f"买了{target}，花了{price}元，剩余{money}元")
        else:
            print("钱不够")

    return child_buy


# 调用  ---> 下列代码是连续的逻辑
action = give_gife_money(10000)
action("玩具",30)
action("手机",3000)
action("汽车",20000)






















































































