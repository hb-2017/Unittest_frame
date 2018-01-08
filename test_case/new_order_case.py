#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

from frame_base_class.driver_base import Drivrser_base
from frame_base_class.logger_base import Logger
from page_elements.skin01_new_order import skin01_new_order
import unittest
import configparser
import os

logger = Logger(logger='new_order').getlog()

class new_order(unittest.TestCase):

    def get_order_info(self):
        order_info = []
        config = configparser.ConfigParser()
        config_xpath = os.path.dirname(os.path.abspath('.'))+'/config/common_data.ini'
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


    def new_order_statr(self,browser):
        new_order = skin01_new_order(browser)
        order_info = self.get_order_info()
        if len(order_info)!=0:
            new_order.new_order(browser,order_info)
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


