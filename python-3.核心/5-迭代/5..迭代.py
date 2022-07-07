# @Project   : Python
# @File      : 5..迭代.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/15, 16:25
#


'''
    迭代  :每一次对过程的重复称为一次迭代，而每次迭代得到的结果会作为下次迭代的开始值

        可迭代对象：iterable  :具有__iter__函数的对象，可以返回迭代器对象

        迭代器对象：iterator

    语法：
        class 可迭代对象：
            def __iter__():
                创建迭代器对象

        class 迭代器:
            def __next__():
                返回一个元素

        for 变量 in 可迭代对象:
            变量得到的就是__next__方法返回值


    迭代原理：
            1，获取迭代器
            2，循环获取下一个元素
            3，遇到异常 停止迭代

    启发：调用next执行一次，计算一次，返回一次

'''

# 示例：

# 可迭代对象  --> 容器
list01 = [1,2,5,88,2,4]
# 迭代过程
for item in list01:
    print(item)


# 迭代原理：
# 1，获取迭代器
iterator = list01.__iter__()

# 2，循环获取下一个元素
while True:
    try:
        item = iterator.__next__()
# 3，遇到异常 停止迭代
    except StopIteration:
        break   # 退出循环
    print(item)


'''
#  面试题1：for循环的原理是什么？

        答:  1，获取迭代器
            2，循环获取下一个元素
            3，遇到异常 停止迭代
        
#  面试题2：可以被for的条件是什么？

            答：能被for的对象是可迭代对象，必须具备__iter__方法
            
'''

'''
#  面试题3：简述一下生成器和迭代器
        
        生成器 本质就是 迭代器 + 可迭代对象
        
        而可迭代对象就是为了可以迭代(可以for)，而迭代的本质就是不断的调用next方法
        
        生成器最重要的特点就是 调用一次next，计算一次结果，返回一个数据
        这个过程称为 惰性操作/延迟操作
        
        优点：在海量数据下，可以大量节省内存
        
        如果要将惰性操作 --> 立即操作(灵活获取结果)
        list01 = list(生成器)
        




'''






print("------------------------------- 练习 ------------------------------------")


# 练习1：("铁扇公主","铁锤公子","扳手王子")
#   使用迭代器原理  遍历元组
tuple01 = ("铁扇公主","铁锤公子","扳手王子")

iterator = tuple01.__iter__()
while True:
    try:
        item01 = iterator.__next__()
        print(item01)
    except StopIteration:
        break





# 练习2：{"铁扇公主":101,"铁锤公子":102,"扳手王子":103}
#   不使用for  获取字典所有数据

dict01 = {"铁扇公主":101,"铁锤公子":102,"扳手王子":103}

iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key,dict01[key])
    except StopIteration:
        break
































































