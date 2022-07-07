#
# @Project   :Python
# @File         :2.1..列表-list.py
# @Time       :2022/5/16,21:45
#

'''
列表：
    定义：由一系列变量组成的 可变 序列 容器

'''

''' 1,创建列表'''
list01 = []   # 根据数据创建列表
list01 = list()   # 根据一种另一种容器创建列表，比如字符串

list01 = list("我是齐天大圣")
print(list01)


'''2,获取元素'''
# 索引
print(list01[2])  # 齐
# 切片
print(list01[-4:])  # ['齐', '天', '大', '圣']


'''-------> 3,新增添加元素'''

# append  追加（是在末尾添加）-----> 列表名.append(元素)

list01.append("八戒")
print(list01)   # ['我', '是', '齐', '天', '大', '圣', '八戒']

# insert 插入 ---->    列表.insert(索引,元素)

list01.insert(1,True)  # 在索引为1的位置添加True
print(list01)   # ['我', True, '是', '齐', '天', '大', '圣', '八戒']

list01.insert(0,"俺老孙")  # 在索引为0的位置添加"俺老孙"
print(list01)       # ['俺老孙', '我', True, '是', '齐', '天', '大', '圣', '八戒']


# 列表名.extend(可迭代对象) ---> 尾部扩展多个元素
list02 = [1,2,3]
print(list02)
# 使用range函数做可迭代对象
print(list02.extend(range(4,8,1)))  # 就地修改  返回None说明修改完成
print(list02)               # [1, 2, 3, 4, 5, 6, 7]

# 使用列表做可迭代对象
print(list02.extend([5,6,7]))  # 就地修改  返回None说明修改完成
print(list02)               # [1, 2, 3, 4, 5, 6, 7, 5, 6, 7]




'''--------->4，删除'''

#### remove 根据元素删除 ----> 列表名.remove(元素)
list01.remove(True)     # 删除列表内True元素
print(list01)       # ['俺老孙', '我', '是', '齐', '天', '大', '圣', '八戒']

list01.remove("是")      # 删除列表内"是"元素
print(list01)   # ['俺老孙', '我', '齐', '天', '大', '圣', '八戒']


### del 根据位置删除 -----> del 列表名[索引或切片]
del list01[0]
print(list01)  # ['我', '齐', '天', '大', '圣', '八戒']


#### pop 末尾移除，并将移除的元素弹出来
# 移除列表内元素，并弹出来
x = list01.pop(0)
print(x)            # 我
print(list01)       # ['齐', '天', '大', '圣', '八戒']



'''------> 5，定位元素，--->定位元素的目的，可以增删改查元素'''
# 切片
del list01[1:3]   # ['齐', '圣', '八戒']
print(list01)

# 修改
list01[1:3] = ["a","b"]   # ['齐', 'a', 'b']
print(list01)
list01[1:3] = [1,2,3,4,5]   # ['齐', 1, 2, 3, 4, 5]
print(list01)
list01[1:3] = []    # 为空时相当于删除----> ['齐', 3, 4, 5]
print(list01)


list02 = list("我是齐天大圣")
print(list02)

# 遍历列表
# 获取列表中索引元素
for item in list02:
    print(item)

print("`````````````````")

''' 倒叙获取所有元素 '''

# 不建议，因为list02[::-1]是通过切片拿元素，重新创建了一个新列表
# for item in list02[::-1]:
#     print(item)

# 按索引 5 4 3 2 1 0
# for index in range(5,-1,-1):
for index in range(len(list02)-1, -1, -1):
    print(list02[index])

print("`````````````````")

# 或者：负索引  -1  -2  -3  -4 -5 -6
for index in range(-1,-len(list02)-1, -1):
    print(list02[index])

print("`````````````````")

# 或者：跳着来 改步长
for index in range(-1,-len(list02)-1,-2):
    print(list02[index])





 # 练习1：
 #       在控制台中录入，西游记中你喜欢的人物
 #       输入空字符串，打印所有（一行一个打印）人物

