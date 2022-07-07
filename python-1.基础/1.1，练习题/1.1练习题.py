#
# @Project  :test
# @File     :作业习题.py
# @Date     :2022/5/1020:27
#
import math

# 1，给一个半径，求圆的面积和周长，圆周率3.14
'''
num = int(input('请输入一个半径：'))
zc = 3.14 * num * 2
mj = 3.14 * num **2
print('周长等于',zc)
print('面积等于',mj)
'''

# 2，输入两个数，比较大小后，从小到大升序打印
'''
a = int(input('num1='))
b = int(input('num2='))
if a > b:
    print(b,a)
else:
    print(a,b)  # == 代表相等，相等的时候，随便排
'''

# 3，依次输入若干个整数，打印最大值。如果输入为空，则退出程序
'''
list_nums = []
while True:
    nums = input('请输入数字：')
    if nums == '':
        break
    list_nums.append(int(nums))
    # if a < nums:
    #     a = nums
print(list_nums)
print('最大值为：',max(list_nums))
'''

# 4，给定一个不超过5位的整数（不转换为字符串），
#       判断该数的位数，依次打印出万位，千位，百位，十位的数字

'''
#   第一种方法
a = int(input('num= '))
count = len(str(a))     # 输入的数字的位数
w = 10**len(str(a))
for i in range(count):
    x = a // w    # 如果输入的数字是5位，循环第一次，得出万位数字，循环第二次，得出千位数字......
    a = a % w     # 循环第一次，得出后面几位余数
    print(x,a)
    w = w//10

#   第二种方法
a = int(input('num='))
w = 10000
for i in range(4):
    x = a // w    # 如果输入的数字是5位，循环第一次，得出万位数字，循环第二次，得出千位数字......
    a = a % w     # 循环第一次，得出后面几位余数
    print(x,a)
    w = w//10
else:
    print(a)

#  第三种方法
a = int(input('num='))
#w = 10000
for i in range(4):
    w = 10 ** (4-i)
    x = a // w
    a = a % w
    print(x, a)
    w = w // 10
else:
    print(a)

#   第四种方法
a = int(input('num='))
#w = 10000
for i in range(4,0,-1):
    w = 10 ** i
    x = a // w
    a = a % w
    print(x, a)
    #w = w // 10
print(a)
'''


# 5，给定一个不超过5位的正整数（不转换为字符串），判断该数是几位数，依次打印出万位，千位，百位，十位,个位的数字

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

'''
while w:               # while循环
    x = a // w    #
    if not flag:
        if x :
            flag = True    # 打开开关，或者叫打标记
        else:
            length -=1
    if flag:
        print(x)
    a = a % w     #
    w = w//10
print('该数字的长度是：',length)
'''

#  三元表达式，是一个表达式，非常简单的表达式，一般只能写一行

# 输入一个数字，判断是否大于5，
'''
a = input('请输入一个数字：')    #一般写法
a = int(a)
if a > 5:
    print('>5')
else:
    print('<=5')
'''


###### 三元表达式格式为：
####  ------ 真值执行的表达式 if 表达式 else 假值执行的表达式
'''
a = input('请输入一个数字：')    #三元表达式写法
a = int(a)

print('>5') if a > 5 else print('<=5')
# 或者改成：
print('>5' if a > 5 else '<=5')
'''

# 6，输入n个数，求每次输入后的算数平均数
'''
n = 0    # 代表输入的个数
s = 0    # 代表累加值，输入的数字总和

while True:
    x = int(input('>>>'))   # 输入一个数字
    s += x              # 累计，平均数 s / n
    n += 1
    print("sum=",s,'avg=',s / n)
'''


# 7，打印一个边长为n的正方形

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



# 8，求100以内所有奇数的和（2500）
'''
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

'''


# 9，成绩问题：
#     判断学生成绩，成绩等级A至E。其中，90分以上为A，80~89分为B，70~79分为C,60~69分为D，60分以下为E
'''
socre = int(input('请输入分数：'))
if socre >= 90:
    print('A')
elif socre >=80:
    print('B')
elif socre >=70:
    print('C')
elif socre >=60:
    print('D')
else:            # 也即socre < 60:
    print('E')
'''


