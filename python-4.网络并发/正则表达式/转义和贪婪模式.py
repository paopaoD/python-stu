'''
    正则表达式 转义
'''

import re

## 正则表达式转义 \
s = re.findall("-?\d+\.?\d*","12,2.58,25，-5.6")
print(s)    # ['12', '2.58', '25', '-5.6']

## 正则表达式转义 r
s = re.findall("\bde\b","this is code  de janme")
print(s)    # []        \b 原意为 退格 不转义无法匹配

## r 转义后
s = re.findall(r"\bde\b","this is code  de janme")
print(s)    # ['de']


# 匹配双 \\  原本是要加 \
s = re.findall("\\\\","\\")
print(s)    # ['\\']

#  r 转义后
s = re.findall(r"\\","\\")
print(s)    # ['\\']





'''
    贪婪和非贪婪模式
        贪婪模式：默认情况下，匹配重复的元字符总是尽可能多少向后匹配内容。比如：*+？{吗，n}
        非贪婪模式(懒惰模式)：让匹配重复的元字符尽可能少的向后匹配内容。   
'''

print("------------------贪婪模式----------------------")

#  * 表示匹配0个或多个，但默认匹配多个  --->尽可能向后匹配:贪婪模式
s = re.findall("ab*","abbbbbbbbbdf")
print(s)    # ['abbbbbbbbb']

# + 表示匹配1个或多个，但默认匹配多个  --->尽可能向后匹配:贪婪模式
s = re.findall("ab+","abbbbbbbbbdf")
print(s)    # ['abbbbbbbbb']

# ? 表示匹配0个或1个，但默认匹配1个  --->尽可能向后匹配:贪婪模式
s = re.findall("ab?","abbbbbbbbbdf")
print(s)    # ['ab']

# 表示匹配3~4个，但默认匹配4个  --->尽可能向后匹配:贪婪模式
s = re.findall("ab{3,4}","abbbbbbcd")
print(s)    # ['abbbb']


s = re.findall("ab{3}","abbbbbbbbbdf")
print(s)    # ['abbb']


print("------------------非贪婪模式----------------------")

#### 贪婪模式 转换为 非贪婪模式，在匹配元字符后面加 ? 号即可。

# * 表示匹配0个或多个，此时匹配0个  --->匹配最少的内容： 非贪婪模式
s = re.findall("ab*?","abbbbbbbbbdf")
print(s)    # ['a']

# + 表示匹配1个或多个，此时匹配1个  --->匹配最少的内容： 非贪婪模式
s = re.findall("ab+?","abbbbbbbbbdf")
print(s)    # ['ab']

#  ? 表示匹配0个或1个，此时匹配0个  --->匹配最少的内容： 非贪婪模式
s = re.findall("ab??","abbbbbbbbbdf")
print(s)    # ['a']

# 表示匹配3~4个，此时匹配3个  --->匹配最少的内容： 非贪婪模式
s = re.findall("ab{3,4}?","abbbbbbcd")
print(s)    # ['abbb']



# 练习1：
content = "[杉杉来了],[花千骨],[新还珠格格],[楚乔传]"

s = re.findall(r"\[\w+?\]+",content)
print(s)    # ['[杉杉来了]', '[花千骨]', '[新还珠格格]', '[楚乔传]']

s = re.findall(r"\[.+?\]", content)
print(s)    # ['[杉杉来了]', '[花千骨]', '[新还珠格格]', '[楚乔传]']


# 练习2：
content = "(abc)dfgh(higk)"

s = re.findall(r"\(\w+?\)",content)
print(s)    # ['(abc)', '(higk)']

s = re.findall(r"\(.+?\)",content)
print(s)    # ['(abc)', '(higk)']










