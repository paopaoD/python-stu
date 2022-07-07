# @Project   : Python
# @File      : 1..模块.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/13, 15:01
#

'''
    模块
        1，定义:xx.py文件

        2，作用:多人合作开发

        3，导入：
           1， import 模块  ---> 本质：是将module01看做一个变量名使用

               模块.成员名   ---> 调用

                import 模块 as 别名   --->给导入的模块名另起名称

                模块.成员名


            2， 从模块xx中 导入 成员 方法
                from 模块 import 成员  --->本质:将指定的成员导入到当前模块作用域中

                直接使用成员             注意：导入进来的成员不要和当前模块成员名称相同  比如 fun01


            3，from 模块 import *    --->本质:将指定模块的所有成员导入到当前模块作用域中

'''


print("---------------------------导入方式1------------------------------")
# 导入方式1

# 导入模块 module01
import module01    # 本质：是将module01看做一个变量名使用，module01 = module01.py

# 调用模块内的方法
module01.fun01()

# 调用模块内的类，和类中的方法
m01 = module01.MyClass02()
m01.fun02()


#### 或者 给导入的模块名另起名称

import module01 as mod01    # 可以避免与当前模块的成员名称相同

mod01.fun01()

m01 = mod01.MyClass02()
m01.fun02()


print("---------------------------导入方式2------------------------------")

# 导入方式2      # 本质:将指定的成员导入到当前模块作用域中
# 注意：导入进来的成员不要和当前模块成员名称相同  比如 fun01

# 从模块module01中 导入 fun01方法
from module01 import fun01
# 或者写成： from module01 import fun01 as fun03   可以避免与当前模块的成员名称相同

from module01 import MyClass02


# 调用
fun01()
m02 = MyClass02()
m02.fun02()



print("---------------------------导入方式3------------------------------")

# 导入方式3

from module01 import *      # 本质:将指定模块的所有成员导入到当前模块作用域中


# 调用
fun01()

m03 = MyClass02()
m03.fun02()


print("---------------------------导入隐藏成员------------------------------")

# 在module01模块中隐藏的成员，可以直接调用
# 只能使用 from 模块 import * 这种写法
from module01 import _fun03


# 调用隐藏成员
_fun03()





'''
    模块分类：
            1，内置模块(builtins)，在解析器的内部可以直接使用
            2，标准库模块，安装Python时已经安装且可直接使用
            3，第三方模块(通常为开源)，需要自己安装
            4，用户自己编写的模块(可以作为其他人的第三方模块)

'''














