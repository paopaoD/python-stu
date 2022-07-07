# @Project   : Python
# @File      : 10.1装饰器练习.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/20, 17:13
#

'''
    在不改变原有功能(fun01,fun02)调用与定义情况下
    为其增加新功能(打印函数执行时间)
'''

import time


def fun01():
    time.sleep(2)
    print("fun01执行完毕")

def fun02(a):
    time.sleep(1)
    print("fun02执行完毕,参数是：",a)



# 定义 计算时间 函数
def calculate_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()    # 调用之前的时间
        result = func(*args,**kwargs)
        end_taime = time.time()     # 调用之后的时间
        execute_time = end_taime - start_time   # 执行使用的时间
        print(f"执行的时间为{execute_time}秒")
        return result
    return wrapper


@calculate_time
def fun011():
    time.sleep(2)
    print("fun01执行完毕")


@calculate_time
def fun022(a):
    time.sleep(1)
    print("fun02执行完毕,参数是：",a)


fun011()
fun022(100)




















































































