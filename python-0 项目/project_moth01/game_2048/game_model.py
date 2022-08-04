# @Project   : Python
# @File      : game_model.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/21, 16:38
#
'''
    数据模型

'''

class DirectionModel:
    '''
        方向数据模型
        枚举  常量
    '''
    # 在整数基础上 添加一个人容易识别的标签
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3



class Location:
    '''
        位置索引
    '''
    def __init__(self,r,c):
        self.r_index = r
        self.c_index = c



























