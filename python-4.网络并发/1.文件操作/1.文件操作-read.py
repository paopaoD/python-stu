# @Project   : Python
# @File      : 1.文件操作-read.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/24, 11:31
#

'''
    文件读取
        语法：file_object = open(file_name,access_mode='r',buffering = 1)
            file_name 文件名
            access_mode 打开文件的方式，如果不写 默认为'r'

            文件模式
                r   以 读 的方式打开，文件必须存在
                w   以 写 的方式打开 文件不存在则创建，存在则清空
                a   以 追加 模式打开

                r+   以 读写 模式打开，文件必须存在
                w+   只 读写 方式打开 文件不存在则创建，存在则清空
                a+   以 读写 模式打开，追加模式

                rb   以二进制 读 的方式打开，同r
                wb   只二进制 写 的方式打开,同w
                ab   以二进制 追加模式打开,同a

                rb+   以二进制 读写 模式打开，同r+
                wb+   只二进制 读写 模式打开,同w+
                ab+   以二进制 读写 模式打开,同a+

            buffering ：  1 表示有行缓冲
                        -1 为默认，表示使用系统默认提供的缓冲机制

        read([size]):读取文件，size不填  默认读取全部，填写表示读取到size位置

        readline([size]):用来读取文件中一行
                            size(默认值-1),默认读取一行，填写表示读取到size位置

        readlines([size]):读取文件中的每一行作为列表中的一项
                            size(默认值-1),默认读取一行，填写则读取到size位置
'''

######1，read

# 打开文件
f = open('test', 'r') # 打开 test 文件  以 读 的方式

data = f.read(8)   # 表示读取到第8个位置 空格 换行符都算
print(data)

f.close()


print()
# 打开文件
f = open('test', 'r')

while True:
    # 读到文件结尾返回空字符串
    data = f.read(100)  # 每次最多读取100个字符
    if not data:        #读到结尾 跳出循环
        break
    print(">",data)

f.close()




######2，readline
print()
# 打开文件
f = open('test', 'r')

data = f.readline() # 读取一行内容
print("一行内容：",data)

# 第一次不填默认值，再次读取  则会换行，
# 如果填写，再次读取则是读取这行剩下的内容
data = f.readline(5)    # 读取第二行 前5个字符
print("一行内容：",data)
data = f.readline()    # 读取的是第二行 5个以后 剩余的内容
print("一行内容：",data)

f.close()


######2，readlines
print()
# 打开文件
f = open('test', 'r')

# 将内容读取为列表
data = f.readlines(12)   # 第一行不足12个字符，则会读取第一行第二行内容
print(data)

data = f.readlines()    # 将内容读取为列表
print(data)

f.close()



print()
# 打开文件
f = open('test', 'r')

# 打开的文件本身 f 也是一个可迭代对象
for i in f:     # 获取每一行
    print(i)





# 练习：输入一个单词，从单词本中找到该单词，打印解释内容，
#                   如果找不到  则打印“找不到”

word = input("word:")

f = open("dict.txt")

# 获取每一行
for line in f:
    # 将每一行分割之后，取第一个
    w = line.split(" ")[0]
    # 如果遍历到的单词已经大于word 就结束查找
    if w >word:
        print("没找到")
        break
    elif w == word:
        print(line)
        break
else:
    print("没找到")

f.close()






