# list_names = []  # 创建一个列表
# while True:
#     names = input("西游记中你喜欢的人物：")
#     if names == "":
#         break
#     # 将输入的名字新增到列表内
#     list_names.append(names)
#     print(names)
# # 打印列表内名字
# print(list_names)
# # 一行一个打印所有人物时，就要将列表内元素遍历一遍
# for item in list_names:
#     print(item)
    


# 练习2：
#       在控制台中，录入所有学生成绩
#       录入空字符串，打印（一行一个）所有成绩
#       打印成绩最高分，打印最低分，打印平均分

# list_socre = []
#
# while True:
#     score = input("请输入成绩：")
#     if score == "":
#         break
#     # 把每次输入的成绩增加到列表内--->上面录入的成绩是字符串，转换为int类型
#     list_socre.append(int(score))
# print(list_socre)
# for item in list_socre:
#     print(item)
# # 输入的最大的分数
# print("max=",max(list_socre))
# # 输入的最小的分数
# print("min=",min(list_socre))
# # 获取平均分
# print("avg=",sum(list_socre) / len(list_socre))




# 练习3：
#       在控制台中录入学生姓名
#       如果姓名重复，则提示“姓名已经存在”，不添加到列表中
#       如果录入空字符串，则倒叙打印所有学生


# list_name = []
#
# while True:
#     str_name = input("请输入学生姓名：")
#     if str_name == "":
#         break
#     # 判断变量在列表中是否存在 --->如果姓名已存在，说明重复
#     if str_name in list_name:
#         print("姓名已经存在")
#     else:  # 如果不存在，就新增到列表内
#         list_name.append(str_name)
# print(list_name)
# for item in range(-1,-len(list_name)-1,-1):
#     print(list_name[item])





print("----------------- join ----------------------")

'''
####  join 函数  ----> 生成一个全新的字符串
#           可迭代对象必须是字符串
#            list---> str

 "连接符".join(列表)
'''

x = ','.join("abc")
print(x)        # a,b,c

# 将++号添加到字符串中 代替，号
print('++'.join(['a','b','cde']))  # a++b++cde


# 需求： 根据xx逻辑，拼接一个字符串
# "0123456789"

# 第一种写法：缺点：每次循环形成一个新的字符串对象，替换变量引用result
# reslut = ""
# for item in range(10):
#     reslut += str(item)
# print(reslut)


# 第二种写法：优点: 每次循环只想列表添加字符串，没有创建对象
list_temp = []
for item in range(10):
    list_temp.append(str(item))
# join : list --> str  把列表变成字符串
result = "".join(list_temp)     #
print(result)


# 练习1：
#       在控制台中，循环输入字符串，如果输入空则停止
#       最后打印所有内容（拼接后的字符串）
#
'''
list_temp = []
while True:
    result = input("请输入：")
    if result == "":
        break
    else:
        list_temp.append(result)
# 将列表生成一个全新的字符串
str_result = ",".join(list_temp)

print(str_result)
'''


####  split函数 分割，拆分
#           将一个字符串拆分为多个
#           列表 = "a-b-c-d".split("分隔符")
#           str--->list
#

str01 = "张无忌-赵敏-周芷若"
# 将字符串拆分为列表，并从"-"分割
list_result = str01.split("-")      # ['张无忌', '赵敏', '周芷若']
print(list_result)


# 练习1： 英文单词翻转
#       "How are you" ---> "you are How"

str01 = "How are you"
list_str02 = []

# 将字符串转变为列表
list_str01 = str01.split(" ")
# print(list_str01)
# 依次循环列表索引
for item in range(len(list_str01)-1,-1,-1):
    # print(list_str01[item])
    # 将索引代表的元素依次添加到列表list_str02中
    list_str02.append(list_str01[item])
# 将列表转为字符串
str02 = " ".join(list_str02)
print(str02)



# 或者使用切片：
str01 = "How are you"
# 将字符串转变为列表
list_str01 = str01.split(" ")
# 直接翻转列表  再转为字符串
str02 = " ".join(list_str01[::-1])
print(str02)






















