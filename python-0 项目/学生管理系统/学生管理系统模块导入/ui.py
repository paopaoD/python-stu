# @Project   : Python
# @File      : test_login.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/13, 16:08
#


# 界面模块

from bll import StudentManagerController
# 或者写为 from bll import *
from model import StudentModel
# 或者写为 from model import *


class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerController()

    # 显示菜单
    def __display_menu(self):
        print("1，增加学生")
        print("2，显示学生")
        print("3，删除学生")
        print("4，修改学生")
        print("5，按成绩升序显示学生")

    # 选择菜单
    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_student(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_student_by_score()

    # 界面视图入口
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    # 对输入的内容进行错误异常处理
    def __input_number(self,message):
        while True:
            try:
                message = int(input(message))
                return message
            except:
                print("输入错误")

    # 输入学生
    def __input_student(self):
        name = input("请输入姓名：")
        age = self.__input_number("请输入年龄：")
        score = self.__input_number("请输入成绩：")
        # # 将方法定义函数 __input_number
        # while True:
        #     try:
        #         age = int(input("请输入年龄："))
        #         break
        #     except:
        #         print("输入错误")

        # # 将方法定义函数 __input_number
        # while True:
        #     try:
        #         score = int(input("请输入成绩："))
        #         break
        #     except:
        #         print("输入错误")

        stu = StudentModel(name,age,score)

        # # 跨类调用  将其做成实例变量  放到__init__内
        # manager = StudentManagerController()
        self.__manager.add_student(stu)

    # 输出学生
    def __output_student(self,list_output):
        for item in list_output:
                print(item.__dict__)

    # 根据编号 删除学生
    def __delete_student(self):
        '''
            根据编号 删除学生
        :return:
        '''
        id = int(input("请输入编号："))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    # 根据编号 修改学生信息
    def __modify_student(self):
        '''
            根据编号 修改学生信息
        '''
        # id = int(input("请输入需要修改的编号："))
        # 调用错误异常处理函数
        id = self.__input_number("请输入需要修改的编号：")
        # name = input("请输入需要修改的姓名：")
        # 调用错误异常处理函数
        name = self.__input_number("请输入需要修改的姓名：")
        # age = int(input("请输入需要修改的年龄："))
        # 调用错误异常处理函数
        age = self.__input_number("请输入需要修改的年龄：")
        # score = int(input("请输入需要修改的成绩："))
        # 调用错误异常处理函数
        score = self.__input_number("请输入需要修改的成绩：")

        stu = StudentModel(name,age,score,id)
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    # 8,根据成绩升序显示学生信息
    def __output_student_by_score(self):

        self.__manager.order_by_score()
        # 调用输出学生函数
        self.__output_student(self.__manager.stu_list)