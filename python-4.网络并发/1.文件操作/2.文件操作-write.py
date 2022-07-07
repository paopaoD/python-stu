# @Project   : Python
# @File      : 2.文件操作-write.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/24, 14:05
#

'''
    写入文件

        write(string):把文本数据或二进制数据块的字符串  写入到文件中去
                        string 要写入的内容     如果要换行，要自己在写入内容中添加\n

        writelines(str_list):接受一个字符串列表作为参数，将它们写入到文件中去


    with ..as..

        with 对象生成语句 as f:
            f.read()
'''

### 1,write  文件写入

# 打开文件
f = open("test02", "w")  # 以写的模式打开，文件不存在，则新建

# 写操作
f.write("hello 老王\n你说  爱不爱我\n")
f.write("hello kitty")

f.close()


### 2，write  文件写入
f = open("test", "a")  # 以追加的模式 写入内容

# 写操作
f.write("hello 老王\n你说  爱不爱我\n")
f.write("hello kitty")

f.close()




### 2，writelines  文件写入
f = open("test", "a")  # 以追加的模式 写入内容

# 写操作
l = ['hello kitty\n',"哈哈"]
f.writelines(l)


f.close()


print("----------------- with ..as..-------------------------")

'''
    with ..as..
        
        with 对象生成语句 as f:
            f.read()
            
'''
# 示例 -- 读取
with open("test02", ) as f:
    data = f.read()
    print(data)


# 示例 -- 写入
with open("test02", "a") as f:
    f.write("哼哼哈哈")
    print("已写入。")




















































