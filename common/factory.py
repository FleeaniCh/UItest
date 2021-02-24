#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    工厂函数
"""
from common.getconf import Config
from common.getcase import ReadCase
from basefactory.browseroperator import BrowserOperator
from basefactory.webdriveroperator import WebdriverOperator


class Factory(object):
    def __init__(self):
        self.con = Config()
        # self.con_fun = dict(self.con.items('Function')) # ??
        self.browser_opr = BrowserOperator()  # 浏览器操作对象
        self.webdriver_opr = None  # 网页操作对象

    def init_webdriver_opr(self, driver):
        """初始化网页操作对象"""
        self.webdriver_opr = WebdriverOperator(driver)

    def init_execute_case(self):
        """初始化执行用例"""
        print("----------------初始化用例----------------")
        xlsx = ReadCase()
        isOk, result = xlsx.readallcase()
        if not isOk:
            print(result)
            print("----------------结束执行----------------")
            exit()
        all_cases = result
        # print(all_cases)
        excu_cases = []
        for case_dict in all_cases:
            # print(case_dict)
            '''
case_1 , [{'id': 1, 'result': None, 'keyword': '打开网页', 'type': 'url', 'locator': 'https://www.baidu.com/', 'index': None, 'input': None, 'check': None, 'time': None}, {'id': 4, 'result': None, 'keyword': '等待元素可见', 'type': 'xpath', 'locator': '//*[@id="kw"]', 'index': None, 'input': None, 'check': None, 'time': 3}, {'id': 2, 'result': None, 'keyword': '输入', 'type': 'xpath', 'locator': '//*[@id="kw"]', 'index': None, 'input': 'Flyman', 'check': None, 'time': None}, {'id': None, 'result': None, 'keyword': '调用用例', 'type': None, 'locator': 'common-bai', 'index': None, 'input': None, 'check': None, 'time': None}]
common-bai , [{'id': 2, 'result': None, 'keyword': '输入', 'type': 'xpath', 'locator': '//*[@id="kw"]', 'index': None, 'input': 'JorDab', 'check': None, 'time': None}]
            '''
            for key, cases in case_dict.items():
                # print(key, ',', cases)
                isOk, result = self.init_common_case(cases)
                if isOk:
                    case_dict[key] = result
                else:
                    case_dict[key] = cases
                    excu_cases.append(case_dict)
        print("--------------初始化用例完成--------------")
        return excu_cases

    def init_common_case(self, cases):
        """
            初始化调用用例
        :param cases: 传入的用例表中的数据列表
        :return:追加公共用例后的用例数据列表  -->> list
        """
        cases_len = len(cases)
        index = 0
        for case in cases:
            if case['keyword'] == '调用用例':
                xlsx = ReadCase()
                try:
                    case_name = case['locator']
                except KeyError:
                    return False, '调用的用例没有提供用例名'
                isOk, result = xlsx.get_common_case(case_name)
                list_rows = result[case_name]
                cases[index:index + 1] = list_rows  # 追加数据至当前用例数据列表
            index += 1
        if cases_len == index:
            return False, ''
        return True, cases

    def get_base_fucntion(self, fucntion_name):
        """获取执行方法"""
        try:
            function = getattr(self.browser_opr, fucntion_name) # 方法名是否在浏览器操作类中【Python反射】
        except Exception:
            try:
                function = getattr(self.webdriver_opr, fucntion_name)   # 方法名是否在页面操作类中【python反射】
            except Exception:
                return False, '未找到注册方法[' + fucntion_name + ']所对应的执行函数，请检查配置文件'
        return True, function

    def execute_keyword(self,**kwargs):
        """用例中keyword对应方法入口"""
        try:
            keyword = kwargs['keyword'] # 从excel用例中获取keyword内容
            if keyword is None:
                return False, 'keyword内容为空，请检查用例'
        except KeyError:
            return False,'没有keyword字段，请检查用例'

        _isbrowser = False

        try:
            function_name = self.con.get('Function',keyword)    # 从配置文件中获取keyword对应的方法名
        except KeyError:
            return False,'方法Key['+keyword+']未注册'

        isOk, result = self.get_base_fucntion(function_name)
        if isOk:
            function = result
        else:
            return isOk,result

        isOk,result = function(**kwargs)

        if '打开网页' == keyword and isOk:
            url = kwargs['locator']


if __name__ == '__main__':
    fc = Factory()
    # result = fc.init_execute_case()
    # print(result)
    isOk,result = fc.get_base_fucntion('open_url')
    print(result)
