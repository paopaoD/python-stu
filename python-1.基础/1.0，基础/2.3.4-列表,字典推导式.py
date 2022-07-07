# @Project   : Python
# @File      : 2.3.4-列表,字典推导式.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/24, 20:15
#

'''
    列表推导式
        定义：使用简易方法，将可迭代对象转换为列表

        语法：
            变量 = [表达式 for 变量 in 可迭代对象]

            变量 = [表达式 for 变量 in 可迭代对象 if 条件]
'''

# 将list01中所有元素，增加1后存入list02中
list01 = [5, 56, 6, 7, 8, 9]
list02 = []
for item in list01:
    list02.append(item + 1)
print(list02)

# 使用列表推导式
list02 = [item + 1 for item in list01]
print(list02)

# 将list01中大于10的元素，增加1以后存入list02中
list01 = [5, 56, 6, 27, 8, 19]
# for item in list01:
#     if item > 10:
#         list02.append(item+1)
# 列表推导式
list02 = [item + 1 for item in list01 if item > 10]
print(list02)




print("----------------------------练习------------------------------")

# 练习1：使用range生产1-10之间的数字，将数字的平方存入list01中
# 将list01中 所有奇数存入list02
# 将list01中 所有偶数存入list03
# 将list01中 所有大于5的偶数，增加1后存入list04

# list01 = []
# for item in range(1,11):
#     list01.append(item**2)
# print(list01)
# 列表推导式写法
list01 = [item ** 2 for item in range(1, 11)]
print(list01)

# list02 = []
# for item in list01:
#     if item % 2 ==1:
#         list02.append(item)
# print(list02)
# 列表推导式写法
list02 = [item for item in list01 if item % 2 == 1]
print(list02)

# list03 = []
# for item in list01:
#     if item % 2 ==0:
#         list03.append(item)
# print(list03)
# 列表推导式写法
list03 = [item for item in list01 if item % 2 == 0]
print(list03)

# list04 = []
# for item in list01:
#     if item > 5 and item % 2 ==0:
#         list04.append(item+1)
# print(list04)
# 列表推导式写法
list04 = [item + 1 for item in list01 if item > 5 and item % 2 == 0]
print(list04)


print("---------------------------字典推导式-------------------------------------")



'''
    字典推导式：
         
        语法：
            变量 = [key:value for 变量 in 可迭代对象]

            变量 = [key:value for 变量 in 可迭代对象 if 条件]
                  
'''

# 1,2,3,4....10 --> 每个数字做key  数的平方做value  放到字典里
dict01 = {}
for item in range(1,11):
    dict01[item] = item**2

print(dict01)

# 字典推导式写法：

dict02 = {item:item**2 for item in range(1,11)}
print(dict02)



# 练习：1,2,3,4....10 --> 每个数字做key  数的平方做value
#     只记录大于5的数字，放到字典里

dict01 = {}
for item in range(1,11):
    if item > 5:
        dict01[item] = item**2

print(dict01)


# 字典推导式写法：

dict02 = {item : item**2 for item in range(1,11) if item > 5}






# 练习1: ["无忌","赵敏","周芷若"]
#       再把列表元素作为key  元素长度作为value

list01 = ["无忌","赵敏","周芷若"]
dict01 = {}
for item in list01:
    dict01[item] = len(item)
print(dict01)

# 推导式写法
dict02 = {item : len(item) for item in list01}
print(dict02)



# 练习2: ["无忌","赵敏","周芷若"]  [101,102,103]
#           变成{"无忌":101,"赵敏":102,"周芷若":103}

list01 = ["无忌","赵敏","周芷若"]
list02 = [101,102,103]
dict01 = {}

for i in range(len(list01)):
    dict01[list01[i]] = list02[i]
print(dict01)

# 推导式写法
dict02 = {list01[i] : list02[i] for i in range(len(list01))}
print(dict02)           # {'无忌': 101, '赵敏': 102, '周芷若': 103}




'''    --------->     #### 需求：如何根据value查找key                    '''



dict001 = {'无忌': 101, '赵敏': 102, '周芷若': 103}

#### 解决方案1： ----> 缺点：如果原字典内的value有重复的  会覆盖导致丢失数据
dict04 = {}
for key,value in dict001.items():
    dict04[value] = key
print(dict04)


# 推导式写法
dict04 = {value : key for key,value in dict001.items()}
print(dict04)       # {101: '无忌', 102: '赵敏', 103: '周芷若'}



#### 解决方案2：-----> 使用列表内嵌套元组
list01 = []
for key,value in dict001.items():
    list01.append((value,key))
print(list01)


# 推导式写法
list01 = [(value,key) for key,value in dict001.items()]
print(list01)       # [(101, '无忌'), (102, '赵敏'), (103, '周芷若')]
































