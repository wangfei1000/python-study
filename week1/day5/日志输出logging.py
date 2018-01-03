#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

# http://www.cnblogs.com/wupeiqi/articles/5501365.html

import logging

# create logger
logger = logging.getLogger('TEST-LOG') # TEST-LOG 标记，先获取loger对象
logger.setLevel(logging.DEBUG) # 设置一个全局的日志级别

# create console handler and set level to debug
ch = logging.StreamHandler() # 将日志输出到屏幕
ch.setLevel(logging.DEBUG) # 屏幕的日志输出级别

# create file handler and set level to warning
fh = logging.FileHandler("access.log")
fh.setLevel(logging.WARNING)

# create formatter # 设置日志格式
# 日志格式里甚至能够打印是哪一行的日志输出的格式，哪个线程输出的日志，那个进程输出的日志。
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter_fh = logging.Formatter('%(asctime)s - %(filename)s -%(lineno)d - %(levelname)s - %(message)s')

# add formatter to ch and fh # 将输出的目的和日志格式绑定起来
ch.setFormatter(formatter) # 将format注册给handle
fh.setFormatter(formatter_fh)

# add ch and fh to logger
logger.addHandler(ch) # 将handle注册给logger
logger.addHandler(fh)

# 'application' code
logger.debug('debug message' )
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')