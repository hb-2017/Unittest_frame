#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import os
import unittest
from common_class.Root_path import xpath
# 获取项目绝对路劲并且组合需要的新路径
x = xpath()
dir = x.get_root_path()

case_path = dir + '/test_case'

suite = unittest.TestLoader().discover(case_path)

print(suite)
if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)