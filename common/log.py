#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    注：eval()函数可将字符串转换成python代码
"""

import logging
from common.getfiledir import LOGDIR
from common.getconf import Config
import os

class Handloging:

    @staticmethod
    def emplorlog():
        con = Config()  # 初始化读取配置文件方法
        # print(con.get('LOG','level'))
        # print(type(eval(con.get('LOG','level'))))
        formatter = logging.Formatter("%(asctime)s - %(name)s-%(levelname)s %(message)s")   # 设置日志格式

        # # 创建一个Logger
        mylog = logging.getLogger('Kr')
        mylog.setLevel(eval(con.get('LOG','level')))  # 设置日志级别
        # mylog.setLevel(logging.INFO)

        # 创建一个Handle，用于写入日志
        log_path = os.path.join(LOGDIR,'test')
        fh = logging.FileHandler(log_path,encoding='utf-8')
        fh.setLevel(eval(con.get('LOG','level')))
        fh.setFormatter(formatter)
        mylog.addHandler(fh)    # 给日志器添加handler


        # 创建一个Handler，用于将日志输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(eval(con.get('LOG','level')))
        sh.setFormatter(formatter)
        mylog.addHandler(sh)


mylog = Handloging.emplorlog()