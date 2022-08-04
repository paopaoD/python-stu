# @Project   : Python
# @File      : student_manager_system.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/6, 18:25
#
'''
学生管理系统：
    项目计划：
            1,完成数据模型类StudentModel
            2,创建逻辑控制类StudentManagerController
            3,完成数据：学生列表 __stu_list
            4,行为：获取列表 stu_list
            5,添加学生方法 add_student
            6,根据编号 删除学生 remove_student
            7,根据编号修改学生信息 update_student
            8,根据成绩，升序显示学生信息

    在界面视图类中：
            1,显示菜单  __display_menu
            2,选择菜单  __select_menu
            3,添加学生方法  __input_student
            4,显示学生信息  __output_student
            5,根据编号 删除学生 __delete_student
            6,根据编号修改学生信息 __modify_student
'''
#### 第一步：

# 数据模型类
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


# 逻辑控制类
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


# 测试添加功能
'''
# manager = StudentManagerController()
# s01 = StudentModel("ss",18,100,1002)
# print(s01.__dict__)
# manager.add_student(s01)
# print(s01.__dict__)
# print(s01.id)
#
# s02 = StudentModel("ls",18,100,1005)
# print(s02.__dict__)
# manager.add_student(s02)
# print(s02.__dict__)
# print(s02.id)
#
# for item in manager.stu_list:
#     print(item.id)
'''
# 根据编号 删除学生
'''
manager02 = StudentManagerController()
manager02.add_student(StudentModel("ff",))
manager02.add_student(StudentModel("rr",))

manager02.remove_student(1001)
for item in manager02.stu_list:
    print(item.name,item.id)
'''
# 根据编号 修改学生信息
'''
manager = StudentManagerController()
manager.add_student(StudentModel("无忌"))
manager.add_student(StudentModel("逍遥"))
for item in manager.stu_list:
    print(item.__dict__)

# stu_info 需要的是学生信息参数
manager.update_student(StudentModel("陈寒",25,99,1001))
print("修改后。。。。")
for item in manager.stu_list:
    print(item.__dict__)


manager.update_student(StudentModel("韩燕",26,88,1001))
print("修改后。。。。")
for item in manager.stu_list:
    print(item.__dict__)
'''



# 界面视图类
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

    # 输入学生
    def __input_student(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
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
        id = int(input("请输入需要修改的编号："))
        name = input("请输入需要修改的姓名：")
        age = int(input("请输入需要修改的年龄："))
        score = int(input("请输入需要修改的成绩："))

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



View = StudentManagerView()
View.main()




































