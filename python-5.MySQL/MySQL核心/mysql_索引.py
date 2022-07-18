

'''

索引概述：
    定义：对数据库表的一列或多列的值进行排序的一种结果(Btree方法)  MySQL中Btree即相当于B+树

        B树的特点：1,全部节点，均包含索引(id)+数据('Tom_0')
                 2,范围查询是从根节点遍历至指定数据

        B+树的特点：1,非叶子节点，只保存索引 【树宽度优于B树，从而降低了磁盘IO】
                  2,叶子节点保存索引的索引与数据
                  3,叶子节点之间相互连接，形成链表结构【可以做范围查询】

    优点：加快数据检索速度

    缺点：占用物理存储空间
         当对标中数据更新是，索引需要动态维护，降低数据维护速度

'''

### 1 首先，向数据库中导入数据

# 导入数据
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                port=3306,
                user="root",
                password="123456",
                database="stu",
                charset="utf8",)

# 2 获取游标 (操作数据库，执行sql语句)
cur = db.cursor()

# 3 执行SQL语句
data_list = []
for x in range(2000):
    name = "TOM_%s"%(x)
    data_list.append(name)

sql = "insert into students(name) values(%s)"

# 可以使用列表 直接给SQL语句的values传值
cur.executemany(sql,data_list)
db.commit()     # 将写操作提交，也可多次写操作一同提交


# 4 关闭游标，数据库
cur.close()
db.close()



### 2 然后查看索引  ---> 语句查看

# 开启运行时间检测  profiling选项默认off   执行打开
#       mysql> show variables like '%pro%';

# 打开 profiling  1 表示on
#       set profiling = 1;

# 执行查询语句(无索引)
#       select * from students where name = 'Tom_1888';

# 查看执行时间
#       show profiles;

# 在students表的name字段创建索引
#       create index name on students(name);

# 再执行查询语句
#       select * from students where name= 'Tom_1888';

# 查看执行时间
#       show profiles;

















































































