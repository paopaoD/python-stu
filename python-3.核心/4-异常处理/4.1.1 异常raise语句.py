# @Project   : Python
# @File      : 4.1.1 异常raise语句.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/15, 14:27
#
'''
    raise 语句
        作用：抛出一个错误，让程序进入异常状态
'''



'''
class Wife:
    def __init__(self,age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if 21 <= value <=31:
            self.__age = value
        else:
            raise ValueError('输入的年龄错误')


while True:
    # 对会错误的内容处理
    try:
        w01 = Wife(int(input("请输入年龄:")))
        print(f"老婆的年龄为{w01.age}")
    except :
        print("重新输入")
        continue

'''



'''
    自定义异常
        定义：
            class 类名Error(Exception):
                    def __init__(self,参数):
                        super().__init__(参数)
                        self.数据 = 参数
        
        调用：
            try:
                ...
                raise 自定义异常类名(参数)
                ...
            except 定义异常类 as 变量名:
                变量名.数据
                
    作用：用于封装错误信息
    
'''

### 示例

# 创建异常 类
class AgeError(Exception):
    #                异常内容   异常的年龄值  异常的代码行数
    def __init__(self,message,age_value,code_line):
        super().__init__(message,age_value,code_line)     #
        self.message = message
        self.age_value = age_value
        self.code_line = code_line


class Wife:
    def __init__(self,age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if 21 <= value <=31:
            self.__age = value
        else:
            # 直接调用上面 定义的 异常 类
            raise AgeError("这个老婆我不要",88,67)

while True:
    # 对会错误的内容处理
    try:
        w01 = Wife(int(input("请输入年龄:")))
        print(f"老婆的年龄为{w01.age}")
    # 将异常类 定义 另一个变量名
    except AgeError as a:
        print("异常内容：",a.message)
        print("异常的年龄值：",a.age_value)
        print("异常的代码行数：",a.code_line)
        continue










































































