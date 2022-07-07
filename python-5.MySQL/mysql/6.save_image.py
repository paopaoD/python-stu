# @Project   : Python
# @File      : 6.save_image.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/29, 12:26
#

'''
    pymysql
        二进制图片存储  读取

'''

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

# 3 读取图片
with open('timg.jpg','rb') as f:
    data = f.read()

# 将图片 存储 到数据库中
try:
    sql = "update class_1 set image = %s where name = 'jame'"

    cur.execute(sql,[data])
    db.commit()

except Exception as e:
    db.rollback()
    print(e)



# 4 关闭游标，数据库
cur.close()
db.close()





###########   读取/提取

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8",)

# 2 获取游标 (操作数据库，执行sql语句)
cur = db.cursor()


# 执行sql命令

sql = "select image from class_1 where name = 'jame'"

cur.execute(sql)    # 执行sql命令

data = cur.fetchone()   # 获取查询结果集的第一条数据 以元组的形式


# 读取图片  将获取的突破 以 二进制 方式写入到 tutu.jpg 中
with open('tutu.jpg','wb') as fp:
    fp.write(data[0])


# 4 关闭游标，数据库
cur.close()
db.close()


























