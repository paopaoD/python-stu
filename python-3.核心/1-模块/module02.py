# @Project   : Python
# @File      : module02.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/13, 15:35
#




# 练习1：
list01 = [
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
]

# 在二维列表list01中，获取13位置，向左，3个元素
# 在二维列表list01中，获取22位置，向上，2个元素
# 在二维列表list01中，获取03位置，向下，2个元素

class Vector01:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @staticmethod
    # 定义函数   向左移动
    def left():
        return Vector01(0,-1)

    @staticmethod
    # 定义函数   向右移动
    def right():
        return Vector01(0,1)

    @staticmethod
    # 定义函数   向上移动
    def up():
        return Vector01(-1,0)

    @staticmethod
    # 定义函数   向下移动
    def down():
        return Vector01(-1,0)



class DoubleListHelper:
    @staticmethod
    def get_elements(list01,vect_pos,vect_dir,count):
        list02 = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = list01[vect_pos.x][vect_pos.y]
            list02.append(element)
        return list02





# 在二维列表list01中，获取13位置，向左，3个元素
result01 = DoubleListHelper.get_elements(list01,Vector01(1,3),Vector01.left(),3)
for item in result01:
    print(item)     # ['12', '11', '10']

# 在二维列表list01中，获取22位置，向上，2个元素
result02 = DoubleListHelper.get_elements(list01,Vector01(2,2),Vector01.up(),2)
for item in result02:
    print(item)     # ['12', '02']

# 在二维列表list01中，获取03位置，向下，2个元素
result03 = DoubleListHelper.get_elements(list01,Vector01(0,3),Vector01.down(),2)
for item in result03:
    print(item)     # ['23', '13']


































