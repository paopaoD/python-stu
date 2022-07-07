#
# @Project   :Python
# @File         :1.3.1字符串.py
# @Time       :2022/5/22,12:56
#
'''
字符串
     字面常量   不可变
'''

a = 'asdfa'
print(a)

s = 'c:\\windows\nt'
print(s)

for i in s:
    print(type(i),i)

x = 'a'+ 'b'   #  生成了一个全新的字符串   依然是个字面常量
print(x)


####  join 加入 增加 ----> 生成一个全新的字符串
#           可迭代对象必须是字符串
#
''' "连接符".join(列表)'''


x = ','.join("abc")
print(x)        # a,b,c

# 将++号添加到字符串中 代替，号
print('++'.join(['a','b','cde']))  # a++b++cde

# print(''.join(range(5))) # 可迭代对象必须是字符串

# 可以写成
print(' '.join(map(str,range(5))))



####  index索引
x = '\t'.join('1234')
print(x)
# 字符串"1"的索引
print(x.index("1"))  # 为 0
# 统计"2"出现的次数
print(x.count("2")) # 1次
# 统计"\t"出现的次数
print(x.count("\t")) # 3次



####  find  查找
#           find系方法，找到后返回正索引
#                      找不到不返回异常，而是返回负数
s = "abcabc"
# 查找字符串中"c"的索引
print(s.find("c"))   # 2
# 查找字符串中"abc"的索引
print(s.find("abc"))  # 0



#### ----> 字符串的分割
#    a.split() -->从左至右切  立即返回列表
#
#    rsplit() -->从右至左切  立即返回列表
#
#    splitlines() -->按照行来切分字符串，行的分隔符包括\n,\r\n,\r等

a = '1,2,3,a,b,c'
# 找到分割符切断   立即返回一个列表
print(a.split())                # ['1,2,3,a,b,c']
# 以字符串中的","为分隔符切割
print(a.split(","))          # ['1', '2', '3', 'a', 'b', 'c']
# 以字符串中的"3"为分隔符切割---> 直接将该字符切掉，又称一刀两断
print(a.split('3'))         # ['1,2,', ',a,b,c']


b = '\n\t\r\n a\nb\t    \nc\t\n'        # 空格，换行符，tab，统称为空白字符space

# 缺省值来分割，开头结尾切一刀，不会多出空串--->切割行为：把尽可能长的空字符串作为切割点切割
print(b.split())    # ['a', 'b', 'c']

# 指定切割符，你说切谁就切掉谁
print(b.split('\n'))      # ['', '\t\r', ' a', 'b\t    ', 'c\t', '']
# 比如：
print(b.split('\t\n'))    # ['\n\t\r\n a\nb\t    \nc', '']

# 带上最大切割数--->2代表切割次数
print(b.split('\n',2))   # ['', '\t\r', ' a\nb\t    \nc\t\n']


b = '\n\t\r\n a\nb\t    \nc\t\n'

###  rsplit() -->从右至左切  立即返回列表
print(b.rsplit())       # ['a', 'b', 'c']

# 带上最大切割数---->从右往左切  2代表切割次数
print(b.rsplit('\n', 2))    # ['\n\t\r\n a\nb\t    ', 'c\t', '']





###  splitlines() -->按照行来分割字符串，行的分隔符包括\n,\r\n,\r等

c = b + "d\re"
print(c)        # '\n\t\r\n a\nb\t    \nc\t\nd\re'

# 按照行来分割字符串
print(c.splitlines())   # ['', '\t', ' a', 'b\t    ', 'c\t', 'd', 'e']





####  partition  分割 ---->立即返回一个元组

d = "a,b,c,d,e,f，g"

# 以","为切入点   立刻返回三元组（part1,sep,part2） 切的切入点字符串也会保留
print(d.partition(','))     # ('a', ',', 'b,c,d,e,f,g')
# 如果没找到切的字符串，会在最后切一刀  切的切入点字符串也会保留
print(d.partition("#"))     # ('a,b,c,d,e,f，g', '', '')

# 从右边开始切  没切到时
print(d.rpartition('$'))    # ('', '', 'a,b,c,d,e,f，g')
# 以字符串中的元素'g'为切入点
print(d.partition('g'))     # ('a,b,c,d,e,f，', 'g', '')





####  replace  替换
#               字符串替换不是就地修改，而是返回新的字符串
#               字符串本身并不改变

e = 'a,b,c,d,d,f,g'
# 将字符串中的','号替换成'*'---->字符串本身并不改变
print(e.replace(",","*"))   # a*b*c*d*d*f*g

print(e.replace(",","++"))  # a++b++c++d++d++f++g

# 找不到时，依然返回新字符串，只是没有内容被替换
print(e.replace("...","***"))   # a,b,c,d,d,f,g

# 将字符串中','号替换为'++'，只替换两次----> 2代表的是替换的次数
print(e.replace(',','++',2))    # a++b++c,d,d,f,g

f = e.replace(",","***")
print(f)        # a***b***c***d***d***f***g

# 把"**"替换成"*"时，只遍历一遍
print(f.replace("**","*"))      # a**b**c**d**d**f**g





####  大小写函数
#               upper()大写 ---> 所有的字母全大写
#               lower()小写 ---> 所有的字母全小写

a = "abcd"      # 字母全大写
print(a.upper())    # ABCD

b = "ABcd"      # 字母全大写
print(b.upper())    # ABCD

# 字母全小写
print(b.lower())    # abcd

c = "ABCD"      # 字母全小写
print(c.lower())    # abcd












