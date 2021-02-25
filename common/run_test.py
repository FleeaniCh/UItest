#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    run_test.py:    test code
"""
from common.factory import Factory

fac = Factory()
# isOk,result = fac.execute_keyword(keyword='打开网页',locator='http://www.baidu.com')
# print(result)
# isOk1,result1 = fac.execute_keyword(keyword='等待元素可见',type='xpath',locator='//*[@id="kw"]')
# print(result1)
# isOk2,result2 = fac.execute_keyword(keyword='输入',type='xpath',locator='//*[@id="kw"]',input='selenium')
# print(result2)
# isOk3,result3 = fac.execute_keyword(keyword='点击',type='xpath',locator='//*[@id="su"]')
# print(result3)
result = fac.init_execute_case()
print(result)
for dict_re in result:
    print(dict_re)
    for key,cases in dict_re.items():
        for case in cases:  # 遍历每个sheet表中的每一行
            isOk,result = fac.execute_keyword(**case)
            print(result)


'''
    baidu --> common-bai --> baidu
    common-bai
'''