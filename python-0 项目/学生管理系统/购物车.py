# @Project   : Python
# @File      : 购物车.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/8, 11:01
#

'''
    将面向过程的购物车，改为面向对象的购物车
'''


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




'''
    改为面向对象的购物车:
'''

# 商品类信息
class CommodityModel:
    def __init__(self,name,price):
        self.name = name
        self.price = price


class commodityController:
    def __init__(self):
        self.__list = []


















