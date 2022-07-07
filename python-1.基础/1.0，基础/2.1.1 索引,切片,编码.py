#
# @Project   :Python
# @File         :2.1.1 索引,切片,编码.py
# @Time       :2022/5/19,14:48
#

# 1.容器
#       字符串str：存放的是编码值

#####  成员运算符
'''
语法：
    数据 in 序列
    数据 not in 序列

作用：
    如果再指定的序列中找到值，则返回bool类型
'''

# 返回值是True
print('大圣' in '我叫齐天大圣')  # True

# 返回值是False
print('悟空' not in '我叫悟空齐天大圣')  # False


# 字符串必须是相连的
# print('叫我' not in '我叫齐天大圣')  # False


'''
###### str编码的相关函数   
            常用的 utf-8 --->变字长的编码,定义是1~6字节  Ascii是单字节，中文字
                            符绝大多数3字节，一些特殊字符，是4字节
                            
        1字节，256种状态   2字节，65536种状态
        
        str在字符的世界中，是有编码的  要查编码表
        bytes在字节的世界里，只有一个个字节，没有编码
'''

# Ascii编码表中熟记：
#       1.\x00 -----> 表中第一项
#       2.\x01 -----> 1 字符 "1"
#       3.\x09 -----> 9  \t  tab字符
#       4.\x0a -----> 13  \n  换行符
#       5.\x0d -----> 13  \r  回车
#       6.\x30~\x39 -----> 48~57 字符 0~9 \x31 字符1
#       7.\x41 -----> 65 A
#       8.\x61 -----> 97 a

print("A" > "a") # 谁大 False ---> a大  因为a的编码是97 A的是65
print("a" > "A")

# ord(字符串): 返回该字符串的Unicode码
num01 = ord('a')
print(num01)

# chr(Unicode码)：返回该Unicode码相对应的字符串
str01 = chr(97)
print(str01)



####  索引 index     一般作为定位使用，定位一个
# 作用:访问容器元素
# 语法：容器[整数]
# 说明：
#     正向索引从0开始，第二个索引为1，最后一个为len()
#     反向碎银从-1开始，-1代表最后一个，-2代表倒数第二个

message = '我叫齐天大圣'
# 获取正数第三个字索引
print(message[3])  # 天
# 获取最后一个字索引
print(message[-1])  # 圣



####  切片 slice  --->生成一个新列表
#               一般作为定位使用，可以定位一片，好多个

# 作用：从容器中取出相应的元素重新组成一个容器
# 语法：
#     容器[(开始索引):(结束索引)]  --->[]内也是前包后不包

message = '我叫齐天大圣'
print(message[0:2])  # 我叫
# 开始值默认为开头
print(message[:2])  # 我叫
# 结束值默认为末尾
print(message[-2:])  # 大圣
# 结束值和末尾都不写
print(message[:])  # 我叫齐天大圣

# 如果打印 大天齐
print(message[-2:-5:-1])  # 大天齐
print(message[::-1])  # 圣大天齐叫我

# 打印 空
print(message[1:1])  # 空  --->[]内也是前包后不包
print(message[3:1])  # 空  --->需要加步长[3:1:-1]
print(message[-2:1])  # 空  ---> 不能切断

# 索引不能越界
'''print(message[7])'''
# 切片可以越界，但是界外切不到东西，并且不报错
print(message[1:7])  # 叫齐天大圣






# 练习： 在控制台获取一个字符串
#       打印第一个字符，最后一个字符，倒数第三个字符，前两个字符
#       倒序打印字符，
#       如果字符串长度是奇数，则打印中间字符
#
'''
str_num = input('请输入：')
print(str_num[0])
print(str_num[-1])
print(str_num[-3])
print(str_num[0:2])
print(str_num[::-1])
x = len(str_num) // 2
if len(str_num) % 2 !=0:
    print(str_num[x])
# else:
#     print('为偶数')
'''

# 练习1：
# 在控制台中，获取一个字符串，
# 并打印每个字符的编码值
'''
str_num = input('请输入：')
for i in str_num:
    print(ord(i))
'''

# 练习2：
# 在控制台中，重复录入一个编码值，然后打印字符
# 如果输入空字符串，则退出程序
'''
while True:
    str_code = input('请输入编码值：')
    if str_code =='':
        break
    code_num = int(str_code)
    print(chr(code_num))

print('输入错误，退出')
'''


# 练习题3：
'''
name = '悟空'
age = '800'
score = 99.5

print(f'我叫{name},年龄是{age},成绩是{99.5}')
print('我的名字是%s,今天%s岁了,成绩是%.1f' %(name,age,score))
'''

# 打印
'''
number = int(input("请输入："))
print("*" * number)
for item in range(number - 2):
    print("*" + " " * (number - 2) + "*")
print("*" * number)
'''

# 录入一个字符串，判断是否是回文
'''
a = input('输入回文：')
if a[:] == a[::-1]:
    print('是回文')
else:
    print('不是回文')
'''


# 一个小球从100m的高度落下，每次弹回原高度一半。
# 计算：
#       总共弹起来多少次（最小弹起高度0.01m）
#       总共走了多少米

hight = 100
distance = hight  # 经过的距离
count = 0  # 次数

# 弹起来的高度 大于  最小弹起高度
while hight / 2 > 0.01:
    count += 1
    # 每次弹起的高度
    hight /= 2
    # 累加弹起/落下的高度
    distance += hight * 2
    print("第%d次弹起来的高度是%f米" % (count, hight))
print(f"总共弹起来{count}次,总共走了{distance}米")
print("总共弹起来%d次,总共走了%.2f米"%(count,distance))








































