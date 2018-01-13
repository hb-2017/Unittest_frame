#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import unittest
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.1dadan.com')
browser.find_element_by_id('userName').send_keys('new165')
browser.find_element_by_name('password').send_keys('1qaz2wsx')
browser.find_element_by_id('submit').click()
browser.find_element_by_id('createOrderBtn').click()
time.sleep(2)
browser.find_element_by_name('receiverAddressBtn').click()
table = browser.find_element_by_class_name('recipientTbody')
tr = table.find_elements_by_tag_name('tr')
for t in tr:
    t.click()