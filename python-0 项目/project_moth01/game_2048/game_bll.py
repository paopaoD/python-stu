# @Project   : Python
# @File      : game_bll.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/21, 14:17
#

'''
    游戏逻辑控制器
                负责处理游戏核心算法

'''

from game_model import DirectionModel
from game_model import Location

import random


class GameCoreCOntroller:
    def __init__(self):
        self.__list_merge = None
        self.__map = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]
                      ]
        self.__list_empty_localtion = []    # 空位置列表

    @property
    def map(self):
        return self.__map

    # 0 移至末尾
    def __zero_to_end(self):
        '''
            零元素移动到末尾
        '''
        for i in range(len(self.__list_merge)-1,-1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    # 合并
    def __merge(self):
        '''
            合并
        '''
        self.__zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    # 向左移动
    def __move_left(self):
        '''
            数字左移
        '''
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    # 向右移动 ---> 切片
    def __move_right(self):
        '''
            数字右移 ---> 切片
        '''
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    # 方阵转置 ---> 行变为列，列变为行
    def __square_matrix_transpose(self,square_matrix):
        '''
            方阵转置
        :param square_matrix:
        :return:
        '''
        for c in range(1, len(square_matrix)):
            for r in range(c, len(square_matrix)):
                square_matrix[c - 1][r], square_matrix[r][c - 1] = \
                    square_matrix[r][c - 1], square_matrix[c - 1][r]

    # 定义 上移函数
    def __move_up(self):
        # 调用 转置方阵 函数
        self.__square_matrix_transpose(self.__map)
        # 调用 左移合并
        self.__move_left()
        # 再次调用 转置函数，变为原方阵
        self.__square_matrix_transpose(self.__map)

    # 定义 下移函数
    def __move_down(self):
        # 调用方阵转置函数 ---> 行变为列，列变为行
        self.__square_matrix_transpose(self.__map)
        # 右移合并
        self.__move_right()
        # 再次转置，变为原方阵
        self.__square_matrix_transpose(self.__map)



    # 定义 方向 函数 ---> 将上移，下移，左移，右移，统一放入方向函数中 并放入model模块中
    def move(self,dir):
        '''
            移动
        :param dir:方向，DirectionModel类型
        :return:
        '''
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()



    ## 2，在空白位置 生成 新的 随即数字
    def generate_new_number(self):
        '''
            生成新数字
        :return:
        '''
        # 调用空白位置函数
        self.__get_empty_location()

        # 当列表长度为0时,说明map列表中没有空白位置
        if len(self.__list_empty_localtion) == 0:
            return

        # 随即选择列表中的某个元素 ---> 获取的是 某个为零的位置
        loc = random.choice(self.__list_empty_localtion)
        # 获取随即数字
        # random_num = random.randint(1, 10)
        # if random_num == 1:
        if random.randint(1, 10) ==1:   # 相当于是 出现4的几率10%
            self.__map[loc.r_index][loc.c_index] = 4
        else:                           # 相当于是 出现2的几率90%
            self.__map[loc.r_index][loc.c_index] = 2

        # 或者：表达式
        # self.__map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) ==1 else 2

        # 因为在该位置生成了新数字，所以该位置就不是空位置 要把这个位置删除
        self.__list_empty_localtion.remove(loc)


    # 获取 空白 位置
    def __get_empty_location(self):
        '''
            获取空位置(也即为0的位置)
        :return:
        '''
        # 每次统计空位置，都先清空之前的数据，避免影响本次数据
        self.__list_empty_localtion.clear()
        # 确定哪个空白位置
        for r in range(len(self.__map)):  # 获取行数
            for c in range(len(self.__map[r])):  # 获取列数
                if self.__map[r][c] == 0:
                    # 把 为零的位置 以元组的形式存入列表
                    # 空白位置 从game_model模块中导入
                    self.__list_empty_localtion.append(Location(r,c))
        # return list_empty_localtion



    def is_game_over(self):
        '''
            游戏是否结束
        :return: False 表示没有结束  True 表示结束
        '''
        #是否有空位置
        if len(self.__list_empty_localtion) > 0:
            return False    # 没有结束

        # # 横向没有相同的元素
        # for r in range(len(self.__map)):
        #     for c in range(len(self.__map[r])-1):
        #         if self.__map[r][c] == self.__map[r][c+1]:
        #             return False
        #
        # # 竖向没有相同的元素
        # for c in range(len(self.__map)):
        #     for r in range(len(self.__map[c])-1):
        #         if self.__map[r][c] == self.__map[r+1][c]:
        #             return False

        # 横向没有相同的元素
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])-1):
                if self.__map[r][c] == self.__map[r][c+1] or \
                        self.__map[r][c] == self.__map[r+1][c]:
                    return False

        return True





"""
# 测试代码
if __name__ == '__main__':
    controller = GameCoreCOntroller()
    # # controller.__move_left()
    # # print(controller.map)   # 测试左移
    # controller.__move_down()
    # print(controller.map)
    # controller.move(DirectionModel.LEFT)    #
    # print(controller.map)   # 测试左移

    # 测试随机数函数
    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()
    print(controller.map)

    # 判断是否结束
    controller.is_game_over()
    print(controller.map)
"""














































