#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import configparser
import os
import unittest
from common_class.Root_set_up import root_xpath
from frame_base_class.driver_base import Driver_base
from frame_base_class.logger_base import Logger
from page_elements.Home_page.register_page import skin01_register

logger = Logger(logger = 'register').getlog()

class register(unittest.TestCase):
    # 获取项目绝对路劲并且组合需要的新路径
    x = root_xpath()
    dir = x.get_root_path()

    def setUp(self):
        # 测试固件的setUp()的代码，主要是测试的前提准备工作
        Drivrser = Drivrser_base(self)
        self.browser = Drivrser.open_browser(self)

    def tearDown(self):

        # 测试固件的tearDown()的代码，这里基本上都是关闭浏览器
        self.browser.quit()

        # 获取页面标题
    def page_title(self, title):
        register = skin01_register(self.browser)
        page_title = register.get_page_title()
        if page_title == title:
            logger.info(' 预期页面标题：%s 与实际标题%s相符' % (title, page_title))
            return True
        else:
            logger.error(' 预期页面标题：%s 与实际标题%s不相符' % (title, page_title))
            return False

    #获取注册时需要的信息
    def get_register_data(self):
        config = configparser.ConfigParser()
        config_xpath = self.dir+'/config/common_data.ini'
        config.read(config_xpath,encoding='utf-8-sig')
        Mobile = config.get('registerinfo','Mobile')
        password = config.get('registerinfo','password')
        username = config.get('registerinfo', 'username')
        logger.info('get register data Mobile:%s ,username:%s ,password:%s '%(Mobile,username,password))
        return Mobile,username,password

    # 验证手机
    def Verifying_mobile(self):
        Mobile,username, password = self.get_register_data()
        self.browser.find_element_by_id('free_reg').click()
        self.register.Verifying_mobile(Mobile)
        tip_statu = self.register.get_error_tip()
        if tip_statu==None:
            logger.info('%s Verifying mobile is pass'%Mobile)
            return True
        else:
            logger.info('%s Verifying mobile is fail , %s'%(Mobile,tip_statu))
            return tip_statu

    # 设置密码
    def Set_password(self):
        Mobile,username,password = self.get_register_data()
        self.register.Set_password(username,password)
        tip = self.register.get_tip()
        if tip==None:
            logger.info('%s Set_password is pass'%username)
            return True
        else:
            logger.info('%s Set_password is fail , %s'%(username,tip))
            return tip


    # 注册用例
    def register(self):
        self.register = skin01_register(self.browser)
        tip_statu = self.Verifying_mobile()
        if tip_statu==True:
            tip = self.Set_password()
            if tip==True:
                self.register.click_loginbutton()
                if self.page_title('易打单 | 批量打印'):
                    logger.info('test_register is pass')
                else:
                    self.register.get_windows_img()
                    page_title = self.page_title('易打单 | 批量打印')
                    logger.info('test_register is fail, page_title is %s'%page_title)
                    self.assertTrue(False,'test_register is fail, page_title is %s'%page_title)
            else:
                self.register.get_windows_img()
                logger.info('test_register is fail, page_title is %s' % tip)
                self.assertTrue(False, 'Set_password is fail, error is %s' % tip)
        else:
            self.register.get_windows_img()
            logger.info('test_register is fail, page_title is %s' % tip_statu)
            self.assertTrue(False, 'Verifying_mobile is fail, error is %s' % tip_statu)

#
# if __name__ == '__main__':
#     unittest.main()
