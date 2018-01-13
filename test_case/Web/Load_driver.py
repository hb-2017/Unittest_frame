#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)
import unittest
from frame_base_class.driver_base import Driver_base

class Load_drive(unittest.TestCase):

    Driver = Driver_base()
    browser = Driver.open_browser()

    def setUp(self):
        # 测试固件的setUp()的代码，主要是测试的前提准备工作
        pass

    def tearDown(self):
        # 测试固件的tearDown()的代码，这里基本上都是关闭浏览器
        # self.browser.quit()
        pass

