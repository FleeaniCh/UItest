#!/usr/bin/python
# -*- coding: UTF-8 -*-
from configparser import ConfigParser
from common.getfiledir import CONFDIR


class Config:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(CONFDIR + r'\base.ini',encoding='UTF-8')   # 包含中文字符时注意编码

    def get(self, section, option):
        return self.config.get(section, option)


if __name__ == '__main__':
    cf = Config()
    f_name = cf.get('Function','打开网页')
    print(f_name)
