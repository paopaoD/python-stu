'''
    re模块 功能函数演示2：
        生成match对象函数
'''
import re


'''
re.finditer()   根据正则表达式匹配目标字符串内容    -->返回匹配结果的迭代器
    re.finditer(pattern,string,flags=0)
        pattern：正则表达式
        string：目标字符串
'''
#
content = "今年是2022年，建国73年。"
pattern = r"\d+"

# 返回迭代对象
it = re.finditer(pattern,content)
for s in it:
    print(s)
    print(s.group())    #  获取match对象相应内容






'''
re.fullmatch()   完全匹配目标字符串内容    -->返回匹配内容 match object
    re.finditer(pattern,string,flags=0)
        pattern：正则表达式
        string：目标字符串
'''
#
content = "今年是2022年，建国73年。"

s = re.fullmatch(r"\S+",content)
print(s)
# print(s.group())

# m = re.fullmatch(r"[,\w]+",content)
# print(m)
# # print(m.group())






'''
re.match()   匹配目标字符串开始位置    -->返回匹配内容 match object
    re.finditer(pattern,string,flags=0)

'''

content = "今年是2022年，建国73年。"

s = re.match(r"\d+",content)
print(s)
print(s.group())


























