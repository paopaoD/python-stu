# @Project   : Python
# @File      : 1 -经典练习题.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/24, 15:58
#


'''  # 1,给定一个不超过5位的整数（不转换为字符串），
            判断该数的位数，依次打印出万位，千位，百位，十位的数字  '''
# #   第一种方法
# a = int(input('num= '))
# count = len(str(a))     # 输入的数字的位数
# w = 10**len(str(a))
# for i in range(count):
#     x = a // w    # 如果输入的数字是5位，循环第一次，得出万位数字，循环第二次，得出千位数字......
#     a = a % w     # 循环第一次，得出后面几位余数
#     print(x,a)
#     w = w//10
#
# #   第二种方法
# a = int(input('num='))
# w = 10000
# for i in range(4):
#     x = a // w    # 如果输入的数字是5位，循环第一次，得出万位数字，循环第二次，得出千位数字......
#     a = a % w     # 循环第一次，得出后面几位余数
#     print(x,a)
#     w = w//10
# else:
#     print(a)
#
# #  第三种方法
# a = int(input('num='))
# #w = 10000
# for i in range(4):
#     w = 10 ** (4-i)
#     x = a // w
#     a = a % w
#     print(x, a)
#     w = w // 10
# else:
#     print(a)
#
# #   第四种方法
# a = int(input('num='))
# #w = 10000
# for i in range(4,0,-1):
#     w = 10 ** i
#     x = a // w
#     a = a % w
#     print(x, a)
#     #w = w // 10
# print(a)




print("---------------------------------------------------------------")

''' # 5，给定一个不超过5位的正整数（不转换为字符串）， 
                判断该数是几位数，依次打印出万位，千位，百位，十位,个位的数字 '''

a = int('321')     # 举例，输入的为300
w = 10000
length = 5      # 前提是输入的是不超过5位数的数字
flag = False     # 定义标记 ---> 也即没有找到第一个有效数字

for i in range(5):               # for循环
    x = a // w    #
    if not flag:    # True  说明没有找到第一个有效数字
        if x :      # True  也即 x > 0  说明找到了第一个有效数字
            flag = True    # 打开开关
        else:       #  False  说明没找到
            length -=1
    if flag:    # 如果找到了第一个有效数字
        print(x)
    a = a % w     #
    w = w//10
print('该数字的长度是：',length)





print("---------------------------------------------------------------")


''' # 8，求100以内所有奇数的和（2500） '''

# 第一种写法
s = 0
for i in range(100):
    if i % 2:
        s += i
print(s)

# 第二种写法
s = 0
for i in range(1,100,2):
    s += i
print(s)

# 第三种方法，使用内建函数：sum
print(sum(range(1,100,2)))

# 0-100的偶数和
print(sum(range(0,102,2)))

s = 0
for i in range(0,102,2):
    if i % 2 ==0:
        s += i
print(s)


print("---------------------------------------------------------------")


''' # 10,给一个数，判断它是否是素数（质数）：{质数，一个大于1的自然数只能被1和它本身整除}'''

# # 第一种方法
# x = int(input('请输入一个数字：'))
# for i in range(2,x):    #
#     if x % i == 0:       # 被整除说明是合数
#         #print('被整除的数字：',i)         # 如果不是素数，那么打印被整除的数字
#         print('不是素数')
#         break            # 只要在测试途中，被任何一个整数整除，就是合数
# else:
#     print('素数')
#
#
# # 第二种方法
# x = int(input('请输入一个数字：'))
# flag = False                      # 打标记
# for i in range(2,x):
#     if x % i == 0:       # 被整除说明是合数
#         flag = True
#         break
# if flag:
#     print('合数')
# else:
#     print('素数')



print("---------------------------------------------------------------")


''' # 11， 九九乘法表 '''
# for i in range(1,10):
#     line = ''  # 重置，从头开始
#     for n in range(1,i+1):
#         if n <= i:
#             # line += str(n) + '*' + str(i) + '='+str(i*n) + ' '
#             line += "{} * {} = {}  ".format(n,i,n*i)      # 这样打印出来会有错位
#     print(line)  # 换行
#
# # 或者：
# for i in range(1,10):
#     for n in range(1,i+1):
#             line = "{} * {} = {} ".format(n,i,n*i)
#             print(line,end=' ')
#     print()  # 换行


# 或者：改进后
for i in range(1,10):
    for n in range(1,i+1):
        print(n,'*',i,'=',i*n,end='\t')
    print()  # 换行


print("---------------------------------------------------------------")


''' # 7，打印一个边长为n的正方形 '''

a = '*'
n = 6

for i in range(n):
    if i ==0 or i== n-1:
        print(a * n)
    else:
        print(a + ' '* (n-2) + a)

# 或者改为：
n = 4
for i in range(n):
    if i % (n-1) ==0:   #或者   if not i % (n-1)：
        print('*' * n)
    else:
        print('*' + ' '* (n-2) + '*')



'''# 打印矩形（中间空心）  '''

# number = int(input("请输入："))
number = 8
print("*" * number)
for item in range(number - 2):
    print("*" + " " * (number - 2) + "*")
print("*" * number)



print("---------------------------------------------------------------")

''' # 13，打印菱形   边长为n '''
n = 7 # 当边长为7时
leadingchar = '$' # 定义空格，用$代替空格
char = '*'        # 定义星号*

