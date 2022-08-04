# @Project   : Python
# @File      : game_ui.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/22, 10:55
#

'''
    2048控制台界面

'''
import os

from game_bll import GameCoreCOntroller
from game_model import DirectionModel

class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreCOntroller()

    # 入口
    def main(self):
        self.__start()
        self.__update()


    # 开始游戏
    def __start(self):
        # 产生两个数字
        # controller = GameCoreCOntroller()
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        # 调用 绘制界面 函数
        self.__draw_map()


    # 绘制界面
    def __draw_map(self):
        # # 清空控制台
        # os.system("clear")

        # controller = GameCoreCOntroller()
        for line in self.__controller.map:
            for item in line:
                print(item,end=" ")
            print()


    # 更新游戏
    def __update(self):
        # 循环
        while True:
            # 判断玩家的输入 ---> 移动
            self.__move_map_for_input()

            # 产生新数字
            self.__controller.generate_new_number()
            # 绘制界面
            self.__draw_map()
            # 游戏结束 ---> 提示
            if self.__controller.is_game_over():
                print("游戏结束！")
                break


    # 根据 玩家的输入 移动
    def __move_map_for_input(self):
        dir = input("请输入方向(wsad):")
        dict_dir = {
            "w":DirectionModel.UP,
            "s":DirectionModel.DOWN,
            "a":DirectionModel.LEFT,
            "d":DirectionModel.RIGHT,
        }
        if dir in dict_dir: # 判断输入的是否为方向
            self.__controller.move(dict_dir[dir])








































