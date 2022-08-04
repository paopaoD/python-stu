# @Project   : Python
# @File      : main.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/13, 16:09
#


# 入口模块

from ui import StudentManagerView
# 或者写为 from ui import *

# 限制只有当前模块为主模块(第一个运行)时，才会执行
if __name__ == '__main__':
    View = StudentManagerView()
    View.main()





