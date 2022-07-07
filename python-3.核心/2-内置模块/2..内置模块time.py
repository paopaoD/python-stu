# @Project   : Python
# @File      : 2..内置模块time.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/14, 10:23
#

'''
    时间模块
            time
'''

import time

# 1,获取当前时间戳  (显示的是从1970年1月1日起到现在经过的秒数)
print(time.time())  # 1655173614.3367639



# 2,获取当前时间，以元组的方式
#               (年，月，日，时，分，秒，一周第几天，一年第几天，夏令时)
print(time.localtime())


tuple_time = time.localtime()
# 通过元组的操作 获取时间
for item in tuple_time:
    print(item)
print(tuple_time[1])    # 获取 月

# 通过类的操作 获取时间
print(type(tuple_time))
print(tuple_time.tm_year)   # 获取 年



# 时间元组 --> 时间戳
print(time.mktime(tuple_time))



# 时间元组 --> str
str_time01 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(str_time01)


# str --> 时间元组
print(time.strptime(str_time01,"%Y-%m-%d %H:%M:%S"))




import datetime

# 返回一个当前时区时间对象
time01 = datetime.datetime.now()
print(time01)

time02 = datetime.datetime.today()
print(time02)







print("--------------------练习-----------------------")


# 练习：定义函数，根据年月日，返回星期数
#       "星期一"，"星期二"，"星期三"...
#   思路：年月日 --> 时间元组 --> 星期 --> 格式


def get_week(year,month,day):
    '''
        获取星期数
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 星期几
    '''
    tuple_time = time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
    dict_weeks = {
        0:"星期一",
        1:"星期二",
        2:"星期三",
        3:"星期四",
        4:"星期五",
        5:"星期六",
        6:"星期日",
    }
    return dict_weeks[tuple_time[6]]

re = get_week(2022,6,13)
print(re)





# 练习2：根据生日(年月日)，计算活了多少天

def life_day(year,month,day):
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    born_time = time.mktime(tuple_time)
    now_time = time.time()
    get_time = now_time - born_time
    return int(get_time / 3600 // 24)

re = life_day(1993,6,14)
print(f"一共活了{re}天")






























