#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    注：eval()函数可将字符串转换成python可执行代码
"""

import logging
from common.getfiledir import LOGDIR
from common.getconf import Config
import os


# import sys

class Handloging:

    @staticmethod
    def emplorlog():  # @staticmethod：静态方法，可通过类名直接调用
        con = Config()  # 初始化读取配置文件方法
        # print(con.get('LOG','level'))
        # print(type(eval(con.get('LOG','level'))))
        formatter = logging.Formatter("%(asctime)s - %(name)s-%(levelname)s %(message)s")  # 设置日志格式

        # 创建一个Logger
        mylog = logging.getLogger('Kr')
        mylog.setLevel(eval(con.get('LOG', 'level')))  # 设置日志级别
        # mylog.setLevel(logging.INFO)

        # 创建一个Handle，用于写入日志
        log_path = os.path.join(LOGDIR, 'test')
        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel(eval(con.get('LOG', 'level')))
        fh.setFormatter(formatter)
        mylog.addHandler(fh)  # 给日志器添加handler

        # 创建一个Handler，用于将日志输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(eval(con.get('LOG', 'level')))
        sh.setFormatter(formatter)
        mylog.addHandler(sh)
        return mylog


mylog = Handloging.emplorlog()

# print(sys.path)
mylog.info('开始执行测试用例')

# logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(name)s-%(levelname)s %(message)s")
# logging.info('开始执行测试用例。')
