# @Project   : Python
# @File      : mysql-练习2.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/29, 12:52
#

'''
练习：
    1，编写一个程序模拟注册和登录的过程

        创建一个user表  包含用户名和密码字段
        应用程序中模拟注册和登录功能

        注册则输入用户名密码  并将其存放到数据库中
                (用户名不能重复)

    登录则进行数据库比对，如果有该用户，打印登录成功，否则让重新登陆

'''

import pymysql

# 创建一个user表  包含用户名和密码字段
#   create table user (users varchar(32) not null primary key,password varchar(32) not null);


#  连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="user",       # 数据库为 user
                     charset="utf8",)

# 5 获取游标 (操作数据库，执行sql语句)
cur = db.cursor()

# 定义  注册
def register():
    name = input("用户名：")
    password = input("密 码：")
    # 获取数据库中的用户名
    sql = "select * from user where name = '%s'"%name
    cur.execute(sql)
    result = cur.fetchone()
    # 判断用户名是否重复
    if result:      # 如果为True 说明有 说明查到了信息，表示已经注册过
        return False

    try:            # 如果查不到，说明没有注册过，将该数据插入进去
        sql = "insert into user (name,password) values (%s,%s)"
        cur.execute(sql,[name,password])
        db.commit()
        return True

    except:
        db.rollback()
        return False


# 定义  登录
def login():
    name = input("用户名：")
    password = input("密 码：")
    sql = "select * from user where " \
          "name = '%s' and password = '%s' "%(name,password)
    cur.execute(sql)
    result = cur.fetchone() # 获取一个结果
    if result:          # 如果为True 说明有该用户，可以登陆
        return True


while True:
    print("""=============
 1,注册  2,登录
 =============
    """)
    cmd = input("请选择：")
    if cmd == "1":
        # 执行
        if register():
            print("注册成功")
        else:
            print("注册失败")

    elif cmd == "2":
        # 执行
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")





# 4 关闭游标，数据库
cur.close()
db.close()















































































