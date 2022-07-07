# @Project   : Python
# @File      : 5.mysql_update.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/29, 9:32
#

'''
    mysql
        update   修改
        delete  删除

'''

#### 修改

import pymysql

# 1 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8",)

# 2 获取游标 (操作数据库，执行sql语句)
cur = db.cursor()

# 写数据库
try:
    # 写sql语句执行

    # 修改操作
    sql = "update interest set price= 11800 where id = 2"
    cur.execute(sql)
    db.commit()


except Exception as e:
    db.rollback()   # 一旦报错，退回到commit执行之前的数据库状态
    print(e)



# 4 关闭游标，数据库
cur.close()
db.close()







###### 删除

# 1 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8",)

# 2 获取游标 (操作数据库，执行sql语句)
cur = db.cursor()

# 写数据库
try:
    # 写sql语句执行

    # 删除操作
    sql = "delete from class_1 where score < 80"
    cur.execute(sql)
    db.commit()

except Exception as e:
    db.rollback()   # 一旦报错，退回到commit执行之前的数据库状态
    print(e)



# 4 关闭游标，数据库
cur.close()
db.close()











































































