# @Project   : Python
# @File      : 正则表达式-re.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/7/2, 13:45
#

'''
    re模块
        定义：即文本的高级匹配模式，提供搜索，替换功能。
                其本质是由一些列字符和特殊符号构成的字串，这个字串即正则表达式

        原理：通过普通字符和有特定含义的字符，来组成字符串，用以描绘一定的字符串规则
                比如：位置，重复等 来表达某类特定的字符串，进行匹配

    字符分类：
        匹配字符：. [...] [^...] \d \D \w \W \s \S
        匹配重复：* + ? {n} {m,n}
        匹配位置：^ $ \A \Z \b \B
        其他   ：| () \

'''


import re

'''----正则元字符----'''

## 元字符 [] 字符集 匹配一组可能出现的字符。
s = re.findall('[0-9]',"123asdWERWE")
print(s)
s = re.findall('[0-9a-z]',"123asdWERWE")
print(s)
s = re.findall('[0-9a-zA-Z]',"123asdWERWE")
print(s)


## 元字符 [^字符集]  字符集取反集  匹配除了字符集以外的任意一个字符
s = re.findall('[^0-9]',"123asdWERWE")
print(s)    # ['a', 's', 'd', 'W', 'E', 'R', 'W', 'E']

s = re.findall('[^WE]',"123asdWERWE")
print(s)    # ['1', '2', '3', 'a', 's', 'd', 'R']


## 元字符 ^  开始位置  匹配目标字符串的开头位置
s = re.findall('^Jame',"Jame,hello")
print(s)    # ['Jame']

s = re.findall('^python',"python,pymysql,ipython")
print(s)    # ['python']


## 元字符 $  结束位置  匹配目标字符串的结尾位置
s = re.findall('python$',"hi,python")
print(s)    # ['python']


### 规则技巧：^和$必然出现在正则表达式的开头和结尾处。
#            如果两者同时出现，则中间部分必须匹配整个目标字符串的全部内容
s = re.findall('^Jame$',"Jame")
print(s)    # ['Jame']



## 元字符 . 字符代表匹配任何单个字符，它只能出现在方括号以外。
s = re.findall("ab.d","abcd,abdd,abmd")
print(s)    # ['abcd', 'abdd', 'abmd']

s = re.findall("[A-Z][a-z].","How are you?Fine,Jame")
print(s)    # ['How', 'Fin', 'Jam']


## 元字符 *  匹配前面的字符出现0次或多次  等价于{0,} 表示0个以上
s = re.findall("wo*","woooooooo~~w!")
print(s)    # ['woooooooo', 'w']

s = re.findall("a\d*","a,a123,123456789,abcde")
print(s)    # ['a', 'a123', 'a']


## 元字符 +  匹配前面的字符出现1次或多次  等价于{1,} 表示1个以上
s = re.findall("[A-Z][a-z]+","How are you?Fine,JAME")
print(s)    # ['How', 'Fine', 'Jame']

s = re.findall("[A-Z][a-z]+","How are you?Fine,J")
print(s)    # ['How', 'Fine']


## 元字符 ? 匹配字符出现零次或一次。
s = re.findall("honou?r","honour,honor")
print(s)    # ['honour', 'honor']

s = re.findall("-?[0-9]+","15 -58 -8 78")
print(s)    # ['15', '-58', '-8', '78']


### 练习：匹配"Port-9 Error #404# %@STD"
s = re.findall("[^ ]+","Port-9 Error #404# %@STD")
print(s)    # ['Port-9', 'Error', '#404#', '%@STD']



## 元字符 {n}  匹配前面的字符出现n次
s = re.findall("ab{3}","abb,abbb,abbbb,abbbbb")
print(s)    # ['abbb', 'abbb', 'abbb']


### 练习：匹配手机号
s = re.findall("1[3-9][0-9]{9}","18736135509,17335725874,123456887")
print(s)    # ['18736135509', '17335725874']

s = re.findall("\d{3}-\d{5}","010-88480,030-98788")
print(s)    # ['010-88480', '030-98788']


## 元字符 {m,n}  匹配前面的字符出现m~n次  m是下界而n是上界。
s = re.findall("ab{3,4}","abb,abbb,abbbb,abbbbb")
print(s)    # ['abbb', 'abbbb', 'abbbb']


#  开闭区间  闭区间不写即可表示匹配一个或无数个。
s = re.findall("\d{1,}?","12,1234,123456789")
print(s)


### 练习：获取QQ号    最少6位  最多11位
s = re.findall("[1-9][0-9]{5,10}","qq:252732030")
print(s)



# 元字符 \d 匹配任意数字字符。
s = re.findall("\d","326weSD_")
print(s)    # ['3', '2', '6']

# 元字符 \D 匹配任意非数字字符。 ---> 等同于[^0-9]
s = re.findall("\D","32weSD_#")
print(s)    # ['w', 'e', 'S', 'D', '_', '#']



### 练习：匹配端口
s = re.findall("\d{1,5}","Mysql:3306,http:80")
print(s)    # ['3306', '80']

s = re.findall("\D+","Mysql:3306,http:80")
print(s)    # ['Mysql:', ',http:']


# 元字符 \w  匹配普通字符。 普通字符包括:[A-Z][a-z][0-9]、下划线_、汉字
s = re.findall("\w","32weSD_#$，大小")
print(s)    # ['3', '2', 'w', 'e', 'S', 'D', '_']

# 元字符 \W  匹配非普通字符。 非普通字符等同于:[^A-Za-z0-9_] 标点符号也算
s = re.findall("\W","32weSD_#$，大小")
print(s)    # ['#', '$', '，']


# 元字符 \s 匹配任意空字符  空字符指:空格，\r tab、换行\n,\t \v \f 等。
s = re.findall("\s"," ,code j")
print(s)    # [' ', ' ']

s = re.findall("\w+\s+\w+"," ,code j")
print(s)    # ['code j']


# 元字符 \S 匹配任意非空字符  ---> 等同于[^空字符]
s = re.findall("\S+","code  janme")
print(s)    # [',', 'c', 'o', 'd', 'e', 'j']


# 元字符 \A 表示开头位置  ---> 等同于 ^
s = re.findall("\Acode","code  janme")
print(s)    # ['code']

# 元字符 \Z 表示结尾位置  ---> 等同于 $
s = re.findall("janme\Z","code  janme")
print(s)    # ['janme']


# 元字符 \b 表示单词边界  单词边界指数字字母(汉字)下划线与其他字符的交界位置
s = re.findall(r"\bis","this is code  janme")
print(s)    # ['is', 'is']

s = re.findall(r"\bis","this 123is code  janme")
print(s)    # []

s = re.findall(r"\b\d+","123 45 mnM007")
print(s)    # ['123', '45']


# 元字符 \B 表示非单词边界
s = re.findall(r"\Bde","this is code  de janme")
print(s)    # ['is']



































