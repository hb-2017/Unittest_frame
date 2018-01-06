#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import time
from selenium.common.exceptions import NoSuchElementException
import os
from frame_base_class.logger_base import Logger

#实例化日志类
logger = Logger(logger = 'Basepage').getlog()

class Basepage():
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self,driver):
        self.browser = driver

    #退出浏览器
    def quir_browser(self):
        self.browser.quit()

    #浏览器前进
    def browser_forward(self):
        self.browser.forward()
        logger.info('Click forward on current page.')

    #浏览器后退
    def browser_back(self):
        self.browser.back()
        logger.info('Click back on current page')

    #隐式等待
    def browser_wait(self,seconds):
        self.browser.implicitly_wait(seconds)
        logger.info('browser wait for %d seconds." % seconds')



    #关闭当前窗口
    def browser_close(self):
        try:
            self.browser.colse()
            logger.info('Closing and quit the browser')
        except NameError as e:
            logger.error('Failed to quit the browser with %s' % e)

    #截图并且保存
    def get_windows_img(self):
        """
            在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        screenname = file_path+rq+'.png'
        try:
            self.browser.get_screenshot_as_file(screenname)
            logger.info('Had take screenshot and save to folder : /screenshots')
        except NameError as e:
            logger.error('Failed to take screenshot! %s' % e)
            self.get_windows_img()


    # 定位元素方法
    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        #分割元素
        if '=>' not in selector:
            return self.browser.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.browser.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.browser.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.browser.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.browser.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.browser.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.browser.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.browser.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.browser.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    # 输入
    def input(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.browser.title)
        return self.browser.title


    #判断元素是否存在
    def element_is_dispalynd(self,selector):
        # 分割元素
        if '=>' not in selector:
            try:
                return self.browser.find_element_by_id(selector)
            except:
                element_dispaly = False
                return element_dispaly
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        try:
            if selector_by == "i" or selector_by == 'id':
                element_dispaly = self.browser.find_element_by_id(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "n" or selector_by == 'name':
                element_dispaly = self.browser.find_element_by_name(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "c" or selector_by == 'class_name':
                element_dispaly = self.browser.find_element_by_class_name(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "l" or selector_by == 'link_text':
                element_dispaly = self.browser.find_element_by_link_text(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "p" or selector_by == 'partial_link_text':
                element_dispaly = self.browser.find_element_by_partial_link_text(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "t" or selector_by == 'tag_name':
                element_dispaly = self.browser.find_element_by_tag_name(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "x" or selector_by == 'xpath':
                element_dispaly = self.browser.find_element_by_tag_xpath(selector_value).is_displayed()
                return element_dispaly
            elif selector_by == "s" or selector_by == 'selector_selector':
                element_dispaly = self.browser.find_element_by_tag_selector_selector(selector_value).is_displayed()
                return element_dispaly
        except:
            element_dispaly = False
            return element_dispaly




    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)



    def get_elemeent_text(self,selector):
        el = self.find_element(selector)
        elemeent_text = el.text
        logger.info('get element text is %s'%elemeent_text)
        return elemeent_text


