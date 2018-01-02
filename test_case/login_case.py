#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import os
import unittest
import configparser
from frame_base_class.driver_base import  Drivrser_base #浏览器驱动
from frame_base_class.page_base import Logger # 日志
from data.get_excel_data import Get_excel_data # excel参数
from page_elements.skin01_login import skin01_user_login,taobao_login #页面元素


#实例化日志类
logger = Logger(logger = "skin01_login").getlog()

class Skin01_login(unittest.TestCase):

    def setUp(self):
        # 测试固件的setUp()的代码，主要是测试的前提准备工作
        Drivrser = Drivrser_base(self)
        self.browser = Drivrser.open_browser(self)

    def tearDown(self):
        # 测试固件的tearDown()的代码，这里基本上都是关闭浏览器
        self.browser.quit()


    #账号密码登录
    def test_user_login(self):
        #从配置文件读取登录的账号密码
        config = configparser.ConfigParser()
        userinfo_config_xpath = os.path.dirname(os.path.abspath('.'))+'config/common_data.ini'
        config.read(userinfo_config_xpath)
        username = config.get('userinfo','username')
        password = config.get('userinfo','password')
        logger.info('get userinfo from config ')
        #开始输入账号密码
        user_login = skin01_user_login(self)
        try:
            user_login.input_userinfo(username,password)
            self.browser.find_element_by_id('submit').click()
            user_login.sleep(2)
        except:
            pass
        try:
            page_title = user_login.get_page_title()
            if page_title=='易打单 | 批量打印':
                logger.info('%s lonin_test pass' % username)
                print('%s lonin_test pass' % username)
            elif page_title=='易打单 登录':
                error_tip = user_login.get_error_tips()
                if error_tip == '请输入图片验证码':
                    user_login.input_code()
                    logger.info('error tips input code')
                    self.browser.find_element_by_id('submit').click()
                    user_login.sleep(2)

                    page_title = user_login.get_page_title()
                    if page_title == '易打单 | 批量打印':
                        logger.info('%s lonin_test pass' % username)
                        print('%s lonin_test pass' % username)
                    else:
                        logger.info('%s lonin_test fail' % username)
                        print('%s lonin_test fail' % username)
                else:
                    logger.error('%s login_test is fail ,%s'%(error_tip))
        except:
            pass









