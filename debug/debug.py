#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import *       #用于鼠标事件


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


lis = [1,2,3,4,5]

print(lis[-2:])