# 10，求1到5阶乘之和
'''
# 第一种方法
p = 1   # 阶乘
s = 0   # 总和
for i in range(1,6):
    p = p * i
    # print(p)
    s += p
print(s)

# 第二种方法
p = 1
s = 0
for i in range(1,6):
    p *= i
    # print(a)
    s += p
print(s)

# 当求的是1到n阶乘之和
n = 5
p = 1
s = 0
for i in range(1,n+1):
    p = p * i
    s = s+p
print(s)
'''



# 10,给一个数，判断它是否是素数（质数）：{质数，一个大于1的自然数只能被1和它本身整除}

'''
# 第一种方法
x = int(input('请输入一个数字：'))
for i in range(2,x):    #
    if x % i == 0:       # 被整除说明是合数
        #print('被整除的数字：',i)         # 如果不是素数，那么打印被整除的数字
        print('不是素数')
        break            # 只要在测试途中，被任何一个整数整除，就是合数
else:
    print('素数')


# 第二种方法
x = int(input('请输入一个数字：'))
flag = False                      # 打标记
for i in range(2,x):
    if x % i == 0:       # 被整除说明是合数
        flag = True
        break
if flag:
    print('合数')
else:
    print('素数')
'''

print('----------------------------分割线---------------------------------')


# 11， 九九乘法表
'''
print('--------------------第一次--------------------------')
for i in range(1,10):
    line = ''  # 重置，从头开始
    for n in range(1,i+1):
        if n <= i:
            # line += str(n) + '*' + str(i) + '='+str(i*n) + ' '
            line += "{} * {} = {}  ".format(n,i,n*i)      # 这样打印出来会有错位
    print(line)  # 换行

# 或者：
print('----------------------第二次------------------------')
for i in range(1,10):
    line = ''  # 重置，从头开始
    for n in range(1,i+1):
        if n <= i:
            line += "{} * {} = {:<{}}  ".format(
                n,i,n*i, 2 if n == 1 else 3      # 相比较上一个，改了错位
            )
    print(line)  # 换行

# 或者：
print('-----------------------第三次-----------------------')
for i in range(1,10):
    for n in range(1,i+1):
            line = "{} * {} = {} ".format(n,i,n*i)
            print(line,end=' ')
    print()  # 换行

# 或者：
print('-----------------------第四次-----------------------')
for i in range(1,10):
    for n in range(1,i+1):
            print("{} * {} = {} ".format(
                n,i,n*i
            ),end='\t' if i != n else '\n')    # i和n不相等往后打印，相等时换行

# 或者：改进后
print('----------------------第五次------------------------')
for i in range(1,10):
    for n in range(1,i+1):
        print(n,'*',i,'=',i*n,end='\t')
    print()  # 换行
'''

print('----------------------------分割线---------------------------------')
# 12，用户登录验证：
#      用户依次输入用户名和密码，然后提交验证
#      用户不存在，密码错误，都显示用户名或密码错误提示
#      错误三次，则退出程序
#      验证成功则现实登录信息

'''
username = '123'
password = '321'

for i in range(3):
    a1 = input('请输入用户名:')
    a2 = input('请输入密码:')
    if a1 == username and a2 == password:
        print('登录成功！')
        break
    else:
        print('用户名或密码错误。')
'''


print('----------------------------打印菱形--------------分割线---------------------------------')

# 13，打印菱形   边长为n

''''''
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

print('----------------------------分割线---------------------------------')
###     或者精简为：
''''''
n = 7               # 当边长为7时
leadingchar = ' '   # 定义空格
char = '*'          # 定义星号

for i in range(-3,4):
    spaces = -i if i<0 else i       # 使用三元表达式，直接计算出需要打印的空格数量
    print(leadingchar * spaces,end='')    # 打印空格  不换行 
    print((n - 2 * spaces)*char)    #  总长度n，减去星号前后需要打印的总空格数量，= 等于改行需要打印的星号数量

