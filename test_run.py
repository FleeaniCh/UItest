#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Renkai

"""
    用例执行入口
"""

import os
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.getfiledir import LOGDIR,REPORTDIR,CASEDIR

class TestRun(object):
    def __init__(self):
        self.suite = unittest.TestSuite()   # 生成测试套件对象
        self.load = unittest.TestLoader()
        self.suite.addTest(self.load.discover(CASEDIR)) # 添加测试用例至测试套件
        self.runner = HTMLTestRunner.HTMLTestRunner(stream=open(os.path.join(REPORTDIR,'reporter.html'),'w',encoding='utf-8'),
                                                    title='自动化测试框架验证报告',
                                                    description='测试框架是否可正常执行')

    def execute(self):
        self.runner.run(self.suite)


if __name__ == '__main__':
    test_run = TestRun()
    test_run.execute()

