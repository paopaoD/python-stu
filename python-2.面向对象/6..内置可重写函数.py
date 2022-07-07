# @Project   : Python
# @File      : 6..内置可重写函数.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/10, 12:51
#

'''
    以双下划线开头，双下划线结尾的是系统定义的成员函数

    __str__函数：将对象转换为字符串(对人友好的)
    __repr__函数：将对象转换为字符串(解释器可识别的)

'''

class StudentModel:
    '''
        学生信息模型
    '''
    def __init__(self,name = "",age = 0,score = 0,id = 0):
        '''
            创建学生对象
        :param name: 姓名  str类型
        :param age: 年龄  int类型
        :param score: 成绩 float类型
        :param ID: 编号(该学生对象的唯一标识)
        '''
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    # 把对象--->字符串(格式随意)
    def __str__(self):
        return f"我叫{self.name}，编号是{self.age}，年龄{self.score}，分数是{self.id}"

    # 把对象--->字符串(解释器可识别的)
    def __repr__(self):
        return "StudentModel('%s',%d,%d,%d)"%(self.name,self.age,self.score,self.id)


s01 = StudentModel("张三",22,100,101)
print(s01)
str01 = str(s01)
print(str01)

str02 = repr(s01)
print(str02)
# 根据字符串执行代码
print(eval("1+2*5"))

# repr 返回python格式的字符串
# eval 根据字符串执行代码 ---->  相当于是克隆一个对象
s02 = eval(repr(s01))
s02.name = "陈思"
print(s01.name)
print(s01.__dict__)

# 相当于是克隆一个对象
print(s02.name)
print(s02.__dict__)





print("-----------------------------练习1------------------------------------")
'''
    创建Enemy类对象，将对象打印在控制台中
    克隆Enemy类对象，体会克隆对象变量的改变，不影响原对象
    
'''

class Enemy:
    def __init__(self,name,blood,attack):
        self.name = name
        self.blood = blood
        self.attack = attack

    def __str__(self):
        return f"这个敌人叫{self.name}，血量有{self.blood}，攻击力有{self.attack}。"

    def __repr__(self):
        return "Enemy('%s',%d,%d)"%(self.name,self.blood,self.attack)


e01 = Enemy("灭霸",100,50)
print(e01)

e02 = repr(e01)
print(e02)

e03 = eval(repr(e01))
print(e03.name)

e01.name = "张三"
print(e03.name)

print(e03.__dict__)
print(e01.__dict__)








print("----------------------------- 运算符重载 ------------------------------------")

# 加法  __add__
class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "一维向量的分量x是:" + str(self.x)

    def __add__(self, other):
        return Vector1(self.x + other)

v01 = Vector1(10)
# 对象与数值的加法
print(v01 + 2)



#########

# 减法 __sub__
class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "一维向量的分量x是:" + str(self.x)

    def __sub__(self, other):
        return Vector1(self.x - other)

v01 = Vector1(10)
# 对象与数值的减法
print(v01 - 2)



#########

# 乘法 __mul__
class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "一维向量的分量x是:" + str(self.x)

    def __mul__(self, other):
        return Vector1(self.x * other)

v01 = Vector1(10)
# 对象与数值的减法
print(v01 * 2)




print("----------------------------- 反向运算符重载 ------------------------------------")

# 加法  __radd__
class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "一维向量的分量x是:" + str(self.x)

    def __radd__(self, other):
        return Vector1(other + self.x)

v01 = Vector1(10)
# 对象与数值的加法
print(2 + v01)


#########

# 减法 __sub__
class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "一维向量的分量x是:" + str(self.x)

    def __rsub__(self, other):
        return Vector1(other - self.x)

v01 = Vector1(10)
# 对象与数值的减法
print(12 - v01)


#########

# 乘法 __mul__
class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "一维向量的分量x是:" + str(self.x)

    def __rmul__(self, other):
        return Vector1(self.x * other)

v01 = Vector1(10)
# 对象与数值的减法
print(5 * v01)




print("----------------------------- 复合运算符重载 ------------------------------------")

# 加法  __iadd__
class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "一维向量的分量x是:" + str(self.x)

    def __add__(self, other):
        return Vector1(self.x + other)

    def __iadd__(self, other):
        self.x += other
        return self

v01 = Vector1(10)
print(id(v01))

print(v01 + 2)
print(id(v01))

# 重写 __iadd__函数  是在原有的基础上发生变化，
# 如果不使用__iadd__  那么默认的是使用__add__ 一般会产生一个新对象
v01 += 2
print(v01,id(v01))



# 减法 __isub__
class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "一维向量的分量x是:" + str(self.x)

    def __isub__(self, other):
        return Vector1(self.x - other)

v01 = Vector1(10)
# 对象与数值的减法
v01 -= 2
print(v01)


















