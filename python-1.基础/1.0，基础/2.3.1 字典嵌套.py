# @Project   : Python
# @File      : 2.3.1 字典嵌套.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/24, 13:52
#



# 练习2：在控制台中循环录入学生信息(姓名，年龄，成绩，性别)
#       如果名称输入空字符，则停止录入
#       将所有信息逐行打印出来

'''
###  字典 {           }
'''

# dict_02 = {}
# while True:
#     list_01 = []
#     stu_name = input("请输入学生名称：")
#     if stu_name =="":
#         break
#     age = input("请输入年龄：")
#     list_01.append(age)
#     score = input("请输入成绩：")
#     list_01.append(score)
#     sex = input("请输入性别：")
#     list_01.append(sex)
#
#     dict_02[stu_name] = list_01
#
# print(dict_02)
#
# for name,list_01 in dict_02.items():
#     print(name)
#     print(list_01)




## 或者写成:

'''
####  使用 字典内嵌列表  方法


# {     '张三' : ['age': '25', 'score': '78', 'sex': '男'],      }

'''


# dict_stu = {}
#
# while True:
#     stu_name = input("请输入学生姓名：")
#     if stu_name == "":
#         break
#
#     age = input("请输入年龄：")
#
#     score = input("请输入成绩：")
#
#     sex = input("请输入性别：")
#
#     dict_stu[stu_name] = [age, score, sex]
#
# print(dict_stu)
#
# for name, dict_01 in dict_stu.items():
#     print(f"{name}年龄是{dict_01[0]},成绩是{dict_01[1]},性别是{dict_01[2]}.")



'''
####  使用 字典内嵌字典  方法



# {     '张三' : {'age': '25', 'score': '78', 'sex': '男'},      }

'''

# list_stu = {}
#
# while True:
#     stu_name = input("请输入学生姓名：")
#     if stu_name == "":
#         break
#     age = input("请输入年龄：")
#     score = input("请输入成绩：")
#     sex = input("请输入性别：")
#
#     list_stu[stu_name] = {"age":age, "score":score, "sex": sex}
#
# print(list_stu)
#
# for name, dict_01 in list_stu.items():
#     print(f'{name}年龄是{dict_01["age"]},成绩是{dict_01["score"]},'
#           f'性别是{dict_01["sex"]}.')


'''
### 列表内嵌字典

# [    {'name':'张三'，'age': '25', 'score': '78', 'sex': '男'}    ]

'''

list_stu = []

while True:
    stu_name = input("请输入学生姓名：")
    if stu_name == "":
        break
    age = input("请输入年龄：")
    score = input("请输入成绩：")
    sex = input("请输入性别：")

    list_stu.append({"name":stu_name,"age":age, "score":score, "sex": sex})

print(list_stu)

for item in list_stu:
    print(f'{item["name"]}年龄是{item["age"]},成绩是{item["score"]},'
          f'性别是{item["sex"]}.')

# 获取第一个学生的信息
print(list_stu[0])
print(f'第一个录入的是{item["name"]}，年龄是{item["age"]},成绩是{item["score"]},性别是{item["sex"]}.')

# 获取最后一个学生信息
print(list_stu[-1])
print(f'最后一个录入的是{item["name"]}，年龄是{item["age"]},成绩是{item["score"]},性别是{item["sex"]}.')

