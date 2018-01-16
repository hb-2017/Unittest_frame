#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)
import os
import unittest
from test_case.Login_and_register.Test_login import Test_login
from test_case.Order_processing.Test_new_order import new_order
from test_case.Web.Load_driver import Load_drive
import HTMLTestRunner
from common_class.Root_set_up import report
import time


suite = unittest.TestSuite()
suite.addTest(Test_login("test_user_login"))  #登录测试用例
# suite.addTest(new_order("test_new_order_manual_input"))  #登录测试用例
suite.addTest(new_order("test_new_order_choose"))  #新建订单
suite.addTest(Load_drive("test_quit_browser"))  #退出浏览器

if __name__=='__main__':
    # 实例化测试报告
    re = report()
    report_title = 'test_new_order_choose'
    fp = re.report_exist_statu(report_title)
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"全节点登录测试", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)

    # # 执行用例
    # runner = unittest.TextTestRunner()
    # runner.run(suite)