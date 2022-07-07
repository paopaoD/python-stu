
print('hello python')

#### 111111111111

'''
1,书写input
input('提示信息：')

2，观察特点
   2.1 当程序执行到此，等待用户输入，之后才会继续向下执行
   2.2 接收input存变量
   2.3 input接收到的数据类型都是字符串

'''



input('请输入你的密码：')   # 2.1 当程序执行到此，等待用户输入，之后才会继续向下执行

password = input('请输入你的密码：')
print(password)

# 使用输出语法 f'{表达式}'
print(f'你输入的密码是{password}')   # 2.2 接收input存变量

print(type(password))   # 2.3 input接收到的数据类型都是字符串


print("   ")



####  222222222222

'''
# 数据类型转换

int(x[,base])   将x转换成一个整数
flocat(x)       将x转换成一个小数
str(x)          将x转换成一个字符串
tuple(s)        将s转换成一个元组
list(s)         将s转换成一个列表

'''


# 1.float() -- 数据转换成浮点型
num1 = 2
str1 = '10'
print(type(float(num1)))   # 数据转换成了float
print(float(num1))        # 1.0

print(float(str1))        # 10.0


num2 = 2
# 2.str() -- 数据转换成字符串
print(type(str(num2)))   # 数据转换成字符串


# 3.tuple() -- 将一个序列转换成元组
list1 = [10,20,30]
print(tuple(list1))

# 4.list() -- 将一个序列转换成列表
t1 = (100,200,300)
print(list(t1))

# 5.eval() -- 计算在字符串中的有效Python表达式，并返回一个对象
             # (也可以说成是将字符串中的数据转换成原本的类型)
str2 = '1'
str3 = '1.1'
str4 = '(100,200,300)'
str5 = '[1000,2000,3000]'
str6 = '{123,321,256}'
                               # 将字符串中的数据转换成原本的类型

print(eval(str2))        # 转换为 int整数 类型
print(type(eval(str2)))

print(eval(str3))        # 转换为 float小数 类型
print(type(eval(str3)))

print(eval(str4))        # 转换为 tuple元组 类型
print(type(eval(str4)))

print(eval(str5))        # 转换为 list列表 类型
print(type(eval(str5)))

print(eval(str6))         # 转换为 set集合 类型
print(type(eval(str6)))




####  3333333333333

'''

运算符分类：
  1.算数运算符
  2.赋值运算符
  3.复合赋值运算符
  4.比较运算符
  5.逻辑运算符

'''


# 1.算数运算符
a = 1+1  #
print(a)
b = 5*2  #
print(b)
c = 8/2  # 除后都是 float小数类型
print(c)
d = 9//4  # 取整数
print(d)
f = 9%2  # 取余数
print(f)

# 2.赋值运算符
num,int,float = 1,26,2.6
print(num)
print(int)
print(float)


# 3.复合赋值运算符
a = 10
a += 2
print(a)

b = 10
b -= 1
print(b)

c = 10
c += 1+5    # c += 6 ---> c = 10+6   注意：先算符合赋值运算符右面的表达式
print(c)

d = 10
d *= 1+5
print(d)

f = 10
f /= 2
print(f)


# 4.比较运算符
'''
>
<
=
<=
>=
'''
# 5.逻辑运算符


















































