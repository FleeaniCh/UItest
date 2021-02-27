#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Renkai

"""
    test_caserun.py:    test cases
"""

import unittest
from common.factory import Factory
from library.ddt import *
from common.log import *


@ddt
class TestCaserun(unittest.TestCase):
    fac = Factory()
    execu = fac.init_execute_case()

    @data(*execu)  # 解包 -->> <class 'dict'>
    def test_run(self, ele_dict):
        for key, cases in ele_dict.items():
            print(key,cases)
            mylog.info('\n-----------用例【%s】开始-------------' % key)  # ??ele_dict[0].get['sheet']
            print('\n')
            for case in cases:
                isOk, result = self.fac.execute_keyword(**case)  # 将字典实参解析成关键字实参
                if isOk:
                    print(result)
                    mylog.info(result)
                else:
                    mylog.error(result)
                    raise Exception(result)
            mylog.info('\n-----------用例【%s】结束-------------' % key)



