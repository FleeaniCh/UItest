#!/usr/bin/python
# -*- coding: utf-8 -*-

from common.getconf import Config
import os
from selenium import webdriver
import time
from common.getfiledir import BASEFACTORYDIR


class BrowserOperator:
    """
        浏览器操作类
    """
    def __init__(self):
        # self.conf = Config()
        self.driver_path = os.path.join(BASEFACTORYDIR, 'chromedriver.exe')
        # self.driver_type = str(self.conf.get('base', 'browser_type')).lower()
        self.driver_type = 'chrome'

    def open_url(self, **kwargs):
        """打开url地址"""
        try:
            url = kwargs['locator']  # 获取url
        except KeyError:
            return False, "没有url参数"
        try:
            if self.driver_type == 'chrome':  # 判断浏览器类型
                self.driver = webdriver.Chrome(executable_path=self.driver_path)
                # self.driver.maximize_window() # 最大化窗口
                self.driver.get(url)
            elif self.driver_type == 'ie':
                print("IE浏览器")
            elif self.driver_type == 'firefox':
                print("Firefox浏览器")
        except Exception as e:
            return False, e
        return True, self.driver

    def close_browser(self):
        time.sleep(2)
        self.driver.quit()
        time.sleep(1)
        return True, "关闭浏览器成功"


if __name__ == '__main__':
    w = BrowserOperator()
    w.open_url(locator='https://www.baidu.com')
    w.close_browser()
