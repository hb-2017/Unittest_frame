#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import os
import unittest
from test_case.Login_and_register.Test_login import Test_login
from test_case.Web.Load_driver import Load_drive

suite = unittest.TestSuite()
#全节点登录测试用例
suite.addTest(Test_login("test_All_node_login"))
#退出浏览器
suite.addTest(Load_drive("test_quit_browser"))

if __name__=='__main__':
    #执行用例
    runner=unittest.TextTestRunner()
    runner.run(suite)
