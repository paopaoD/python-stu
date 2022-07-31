# @Project   : Python
# @File      : unitest_run.py
# @Auther    : 等到秋叶金黄
# @Time      : 2022/6/23, 12:11
#

import unittest

from unittest_case import TestBBSTopic

from BeautifulReport import BeautifulReport


if __name__ == '__main__':

    # 1，一系列的测试用例，或者测试计划
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBBSTopic))


    # 2，生成HTML报告
    # 下载并导入 BeautifulReport 模块

    # 将要生成报告的 测试组件传入
    BeautifulReport(suite).report(filename= 'test',description="测试报告")








































