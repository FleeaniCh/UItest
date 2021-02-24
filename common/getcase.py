#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    读取EXCEL用例
"""

# import json

import openpyxl
import os
from common.getfiledir import DATADIR

file = os.path.join(DATADIR, 'case.xlsx')


class ReadCase(object):
    def __init__(self):
        self.rw = openpyxl.load_workbook(file)  # 加载excel工作簿
        # print(self.rw)

    def readcase(self, sh):
        """
            读取用例数据
        :param sh: sheet表
        :return: 返回sheet页里面的组合数据-->> dict: {'sheetname': data}
        """
        if sh is None:
            return False, '用例页未传参'
        datas = list(sh.rows)
        if datas == []:
            return False, '用例[' + sh.title + ']里面是空的'
            # return datas
        title = [i.value for i in datas[0]]  # 列表推导式获取当前sheet页标题
        # print(title)
        rows = []
        sh_dict = {}
        for i in datas[1:]:  # 遍历当前sheet表各行
            data = [v.value for v in i]
            # print(zip(title,data))
            row = dict(zip(title, data))  # 两对象打包成元组返回列表，再转换成dict
            # print(row)
            rows.append(row)
            sh_dict[sh.title] = rows
        return True, sh_dict
        # return True,json.dumps(sh_dict)

    def readallcase(self):
        """获取所有sheet表用例数据"""
        sheet_list = []
        for sh in self.rw:
            isOk, result = self.readcase(sh)
            if isOk:
                sheet_list.append(result)
        if sheet_list is None:
            return False, '用例集是空的，请检查用例'
        return True, sheet_list

    def get_common_case(self, case_name):
        """获取指定表名的用例数据"""
        try:
            sh = self.rw.get_sheet_by_name(case_name)
        except KeyError:
            return False, '未找到指定用例[' + case_name + ']请检查用例'
        return self.readcase(sh)


# 测试
if __name__ == '__main__':
    xlsx = ReadCase()
    for sh in xlsx.rw:  # 遍历工作簿中的所有sheet表
        isOk, sh_dict = xlsx.readcase(sh)
        print(sh_dict)
    # print(xlsx.readallcase())
    # xlsx.get_common_case('common-bai')
