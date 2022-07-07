# @Project   : Python
# @File      : 2. 函数练习题.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/26, 13:02
#



# 练习：定义 根据学生成绩，计算等级 的函数。
#

# def get_score_level(socre):
#     ''''''
#     if socre >= 90:
#         return 'A'
#     elif socre >=80:
#         return 'B'
#     elif socre >=70:
#         return 'C'
#     elif socre >=60:
#         return 'D'
#     else:
#         return 'E'
#
#
# socre = int(input('请输入分数：'))
# re = get_score_level(socre)
# print("",re)


# def get_score_level(socre):
#     '''
#         根据学生成绩，计算等级
#     :param socre:成绩
#     :return:    等级
#     '''
#     if socre >= 90:
#         return 'A'
#     if socre >=80:
#         return 'B'
#     if socre >=70:
#         return 'C'
#     if socre >=60:
#         return 'D'
#     return 'E'
#
#
# socre = int(input('请输入分数：'))
# re = get_score_level(socre)
# print("",re)



# 练习： 判断列表中元素是否具有相同元素的   函数
# list01 = [3,80,45,5,80,1]
# result = False      # 定义标记，假设没有相同项
# for i in range(len(list01)-1):
#     for n in range(i+1,len(list01)-1):
#         if list01[i] == list01[n]:
#             print("具有相同项")
#             result = True       # 进入到这里，说明有相同项
#             break       # 退出当前内循环
#     if result == True:
#         break       # 退出全部循环
# if result == False: # 如果没有相同项
#     print(list01)


# def get_same_num(list_target):
#     ''''''
#     for i in range(len(list_target) - 1):
#         for n in range(i + 1, len(list_target)):
#             if list_target[i] == list_target[n]:
#                 return ("具有相同项")
#     return ("没有相同项")
#
#
# list_target = [3,2,45,2,80,1]
# re = get_same_num(list_target)
# print(re)



# 练习1：定义函数 根据年月，计算共有多少天，考虑闰年2月29天，平年28天
#
# list_target = [31,28,31,30,31,30,31,31,30,31,30,31]
# days = 0
# while True:
#     year = input("输入年份：")
#     if year == "":
#         break
#     month = int(input("输入月份："))
#     for i in range(month):
#         days += list_target[i]
#     if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
#         days += 1
# print(days)

'''
def get_day_of_year(year,month):

    days = 0
    for i in range(month):
        days += list_target[i]
    # 判断年份是否是闰年，但是同时又做了一件事，违背了函数干一件事的原则
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days += 1
    return days


list_target = [31,28,31,30,31,30,31,31,30,31,30,31]
year = int(input("输入年份："))
month = int(input("输入月份："))
result = get_day_of_year(year,month)
print(result)
'''



# 练习2：定义函数 根据年月，计算当月有多少天，考虑闰年2月29天，平年28天

# moth = int(input('请输入一个月份：'))
# if moth >12 or moth <1:
#     print('输入的月份错误')
# elif moth == 2:
#     print('28')
# elif moth in (4,6,9,11):
#     print('30天')
# else:
#     print('31天')


# 定义一个新的年份函数，保证函数只做一件事
def get_year(year):
    '''
        是否是闰年
    :return: 闰年
    '''
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return True
    # else:
    #     return False
    return  year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_day_by_month(year,month):
    '''
        计算当月天数
    :param year:
    :param month:
    :return:
    '''
    if month > 12 or month < 1:
        return 0
    if month == 2:
        # 调用定义的闰年函数
        if get_year(year):  # 如果是闰年 --->if get_year(year) = True
            return 29
        else:
            return 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


# year = int(input('请输入一个年份：'))
# month = int(input('请输入一个月份：'))
# day = get_day_by_month(year,month)
#
# print(day)






# 练习：定义  列表升序排列的函数

# list01 = [9, 8, 7, 66, 54, 2, 3, 88, 4, 5, 99]
# # 取前一个数据
# for n in range(len(list01) - 1):
#     # 取后一个数据
#     for i in range(n+1, len(list01) - 1):
#         # 两者作比较
#         if list01[n] > list01[i]:
#             list01[n], list01[i] = list01[i], list01[n]
#         # print(list02)
# print(list01)


