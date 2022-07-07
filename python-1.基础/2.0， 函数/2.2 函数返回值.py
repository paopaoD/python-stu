# @Project   : Python
# @File      : 2.2 函数返回值.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/26, 11:40
#
'''

    函数返回值：
        语法：
            参数：调用者传递给定义者的信息
            返回值：是定义者传递给调用者的结果


'''



# 无返回值函数
def fun01(a):
    print("fun01执行了")


re = fun01(10)  # fun01执行了
print(re)       # 打印结果 None  renturn为None


# 有返回值时
def fun02(a):
    print("fun02执行了")
    # return作用：1,返回结果,2,退出方法
    return 20

re = fun02(10)  # fun02执行了
print(re)       # 20






'''
    
    函数返回值  应用
            
            设计思想： 分而治之---> 分解后 一个一个处理，也就是专注的干一件事
    
'''

# 需求：定义两个数字相加的函数

# def add(number01,number02):
#     # 进行逻辑运算
#     # result = number01 + number02
#     return number01 + number02      # 返回计算的结果
#
# # 调用者提供数据
# number01 = int(input("请输入第一个数字："))
# number02 = int(input("请输入第二个数字："))
# result = add(number01,number02)
# # 调用者复杂显示结果
# print("结果是：",result)



# 练习： 定义计算四位整数，每位相加和的函数
#        并测试 "1234","5428"

def num_sum(number01):
    '''
        每位相加和
    :param number01: 录入的数字
    :return: 每位数字相加的和
    '''
    # 得出各位数字
    result = number01 % 10
    # 累加十位
    result += number01 //10 % 10
    # 累加百位
    result += number01 //100 % 10
    # 累加千位
    result += number01 //1000
    return result


number01 = int(input("请输入一个四位数字："))
re = num_sum(number01)
print("每位相加的和为：",re)


# 或者写为：

def num_sum(number01):
    '''
        每位相加和
    :param number01: 录入的数字
    :return:  每位数字相加的和
    '''
    result = 0
    for item in number01:
        result += int(item)
    return result


number01 = input("请输入一个数字")
re = num_sum(number01)
print("每位相加的和为：",re)




# 练习：根据两  计算几斤零几两

def get_weight_sum(weight_liang):
    '''
        计算斤两
    :param weight_liang: 输入两
    :return: 元组 (斤，两)
    '''
    jin = weight_liang // 16
    liang = weight_liang % 16
    return (jin,liang)


weight_liang = int(input("请输入两："))
re = get_weight_sum(weight_liang)
print(f"输入的是{re[0]}斤零{re[1]}两。")
























