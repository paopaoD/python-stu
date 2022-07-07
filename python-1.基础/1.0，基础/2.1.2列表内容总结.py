#
# @Project   :Python
# @File         :2.1.2列表内容总结.py
# @Time       :2022/5/22,18:04
#

######  列表内容回顾

'''

容器
通用操作

    字符串：存储数据的容器  不可变的字面常量  存储编码值     序列

    列表 list:
            定义：由一系列变量组成的可变序列容器
                    存储数据的容器  可变    存储变量      序列


    元组 tuple
            定义：由一系列变量组成的'不可变'序列容器
                        不可变是指一旦创建，不可以再添加/删除/修改元素

    字典 dict
            定义：1，由一系列键值对组成的 "可变" 映射容器
                    2，映射：一对一的对应关系，且每条记录 "无序"
                    3，键值对 "唯一" 且不可变（字符串/数字/元组），值没有限制




        列表基础操作
                1，创建：

                    变量 = [数据]
                    变量 = list(可迭代对象)

                2，定位/修改：---> 通过索引/切片

                    # 从列表中获取一个元素
                    变量 = 列表名[索引] ---> 定位一个元素

                    # 从列表中获取一片元素组成新列表
                    变量 = 列表名[切片] ---> 定位一片元素

                    # 修改一个元素
                    列表名[切片]  = 变量

                    # 修改一个元素
                    列表名[索引]  = 变量


                3，增加：
                    列表名.append(元素) ----> 在列表最后增加元素

                    列表名.insert(索引,元素) ----> 在列表索引位置增加某个元素

                    # 列表名.extend(可迭代对象(range()/列表)) ---> 尾部扩展多个元素



                4，删除：
                    del 列表名[索引/切片] ---> 删除单个/多个元素

                    列表名.remove(元素) ---> 删除某个元素

                    列表名.pop(元素) ---> 删除某个元素，并将该元素弹出来

                  #从列表中删除多个元素时，建议倒叙删除，因为删除元素，是后一个替换前一个
                   例如：
                    #list01 = [9,25,12,8]

                    # for i in range(len(list01)-1,-1,-1):
                    #     if list01[i] > 10:
                    #         list01.remove(list01[i])
                    # print(list01)
                    #
                    # for i in range(-1,-len(list01),-1):
                    #     if list01[i] > 10:
                    #         list01.remove(list01[i])
                    # print(list01)



                5，获取所有元素: ---> 也叫遍历元素

                        1, 依次拿列表内每个元素
                            for item in 列表名：
                                print(item)

                        2, 倒叙依次拿列表内每个元素 ---> 索引倒叙/负索引
                            例如：
                                list01 = [9,25,12,8]

                                # 正索引倒叙 ---> 3 2 1 0
                                for i in range(len(list01)-1,-1，-1)
                                    print(list01[i])

                                或者：
                                # 负索引 ---> -1 -2 -3 -4
                                for i in range(-1，-len(list01)-1,-1):
                                    print(list01[i])

                6，转变函数：

                    1,  #  join 函数  ----> 生成一个全新的字符串
                        #           可迭代对象必须是字符串
                        #            list---> str
                        # 语法：
                        #   变量 = "连接符".join(列表)

                        # 例如：
                        x = ','.join("abc")
                            print(x)        # a,b,c

                        # 将++号添加到字符串中 代替，号
                        print('++'.join(['a','b','cde']))  # a++b++cde


                    2,  # split 函数 ----> 分割，拆分
                        #           将一个字符串拆分为多个
                        #           str--->list
                        # 语法:
                        #   列表 = "a-b-c-d".spilt("分隔符")

                        # 例如：
                        str01 = "张无忌-赵敏-周芷若"

                        # 将字符串拆分为列表，并从"-"分割
                        list_result = str01.split("-")
                            print(list_result)  # ['张无忌', '赵敏', '周芷若']


                7, 列表扩容原理：
                            1，列表都会‘预留空间’
                            2，当空间不足时，会生成一个新列表（也就是开一个更大的空间）
                            3，把原来列表里的数据都拷贝到新列表内
                            4，变量替换引用

                    元组：   按需分配，不可变






'''


'''
# 从列表中删除多个元素时，建议倒叙删除，因为删除元素，是后一个替换前一个
# 例如：
list01 = [9,25,12,8]

for i in range(len(list01)-1,-1,-1):
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01)

# 或者：
for i in range(-1,-len(list01),-1):
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01)
'''




### 练习1：

# 彩票：双色球
#         红球：6个，1--33之间的整数，且不能重复
#         蓝球：1个，1--16只见的整数
#   (1) 随机产生一注彩票[6个红球1个蓝球]


import random

# red_num = random.randrange(1,33)   # 产生一个随机数：
blue_num = random.randrange(1,16)  #

list01 = []
# for i in range(6):  # 如果用for循环，当随机的数字重复时，就不会放进列表，列表内的数字不满6个
while len(list01) < 6:
    # 产生一个随机数
    red_num = random.randrange(1, 33)
    # 如果随机的数字不重复
    if red_num not in list01:
        list01.append(red_num)
# 随机生成蓝球 添加到列表内
list01.append(random.randrange(1,16))
print(list01)


# (2) 在控制台中购买一注彩票，
#            提示："请输入第1个红球号码："
#                 "请输入第2个红球号码"
#                 "号码不在范围内"
#                 "号码已经重复"
#                 "请输入蓝球号码:"

# 红球：6个，1--33之间不重复的整数
list02 = []
while len(list02) < 6:
    nums = int(input(f"请输入第{len(list02)+1}个红球号码："))
    if nums < 1 or nums > 33:
        print("号码不在范围内")
    elif nums in list02:
        print("号码已经重复")
    else:
        list02.append(nums)

# 再输入最后1个蓝球，总长度为7位
while len(list02) < 7:
    nums3 = int(input("请输入蓝球号码："))
    #在1--16之间的整数
    if 1 <= blue_num <= 16:
        list02.append(nums3)
    else:
        print("号码不在范围内")

print(list02)