# 定义函数：

def sort_list_num(list_target):
    # 1，传入的是可变对象，
    # 2，函数体修改的栈中传入的对象
    # 满足以上两个条件，就无须通过返回值传递结果

    for n in range(len(list_target) - 1):
        for i in range(n + 1, len(list_target) - 1):
            if list_target[n] > list_target[i]:
                list_target[n], list_target[i] = list_target[i], list_target[n]

    # # 传的是可变对象，改的是传入的对象，满足前面两个条件，就不需要return
    # return list_target


list01 = [9, 8, 7, 66, 54, 2, 3, 88, 4, 5, 99]
sort_list_num(list01)
print(list01)





'''#### 练习：定义  方阵转置 函数  '''

# list01 = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,1,4,2],
#     [3,4,9,1],
# ]
# # 中间斜线的1,6,4,1 不用交换位置，只交换对应的元素
# for c in range(1,len(list01)):
#     # list01[0][r] = list01[r][0]
#     for r in range(c,len(list01)):
#         #
#         list01[c-1][r],list01[r][c-1] = list01[r][c-1],list01[c-1][r]
#     # print(list01)
# print(list01)



# 定义函数：

def square_matrix_transpose(list01):
    '''
        方阵转置
    :param list01:
    :return:
    '''
    for c in range(1, len(list01)):
        for r in range(c, len(list01)):
            list01[c - 1][r], list01[r][c - 1] = \
                list01[r][c - 1], list01[c - 1][r]


list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,1,4,2],
    [3,4,9,1],
]
# 执行转置后，行变为列，列变为行
square_matrix_transpose(list01)
print(list01)

# 再次转置后，又变回原来的方阵
square_matrix_transpose(list01)
print(list01)








# 练习：1，实现字符串：" 校  训：自  强不息，厚德载物。   "
#       查找空格的数量，
#       删除字符串前后空格  所有空格
#       查找"载物"的位置
#       判断字符串是否以"校训"开头

str01 = " 校  训:自 强不息,厚德载物.   "

# 查找空格的数量，
a = str01.count(" ")
print(a)

# 删除字符串前后空格
str02 = str01.rstrip().strip()
print(str02)                # 校  训:自  强不息,厚德载物.

# 删除字符串所有空格 --> 没有删除所有空格的函数，所以使用replace替换
print(str01.replace(" ",""))    # 校训:自强不息,厚德载物.


# 查找"载物"的位置 ---> find
print(str01.find("载物"))
print(str01.find("载车"))  # 没有该字符  返回-1

#   或者 index
print(str01.index("载物"))


# 判断字符串是否以"校训"开头
print(str01.startswith("校训"))
print(str01.startswith(" "))

# 判断字符串是否以"载物"开头
print(str01.endswith("载物"))


print("$".join(str01))



# 练习：2，定义函数，统计指定范围内的素数，并打印到列表  比如1-100或1-50之间
#
# 一般写法：
# def get_prime(begin,end):
#     result_num = []
#     # 生成范围内的整数
#     for number in range(begin,end):
#         for item in range(2,number):
#             # 判断是否是素数
#             if number % item == 0:
#                 break
#         else:
#             result_num.append(number)
#     return result_num
#
# print(get_prime(5,30))


print("-------------------------------------")
# 写法二：函数只做一件事

# 定义函数 判断是否是素数
def is_prime(number):   # 定义函数 判断是否是素数
    '''
        判断是否是素数
    :param number: 范围内的整数
    :return: True 代表是素数，False 代表不是素数
    '''
    for item in range(2, number):
        if number % item == 0:
            return False
    return True


# 获取范围内的素数
def get_prime(begin,end):
    '''
        获取范围内的素数
    :param begin: 开始值(包含)
    :param end: 结束值（不包含）
    :return: 所有素数的列表
    '''
    result_num = []
    # 生成范围内的整数
    for number in range(begin,end):
            if is_prime(number):
                result_num.append(number)
    return result_num

print(get_prime(5,30))





