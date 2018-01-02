#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import  configparser
import os
from selenium import webdriver
from frame_base_class.logger_base import Logger

#实例化Logger类
logger = Logger(logger = "Drivrser_base").getlog()

class Drivrser_base():

    # 获取绝对路劲并且把绝对路劲的最后一层目录去除
    dir = os.path.dirname(os.path.abspath('.'))
    # 获取浏览器驱动的路径
    Chrome_driver_path = dir + '/tools/chromedriver.exe'
    Ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver

    def open_browser(self, driver):
        #实例化配置文件类
        config = configparser.ConfigParser()
        #获取配置文件路劲,并读取
        driver_config_xpath = os.path.dirname(os.path.abspath('.')+'config/driver_config.ini')
        url_manage_xpath = os.path.dirname(os.path.abspath('.')+'config/url_manage.ini')
        config.read(driver_config_xpath)
        config.read(url_manage_xpath)
        #读取config的驱动,url信息
        browser = config.get('browserType','browserName')
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)
        # 驱动启动，写日志
        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.Chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.Ie_driver_path)
            logger.info("Starting IE browser.")
        # 打开网址并且写入日志
        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    # 退出浏览器
    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()


