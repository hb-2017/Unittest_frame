#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        '''''
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        '''
        #创建一个记录器logger
        self.logger = logging.getLogger(logger)
        # 指定日志的最低输出级别，默认为WARN级别
        self.logger.setLevel(logging.DEBUG)


        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s[line:%(lineno)d] - %(message)s')
        #指定日志的输出路劲
        time_ = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        log_xpath =os.path.dirname(os.path.abspath('.'))+'/logs/'  #os.path.abspath返回文件的绝对路径，os.path.dirname返回path最后的文件名
        #指定日志名称
        log_name = log_xpath+time_+'.log'
        # 创建日志输入端，FileHandler输入到日志文件，ch输出到控制台，定义日志级别为info,
        FileHandler_ = logging.FileHandler(log_name,encoding='utf-8')
        FileHandler_.setLevel(logging.INFO)
        FileHandler_.setFormatter(formatter)

        StreamHandler_ = logging.StreamHandler(log_name)
        StreamHandler_.setLevel(logging.INFO)
        StreamHandler_.setFormatter(formatter)


        # 给logger添加handler
        self.logger.addHandler(FileHandler_)
        self.logger.addHandler(StreamHandler_)

    def getlog(self):
        return self.logger

