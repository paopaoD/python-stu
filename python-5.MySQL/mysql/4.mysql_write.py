# @Project   : Python
# @File      : 4.mysql_write.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/28, 21:09
#

'''
    write

        pymysql 写操作
'''

# 示例
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
    # name = input("Name:")
    # age = int(input("Age:"))
    # score = float(input("Score:"))
    # 将变量插入到sql语句合成最终操作语句
    # sql = f"insert into class_1 (name,age,score) " \
    #       "values ('%s',%d,%f)"%(name,age,score)
    #
    # cur.execute(sql)

    name = input("Name:")
    age = input("Age:")
    score = input("Score:")
    sql = "insert into class_1 (name,age,score) " \
          "values (%s,%s,%s)"

    # 可以使用列表 直接给SQL语句的values传值
    cur.execute(sql,[name,age,score])

    db.commit()

except Exception as e:
    db.rollback()   # 一旦报错，退回到commit执行之前的数据库状态
    print(e)



# 4 关闭游标，数据库
cur.close()
db.close()
















































