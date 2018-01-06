#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import unittest
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.1dadan.com')
browser.find_element_by_id('free_reg').click()
browser.find_element_by_id('mobile').send_keys('15896968585')
code= input('验证码')
browser.find_element_by_id('captcha1').send_keys(code)
browser.find_element_by_id('sendMobileCodeBtn').click()
code2= input('验证码')
browser.find_element_by_id('checkCodeMobile').send_keys(code2)

