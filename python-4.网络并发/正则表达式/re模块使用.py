'''
    re模块 功能函数演示1：


'''


import re

''' 
re.search().group() 
    分组：可以被作为整体操作，改变元字符的操作对象
          
'''

s = re.search(r"ab+","ababababababab").group()
print(s)    # ab

s = re.search(r"(ab)+","ababababababab").group()
print(s)    # ababababababab


s = re.search(r"王|李\w{1,3}","李四").group()
print(s)

s = re.search(r"(王|李)\w{1,3}","王者荣耀").group()
print(s)

# 可以通过编程语言某些接口获取匹配内容中，子组对应的内容部分
#   比如获取url协议类型
s = re.search(r"(http|https|ftp|file)://\S+","http://www.baidu.com").group()
print(s)    # http://www.baidu.com

# 或者  获取一部分
s = re.search(r"(http|https|ftp|file)://\S+","http://www.baidu.com").group(1)
print(s)    # http


### 捕获组：可以给震泽表达式的子组起一个名字，表达该子组的一员，这种有名称的子组即为捕获组
#     格式：(?P<name>pattern)

s = re.search(r"(?P<pig>ab)+","ababababababab").group("pig")
print(s)    # ab

# 一个正则表达式可以包含多个子组
# 子组可以嵌套，但是不要重叠或者嵌套结构复杂
# 子组序列号一般从外到内，从左到右计数   1((ab)c)  2(ab)  3(?P<pig>ef)
s = re.search(r"((ab)c)d(?P<pig>ef)+","abcdefghijklmn").group("pig")
print(s)








'''
re.findall(pattern,content)   根据正则表达式匹配目标字符串内容
    pattern：正则表达式
    content：目标字符串
'''
# 目标字符串
content = "Alex:1994,Sunny:1996"
# 正则表达式
pattern = r"\w+:\d+"

# re 模块调用 findall
s = re.findall(pattern,content)
print(s)    # ['Alex:1994', 'Sunny:1996']






'''
regex = compile(pattern,flags=0)    生产表达式对象



regex.findall(string,pos,endpos)    根据正则表达式匹配目标字符串内容
    string：目标字符串
    pos：   截取目标字符串的开始匹配位置
    endpos：截取目标字符串的结束匹配位置
'''

# compile 对象调用findall
regex = re.compile(pattern)
s = regex.findall(content)
print(s)    # ['Alex:1994', 'Sunny:1996']

# 截取下标为 0-12
s = regex.findall(content,0,12)
print(s)    # ['Alex:1994']

'''
re.split()    按照正则表达式匹配内容切割字符串
             
'''
content = "Alex.1994,Sunny:1996"
#
s = re.split(r"[:]",content)
print(s)    # ['Alex.1994,Sunny', '1996']






'''
re.sub()    使用一个字符串替换正则表达式匹配到的内容
    re.sub(pattern,replace,string,max,flags)
             replace：替换的字符串 
             string：目标字符串 
             max：最多替换几处，默认替换全部
'''
content = "Alex:1994,Sunny:1996"
#
s = re.sub(r":","-",content)    # 将 : 替换成 - (max不写  默认替换全部)
print(s)    # Alex-1994,Sunny-1996

s = re.sub(r":","-",content,1)      # 只替换一处
print(s)    # Alex-1994,Sunny:1996























































































