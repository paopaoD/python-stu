# @Project   : Python
# @File      : 2.2. 元组-tuple.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/23, 13:39
#
'''
元组 tuple
    定义：由一系列变量组成的'不可变'序列容器
                    不可变是指一旦创建，不可以再添加/删除/修改元素

    作用：1，元组与列表都可以存储一系列变量，由于列表会预留内存空间，所以可以增加元素
         2，元组会按需分配内存，所以如果变量数量固定，建议使用元组，因为占用空间更小

    应用：
        变量交换的本质就是创建元组： x,y = y,x ---> x,y = (y,x)

        格式化字符串的本质就是创建元组："姓名%s,年龄%d" %("TOM","18")

'''


# 列表扩容原理：
#     1，列表都会‘预留空间’
#     2，当空间不足时，会生成一个新列表（也就是开一个更大的空间）
#     3，把原来列表里的数据都拷贝到新列表内
#     4，变量替换引用

# 元组：按需分配，不可变


'''
元组
    基础操作：
'''

#### 1，创建元组：---> 使用的是()
#
tuple01 = ()
tuple01 = tuple()
#
tuple02 = (1,2,3,4)

# ---> 相当于是将列表-->元组
tuple03 = tuple(["a","b"])  # ('a', 'b')
print(tuple03)
# ---> 相当于是将元组-->列表
list04 = list(tuple02)  # [1, 2, 3, 4]
print(list04)

#----> 如果元组内只有一个元素时，要在元素后加","逗号
a = (100)
print(type(a))  # int类型

# 应该加个逗号
a = (100,)  # ---> 这样写才是元组
print(type(a))  # tuple





'''------> 2，获取元素 (索引   切片) '''

tuple03 = ("a","b","c","d")

# 按索引获取元组内的单个元素，得到的是str
e01 = tuple03[1]
print(type(e01))    # str

# 按切片获取元组内的多个元素，得到的是tuple
e02 = tuple03[-2:]
print(type(e02))    # tuple


# 可以直接将元组赋值给多个变量,变量的数量和元组内元素数量必须一致
tuple04 = (100,200)
a,b = tuple04
print(a)    # 100
print(b)    # 200




'''    ------> 3，遍历元素'''

tuple04 = (100,200,300,400)

# 正向 0  1  2  3
for item in tuple04:
    print(item)


# 反向  3  2  1  0 /
for  i in range(len(tuple04)-1,-1,-1):
    print(tuple04[i])
#       -1  -2  -3  -4
for i in range(-1,-len(tuple04)-1,-1):
    print(tuple04[i])





# 练习1：显示输入的月份的天数
'''
month = int(input("请输入月份："))
if month <1 or month >12:
    print("输入有误")
elif month ==2:
    print("28天")
    # 将30天的月份放入元组
elif month in (4,6,9,11):
    print("30天")
else:
    print("31天")

# 方法二：
month = int(input("输入月份："))
if month <1 or month >12:
    print("输入有误")
else:
    # 将每月的天数，存入元组
    day_m = (31,28,31,30,31,30,31,31,30,31,30,31)
    print(day_m[month-1])
'''



# 练习2：在控制台中录入日期（年月），计算这是这一年的第几天
#       例如：3月5日 =
#           1月天数+2月天数+5

month = int(input("请输入月份："))
day = int(input("请输入日："))

day_of_months = (31,28,31,30,31,30,31,31,30,31,30,31)
days =0

# 按照索引遍历月份
for i in range(int(month)-1):
    # print(months[i])
    # 累加前几个月的天数
    days += day_of_months[i]
# 累加当月的天数
days += day

print(f"这是这一年的第{month}个月")
print(f"这是这一年的第{days}天")


# 方法二：
# 通过切片获取前几个月的总天数
days = sum(day_of_months[:month-1])
days += day
# print(days)
print(f"这是这一年的第{days}天")











































































