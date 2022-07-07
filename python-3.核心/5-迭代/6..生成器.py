# @Project   : Python
# @File      : 6..生成器.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/15, 16:26
#
'''
    生成器 generator
                惰性操作 (调用next执行一次，计算一次，返回一次)

        优势 : 节省内存
        缺点 ：获取结果不灵活(不能使用索引/切片访问结果)

        解决：惰性操作 ---> 立即操作
            变量 = list(generator_变量)     可以将生成器  --> 列表

    生成器函数 --> yield

            def 函数名():
                ...
                yield 数据
                ...

            调用：
                变量 = 函数名()      # 调用方法时不执行
                for item in 变量:   # 这个时候才执行函数体
                    ...

    生成器源码：
            class 生成器:      # 生成器 = 可迭代对象 + 迭代器

                def __iter__(self):
                    return self

                def __next__(self):
                    定义着yield以前的代码
                    返回yield后面的数据

    生成器大致规则：
                 1，将yield以前的语句定义在next方法中
                 2，将yield后面的值作为next方法返回值

'''


'''
class MyRange:
    def __init__(self,stop_value):
        self.stop_value = stop_value

    def __iter__(self):
        return MyRangeIterator(self.stop_value)

class MyRangeIterator:
    def __init__(self,end_value):
        self.__end_value = end_value
        self.__start_value = 0

    def __next__(self):
        # 开始值 等于 最后的传入值   停止
        if self.__start_value == self.__end_value:
            raise StopIteration
        
        temp = self.__start_value
        self.__start_value += 1
        return temp


for item in MyRange(10):
    print(item)
    
'''

# 示例：
class MyRange:
    def __init__(self, stop_value):
        self.stop_value = stop_value

    def __iter__(self):
        # return MyRangeIterator(self.stop_value)
        start_number = 0
        while start_number < self.stop_value:
            # yield 作用:将下列代码改为迭代器模式 也即MyRangeIterator的代码
            # 原理：生成迭代器代码的大致规则：
            # 1，将yield以前的语句定义在next方法中
            # 2，将yield后面的start_number作为next方法返回值
            yield start_number
            start_number += 1


for item in MyRange(10):
    print(item)



# yield 生成器 原理:
class MyGenerator:
    # 生成器 = 可迭代对象 + 迭代器
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        # 定义着yield以前的代码
        # 返回yield后面的数据
        pass


# 直接写成函数
def my_range(stop_value):
    start_number = 0
    while start_number < stop_value:
        yield start_number
        start_number += 1


my01 = my_range(10)
print(type(my01))   # <class 'generator'> 生成器
print(dir(my01))

for item in my01:
    print(item)






print("-------------------------------------------------------------------")


#练习：  将迭代器版本的图形管理器改为yield实现

# 图形 类
class Graph:
    def __init__(self,long,wide):
        self.long = long
        self.wide = wide

# # 图形迭代器
# class GraphIterator:
#     def __init__(self,target):
#         self.__target = target
#         self.__index = 0
#
#     # 获取列表内的下一个数据
#     def __next__(self):
#         if self.__index > len(self.__target)-1:
#             raise StopIteration
#         temp = self.__target[self.__index]
#         self.__index += 1
#         return temp


# 图形管理器 类

class GraphManager:
    def __init__(self):
        self.__graphics = []

    def add_graph(self,value):
        self.__graphics.append(value)

    # 可迭代对象
    def __iter__(self):
         # 执行过程：
         # 1，调用当前方法，不执行(内部创建迭代器对象)
         # 2，调用__next__方法，才执行
         # 3，执行到yield语句，返回值
         # 4，再次返回，调用__next__方法，继续执行
         # 5，重复3,4 步骤，直至最后
        for item in self.__graphics:
            yield item


g01 = Graph(5,6)
g02 = Graph(3,4)
manager = GraphManager()
manager.add_graph(g01)
manager.add_graph(g02)


for item in manager:
    print(item.__dict__)


iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item.__dict__)
    except StopIteration:
        break





print("------------------------------- 练习 1------------------------------------")

# 练习：从列表[4,5,6,7,8,10]中选出所有偶数
#     --  结果存入另外一个列表中
#     --  使用生成器去实现

list01 = [4,5,6,7,8,10]

#--  结果存入另外一个列表中
def get_even01():
    result = []
    for item in list01:
        if item % 2 ==0:
            result.append(item)
    return result

re = get_even01()
print(re)
for item in re:
    print(item)




# --  使用生成器去实现
def get_even02():
    for item in list01:
        if item % 2 == 0:
            yield item


re = get_even02()
for item in re:
    print(item)






































