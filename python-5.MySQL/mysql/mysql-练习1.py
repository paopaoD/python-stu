# @Project   : Python
# @File      : mysql-练习1.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/29, 11:30
#

'''
    将单词本 dict 存入数据库
        1 创建数据库 dict (utf8)
        2 创建数据表 words   将单词和单词解释分别存入不同的字段
        3 将单词存入words单词表中
'''
import re

import pymysql

# 1 创建数据库 dict (utf8)
#   create database dict;
#   use dict;

# 2 创建数据表 words
"""
create table words (id int primary key auto_increment,
                    word char(32),
                    mean text);
"""

# 3 打开 dict.txt 文件
f = open("dict.txt")    # 不写打开方式  默认读的方式 "r"

# 4 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",       # 数据库为 dict
                     charset="utf8",)

# 5 获取游标 (操作数据库，执行sql语句)
cur = db.cursor()

sql = "insert into words (word,mean) values (%s,%s)"

#
for line in f:
    # 6 获取单词和解释
    tup = re.findall(r"(\S+)\s+(.*)",line)[0]
    print(tup)
    try:
        cur.execute(sql,tup)
        db.commit()
    except:
        db.rollback()


# 4 关闭游标，数据库
cur.close()
db.close()









































































