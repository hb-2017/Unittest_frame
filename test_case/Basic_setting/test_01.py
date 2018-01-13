#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import unittest

class my(unittest.TestCase):
    def setUp(self):
        print('开始')
    def tearDown(self):
        print('结束')
    def test_01(self):
        print('1111')
    def test_02(self):
        print('2222')

if __name__ == '__main__':
    unittest.main