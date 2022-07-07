# @Project   : Python
# @File      : 3.静态方法.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/5/31, 15:04
#

'''
    静态方法
'''

# 静态方法示例：
list01 = [
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
]

# 表示列表内元素向左或者向右
# 定义类
class Vector2:
    '''
        二维向量
            可以表示位置/方向
    '''
    def __init__(self,x,y):
        self.x = x          # x代表位置
        self.y = y          # y代表方向

# 定义函数  在类外

# 函数表示向左移动
def left():
    return Vector2(0,-1)    # 向左移动，x不变，y-1#

# 函数表示向右移动
def right():
    return Vector2(0,1)    # 向右移动，x不变，y+1

# 函数表示向上移动
def up():
    return Vector2(-1,0)    # 向右移动，x-1，y不变

# 函数表示向下移动
def up():
    return Vector2(1,0)    # 向右移动，x+1，y不变



#### 如果该位置是在列表的12位置，那么左移后
pos01 = Vector2(1,2)

# 调用左移函数
s01 = left()

# 原位置的xy变量与移动的相加 即为移动后的位置
pos01.x +=s01.x
pos01.y +=s01.y
print(pos01.x,pos01.y)    # 1 1


#### 如果该位置是在列表的12位置，那么上移后
pos01 = Vector2(1,2)
s02 = up()
pos01.x += s02.x
pos01.y += s02.y
print(pos01.x,pos01.y)      # 0 2







'''
    静态方法：   
            将函数移到类中，就是静态方法
        
    总结:
        实例方法：操作对象的变量    --->表示个体行为
        
        类方法：  操作类的变量    --->表示大家共同的行为
        
        静态方法：既不需要操作实例变量，也不需要操作类变量  
'''

list01 = [
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
]

# 表示列表内元素向左或者向右
# 定义类
class Vector3:
    '''
        二维向量
            可以表示位置/方向
    '''
    def __init__(self,x,y):
        self.x = x          # x代表位置
        self.y = y          # y代表方向

    # 静态方法
    @staticmethod     # ---->将函数放到类中
    def left01():
        return Vector2(0,-1)    # 向左移动，x不变，y-1#

    # 函数表示向右移动
    @staticmethod     # ---->将函数放到类中
    def right01():
        return Vector2(0,1)    # 向右移动，x不变，y+1


#### 如果该位置是在列表的12位置，那么左移后
pos01 = Vector3(2,2)

# --->调用函数时，就要用类名调用静态方法
s01 = Vector3.left01()

# 原位置的xy变量与移动的相加 即为移动后的位置
pos01.x +=s01.x
pos01.y +=s01.y
print(pos01.x,pos01.y)    # 2 1







#########      练习：
#           在二维列表中，获取指定位置，指定方向，指定数量的元素
#           例如：list02列表内 "10"元素 右边的3个元素 ---> "11","12","13"

list02 = [
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
]

# 首先定义类
class Vector4:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @staticmethod
    def left01():
        return Vector2(0,-1)

    @staticmethod
    def right01():
        return Vector2(0,1)


'''# 定义获取元素函数 -----> 函数在类外面 '''
#                列表形参 指定位置   指定方向   数量
def get_elements(list02,vect_pos,vect_dir,count):
    '''
        二维列表中，获取指定位置，指定方向，指定数量的元素
    :param list02: 二维列表
    :param vect_pos: 指定位置
    :param vect_dir: 指定方向   --> 调用移动方向函数
    :param count: 指定数量
    :return: 列表
    '''
    list_result = []
    for i in range(count):      # 获取指定的三个元素  循环三次
        vect_pos.x += vect_dir.x    #
        vect_pos.y += vect_dir.y    #
        element = list02[vect_pos.x][vect_pos.y]
        list_result.append(element)
    return list_result

# 例如：list02列表内 "10"元素 右边的3个元素 ---> "11","12","13"
re = get_elements(list02,Vector4(1,0),Vector4.right01(),3)
print(re)       # ['11', '12', '13']

# 例如：list02列表内 "23"元素 左边的2个元素
re = get_elements(list02,Vector4(2,3),Vector4.left01(),2)
print(re)       # ['22', '21']





print("------------------------移到类中----------------------------")

''' # -------> 将获取元素函数移到类中  '''

# 新定义一个类  二维列表助手
class DoubleListHelper:
    @staticmethod  #
    def get_elements(list02,vect_pos,vect_dir,count):
        '''
            二维列表中，获取指定位置，指定方向，指定数量的元素
        :param list02: 二维列表
        :param vect_pos: 指定位置
        :param vect_dir: 指定方向   --> 调用移动方向函数
        :param count: 指定数量
        :return: 列表
        '''
        list_result = []
        for i in range(count):      # 获取指定的三个元素  循环三次
            vect_pos.x += vect_dir.x    #
            vect_pos.y += vect_dir.y    #
            element = list02[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result

# 例如：list02列表内 "10"元素 右边的3个元素 ---> "11","12","13"
re = DoubleListHelper.get_elements(list02,Vector4(1,0),Vector4.right01(),3)
print(re)       # ['11', '12', '13']

# 例如：list02列表内 "23"元素 左边的2个元素
re = DoubleListHelper.get_elements(list02,Vector4(2,3),Vector4.left01(),2)
print(re)       # ['22', '21']











