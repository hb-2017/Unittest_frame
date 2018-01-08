#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from frame_base_class.driver_base import Drivrser_base
from frame_base_class.logger_base import Logger
from page_elements.skin01_new_order import skin01_new_order
import unittest
import configparser


class new_order():

    def __init__(self):
        self.logger = Logger(logger='new_order').getlog()

    # 获取页面标题
    def page_title(self, title):
        register = skin01_new_order(self.browser)
        page_title = register.get_page_title()
        if page_title == title:
            self.logger.info(' 预期页面标题：%s 与实际标题%s相符' % (title, page_title))
            return True
        else:
            self.logger.error(' 预期页面标题：%s 与实际标题%s不相符' % (title, page_title))
            return False


