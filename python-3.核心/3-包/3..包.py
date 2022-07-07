# @Project   : Python
# @File      : 3..包.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/14, 15:05
#
'''
    包   ： 将模块以文件夹的形式进行分组管理

python程序结构
    文件夹 ---- 项目根目录
        包
            模块
                类
                   函数
                       语句

'''

# from 包.模块 import 成员
from package01.module_a import *

fun01()


import package01.module_a as pm

pm.fun01()



# from 包.包.模块 import 成员     深层级导入
from package01.package02.module_b import fun02

fun02()



# # 或者 直接导入包，
#   但是需要在__init__.py 内 定义 __all__ 可导出的模块  不建议
# from skill_system import *
#
# manager = skill_manager.SkillManager()
# manager.fun04()





























































