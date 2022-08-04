# @Project   : Python
# @File      : bll.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/13, 16:08
#


# 业务逻辑模块


class StudentManagerController:
    '''
        逻辑控制类:负责业务逻辑处理
    '''
    #定义类变量，表示初始编号 类内部变量
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        '''
            学生列表
        :return: 存储学生对象的列表
        '''
        return self.__stu_list

    # 添加学生
    def add_student(self,stu_info):
        '''
            添加一个新的学生
        :param stu_info: 没有编号的学生信息
        '''
        # 学生的编号 =    调用生成id函数
        stu_info.id = self.__generate_id()
        # 将学生信息增加到列表内
        self.__stu_list.append(stu_info)

    # 定义 生成id函数
    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    # 6，根据编号 删除学生
    def remove_student(self,id):
        '''
            根据编号 删除学生
        :param id:
        :return:
        '''
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True     # 表示移除成功
        return False        # 表示移除失败

    # 7，根据编号修改学生信息
    def update_student(self,stu_info):  #  根据stu_info.id修改其他信息
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    # 8,根据成绩升序显示学生信息
    def order_by_score(self):
        for n in range(len(self.__stu_list) - 1):
            for i in range(n+1, len(self.__stu_list)):
                if self.__stu_list[n].score > self.__stu_list[i].score:
                    self.__stu_list[n], self.__stu_list[i] = self.__stu_list[i], self.__stu_list[n]