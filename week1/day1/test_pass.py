#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

import getpass  # import 导入模块
username = input("you are name: ")
password = getpass.getpass("password: ")   # 密文输入密码


print (username, password)

import os
# 使用系统命令
os.system("df -h")
# 新建目录
os.mkdir("wangfei")
# 保存命令的结果
time = os.popen("date").read()


import sys
己定义的模块放在/usr/lib/python2.7/dsit-packages目录下
# 查看pyhton默认存储模块的路径
print (sys.path)