for i in range(-3,4):    # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即可以放在range()函数中
    if i < 0:               # i代表的是需要打印的空格数量，
        spaces = -i*leadingchar      # 当i的值小于0，星号前面需要打印的空格
        print(spaces,end='')           # 星号之前，需要打印的空格数量
        print((7 + 2 * i) * char)      # 总长度n，减去星号前后需要打印的总空格数量(i<0时，用+号)，= 等于需要打印的星号数量
    else:
        spaces = i *leadingchar     # 当i的值大于等于0，星号前面需要打印的空格
        print(spaces,end='')          #  打印星号前需要打印的空格数量
        print((7 - 2 * i) * char)     #  总长度n，减去星号前后需要打印的总空格数量，= 等于需要打印的星号数量

###     或者精简为：
n = 7               # 当边长为7时
leadingchar = ' '   # 定义空格
char = '*'          # 定义星号
for i in range(-3,4):
    spaces = -i if i<0 else i       # 使用三元表达式，直接计算出需要打印的空格数量
    print(leadingchar * spaces,end='')    # 打印空格  不换行
    print((n - 2 * spaces)*char)    #  总长度n，减去星号前后需要打印的总空格数量，= 等于改行需要打印的星号数量

#   使用绝对值  abs()
n = 7
leadingchar = '$'
char = '*'
for i in range(-3,4):
    print(abs(i) * leadingchar,end=''+(7-2*abs(i))*'*')
    print()

#   使用中间对齐
for i in range(-3,4):
    print('{:^7}'.format((7-2*abs(i))*'*'))     #{:^7}  7个符号位，中间对齐



print("---------------------------------------------------------------")

''' ####   1， 拓展：打印对顶三角形 '''

print('-------1-------')

n = 7           # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即range(-3,4)函数中
x = n //2       # 定义x 也即取整数，为 3，如果n=9时，x = 4 .....

for i in range(-x,x+1):
    spaces = abs(x) - abs(i)
    print(' '*spaces,end='')
    print((2*abs(i)+1)*'*')

print('------2--------')

n = 11
x = n //2
for i in range(-x,x+1):
    line = (2*abs(i)+1)*'*'
    print("{:^{}}".format(line,n))


for i in range(-3,4):
    print((abs(-3)-abs(i))*" ",(2*abs(i)+1)*"*")


print("---------------------------------------------------------------")

''' # 打印闪电 '''

n = 7           # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即range(-3,4)函数中
x = n//2        # 定义x 也即取整数，为 3，如果n=9时，x = 4 .....

for i in range(-x,x+1):     # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即range(-3,4)函数中
        if i <0:
            print(abs(i)*' '+(x+1+i)*'*')
        elif i ==0:
            print(n*'*')
        else:
            print((n-(x+1))*' '+((x+1)-i)*'*')

print('-------------')

# 或者：
n = 7           # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即range(-3,4)函数中
x = n//2        # 定义x 也即取整数，为 3，如果n=9时，x = 4 .....

for i in range(-x,x+1):
        if i <0:
            print("{:^7}".format((x+1-abs(i))*'*' + (x+i)* ' '))
        elif i ==0:
            print("{:^7}".format((n-2*abs(i))*'*'+ (x-i)*' '))
        else:
            print("{:^7}".format((x-i)*' '+ (x+1-abs(i))*'*'))

print('-----------------')

n = 7           # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即range(-3,4)函数中
x = n//2        # 定义x 也即取整数，为 3，如果n=9时，x = 4 .....
f = x+1

for i in range(-x,f):     # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即range(-3,4)函数中
        if i <0:
            print(abs(i)*' '+(f+i)*'*')
        elif i >0:
            print(x *' '+ (f-i)*'*')
        else: # i == 0 时
            print(n * '*')



print("---------------------------------------------------------------")


'''  # 14，打印100内的斐波那契数列  '''
a = 0
b =1
# print(0,0)
# print(1,1)
count = 1
while True:
    c = a + b
    if c > 100:
        break
    count += 1
    # print(count,c)
    a = b
    b = c
    print(count,c)

print("----------")
# 或者：
a = 0
b = 1
while b <100:
    print(b)
    a,b = b,a+b




print("----------")
'''  # 15，求斐波那契数列第101项  '''

a = 0
b =1
# print(0,0)
# print(1,1)
count = 1
while True:
    c = a + b
    count += 1
    # print(count,c)
    a = b
    b = c
    if count == 101:
        break

print(count,c)



print("---------------------------------------------------------------")



'''*******'''
# 练习：矩阵转置---> 把列转为行
#       第一列转为第一行
#       第二列转为第二行
#

list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

# list_new = []
# for i in range(4):
#     list_line = []
#     for n in range(len(list01)):
#         # print(list01[n][0])
#         list_line.append(list01[n][i])
#     print(list_line)
#     list_new.append(list_line)
#
# print(list_new)

list_new = []
for i in range(4):
    # list_line = []
    list_new.append([])

    for n in range(len(list01)):

        list_new[i].append(list01[n][i])

print(list_new)





'''  *******  '''

# (扩展)方阵转置  (不用做成函数)

list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,1,4,2],
    [3,4,9,1],
]

# 中间斜线的1,6,4,1 不用交换位置，只交换对应的元素
for c in range(1,len(list01)):
    # list01[0][r] = list01[r][0]
    for r in range(c,len(list01)):
        #
        list01[c-1][r],list01[r][c-1] = list01[r][c-1],list01[c-1][r]
    # print(list01)
print(list01)

# 打印后
list01 = [
     [1, 5, 9, 3],
     [2, 6, 1, 4],
     [3, 7, 4, 9],
     [4, 8, 2, 1]
 ]


