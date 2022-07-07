# @Project   : Python
# @File      : 4..异常处理.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/15, 11:21
#
'''
    异常处理
        定义：运行时检测到的错误
        现象：当一次发生时，程序不会再向下执行，而转到函数的执行语句中
        常见的异常类型：
            -名称异常(NameError):变量未定义
            -类型异常(TypeError):不同类型数据进行运算
            -索引异常(IndexError):超出索引范围
            -属性异常(AttributeError):对象没有对应名称的属性
            -键异常(KeyError)：没有对应名称的键
            -未实现异常(NotImplementedError)：尚未实现的方法
            --异常基类 Exception
    处理：
     语法：
        try:
            可能触发异常的语句(可能出错的代码)

        except 错误类型 1 [as 变量 1]:    # 该except语句可以有一个或多个
            处理语句 1

        except 错误类型 2 [as 变量 2]:
            处理语句 2

        except Exception [as 变量 3]:
            不是以上错误类型的处理语句

        else:                           # 该else语句最多只能有一个
            未发生异常的语句

        finally:                         # 该finally语句最多只能有一个
            无论是否发生异常的语句

    作用：将程序由异常状态转为正常流程

'''


def div_apple(apple_count):
    # 直接点击回车，会报错 ValueError
    person_count = int(input("请输入人数："))
    # 如果输入的人数为0，则会报异常 ZeroDivisionError
    result = apple_count / person_count
    print(f"每人分了{result}个苹果")



##### 1,对异常进行处理：

try:
    # 可能出错的代码
    div_apple(10)
# 如果异常，则会拦截，继续向下执行
except Exception:
    print("出错！")

print("后续逻辑....")



##### 2,对异常进行处理：

# “建议” 分门别类的处理，出现的异常分别罗列
try:
    # 可能出错的代码
    div_apple(10)
except ValueError:
    print("出错！")
except ZeroDivisionError:
    print("出错！")


print("后续逻辑....")




##### 3,对异常进行处理：

#
try:
    # 可能出错的代码
    div_apple(10)
except Exception:
    print("出错！")
else:
    # 如果异常，不执行该slse语句
    print("没有出错")


print("后续逻辑....")





##### 4,对异常进行处理：

#
try:
    # 可能出错的代码
    div_apple(10)
finally:  #finally作用：不能处理的错误，但是一定要执行的代码，就定义在finally语句中
    # 无论是否异常，一定会执行的代码
    print("finally")


print("后续逻辑....")































































