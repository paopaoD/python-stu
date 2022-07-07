#
# @Project   :test
# @File         :循环语句.py
# @Time       :2022/5/12,11:32
#

########   if else 语句循环
'''
if 条件1：
    满足条件的执行                 #满足条件只执行一次
else:
    以上条件都不满足执行的语句       #不满足条件只执行一次


if 条件1：
    满足条件的执行
elif 条件二:
    满足条件二执行的语句
elif 条件三:
    满足条件二执行的语句
else:
    以上条件都不满足执行的语句
'''


#########    while 循环：  可以让一段代码满足条件，重复执行  (例子可见4.2作业习题)
# 语法：                      适合根据条件循环执行
'''
while 条件:
    满足条件一直执行

else:    #   else句子可以省略，比如 循环体内用break终止循环时，else子句不执行
    不满足条件只执行一次 

'''


########    for in 循环：用来遍历可迭代的数据   (例子可见4.2作业习题)
# 语法：                    适合执行预定次数的循环
'''
for 变量列表 in 可迭代对象 
    语句块1
else:
    语句块2     
'''


#######  三元表达式，是一个表达式，非常简单的表达式，一般只能写一行

# 输入一个数字，判断是否大于5，
'''
a = input('请输入一个数字：')        #一般写法
a = int(a)
if a > 5:
    print('>5')
else:
    print('<=5')
'''

# 三元表达式格式为：
# -----真值执行的表达式 if 表达式 else 假值执行的表达式-----

'''
a = input('请输入一个数字：')
a = int(a)

print('>5') if a > 5 else print('<=5')      #三元表达式写法
# 或者改成：
print('>5' if a > 5 else '<=5')

'''









print('--------------------------下面是例子----------------------------')

# 吃苹果
'''
a = 1
while a <=5:
    if a > 4:
        print('吃饱了,不吃了')
        break
    print(f'吃了第{a}个苹果')
    a += 1

a = 1
while a <= 5:
    if a ==3:
        print(f'第{a}个苹果不吃了，吃饱了')
        break

    print(f'吃了第{a}个')
    a += 1

for a in range(1,6):
    if a >3:
        print(f'第{a}个苹果不吃了，吃饱了')
        break
    print(f'吃了{a}个苹果')


a = 1
while a <= 5:
    if a ==3:
        print(f'第{a}个苹果不吃了')
        #如果使用continue，在continue之前一定要修改计数器，否则进入死循环
        a += 1
        continue
    print(f'吃了第{a}个')
    a += 1

'''

#### while 循环嵌套

# 女朋友生气了，惩罚：说3遍“媳妇，我错了”，这个循环如何写？
# 如果再加上女朋友说：“还要刷今天的碗”，
# 连续三天

'''
1.循环打印3次媳妇儿，我错了
2，刷今天的碗
3.上面是一套惩罚，这一套惩罚重复执行三天


time = 0
while time < 3:
    a = 0
    while a < 3:
        print('媳妇儿，我错了')
        a += 1
    print('今晚刷碗')
    time += 1
    print(f'------第{time}天的惩罚------')
print(f'-----------{time}天的惩罚结束------------')
'''


# 打印5行星星 每行五个

'''
j = 0
while j < 5:               # 使用while循环
    i = 0
    while i < 5:
        print('*',end='\t')
        i += 1
    print()
    j +=1

for i in range(1,6):        # 使用for  in循环
    for n in range(1,6):
        print('*',end='\t')
    print()
'''


# 打印一个三角形

'''
j = 0
while j < 5:               # 使用while循环
    i = 0
    while i <= j:
        print('*',end='\t')
        i += 1
    print()
    j += 1

for i in range(1,6):        # 使用for  in循环
    for n in range(1,i+1):
        print('*',end='\t')
    print()


for i in range(1,10):
    for n in range(1,i+1):
        print(i,'*',n,'=',i*n,end='\t')
    print()
'''

# 在控制台中输入月份，显示季度，或者提示月份错误
'''
math = int(input('请输入一个月份：'))
if math >12 or math <1:
    print('输入的月份错误')
elif math >=10:
    print('冬季')
elif math >=7:
    print('秋天')
elif math >=4:
    print('夏天')
else:
    print('春天')
'''

# 输入年龄 判断
'''
age = int(input('请输入年龄：'))
if age < 0:
    print('输入有误')
elif age <2:
    print('婴儿')
elif age <13:
    print('儿童')
elif age <20:
    print('青少年')
elif age <65:
    print('成年人')
elif age <150:
    print('老年人')
else:
    print('那不可能')
'''


# 根据身高体重，参照BMI，查看身体状况
# BMI：用体重千克数除以身高米数的平方得出的数字
'''
weight = float(input('请输入体重：'))
high = float(input('请输入身高：'))
BMI = weight / high ** 2

if BMI <18.5:
    print(BMI,'体重过低')
elif BMI <24:
    print(BMI,'正常范围')
elif BMI <28:
    print(BMI,'超重')
elif BMI <30:
    print(BMI,'I度肥胖')
elif BMI <40:
    print(BMI,'II度肥胖')
else:
    print(BMI,'III度肥胖')
'''

# 输入一个开始值，输入一个结束值，打印两个值中间的数字
'''
begin = int(input('请输入开始值:'))
end = int(input('请输入结束值：'))
while begin < end:
    print(begin)
    begin += 1
'''









































