# @Project   : Python
# @File      : 2.4.1 双for循环.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/25, 11:56
#



'''

    双for循环

'''


# 外层循环控制行
for i in range(3):
    # 内层循环控制列
    for n in range(4):
        print("*", end="")
    print()


#
for i in range(1,9,2):
    for n in range(2,8,2):
        print("*"+"#",end="")
    print()

print("--------------")
#
for i in range(4):
    for n in range(3):
        print("*#",end="")
    print()


print("--------------")
#
for i in range(4):
    for n in range(i+1):
        print("*",end="")
    print()



####        练习：

list02 = [9,8,7,66,54,2,3,88,4,5,99]

# 取前一个数据
for n in range(len(list02)-1):
    # 取后一个数据
    for i in range(n+1,len(list02)-1):
        # 两者作比较
        if list02[n] > list02[i]:
            list02[n],list02[i] = list02[i],list02[n]
        # print(list02)

print(list02)






# 练习1：
#        判断列表中元素是否具有相同的，[3,80,45,5,80,1]
#        所有元素两两比较，发现相同则打印结果
#        所有元素比较结束，都没有发现相同项，则打印结果

list01 = [3,80,45,5,80,1]

result = False      # 定义标记，假设没有相同项

for i in range(len(list01)-1):
    for n in range(i+1,len(list01)-1):
        if list01[i] == list01[n]:
            print("具有相同项")
            result = True       # 进入到这里，说明有相同项
            break       # 退出当前内循环
    if result == True:
        break       # 退出全部循环

if result == False: # 如果没有相同项
    print(list01)


#### 练习2：打印列表list01第二行第三个元素，
#       打印第三行内每个元素，
#       打印第一个列每个元素
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

# 第二行第三个元素
print(list01[1][2])

# 打印第三行内每个元素
print(list01[2])

# 打印第一个列每个元素
for i in range(len(list01)):
    print(list01[i][0])

# 打印每一列每个元素
for item in list01:
    for n in range(len(item)):
        print(item[n],end=" ")
    print()









'''
    
    双for 列表推导式嵌套

'''

# 将两个列表内的元素两两拼接，组成一个新的列表
list01 = ["a","b","c"]
list02 = ["A","B","C"]
#
list03 = []
for i in list01:
    for n in list02:
        list03.append(i + n)
print(list03)

# 列表推导式写法：
list04 = [i + n for i in list01 for n in list02]
print(list04)




# 练习:列表的全排列
#   ["香蕉","苹果","哈密瓜"]
#   ["可乐","牛奶"]
#
list01 = ["香蕉","苹果","哈密瓜"]
list02 = ["可乐","牛奶"]

list03 = []
for i in list01:
    for n in list02:
        list03.append(i+n)
print(list03)

#
list04 = [i+n for i in list01 for n in list02]
print(list04)



list01 = ["香蕉","苹果","哈密瓜"]
list02 = ["可乐","牛奶"]
list03 = ["小明","小李","小晨"]
list04 = []
for i in list01:
    for n in list02:
        for c in list03:
            list04.append(c+i+n)
print(list04)






'''         *******   冒泡排序   *******          '''
####

### 第一种方法： 取代

nums = [1, 9, 8, 5, 6, 7, 4, 3, 2]
length = len(nums)  # 长度为 9
#
for i in range(length - 1):  # 比较次数 9-1 = 8次
    #
    for n in range(length - 1 - i):  # n的值为0,1，2....8
        if nums[n] > nums[n + 1]:
            temp = nums[n]    # 取一个代替值 替换
            nums[n] = nums[n + 1]
            nums[n + 1] = temp

    # print(nums)  # 每一趟循环走完的当前情况
print('-----------')
print(nums)  # 最终结果


### 第二种方法：   替换

list02 = [9,8,7,66,54,2,3,88,4,5,99]

# 取前一个数据
for n in range(len(list02)-1):
    # 取后一个数据
    for i in range(n+1,len(list02)-1):
        # 两者作比较
        if list02[n] > list02[i]:
            list02[n],list02[i] = list02[i],list02[n]
        # print(list02)

print(list02)



### 第三种方法： 定义标记

nums = list(range(1,10))  # 升序的列表，count = n(n-1)/2   count_swap = 0
nums = [9, 8, 1, 2, 3, 4, 5, 6, 7]
length = len(nums)

count = 0  # 比较的次数
count_swap = 0  # 交换过的次数

for i in range(length - 1):
    flag = False  # 打标记，假设这一趟没有交换过
    for n in range(length - 1 - i):
        count += 1
        if nums[n] > nums[n + 1]:
            temp = nums[n]
            nums[n] = nums[n + 1]
            nums[n + 1] = temp
            count_swap += 1
            flag = True  #  进入该循环 说明交换过

    print(nums)  # 每一趟循环走完的当前情况
    if not flag:  # 如果不是flag，说明没有交换过
        break
print('-----------')
print(nums)  # 最终结果
print(count, count_swap)
