def get_prime(begin,end):
    result_num = []
    # 生成范围内的整数
    for number in range(begin,end):
        for item in range(2,number):
            # 判断是否是素数
            if number % item == 0:
                break
        else:
            result_num.append(number)
    return result_num

print(get_prime(5,30))








# is 和 == 的区别   is 是地址相同    == 是内容,值相同
# a = [1,2]
# b = [1,2]
#
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))
#
# a = 1
# b = 1
#
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))





# 用 函数嵌套函数 定义代码

dict_commodity_info = {
    101:{"name":"屠龙刀","price":"10000"},
    102:{"name":"倚天剑","price":"10000"},
    103:{"name":"九阴白骨爪","price":"8000"},
    104:{"name":"九阳神功","price":"9000"},
    105:{"name":"降龙十八掌","price":"8000"},
    106:{"name":"乾坤大挪移","price":"10000"}
}

list_order = []

def select_shopping():
    '''
        购物
    :return:
    '''
    while True:
        item = input("1键购买，2键结算。请输入：")
        if item == "1":
            for key,value in dict_commodity_info.items():
                print("编号：%d,名称：%s，单价：%s."%(key,value["name"],value["price"]))
            while True:
                cid = int(input("请输入商品编号："))
                if cid in dict_commodity_info:
                    break
                else:
                    print("不存在")
            count = int(input("输入数量："))
            list_order.append({"cid":cid,"count":count,})
        elif item == "2":
            zong_jia = 0
            for item in list_order:
                shang_pin = dict_commodity_info[item["cid"]]
                print(f"商品：{shang_pin['name']},单价：{shang_pin['price']},数量：{item['count']}")
                zong_jia += int(shang_pin["price"]) * int(item['count'])
            while True:
                qian = float(input(f"总价为{zong_jia}元，请输入金额："))
                if qian >= zong_jia:
                    print(f"购买成功，余额为{qian-zong_jia}。")
                    list_order.clear()
                    break
                else:
                    print("金额不足")

select_shopping()




#——————————> 定义上面代码   使用多个函数



# 菜单列表
dict_commodity_info = {
    101:{"name":"屠龙刀","price":"10000"},
    102:{"name":"倚天剑","price":"10000"},
    103:{"name":"九阴白骨爪","price":"8000"},
    104:{"name":"九阳神功","price":"9000"},
    105:{"name":"降龙十八掌","price":"8000"},
    106:{"name":"乾坤大挪移","price":"10000"}
}

# 购物车
list_order = []

# 选择菜单
def select_menu():
    '''
        选择菜单
    :return:
    '''
    while True:
        item = input("1键购买，2键结算。请输入：")
        if item == "1":
            # 购买 函数
            buying()

        elif item == "2":
            # 结算
            settlement()


# 结算
def settlement():
    '''
        计算总价
    '''
    # 计算总价
    total_price = calculate_total_price()

    # 执行购买
    paying(total_price)


# 执行购买
def paying(total_price):
    '''
        支付过程
    :param total_price:需要支付的价格
    :return:
    '''
    while True:
        money = float(input(f"总价为{total_price}元，请输入金额："))
        if money >= total_price:
            print(f"购买成功，余额为{money - total_price}。")
            list_order.clear()
            break
        else:
            print("金额不足")


# 计算总价
def calculate_total_price():
    total_price = 0
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        print(f"商品：{commodity['name']},单价：{commodity['price']},数量：{order['count']}")
        total_price += int(commodity["price"]) * int(order['count'])
    return total_price


# 购买
def buying():
    '''
        购买
    '''
    # 打印商品信息
    print_commodity_info()
    # 创建订单 添加购物车
    creat_order()


# 创建订单 添加购物车
def creat_order():
    '''
        创建订单 添加购物车
    '''
    # 获取商品编号
    cid = input_commodity_id()

    count = int(input("输入数量："))
    order = {"cid": cid, "count": count}
    list_order.append(order)
    print("添加到购物车。")


# 获取商品编号
def input_commodity_id():
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("不存在")
    return cid


# 打印商品信息
def print_commodity_info():
    for key, value in dict_commodity_info.items():
        print("编号：%d,名称：%s，单价：%s." % (key, value["name"], value["price"]))


select_menu()
































