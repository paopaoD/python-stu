# @Project   : Python
# @File      : 3.mysql_read.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/28, 18:26
#


'''
    read_db
        pymysql 读操作 (select)
'''

# 示例
import pymysql

# 1 连接数据库
db = pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="stu",charset="utf8",)

# 2 获取游标 (操作数据库，执行sql语句)
cur = db.cursor()

# 获取数据库数据
sql = "select * from class_1 where sex='w';"

cur.execute(sql) # 执行后，cur调用函数 获取结果

### 获取一个查询结果
one_row = cur.fetchone()    # 获取查询结果中的第一个
print(one_row)  # 元组的形式
print(one_row[5])   # 可以获取某个字段的信息

### 获取多个查询结果
many_row = cur.fetchmany(2)     # 获取查询结果中第一个后面的2个
print(many_row)

### 获取所有查询结果
all_row = cur.fetchall()     # 获取的是查询结果 之后的  如果想要全部 可以把上面代码注释
print(all_row)



# 4 关闭游标，数据库
cur.close()
db.close()





