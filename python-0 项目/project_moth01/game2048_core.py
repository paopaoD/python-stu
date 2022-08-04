# @Project   : Python
# @File      : game2048_core.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/27, 21:15
#

'''
    2048 游戏核心算法
'''



list_merge = [2, 0, 2, 0]


print("------------去零-------------")
# 练习1,零元素移至末尾
#   [2,0,2,0] --> [2,2,0,0]
#   [2,0,0,2] --> [2,2,0,0]
#   [2,4,0,2] --> [2,4,2,0]

# 零元素移动到末尾

def zero_to_end():
    '''
        零元素移动到末尾
    '''
    # 从后往前,如果发现零元素,删除,并追加
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            # list_merge.remove(0)
            del list_merge[i]
            list_merge.append(0)

# 测试打印结果
zero_to_end()
print(list_merge)

# 练习2,相同数字合并
#   [2,2,0,0] --> [4,0,0,0]
#   [2,0,0,2] --> [4,0,0,0]
#   [2,0,4,0] --> [2,4,0,0]
#   [2,2,2,2] --> [4,4,0,0]
#   [2,2,2,0] --> [4,2,0,0]


print("------------合并-------------")
# 合并相邻形同元素
def merge():
    '''
        合并
    '''
    # 先将中间的零元素移到末尾  在合并相邻形同元素
    zero_to_end()
    # 判断上一个函数执行后是否正确
    # print(list_merge)
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            # 将后一个累加前一个
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)

# 测试打印结果
# merge()
# print(list_merge)


print("------------左移-------------")
# 练习3,列表内数字左移，
map = [
    [4,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]

# 向左移动
def left_move():
    '''
        数字左移
    '''
    for line in map:
        # 定义全局变量list_merge
        global list_merge
        list_merge = line
        merge()
    # return list_merge

# 测试打印结果
# left_move()
# print(map)




print("------------右移-切片------------")

# 向右移动 ---> 切片
def right_move():
    '''
        数字右移 ---> 切片
    '''
    for line in map:
        global list_merge
        # 这右向左反向切片，是创建了一个新列表
        list_merge = line[::-1]
        merge()
        # 执行完函数后，通过切片来定位列表元素，并未生成新列表
        line[::-1] = list_merge

# 测试打印结果
# right_move()
# print(map)


print("------------右移-reverse------------")

# 向右移动 ---> reverse反转列表函数
def right_move02():
    '''
        数字右移 ---> reverse反转列表函数
    '''
    for line in map:
        # 反转列表line
        line.reverse()
        global list_merge
        list_merge = line
        merge()
        # 执行完函数后 再次反转回来
        line.reverse()

# 测试打印结果
# right_move02()
# print(map)




print("-------------上 移------------")


# 练习4：向上移动 ---> 先方阵转置，然后再执行左移合并
map = [
    [4,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]

# 方阵转置 ---> 行变为列，列变为行
def square_matrix_transpose(square_matrix):
    '''
        方阵转置
    :param square_matrix:
    :return:
    '''
    for c in range(1, len(square_matrix)):
        for r in range(c, len(square_matrix)):
            square_matrix[c-1][r], square_matrix[r][c-1] = \
                square_matrix[r][c-1], square_matrix[c-1][r]

# 定义 上移函数
def move_up():
    # 调用 转置方阵 函数
    square_matrix_transpose(map)
    # 调用 左移合并
    left_move()
    # 再次调用 转置函数，变为原方阵
    square_matrix_transpose(map)

# 调用上移函数
move_up()
print(map)

# 打印结果为：
map = [
    [8, 8, 4, 4],
    [2, 0, 0, 4],
    [0, 0, 0, 2],
    [0, 0, 0, 0]
]




print("-------------下 移------------")


# 练习5：向下移动 ---> 先方阵转置，然后再执行右移合并，再次转置
map = [
    [4,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]

"""
# 方阵转置 ---> 行变为列，列变为行
def square_matrix_transpose(square_matrix):
    '''
        方阵转置
    :param square_matrix:
    :return:
    '''
    for c in range(1, len(square_matrix)):
        for r in range(c, len(square_matrix)):
            square_matrix[c-1][r], square_matrix[r][c-1] = \
                square_matrix[r][c-1], square_matrix[c-1][r]
"""

# 定义 下移函数
def move_down():
    # 调用方阵转置函数 ---> 行变为列，列变为行
    square_matrix_transpose(map)
    # 右移合并
    right_move02()
    # 再次转置，变为原方阵
    square_matrix_transpose(map)

# 调用下移函数
move_down()
print(map)

# 打印结果为：
map = [
    [0, 0, 0, 0],
    [0, 0, 0, 4],
    [8, 0, 0, 4],
    [2, 8, 4, 2]
]






























































