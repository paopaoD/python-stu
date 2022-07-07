# @Project   : Python
# @File      : 2.4..集合-set.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/25, 10:47
#

'''
非线性结构

    集合 set
            定义：由一系列不重复的,不可变类型变量,组成的可变,无序的,映射容器
                 相当于只有键没有值的字典，也可以说存的都是字典的键


'''





#### 1,创建集合：---> 创建方式只有这一种
# 创建空集合
set01 = set()
# 创建有默认值的集合
set01 = set("abcdcc")
print(set01,type(set01))        # {'b', 'a', 'd', 'c'} ---> 无序,元素去重

# set ---> str
list01 = list(set01)
str01 = "".join(list01)
print(str01)            # 'cbad'

# 或者:
set02 = {"a","b","c"}
print(set02,type(set02))



#### 2,添加元素

set01.add("ddd")
print(set01)    # {'ddd', 'a', 'd', 'c', 'b'}



#### 3,删除元素

set01.remove("d")
print(set01)     # {'a', 'b', 'ddd', 'c'}



#### 4,获取所有元素

for item in set01:
    print(item)



##### 5, 数学运算

set01 = {1,2,3}
set02 = {2,3,4}

# 交集 ---> &

print(set01 & set02)    # {2, 3}

# 并集 ---> |

print(set01 | set02)    # {1, 2, 3, 4}

# 补集 ---> ^
# 共有
print(set01 ^ set02)    # {1, 4}
# 单个有的
print(set01 - set02)    # {1}
print(set02 - set01)    # {4}

# 子集
set01 = {1,2,3}
set03 = {1,2}

print(set03 < set01)    # True


# 超集
set01 = {1,2,3}
set03 = {1,2}

print(set01 > set03)    # True





### 练习1：在控制台中循环录入字符串，输入空字符停止
#            打印所有不重复的文字
# set_temp = set()
# while True:
#     str_num = input("请输入：")
#     if str_num == "":
#         break
#     set_temp.add(str_num)
# print(set_temp)



### 练习2：两个岗位，经理：曹操，刘备，孙权
#                  技术：曹操，刘备，张飞，关羽
#           请计算：
#                1.是经理也是技术的有谁
#                2.是经理，不是技术的有谁
#                3.是技术，不是经理的有谁
#                4.张飞是经理吗？
#                5.身兼一职的都有谁？
#                6.经理和技术总共有多少人

set01 = {'曹操','刘备','孙权'}
set02 = {'曹操','刘备','张飞','关羽'}

# 是经理也是技术的有谁
print(set01 & set02)

# 是经理，不是技术的有谁
print(set01 - set02)

# 是技术，不是经理的有谁
print(set02 - set01)

# 张飞是经理吗？
print('张飞' in set01)

print(set02 < set01)

# # 孙权是技术吗？
# print(set01 < set02)


# 身兼一职的都有谁？
print(set01 ^ set02)


# 经理和技术总共有多少人
print(set01 | set02)


print("-----------------------------------------------------")



'''
    固定集合 frozenset

            定义：‘不可变’的集合

            作用：固定集合可以作为字典的键，也可以作为集合的值   内存是固定的，按需分配

            语法：
                固定集合名 = frozenset(可迭代对象)
'''


# 创建固定集合

set01 = frozenset([1,2,3,3,5])
print(set01)            # frozenset({1, 2, 3, 5})

set02 = frozenset(range(5))
print(set02)            # frozenset({0, 1, 2, 3, 4})


# 创建新的固定集合相当于是把 list ---> frozenset
set01 = frozenset([1,2,3,3,5])
print(set01)            # frozenset({1, 2, 3, 5})

# 在转换回来 frozenset ---> list
list02 = list(set01)
print(list02)           # [1, 2, 3, 5]





# 不可变   无法增加，删除



# 运算 ----> 等同于集合set






#### 练习：
#   存储全国各个城市的景区与美食(不用录入),在控制台中显示出来
#     北京：
#         景区：故宫，天安门，天坛
#         美食：烤鸭，炸酱面，豆汁，卤煮
#     四川：
#         景区：九寨沟，峨眉山，春熙路
#         美食：火锅，串串香，兔头


# 存储信息：

dict01 = {
        "北京":
            {
                "景区":["故宫","天安门","天坛"],
                "美食":["烤鸭","炸酱面","豆汁","卤煮"]
            },

        "四川":
            {
                "景区":["九寨沟","峨眉山","春熙路"],
                "美食":["火锅","串串香","兔头"]
            }
}

# 获取四川的所有美食
list01 = dict01["四川"]["美食"]
print(list01)

# 获取四川美食的兔头
list01 = dict01["四川"]["美食"][2]
print(list01)

# 获取所有的城市
for item in dict01.keys():
    print(item)

# 获取所有城市的景区
for key in dict01.keys():
    print(dict01[key]["景区"])


# 把所有的景区加到一个列表内
list02 = []
for key in dict01.keys():
    for item in dict01[key]["景区"]:
        list02.append(item)
print(list02)           # ['故宫', '天安门', '天坛', '九寨沟', '峨眉山', '春熙路']


# 把景区加上
list02 = []
for key in dict01.keys():
    for item in dict01[key]["景区"]:
        list02.append("景区：" + item)
print(list02)       # ['景区：故宫', '景区：天安门', '景区：天坛', '景区：九寨沟', '景区：峨眉山', '景区：春熙路']


# 把地区加上
list02 = []
for key in dict01.keys():
    for item in dict01[key]["景区"]:
        list02.append(key + ":"+ item)
print(list02)   # ['北京:故宫', '北京:天安门', '北京:天坛', '四川:九寨沟', '四川:峨眉山', '四川:春熙路']





# (扩展)计算一个字符串中的字符以及出现的次数  abcdefce
# 思路：
#        判断字符出现的次数，如果统计过则加1，如果没统计过则等于1

dict_result = {}
str_target = "abcdefce"
# 遍历字符串
for item in str_target:
    if item not in dict_result:
        # 将字符当做key，出现的次数当做vaule
        # 如果不在字典内，就是没统计过
        dict_result[item] = 1
    else: # 如果在字典内，
        dict_result[item] += 1
print(dict_result)








