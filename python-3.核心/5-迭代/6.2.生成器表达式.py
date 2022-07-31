# @Project   : Python
# @File      : 6.2.生成器表达式.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/16, 16:58
#

'''
    生成器表达式

'''

lsit01 = [3,"25",True,3.25,'55',78,"25",5]

def find01():
    for item in lsit01:
        if type(item) == int:
            yield item


re = find01()
for item in re:
    print(item)



print("------生成器表达式-------")
# 生成器表达式
# 此时没有计算 更没有结果
re = (item for item in lsit01 if type(item) == int)
print(re)
# 循环一次，计算一次，得出一个结果
for item in re:
    print(item)


print("------列表推导式-------")
# 列表推导式
# 此时已经完成所有计算，得到所有结果
re = [item for item in lsit01 if type(item) == int]
print(re)
# 只是获取所有结果
for item in re:
    print(item)




# 变量 = [item for item in 可迭代对象 if 条件]  --> 列表推导式
# 变量 = {key,value for key,value in 可迭代对象 if 条件}  --> 字典推导式
# 变量 = {item for item in 可迭代对象 if 条件}  --> 集合推导式
# 变量 = (item for item in 可迭代对象 if 条件)  --> 生成器表达式





print("------------------------------- 练习 ------------------------------------")



lsit01 = [3,"25",True,3.25,'55',False,2.5,"36",5]

#   获取列表lsit01中所有字符串
#   获取列表lsit01中所有小数
#要求：分别使用生成器函数/生成器表达式/列表推导式完成

def get_str_element():
    for item in lsit01:
        if type(item) == str:
            yield item

result = get_str_element()
for item in result:
    print(item)


# 生成器表达式
result = (item for item in lsit01 if type(item) == str)
for item in result:
    print(item)


# 列表推导式
result = [item for item in lsit01 if type(item) == str]
for item in result:
    print(item)



#   获取列表lsit01中所有小数
#要求：分别使用生成器函数/生成器表达式/列表推导式完成

def get_float_element():
    for item in lsit01:
        if type(item) == float:
            yield item


for item in get_float_element():
    print(item)


# 生成器表达式
for item in (item for item in lsit01 if type(item) == float):
    print(item)


# 列表推导式
for item in [item for item in lsit01 if type(item) == float]:
    print(item)





























