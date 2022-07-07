
print('hello python!')



'''
%s   数据类型格式化为字符串 --- % + str

%f   数据类型格式化为浮点数 --- % + float   格式化为小数类型时后面默认是6位小数

%d   数据类型格式化有符号的十进制整数 --- 可以在数字前加符号的 比如：-1 +2 -4 +7

().format()  函数   

f'{表达式}' --- 该方法更简单易读，更高效

'''


# 浮点数的区别

a = 23.334
b = 1

print('这个数字是%f' % a)   # 默认保留后六位小数

print('这个数字是%.2f' % a)   # 保留两位小数

print('我的学号是%d' %b)   # 我的学号是1

print('我的学号是%03d' %b)   # 我的学号是001

print('我的学号是%04d' %b)   # 我的学号是0001

b = 1000
print('我的学号是%03d' %b)  # %03d 表示输出的整数显示位数，不足以0补全，超出当前位数则原因输出


# 我的数字是a,我的学号是b
print('这个数字是%.3f.我的学号是%04d' % (a,b))

# 我的数字是a,我的学号是b
print('这个数字是%s.我的学号是%s' % (a,b))


age = 18
name = 'Tom'

# 我的名字是x，今年x岁了
print('我的名字是%s,今天%s岁了' %(name,age))


name = "小明"
age = 25
weight = 60
high = 1.68

print("我的名字叫%s，今天%s岁了"%(name,age))
print("我的名字叫%s，今天%s岁了，体重是%s千克，身高是%f"%(name,age,weight,high))


print('-----------------------format--------分割线-----------------------------------')

'''
#  format函数
#           "{},{}".format() ---> {}相当于是占位符，几个{} format()里就要有几个值
'''
name = "小明"
age = 25
weight = 60
high = 1.68

# {}相当于是占位符，几个{}符号  format()里就要有几个值
print("我的名字是{}，今天{}岁了".format("小明",25))
print("我的名字是{}，今天{}岁了，体重是{}，身高{}米".format("小明",25,60,1.76))
# 占位符{}内也可以使用format内值的索引
print("我的名字是{0}，今天{1}岁了，体重是{3}，身高{2}米".format("小明",25,60,1.76))

### 另一种用法：

# 导入时间函数
import datetime
# 获取当前时间
time1 = datetime.datetime.now()
print(time1)        # 2022-05-22 16:08:03.536654

# %Y 年  %m 月  %d 日
print("{:%Y/%m/%d}".format(time1))      # 2022/05/22
# %H 时  %M 分  %S 秒
print("{:%H:%M:%S}".format(time1))      # 16:11:51
# 打印时间
print("{:%Y/%m/%d %H:%M:%S}".format(time1)) # 2022/05/22 16:13:32


print('-------------------------------分割线-----------------------------------')

'''
#  使用另一种语法：
#               f'{表达式}' --- 该方法更简单易读，更高效
'''
name = "小明"
age = 25
weight = 60
high = 1.68

print(f"我的名字叫{name}，今天{age}岁了，体重是{weight}千克，身高是{high}米.")

print(f'我的名字是{name},今天{age}岁了' )

# 我的名字是x，明年x岁了
print(f'我的名字是{name},明年{age+1}岁了' )




print('-------------------------------分割线-----------------------------------')

##### 1111111111
'''
################ 定义变量：
'''
my_name = 'tom'
print(my_name)

b = '你好啊，老王！'
print(b)

a = 23+67
print(a)

price = 8.5     # 苹果价格
weight = 7.5    # 每斤7.5元
money = price * weight   # 总金额
print(money)
money = price * weight-5    # 如果只买苹果，返现5元
print(money)    # 计算金额



#### 222222222
'''
################ 转义字符

# \n : 换行
# \t : 制表符,一个tab键(4个空格)的距离
'''

print('hello world')
print('hello\nworld')   # \n : 换行

print('\tabcd')   # \t : 制表符,一个tab键(4个空格)的距离

print('abcd\tabcd')

print('o\tabcd')

print('oo\tabcd')

print(r'hello\nworld')

print('hello\rworld')   # \r :回车

print('hello\bworld')   # \b :撤回

# print结束符  --- print('内容',end="")

print('hello',end="\n")
print('sorld',end="\t")
print('hello',end="...")
print('python')



'''
##### 3333333333333
##################### 数据类型
'''
num = 1   # int---整型
print(type(num))

num1 = 2.2   # float---浮点型，就是小数
print(type(num1))

a = 'hello world'   # str---字符串，带引号
print(type(a))

b = True     # bool---布尔型，  常做判断使用，布尔型有两个取值 True和False
print(type(b))
b1 = False
print(type(b1))

c = [10,23,34]   # list --- 列表
print(type(c))

d = (13,45,46)   # tuple --- 元组   不可修改的
print(type(d))

e = {45,66,55}   # set --- 集合
print(type(e))

f = {'name':'TOM','age':16}   # dict --- 字典：键值对的形式存储
print(type(f))




####  时间  datetime

# 导入时间函数
import datetime
# 获取当前时间
time1 = datetime.datetime.now()
print(time1)        # 2022-05-22 16:08:03.536654

# %Y 年  %m 月  %d 日
print("{:%Y/%m/%d}".format(time1))      # 2022/05/22
# %H 时  %M 分  %S 秒
print("{:%H:%M:%S}".format(time1))      # 16:11:51
# 打印时间
print("{:%Y/%m/%d %H:%M:%S}".format(time1)) # 2022/05/22 16:13:32



