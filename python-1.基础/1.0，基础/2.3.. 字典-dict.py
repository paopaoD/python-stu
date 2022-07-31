# @Project   : Python
# @File      : 2.3.. 字典-dict.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/23, 16:47
#

'''
非线性结构

    字典 dict

        定义：1，由一系列键值对组成的 "可变" 映射容器
            2，映射：一对一的对应关系，且每条记录 "无序"
            3，键值对 "唯一" 且不可变（字符串/数字/元组），值没有限制

'''

# 字典内的键存放位置，根据哈希算法计算出来

'''
字典
    基础操作
'''

###1，创建字典：
#
dict01 = {}     # {}内放键值对
dict01 = dict() # {}内放容器

# 键和值之间使用冒号                         打印出来是无序的
dict01 = {"wj":100,"zm":80,"zr":90}     #{'wj': 100, 'zm': 80, 'zr': 90}
print(dict01)

# dict01 = dict(["a","b","c","d"])  # 这样写会报错
dict01 = dict([("a","b"),("c","d")])
print(dict01)


'''
### 2，查找元素 --->根据 键(key) 查找 值(value)
'''

# 查找"a"对应的值
print(dict01["a"])  # b

# 查找"c"对应的值
print(dict01["c"])  # d


## 或者使用 ----> get函数   字典.get(key)


print(dict01.get("a"))  # b

print(dict01.get("c"))  # d


## 或者使用 ----> setdefault函数   字典.setdefault(key)--->不常用

print(dict01.setdefault("a"))  # b



'''3，修改元素 ---> 根据key定位vaule  且字典内存在 不然会报错  所以要加判断'''


# 修改"a"对应的值
dict01["a"] = "BB"
print(dict01)       # {'a': 'BB', 'c': 'd'}

# 修改"c"对应的值
dict01["c"] = "DD"
print(dict01)       # {'a': 'BB', 'c': 'DD'}

# 如果key不存在，查找时会报错
# 加if判断
if "xx" in dict01:
    print(dict01["xx"])




'''----> 4，新增 --->字典内之前不存在该key  就是新增 '''

# 修改"e"对应的值，但字典内不存在，所以就是添加
dict01["d"] = "ff"
print(dict01)       # {'a': 'BB', 'c': 'DD', 'd': 'ff'}







'''------>  5，删除 ----> 根据键(key)定位删除   '''

dict01 = {'a': 'BB', 'c': 'DD', 'd': 'ff'}

##  del语句
# 删除key="a"的对应的值 键值对都删掉
del dict01["a"]
print(dict01)       # {'c': 'DD', 'd': 'ff'}


## pop   移除，并且将key对应value弹出来

# 移除'c'对于的value，并将其弹出来    按key弹出
d01 = dict01.pop('c','DD')
print(d01)              # DD
print(dict01)           # {'d': 'ff'}


## popitem()   移除并返回一个任意的键值对    随即弹出item
#               字典为空时，抛出keyerror异常
dict01 = {'a': 'BB', 'c': 'DD', 'd': 'ff','e':200}

d02 = dict01.popitem()
print(d02)
print(dict01)


## clear()  清空字典
dict01.clear()      # {}
print(dict01)






'''------> 6，遍历  --->获取 键 (key) 或者 值 (value) '''

dict01 = {'a': 'BB', 'c': 'DD', 'd': 'ff','e':200}

# 遍历字典，获取key
for key in dict01:
    print(type(key),key)

# 或者：---->推荐使用
for key in dict01.keys():
    print(key)



# 遍历字典，获取value
for value in dict01.values():   #
    print(type(value),value)


# 遍历字典，获取 key  value
for item in dict01.items():     #
    print(type(item),item)


# 或者：
for k,v in dict01.items():      #
    print(k,v)








# 练习1：在控制台中循环录入商品信息(名称，单价)
#         如果名称输入空字符，则停止录入
#         将所有信息逐行打印出来

# dict_01 = {}
#
# while True:
#     num01 = input("请输入商品名称：")
#     if num01 =="":
#         break
#     num02 = int(input("请输入商品价格："))
#
#     dict_01[num01] = num02
#
# print(dict_01)
#
# for key,value in dict_01.items():  # 如果先后输入两个相同的key 而输入的value不同 会发生修改
#     print(key)
#     print(value)

























































