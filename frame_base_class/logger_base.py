#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)

import logging
import os.path
import time
from common_class.Root_path import xpath

class Logger(object):
    # 获取项目绝对路劲并且组合需要的新路径
    x = xpath()
    dir = x.get_root_path()


    def __init__(self, logger):
        '''''
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        '''
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        # 项目根目录下/Logs 保存日志
        # log_path = os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_path = self.dir + r'/logs/'
        # 日志文件名称
        log_name = log_path + rq + '.log'

        #创建日志输入端，fh输入到日志文件，ch输出到控制台，定义日志级别为info
        fh = logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s[line:%(lineno)d] - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger

