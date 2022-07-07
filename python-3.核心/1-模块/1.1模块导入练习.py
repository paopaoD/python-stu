# @Project   : Python
# @File      : 1.1模块导入练习.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/13, 15:31
#


# 将 module02.py中的
#   练习1 Vector2和DDoubleListHelper定义到
#   该模块练习中


import module02 as m01

# 在二维列表list01中，获取13位置，向左，3个元素
result01 = m01.DoubleListHelper.get_elements(m01.list01,m01.Vector01(1,3),m01.Vector01.left(),3)
for item in result01:
    print(item)





from module02 import Vector01
from module02 import DoubleListHelper
from module02 import list01

# 在二维列表list01中，获取22位置，向上，2个元素
result02 = DoubleListHelper.get_elements(list01,Vector01(2,2),Vector01.up(),2)
for item in result02:
    print(item)







from module02 import *


# 在二维列表list01中，获取03位置，向下，2个元素
result02 = DoubleListHelper.get_elements(list01,Vector01(0,3),Vector01.down(),2)
for item in result02:
    print(item)
