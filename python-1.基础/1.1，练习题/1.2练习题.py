#
# @Project   :Python
# @File         :demo.py
# @Time       :2022/5/13,10:34
#

# 练习，游戏运行产生一个1-100之间的随机数，让玩家重复猜测，直到猜对
#  提示：大了，
#       小了
#        猜对了，并统计共猜了多少次

'''
# 导入一个随机数工具：
import random


random_number = random.randint(1,100)   # 产生一个随机数：
n = 0
while True:
    n += 1
    x = int(input('>>>'))
    if x > random_number:
        print('大了')
    elif x < random_number:
        print('小了')
    else:
        print('对了')
        break
print(f'共猜了{n}次')
'''


# 根据成绩判断等级，如果录入空字符串则退出程序
# 如果录入错误次数达到3次，则退出成绩并提示"成绩错误过多"
'''
conut = 0

while conut < 3:
    str_socre = input('请输入分数：')
    if str_socre == '':
        break
    socre = int(str_socre)
    if socre < 0 or socre > 100:
        print('输入错误')
        conut +=1
    elif socre >= 90:
        print('A')
    elif socre >=80:
        print('B')
    elif socre >=60:
        print('C')
    else:   # 也即socre < 60:
        print('D')
else:
    print('成绩错误过多')
'''

# 一张纸的厚度是0.01毫米，请计算对折多少次，超过珠穆朗玛峰8844.43米
'''
h = 0.01
count = 0          # 折的次数
while h < 8844430:
    count += 1
    h *= 2
    # print(h)
print(count,h)
'''


# 1，累加1-100的和
#,2，累加1-100之间偶数和
#,3，累加10-36之间和

a = 0
for i in range(1,101):
    a += i
print(a)

b = 0
for i in range(2,101,2):
    b += i
print(b)

c = 0
for i in range(10,37):
    c += i
print(c)



'''
# 随机加法考试：
#         随机产生两个数字（1-10）
#         回答两个数相加的结果
#         如果用户回答正确，得10分
#         总共3道题，最后输出得分
#      例如：“请输入8+3=？”   输入：10    不得分
#            “请输入4+5=？”   输入：9    得10分
#            “请输入3+8=？”   输入：11    得10分
#            “总分是20”      '''

# # 首先  导入一个随机数工具：
# import random
#
# sum_score = 10    #总分数
# for i in range(3):
#     number1 = random.randint(1,10)   #产生第一个随机数
#     number2 = random.randint(1,10)   #产生第二个随机数
#     sum_s = number1 + number2
#     num = int(input('请输入答案'+str(number1)+'+'+str(number2)+'='+'?'))
#     if num == sum_s:
#         print('回答正确，得10分')
#         sum_score += 10
#     else:
#         print('回答错误，减5分')
#         sum_score -= 5
# print('总分是',sum_score)


'''# # 九九乘法表  '''

# for i in range(1,10):
#     for x in range(1,i+1):
#         print(x , '*', i,'=', x * i,end='\t')
#     print()







print('-----------------------分隔符------------------------------')

# 累加10-50之间，个位不是2,5,9的整数
# sum_value = 0
# for item in range(10,51):
#     # unit = item % 10
#     if item % 10 == 2 or item % 10 == 5 or item % 10 ==9:
#         continue
#     sum_value += item
# print(sum_value)



# 打印矩形（中间空心）

# number = int(input("请输入："))
# print("*" * number)
# for item in range(number - 2):
#     print("*" + " " * (number - 2) + "*")
# print("*" * number)


# 录入一个字符串，判断是否是回文

# a = input('输入回文：')
# if a[:] == a[::-1]:
#     print('是回文')
# else:
#     print('不是回文')

print('-----------------------分隔符------------------------------')

# 一个小球从100m的高度落下，每次弹回原高度一半。
# 计算：总共弹起来多少次（最小弹起高度0.01m）
#       总共走了多少米


# hight = 100
# distance = hight  # 经过的距离
# count = 0  # 次数

# 弹起来的高度 大于  最小弹起高度

# while hight / 2 > 0.01:
#     count += 1
#     # 每次弹起的高度
#     hight /= 2
#     # 累加弹起/落下的高度
#     distance += hight * 2
#     # print("第%d次弹起来的高度是%f米" % (count, hight))
# print(f"总共弹起来{count}次,总共走了{distance}米")
# print("总共弹起来%d次,总共走了%.2f米"%(count,distance))



print('-----------------------分隔符------------------------------')
# 冒泡排序

# nums = list(range(1,10))  # 升序的列表，count = n(n-1)/2   count_swap = 0
# nums = [9, 8, 1, 2, 3, 4, 5, 6, 7]
# length = len(nums)
#
# count = 0  # 比较的次数
# count_swap = 0  # 交换过的次数
#
# for i in range(length - 1):
#     flag = False  # 打标记，假设这一趟没有交换过
#     for n in range(length - 1 - i):
#         count += 1
#         if nums[n] > nums[n + 1]:
#             temp = nums[n]
#             nums[n] = nums[n + 1]
#             nums[n + 1] = temp
#             count_swap += 1
#             flag = True  #  进入该循环 说明交换过
#
#     print(nums)  # 每一趟循环走完的当前情况
#     if not flag:  # 如果不是flag，说明没有交换过
#         break
# print('-----------')
# print(nums)  # 最终结果
# print(count, count_swap)




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





# 将1970年到2050年中的闰年  存入列表
list01 = []
for item in range(1970,2051):
    if item % 4 ==0 and item % 100 !=0 or item % 400 ==0:
        list01.append(item)
print(list01)

# 或者 列表推导式：

list01 = [item for item in range(1970,2051) if item % 4 ==0 and item % 100 !=0 or item % 400 ==0]
print(list01)
































