print('----------------------------分割线---------------------------------')

#   使用绝对值  abs()
''''''
n = 7
leadingchar = '$'
char = '*'
for i in range(-3,4):
    print(abs(i) * leadingchar,end=''+(7-2*abs(i))*'*')
    print()

print('------------------------中间对齐----分割线---------------------------------')

#   使用中间对齐
''''''
for i in range(-3,4):
    print('{:^7}'.format((7-2*abs(i))*'*'))     #{:^7}  7个符号位，中间对齐


print('----------------------------分割线---------------------------------')

#   使用变量代替
'''
n = 7               # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即range(-3,4)函数中
x = n//2             # 定义x 也即取整数，为 3，如果n=9时，x = 4 .....
leadingchar = '$'
char = '*'
for i in range(-x,x+1):
    print('{:^{}}'.format((n-2*abs(i)) * char,n))   # 这样的好处是，可以随意定义n的值
'''

print('----------------------------打印菱形周边--------------分割线---------------------------------')

####   1， 拓展：只打印菱形周边
n = 7
x = n//2
leadingchar = '$'
char = ' '
for i in range(-x,x+1):
    # print('{:$^{}}'.format((n-2*abs(i)) * char,n))  # {:$^{}} 使用符合居中对齐，不使用变量
    print('{:{}^{}}'.format((n-2*abs(i)) * char,leadingchar,n))  # {:{}^{}} 使用变量


print('----------------------------打印对顶三角形--------------分割线---------------------------------')

####   1， 拓展：打印对顶三角形

# n = 7
# leadingchar = ' '
# char = '*'
#
# for i in range(-7,8,2):
#     spaces = (n - abs(i))//2
#     print(leadingchar*spaces,end='')
#     print(abs(i)*'*')
#
# for i in range(-7,8,2):
#     line = ((7 - abs(i))//2)*leadingchar
#     print(line,end='')
#     print(char*abs(i))


n = 7           # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即range(-3,4)函数中
x = n //2       # 定义x 也即取整数，为 3，如果n=9时，x = 4 .....
leadingchar = ' '
char = '*'

for i in range(-x,x+1):
    spaces = abs(x) - abs(i)
    print(leadingchar*spaces,end='')
    print((2*abs(i)+1)*'*')

print('----------------------------分割线---------------------------------')

for i in range(-x,x+1):
    line = (2*abs(i)+1)*'*'
    print("{:^{}}".format(line,n))


print('----------------------------打印闪电-----------------分割线---------------------------')

# 打印闪电

n = 7           # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即range(-3,4)函数中
x = n//2        # 定义x 也即取整数，为 3，如果n=9时，x = 4 .....


for i in range(-x,x+1):     # n=7时，可以对称为-3，-2，-1,0,1,2,3， 也即range(-3,4)函数中
        if i <0:
            print(abs(i)*' '+(x+1+i)*'*')
        elif i ==0:
            print(n*'*')
        else:
            print((n-(x+1))*' '+((x+1)-i)*'*')

print('----------------------------分割线---------------------------------')

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

print('----------------------------分割线---------------------------------')
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


print('------------------------打印斐波那契数列-----分割线---------------------------------')
# 14，打印100内的斐波那契数列
a = 0
b =1
print(0,0)
print(1,1)
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


# 15，求斐波那契数列第101项
'''
a = 0
b =1
print(0,0)
print(1,1)
count = 1
while True:
    c = a + b
    count += 1
    print(count,c)
    a = b
    b = c
    if count == 101:
        break

print(count,c)

'''



# 16，求10万内的所有素数

# n = 0
# for i in range(1,1000):
#     for x in range(2,i):
#         if i % x == 0:
#             #print(i,'是合数')
#             break
#     else:
#         n +=1
#         print(n,i)


n = 0
for i in range(2,1000,2):
    for x in range(2,i):
        if i % x == 0:
            #print(i,'是合数')
            break
    else:
        n +=1
        print(n,i)









