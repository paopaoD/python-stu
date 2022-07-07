# @Project   : Python
# @File      : 2.3 函数参数.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/26, 19:03
#


########     参数：调用者传递给定义者的信息

'''

    函数参数
            实际参数

'''


def fun01(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


'''# 位置实参：--->实参与形参根据位置依次进行对应 '''
fun01(1, 2, 3, 4)


'''# 关键字实参：--->实参与形参根据名称进行对应 '''
fun01(a=4, b=3, c=1, d=2)


'''# 序列实参：--->星号将序列拆分后按位置与形参进行对应 '''
# 如果参数很多，可以存储在序列(字符串/列表/元组)中，通过*号拆分，传入函数
# 列表
list01 = ["a", "b", "c", "d"]
# fun01(list01)     # 会报错
fun01(*list01)

# 字符串
str01 = "ABCD"
fun01(*str01)

# 元组
tuple01 = (1, 2, 3, 4)
fun01(*tuple01)


'''# 字典实参：--->双星号将字典拆分后按名称与形参进行对应 '''
# 如果参数很多，可以存储在字典中，通过*号拆分，传入函数

dict01 = {"a": 1, "c": 3, "d": 4, "b": 2}
fun01(*dict01)  # 得到key
fun01(**dict01)  # 得到vaule






print("-----------------------------------")





'''

    函数参数
            形式参数

'''

'''# 默认值(缺省)参数：如果实参不提供，可以使用默认值'''

def fun01(a=None, b=0, c=0, d=0):
    print(a)
    print(b)
    print(c)
    print(d)


# 实参不填，相当于传入默认值
fun01()  # None 0 0 0

# 如果只填2,3，相当于位置参数
fun01(2, 3)  # 2 3 0 0

# 相当于是 关键字实参 + 默认形参：调用者可以随意传递参数
fun01(b=2, c=3)  # None 2 3 0


print("-----------------------------------")


'''#  星号* 元组形参：*号将所有实参合并成一个元组

#        -------->作用：让位置实参个数无限      '''


# 将传入的实参合并成一个元组
def fun03(*args):
    print(args)


fun03(1)
fun03(1, 2)
fun03(1, "av")
fun03(1, 'a', '啊')


# 练习： 定义 数值相加的函数

def add_number(*args):  # args = (2,32)
    sum_num = 0
    for item in args:
        sum_num += item
    return sum_num


sum_num = add_number(2, 32)
print(sum_num)



print("-----------------------------------")



'''
# 双星号** 字典形参：实参可以传递数量无限的关键字实参 --->实参必须是关键字实参

            -------->作用：把关键字实参合并为字典   关键字实参无限
'''

def fun06(**kwargs):
    print(kwargs)


fun06(a=1, b=3)  # {'a': 1, 'b': 3}



# 命名关键字形参：要求必须是关键字实参
def fun06(*,name,**kwargs):
    print(kwargs)
    print(name)

fun06(a=1, b=3,name="张三")



print("-----------------------------------")



''' # 位置实参无限 + 关键字实参无限  '''
def fun08(*args, **kwargs):
    print(args)
    print(kwargs)

fun08(1,2,3,a=4,b=5)




print("-----------------------------------")



'''# 关键字形参:在星号元组形参后面位置的形参，--->传参要使用关键字传参
          要求：要求实参必须使用关键字实参
'''
#
def fun04(a, *args, b):
    print(a)
    print(args)
    print(b)

fun04(1, b=2)
fun04(1, 2, 3, b=5)
fun04("a", 1, 2, 3, b=4)


#
def fun05(*, a, b):
    print(a)
    print(b)

fun05(a=1, b=2)



print("-----------------------------------")

'''
    参数自左至右的顺序:
    
            位置参数 --> 星号参数 --> 命名关键字参数 --> 双星号字典
            

'''


# 练习：调用fun07
def fun07(a, b, *args, c, d, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)


'''# 关键字参数必填， 星号元组参数后面必须是关键字参数，字典参数必须是关键字参数'''
fun07(99, 2, 3, 4, c=2, d=5, dd=25, cc=32)





print("-----------------------------------")

#
def fun09(*args,d=0,c):
    print(args)
    print(c)
    print(d)


fun08(1,2,3,c=4,d=5)



print("-----------------------------------")



# 练习：定义函数，根据小时，分钟，秒，计算总秒数
#      要求：可以只计算小时--->秒
#      要求：可以只计算分钟--->秒
#      要求：可以只计算小时+分钟--->秒
#      要求：可以只计算小时+秒--->秒


def get_sum_seconds(hours=0, minute=0, seconds=0):
    seconds_sum = hours * 3600 + minute * 60 + seconds

    return seconds_sum

# 只算小时
sum_seconds = get_sum_seconds(1)
print(sum_seconds)

# 只算小时，分钟 ---> 位置参数
sum_seconds = get_sum_seconds(2, 3)
print(sum_seconds)

# 算分钟，秒  ---> 关键字参数 + 默认值参数
sum_seconds = get_sum_seconds(minute=2, seconds=3)
print(sum_seconds)

# 算小时，秒  ---> 关键字参数 + 默认值参数
sum_seconds = get_sum_seconds(hours=2, seconds=3)
print(sum_seconds)









print("---------------------------------------------")
####

# 解释器会将函数含义到方法区(存储一份)，连同默认参数一起创建
# 所以不指定参数时，使用的就是那一份列表对象
def fun01(x,list_target = []):      # 默认参数，不要使用可变对象
    for i in range(x):
        list_target.append(i)
    print(list_target)


fun01(3)    # [0, 1, 2]
fun01(3)    # [0, 1, 2, 0, 1, 2]

list01 = []
fun01(3,list01) # [0, 1, 2]












