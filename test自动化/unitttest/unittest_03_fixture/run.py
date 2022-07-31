# @Project   : Python
# @File      : run.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/23, 14:03
#



import unittest
from BeautifulReport import BeautifulReport

from fixture_case import TestBBSTopic
from parametrize import *



# 1，一系列的测试用例，或者测试计划

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestBBSTopic))


# 2，生成HTML报告
# 下载并导入 BeautifulReport 模块

# 将要生成报告的 测试组件传入
BeautifulReport(suite).report(filename= 'test',description="测试报告")


unittest.result

class TestResult(object):
    def printerrors(self):
        pass