# @Project   : Python
# @File      : 2.3.2-字典嵌套总结.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/24, 14:02
#


#### 字典/列表 内嵌

'''
####  字典内嵌列表

{
        '张三' : ['age': '25', 'score': '78', 'sex': '男'],
}

####  字典内嵌字典

{
        '张三' : {'age': '25', 'score': '78', 'sex': '男'},
}

#### 列表内嵌字典

[
        {'name':'张三'，'age': '25', 'score': '78', 'sex': '男'}
]

#### 列表内嵌列表

[
      ['张三'，'25','78', '男']
]

'''


###  选择策略以及优缺点：

'''
选择策略：
        根据具体需求，结合优缺点，综合考虑(两害相权取其轻)

        **字典：
        
            优点：1,根据键获取值，读取速度快
                 2,代码可读性相对列表更高(根据键获取与根据索引获取)

            缺点：1,内存占用大
                 2,获取值只能根据键，不灵活

        **列表：
        
            优点：1,根据索引/切片，获取元素更灵活
                 2,相比字典占内存更小
                 
            缺点：1,获取信息是通过索引，如果信息较多，可读性不高，
                 2,查找元素需要遍历列表，时间复杂度为O(n)

'''



# 练习1：在控制台中录入多个人的多个喜好
#       比如：请输入姓名：
#            请输入第一个喜好：
#            请输入第二个喜好：
#            ...
#            请输入姓名：
#            请输入第一个喜好：
#       输入空字符停止，最后在控制台打印所有人的所有喜好





####      字典嵌套列表

dict_one = {}

while True:
    name = input("请输入姓名:")
    if name == "":
        break

    list_one = []

    while True:
        hobby = input("请输入喜好:")
        if hobby == "":
            break
        list_one.append(hobby)

    # 直接将新增加的列表作为value
    dict_one[name] = list_one
print(dict_one)

# 打印每个人的喜好信息
for name,values in dict_one.items():
    print(f"{name}喜欢的是")
    for item in values:
        print(item)             # 要换行


'''******** '''
##########   或者使用join函数，把列表变成字符串  不用遍历循环
for name,values in dict_one.items():
    print(f"{name}喜欢的是",",".join(values))   # 张无忌喜欢的是 赵敏,周芷若




#     字典嵌套列表  的列表不同新增法
# dict_one = {}
#
# while True:
#
#     name = input("请输入姓名:")
#     if name == "":
#         break
#
#     dict_one[name] = []
#
#     while True:
#         hobby = input("请输入喜好:")
#         if name == "":
#             break
#         dict_one[name].append(hobby)
#
# print(dict_one)
#
# for names,values in dict_one.items():
#     print(f"{names}的爱好是{values[0]}和{values[1]}。")





# 写法，列表 内嵌 字典 内嵌 列表  ---> [ { '张无忌': [赵敏,周芷若] } ]

# list_one = []
#
# while True:
#
#     name = input("请输入姓名:")
#     if name == "":
#         break
#
#     dict_one = {name:[]}
#     list_one.append(dict_one)
#     while True:
#         hobby = input("请输入喜好:")
#         if hobby == "":
#             break
#         dict_one[name].append(hobby)
# print(list_one)







