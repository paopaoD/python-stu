# @Project   : Python
# @File      : game_model.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/13, 16:08
#


# 数据模块

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