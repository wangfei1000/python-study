#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

import requests
import json

# r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=%E6%9D%AD%E5%B7%9E")
# result = r.text
# dic = json.loads(result)
#
# print(dic)

# li = "['a','b','c']"
# li = '["a","b","c"]'
#
# r1 = json.loads(li)
# print(r1,type(r1))
#
# r = json.dump(li,open("db.conf","w"))
#
# r2 = json.load(open("db.conf","r"))
# print(r2)

# import pickle
#
# r3 = pickle.dumps(li)
# print(type(r3),r3)
#
# print(pickle.loads(r3))


# import time
#
# # print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
# # print(time.strptime("2017-10-08 12:21:32","%Y-%m-%d %H:%M:%S"))
#
#
# # import logging
# # logger = logging.getLogger('TEST-LOG') # 标记，获取loger对象
# # logger.setLevel(logging.DEBUG) # 设置日志的级别
# #
# # ch = logging.StreamHandler()
# # ch.setLevel(logging.DEBUG)
# #
# # fh = logging.FileHandler("access.log")
# # fh.setLevel(logging.WARNING)
# #
# # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # formatter_fh = logging.Formatter('%(asctime)s - %(filename)s -%(lineno)d - %(levelname)s - %(message)s')
# #
# # ch.setFormatter(formatter) # 将format注册给handle
# # fh.setFormatter(formatter_fh)
# # logger.addHandler(ch) # 将handle注册给logger
# # logger.addHandler(fh)
# #
# # logger.debug('debug message' )
# # logger.info('info message')
# # logger.warn('warn message')
# # logger.error('error message')
# # logger.critical('critical message')
#


# print(__name__)


# way1
from lib import commons as aa

aa.login()
