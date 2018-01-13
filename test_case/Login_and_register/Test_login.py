#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import configparser
import os
import unittest
from common_class.Root_path import xpath
from common_class.Assertion import Assertion
from frame_base_class.driver_base import Driver_base  # 浏览器驱动
from frame_base_class.page_base import Logger  # 日志
from page_elements.Home_page.login_page import skin01_user_login, taobao_login  # 页面元素
from test_case.Web.Load_driver import Load_drive

#实例化日志类
logger = Logger(logger = "Test_login").getlog()
Assertion_ = Assertion()

class Test_login(Load_drive):
    # 获取项目绝对路劲并且组合需要的新路径
    x = xpath()
    dir = x.get_root_path()

    # def setUp(self):
    #     # 测试固件的setUp()的代码，主要是测试的前提准备工作
    #     self.Drivrser = Drivrser_base(self)
    #
    #
    #
    # def tearDown(self):
    #     # 测试固件的tearDown()的代码，这里基本上都是关闭浏览器
    #     self.browser.quit()

    # 从配置文件读取登录的账号密码
    def get_user_info(self):

        config = configparser.ConfigParser()
        userinfo_config_xpath =  self.dir+ '/config/common_data.ini'
        config.read(userinfo_config_xpath,encoding="utf-8-sig")
        username = config.get('userinfo', 'username')
        password = config.get('userinfo', 'password')
        logger.info('get userinfo from config ')
        return username,password

    # 获取页面标题
    def page_title(self,title,browser=None):
        user_login = skin01_user_login(browser)
        page_title = user_login.get_page_title()
        if page_title==title:
            logger.info(' 预期页面标题：%s 与实际标题%s相符' %(title,page_title ))
            return True
        else:
            logger.error(' 预期页面标题：%s 与实际标题%s不相符' % (title, page_title))
            return False

    #账号密码登录
    def test_user_login(self):

        print('易打单账号登录开始')
        username,password = self.get_user_info()
        #开始输入账号密码
        user_login = skin01_user_login(self.browser)    #实例化页面类的时候将浏览器驱动带到页面元素类，用于操作页面
        user_login.input_userinfo(username,password)
        self.browser.find_element_by_id('submit').click()
        user_login.sleep(2)
        try:
            if self.page_title('易打单 | 批量打印',self.browser):
                self.assertTrue(True)
            elif self.page_title('易打单 登录',self.browser):
                error_tip = user_login.get_error_tips()
                if error_tip == '请输入图片验证码':
                    # 开始输入验证码
                    user_login.input_code()
                    logger.info('error tips input code')
                    self.browser.find_element_by_id('submit').click()
                    user_login.sleep(2)
                    if self.page_title('易打单 | 批量打印',self.browser):
                        self.assertTrue(True)
                    else:
                        self.assertTrue(False)
                else:
                    logger.error('%s login_test is fail ,%s'%(username,error_tip))
                    self.assertTrue(False)
            else:
                self.assertTrue(False)
        except BaseException as e:
            logger.error('登录错误：%s'%e)
            self.assertTrue(False)

    # 读取淘宝登录的账号密码
    def get_taobao_info(self):
        config = configparser.ConfigParser()
        taobao_xpath = self.dir+'/config/common_data.ini'
        print(taobao_xpath)
        config.read(taobao_xpath,"utf-8-sig")
        username = config.get('taobaoinfo','username')
        password = config.get('taobaoinfo', 'password')
        logger.info('get userinfo from config ')
        return username,password


    # 淘宝登录
    def taobao_login(self,browser):
        print('淘宝登录开始')
        tb_login = taobao_login(browser)
        browser.find_element_by_id('taobaoLogin').click()
        tb_login.browser_wait(2)
        #进入淘宝登录界面
        if self.page_title('应用授权',browser):
            username, password = self.get_taobao_info()
            tb_login.taobaologin_statu()
            tb_login.input_taobaoinfo(username, password)
            if self.page_title('易打单 | 批量打印',browser):
                self.assertTrue(True)
            else:
                self.assertTrue(False)
        else:
            self.assertTrue(False)



# if __name__ == '__main__':
#     print('1')
#     unittest.main()



