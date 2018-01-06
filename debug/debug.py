#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import unittest
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.1dadan.com')
browser.find_element_by_id('taobaoLogin').click()
browser.switch_to.frame("J_loginIframe")
aaa = browser.find_element_by_id('J_SubmitStatic').is_displayed()
print(aaa)

