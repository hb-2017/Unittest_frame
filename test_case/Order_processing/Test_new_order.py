#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import configparser
import os
import unittest
from frame_base_class.driver_base import Driver_base  # 浏览器驱动
from common_class.Root_path import xpath
from frame_base_class.logger_base import Logger
from page_elements.Batch_printing.skin01_new_order import skin01_new_order
from test_case.Load_driver.Load_driver import Load_drive

logger = Logger(logger='new_order').getlog()

class new_order(Load_drive):
    # 获取项目绝对路劲并且组合需要的新路径
    x = xpath()
    dir = x.get_root_path()

    # def setUp(self):
    #     # 测试固件的setUp()的代码，主要是测试的前提准备工作
    #     Drivrser = Drivrser_base(self)
    #     self.browser = Drivrser.open_browser(self)
    #
    #
    # def tearDown(self):
    #
    #     # 测试固件的tearDown()的代码，这里基本上都是关闭浏览器
    #     self.browser.quit()

    def get_order_info(self):
        order_info = []
        config = configparser.ConfigParser()
        config_xpath = self.dir+'/config/common_data.ini'
        config.read(config_xpath,encoding='utf-8-sig')
        receiverName = config.get('order_info','receiverName')
        receiverPhone = config.get('order_info', 'receiverPhone')
        receiverMobile = config.get('order_info', 'receiverMobile')
        province = config.get('order_info', 'province')
        city = config.get('order_info', 'city')
        district = config.get('order_info', 'district')
        receiverAddress = config.get('order_info', 'receiverAddress')
        sellerMessage = config.get('order_info', 'sellerMessage')
        goodsNo = config.get('order_info', 'goodsNo')
        goodsName = config.get('order_info', 'goodsName')
        goodsProps = config.get('order_info', 'goodsProps')
        quantity = config.get('order_info', 'quantity')
        price = config.get('order_info', 'price')
        order_info.append(receiverName)
        order_info.append(receiverPhone)
        order_info.append(receiverMobile)
        order_info.append(province)
        order_info.append(city)
        order_info.append(district)
        order_info.append(receiverAddress)
        order_info.append(sellerMessage)
        order_info.append(goodsNo)
        order_info.append(goodsName)
        order_info.append(goodsProps)
        order_info.append(quantity)
        order_info.append(price)
        logger.info('get order info is %s'%order_info)
        return order_info

    #新建订单-手工输入
    def test_new_order_manual_input(self):
        new_order = skin01_new_order(self.browser)
        order_info = self.get_order_info()
        if len(order_info)!=0:
            new_order.new_order(order_info)
            new_order.sleep(1)
            tip_statu = new_order.new_order_tip()
            if tip_statu==True:
                logger.info('new order case %s is pass'%order_info[0])
                self.assertTrue(True)
            elif tip_statu==None:
                tip = new_order.new_error_tip()
                if tip!=False:
                    logger.error('new order case %s is fail,errpr tip is %s' % (order_info[0],tip))
                    self.assertTrue(False)
            else:
                logger.info('new order case %s is fail' % order_info[0])
                self.assertTrue(False)
        else:
            logger.error('Order info length is "0" ,Unable to build a new order')
            self.assertTrue(False)


    # 新建订单-选收件人



if __name__ == '__main__':
    unittest.main()