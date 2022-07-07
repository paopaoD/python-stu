# @Project   : Python
# @File      : 4.1.异常处理练习.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/15, 12:13
#



#练习：
    # 定义函数，在控制台中获取成绩的函数
    # 要求：如果异常，继续获取成绩，知道得到正确的成绩为止
    #         成绩必须在0~100之间


''''''
def get_score():
    while True:
        input_score = input("请输入成绩：")
        try:
            score = int(input_score)
        except:
            print("输入的成绩不是整数")
            continue
        if 0 <= score <= 100:
            return input_score
        else:
            print("超出范围")

re = get_score()
print(re)





#练习：敌人类(攻击力0--100)
#       抛出异常的信息：消息/错误行/攻击力/错误编号
#

# 定义异常类
class MessageError(Exception):
    '''
        信息类错误
    '''
    def __init__(self,message,code_line,attack,error_num):
        self.message = message
        self.code_line = code_line
        self.attack = attack
        self.error_num = error_num


# 定义敌人类
class Emeny:
    def __init__(self,atk):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,value):
        if 0<= value <= 100:
            self.__atk = value
        else:
            raise MessageError("输入的攻击力错误",61,f"{value}",100001)


try:
    e01 = Emeny(int(input("请输入攻击力：")))
    print(f"输入的攻击力为{e01.atk}")
except MessageError as e:
    print(e.message)
    print(e.code_line)
    print(e.attack)
    print(e.error_num)











































