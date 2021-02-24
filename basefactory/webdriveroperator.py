#!/usr/bin/python
# -*- coding: UTF-8 -*-

from common.getfiledir import SCREENSHOTDIR
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
import time


class WebdriverOperator:
    """
        页面操作类
    """

    def __init__(self, driver: Chrome):  # ?? driver:Chrome ??
        self.driver = driver

    def get_screenshot_as_file(self):
        """截图"""
        pic_name = str.split(str(time.time()), '.')[0] + str.split(str(time.time()), '.')[1] + '.png'
        screen_path = os.path.join(SCREENSHOTDIR, pic_name)
        self.driver.get_screenshot_as_file(screen_path)
        return screen_path

    def web_implicitly_wait(self, **kwargs):
        """设置隐式等待"""
        try:
            s = kwargs['time']
        except KeyError:
            s = 10
        try:
            self.driver.implicitly_wait(s)
        except NoSuchElementException:
            return False, "隐式等待设置失败"
        return True, "隐式等待设置成功"

    def web_element_wait(self, **kwargs):
        """等待指定元素"""
        try:
            type = kwargs['type']
            locator = kwargs['locator']
        except KeyError:
            return False, "未传需要等待的元素"
        try:
            s = kwargs['time']
            if s is None:
                s = 30
        except KeyError:
            s = 30
        try:
            if type == 'id':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.ID, locator)))
            elif type == 'name':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.NAME, locator)))
            elif type == 'class':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            elif type == 'xpath':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            elif type == 'css':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            elif type == 'tag':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.TAG_NAME, locator)))
            else:
                return False, '不能识别的元素类型[' + type + ']'
        except TimeoutException:
            screenshot_path = self.get_screenshot_as_file()  # 返回截图路径
            return False, '元素[' + locator + ']等待出现失败，已截图[' + screenshot_path + ']'
        return True, '元素[' + locator + ']等待出现成功'

    def element_input(self, **kwargs):
        """
            元素输入操作
        """
        try:
            type = kwargs['type']
            locator = kwargs['locator']
            text = str(kwargs['input'])  # 用户输入的字符串
        except KeyError:
            return False, "缺少传参"
        try:
            index = kwargs['index']
        except KeyError:
            index = 0
        isOk, elem = self.find_element(type, locator, index)  # 定位元素
        if not isOk:
            return isOk, elem
        try:
            elem.send_keys(text)
        except Exception:
            screen_path = self.get_screenshot_as_file()
            return False, '元素[' + locator + ']输入[' + text + ']失败，已截图[' + screen_path + ']'
        return True, '元素[' + locator + ']输入成功'

    def find_element(self, type, locator, index=None):
        """查找页面元素"""
        if index is None:
            index = 0
        type = str.lower(type)
        try:
            if type == 'id':
                elem = self.driver.find_elements_by_id(locator)[index]
            elif type == 'name':
                elem = self.driver.find_elements_by_name(locator)[index]
            elif type == 'class':
                elem = self.driver.find_elements_by_class_name(locator)[index]
            elif type == 'xpath':
                elem = self.driver.find_elements_by_xpath(locator)[index]
            elif type == 'css':
                elem = self.driver.find_elements_by_css_selector(locator)[index]
            elif type == 'tag':
                elem = self.driver.find_elements_by_tag_name(locator)[index]
            else:
                return False, '不能识别的元素类型[' + type + ']'
        except Exception as e:
            screen_path = self.get_screenshot_as_file()
            return False, '获取[' + type + ']元素[' + locator + ']失败，已截图[' + screen_path + ']'
        return True, elem

    def element_click(self, **kwargs):
        """元素点击操作"""
        try:
            type = kwargs['type']
            locator = kwargs['locator']
        except KeyError:
            return False, '缺少传参'
        try:
            index = kwargs['index']
        except KeyError:
            index = 0
        isOk, elem = self.find_element(type, locator, index)
        print(elem)
        if not isOk:
            return isOk, elem
        try:
            elem.click()
        except Exception:
            screen_path = self.get_screenshot_as_file()
            return False, '元素[' + locator + ']点击失败，已截图[' + screen_path + ']'
        return True, '元素[' + locator + ']点击成功'

