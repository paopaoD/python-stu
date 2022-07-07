# @Project   : Python
# @File      : list_helper.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/17, 16:28
#

'''
    列表助手模块
'''


class ListHelper:
    '''
        列表助手类
    '''
    # 通用的查找某个条件的 所有元素 方法
    @staticmethod
    def find_num(list_target,func_condition):
        '''
            通用的查找某个条件的 所有元素 方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件，函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素 , 生成器类型
        '''
        for item in list_target:
            if func_condition(item):
                yield item

    # 通用的查找某个条件的 单个元素 方法
    @staticmethod
    def find_all(list_target,func_condition):
        '''
            通用的查找某个条件的 单个元素 方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件，函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素
        '''
        for item in list_target:
            if func_condition(item):
                return item

    # 通用的满足某个条件的 技能数量 方法
    @staticmethod
    def get_skill_count(list_target,func_duration):
        '''
            通用的满足某个条件的 技能数量 方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件，函数类型
                函数名(参数) --> bool
        :return: 满足条件元素的数量
        '''
        count = 0
        for item in list_target:
            if func_duration(item):
                count += 1
        return count

    # 通用的判断是否存在某个 元素 的方法
    @staticmethod
    def is_exists(list_target, func_condition):
        '''
            通用的判断是否存在某个 元素 的方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件，函数类型
                函数名(参数) --> bool
        :return: bool类型   True表示存在  False 不存在
        '''
        for item in list_target:
            if func_condition(item):
                return True
        return False

    # 通用的 求和 的方法
    @staticmethod
    def sum_condition(list_target, func_condition):
        '''
            通用的 求和 的方法
        :param list_target: 需要求和的列表
        :param func_condition: 需要求和的处理逻辑，函数类型
                函数名(参数) --> int/float
        :return: 和
        '''
        sum_vaule = 0
        for item in list_target:
             sum_vaule += func_condition(item)
        return sum_vaule

    # 通用的 筛选 的方法
    @staticmethod
    def select_info(list_target,func_info):
        '''
            通用的 筛选 的方法
        :param list_target: 需要筛选的列表
        :param func_info: 需要筛选 的处理逻辑，函数类型
                函数名(参数) --> int/float/元组/其他类型
        :return: 列表
        '''
        list_result = []
        for item in list_target:
            list_result.append(func_info(item))
        return list_result

    # 通用的 获取最大元素 的方法
    @staticmethod
    def select_max(list_target,func_handle):
        '''
            通用的 获取最大元素 的方法
        :param list_target: 需要查找的列表
        :param func_handle: 需要查找 的处理逻辑，函数类型
                函数名(参数) --> int/str...
        :return: 最大元素
        '''
        max_vaule = list_target[0]
        for i in range(1,len(list_target)):
            if func_handle(max_vaule) < func_handle(list_target[i]):
                max_vaule = list_target[i]
        return max_vaule

    # 通用的 获取最小值 的方法
    @staticmethod
    def select_min(list_target,func_handle):
        '''
            通用的 获取最小元素 的方法
        :param list_target: 需要查找的列表
        :param func_handle: 需要查找 的处理逻辑，函数类型
                函数名(参数) --> int/str...
        :return: 最小元素
        '''
        min_vaule = list_target[0]
        for i in range(1,len(list_target)):
            if func_handle(min_vaule) > func_handle(list_target[i]):
                min_vaule = list_target[i]
        return min_vaule

    # 通用的 升序排列 的方法
    @staticmethod
    def order_by(list_tar, func_handle):
        '''
            通用的 升序排列 的方法
        :param list_target: 需要排序的数据
        :param func_handle: 排序的处理逻辑
                函数名(参数) --> int/float ... 需要比较的数据
        :return:
        '''
        for i in range(len(list_tar) - 1):
            for c in range(i+1, len(list_tar)):
                if func_handle(list_tar[i]) > func_handle(list_tar[c]):
                    list_tar[i], list_tar[c] = list_tar[c], list_tar[i]
        # return list_tar   # 无需返回值

    # 通用的 降序排列 的方法
    @staticmethod
    def order_by_desc(list_tar,func_handle):
        '''
            通用的 降序排列 的方法
        :param list_tar: 需要排序的数据
        :param func_handle: 排序的处理逻辑
                函数名(参数) --> int/float ... 需要比较的数据
        :return:
        '''
        for i in range(len(list_tar) - 1):
            for c in range(i+1, len(list_tar)):
                if func_handle(list_tar[i]) < func_handle(list_tar[c]):
                    list_tar[i], list_tar[c] = list_tar[c], list_tar[i]
        # return list_tar   # 无需返回值


    # 通用的 根据指定条件删除元素 的方法
    @staticmethod
    def deletea_all(list_target,func_condition):
        '''
            通用的 根据指定条件删除元素 的方法
        :param list_target: 需要删除的数据列表
        :param func_condition: 删除条件
        '''
        for i in range(len(list_target) - 1, -1, -1):
            if func_condition(list_target[i]):
                del list_target[i]
































