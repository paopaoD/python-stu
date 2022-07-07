# @Project   : Python
# @File      : 6.1.内置生成器.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/16, 16:58
#

print("------------------------------- enumerate ------------------------------------")

'''
   枚举函数 enumerate : 遍历可迭代对象时，将其(索引,元素)组合成一个元组
'''


list01 = [1,2,5,88,2,4]
for item in enumerate(list01):
    # 获取的是元组(索引，元素)
    print(item)

for index,element in enumerate(list01):
    print(index,element)



# 练习：定义生成器函数 my_enumerate  实现enumerate功能
#          将元素与索引合成一个元组

def my_enumerate(iterable_target):
    for index in range(len(iterable_target)):
        yield (index,iterable_target[index])


list01 = [1,2,5,88,2,4]
my01 = my_enumerate(list01)
for item in my01:
    print(item)




print("------------------------------- zip ------------------------------------")
'''
    zip ：将多个可迭代对象中对应的元素组合成一个个元组  生成的元组数由长度最小的迭代对象决定
'''

list02 = ["孙悟空","猪八戒","唐僧","沙僧",]
list03 = [101,102,103,104,]

for item in zip(list02,list03):
    print(item)



# 练习：定义生成器函数 my_zip  实现zip功能
#       将多个列表的每个元素合成一个元组

# 1，
def my_zip(iterable02,iterable03):
    for i in range(len(iterable02)):
        yield (iterable02[i],iterable03[i])


for item in my_zip(list02,list03):
    print(item)



print("-----")
# 2，(扩展)
def my_zip(*args):
    # 根据星号元组形参args第一个参数的长度作为索引 len(args[0])
    for i in range(len(args[0])):
        result_list = []
        for item in args:
            result_list.append(item[i])
            # 将返回的列表 转为元组
        yield tuple(result_list)


for item in my_zip(list02,list03):
    print(item)




