#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import *       #用于鼠标事件
import os

# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get('https://www.1dadan.com')
# browser.find_element_by_id('userName').send_keys('test09')
# browser.find_element_by_name('password').send_keys('1qaz2wsx')
# browser.find_element_by_id('submit').click()
# el = browser.find_element_by_id('topNavBtn')
# chain=ActionChains(browser)
# chain.move_to_element(el).perform()
# browser.find_element_by_id('logoutBtn').click()


# class xpath():
#
#     def get_root_path(self):
#         root_path = r'D:\Unittest_frame'
#         return root_path
#
# class report():
#
#     def get_report_path(self):
#         path = xpath()
#         dir = path.get_root_path()
#         report_path = dir + '/test_report'
#         return report_path
#
#     def report_exist_statu(self):
#         report_path = self.get_report_path()
#         # 获取系统当前时间
#         month = time.strftime("%m", time.localtime(time.time()))
#         day = time.strftime("%d", time.localtime(time.time()))
#         report_name = time.strftime("%H_%M_%S", time.localtime(time.time()))
#         report_path = report_path+r'/'+month+'月'+r'/'+day+'日'+r'/'+report_name+'-HTMLtemplate.html'
#         report_statu = os.path.exists(report_path)
#         if report_statu:
#
#         else:
#             fp = open(HtmlFile, "wb")

# xxx = report()
# xxx.report_exist_statu()
