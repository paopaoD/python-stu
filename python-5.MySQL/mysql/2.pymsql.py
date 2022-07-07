# @Project   : Python
# @File      : 2.pymsql.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/28, 17:15
#

'''
    pymsql

        使用流程：
            1,建立数据库连接：(db = pymsql.connect(...))
            2,创建游标对象：(c = db.cursor())
            3,游标方法   ： c.execute("insert....")
            4,提交到数据库：db.commit()
            5,关闭游标对象：c.close()
            6,断开数据连接：db.close()


        常用函数：
            db =  pymsql.connect(参数列表)
                host ：主机地址，本地localhost
                port ：端口号 默认3306
                user ：用户名
                password ：密码
                database ：库
                charset ：编码方式 推荐 utf8


        数据库连接对象(db)的方法:
            db.commit()  提交到数据库执行
            db.rollback() 回滚
            cur = db.cursor() 返回游标对象，用于执行具体sql命令
            db.close() 关闭连接


        游标对象(cur)的方法
            cur.execute(sql命令,[列表]) 执行SQL命令
            cur.close() 关闭游标对象
            cur.fetchone() 获取查询结果集的第一条数据
            cur.fetchmany(n) 获取n条((记录1),(记录2))
            cur.fetchall() 获取所有记录

'''

# 示例：
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

# 3 执行SQL语句   --> 写操作
sql = "insert into class_1 values (8,'Kima',18,'w',80.5,'2022-6-27','17535725827');"

cur.execute(sql)    # 执行语句

db.commit()     # 将写操作提交，也可多次写操作一同提交


# 4 关闭游标，数据库
cur.close()
db.close()






















































































