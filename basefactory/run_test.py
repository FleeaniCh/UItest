#!/usr/bin/python
# -*- coding: UTF-8 -*-

from basefactory.webdriveroperator import WebdriverOperator
from basefactory.browseroperator import BrowserOperator
import time

# 测试
bo = BrowserOperator()  # 浏览器操作实例
isOk, driver = bo.open_url(locator='https://ks.stg1.septnet.cn/')
wb = WebdriverOperator(driver)  # 页面操作实例
# result = wb.get_screenshot_as_file()
# print(result)
# result = wb.web_element_wait(type='xpath',locator='//*[@name="userCode"]',time=10)
# result = wb.web_element_wait(type='name',locator='userCode',time=10)
# print(result)
time.sleep(2)
wb.element_input(type='name', locator='userCode', input='17000000364')
wb.element_input(type='name', locator='userPwd', input='123456')
re1 = wb.web_element_wait(type='tag',locator='button')
print(re1)
re2 = wb.element_click(type='tag',locator='button')
print(re2)
# bo.close_browser()
