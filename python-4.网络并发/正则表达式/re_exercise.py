

'''
    正则练习
'''
# 示例：
import re

s = "2006年，因获得《雅虎搜星》比赛冯小刚组冠军而进入演艺圈；" \
    "同年，在冯小刚执导的《跪族篇》中担任女主角。" \
    "2011年，因在古装剧《新还珠格格》中饰演晴儿被更多观众认识。" \
    "2013年，凭借古装剧《陆贞传奇》收获更多关注。" \
    "2014年，在第10届中国金鹰电视艺术节投票活动中被选为“金鹰女神”；" \
    "同年，她还凭借爱情剧《杉杉来了》获得了第5届国剧盛典内地最具人气女演员奖；" \
    "并成立了海润传媒赵丽颖工作室。"


result = re.findall(r"《\w+?》",s)
print(result)


print("------------提取电话号码---------------")
### 1 提取电话号码
content = """
        白日依18799645587山尽，黄河4589665787445221入海流。
        欲穷12345千里目，更上一层17335725874楼。18736135509
"""

# 手机号模式：1开头，总11位，第二位是3~9
import re

pattern = r"1[3-9]\d{9}"

result = re.findall(pattern,content)
print(result)



print("------------提取tel_list文档中的电话号码---------------")
### 2 提取tel_list文档中的电话号码
import re

pattern = r"1[3-9]\d{9}"

file_cont = ""
# 读取文件
with open("tel_list",encoding="utf-8") as fp:
    file_cont = fp.read()

results = re.findall(pattern,file_cont)

print(len(results))
for result in results:
    print(result)




print("------------提取邮箱地址---------------")
### 3 提取邮箱地址
content = """
        寻隐者12345@11.com不要
        差点唐asdfsdf#ddb.com代
        最python666@163.cn这人
        松下问童子，燕子python-abc@163com采药去
        只在此pyton_ant-66@sina.com山中
"""

import re

pattern = re.compile(r"""
        [a-zA-Z0-9_-]+
        @
        [a-zA-Z0-9]+
        \.
        [a-zA-Z]{2,4}
""",re.VERBOSE)

result = re.findall(pattern,content)
print(result)




print("------------密码验证---------------")

def check_password(password):
    if not 6<= len(password) <=20:
        return False, "必须在6-20之间"
    if not re.findall(r"[a-z]",password):
        return False, "必须包含至少1个小写字母"
    if not re.findall(r"[A-Z]",password):
        return False, "必须包含至少1个大写字母"
    if not re.findall(r"[0-9]",password):
        return False, "必须包含至少1个数字"
    if not re.findall(r"[^a-zA-Z0-9]",password):
        return False, "必须包含至少1个特殊字符"
    return True,None

result = check_password("123AS_ssde")
print(result)
result = check_password("123ssde")
print(result)
result = check_password("123AA")
print(result)
result = check_password("AASssde")
print(result)




# 练习：
#    1，匹配一个.com邮箱格式字符串
s = re.findall("\w+@\w+\.com","18736135509@163.com,paopao@tedu.com")
print(s)

#    2，匹配一个密码 8-12位数字字母下划线构成
s = re.findall("\w{8,12}","paopao_258745")
print(s)

#    3，匹配一个数字 正数 负数  整数 小数 分数1/2 百分数45%
s = re.findall(r"-?\d+/?\.?\d*%?","12,-3,-3.5,-5.45,1/2,45%")
print(s)

































