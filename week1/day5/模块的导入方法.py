#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei
'''
import  sys
print(sys.argv)


1、模块都是先导入后使用。

2、什么是模块？
    .py 文件：就叫模块,
    文件：一个大的文件夹里面有很多的文件，构成一个大的模块。

3、为什么有模块呀？
    1、将不同的功能分类，你将10000行代码放到一个py文件里？
    2、将代码归类


4、导入模块的位置？什么依据？
类似于linux的PATH环境变量，如果想要把不再sys.path路径里的脚本导入到python,就可以
将脚本所在的路径append到这个sys.path里边。


5、模块名称的重要性
    不要将自己的模块名创建的和内置模块一样。***重要。。。

'''
# 导入模块的方式
# 类型一
# import s4
# s4.login()

# 类型二 文件夹
# import  lib.comment
# lib.comment.login()

# import  sys
# # print(type(sys.path))
# for item in sys.path:
#     print(item)

# import  sys
# 类似于linux的环境变量，将需要访问模块的路径放到sys.path里面
# sys.path 是一个列表
# sys.path.append("D:\\python\\PycharmProjects\\python\\")
# for item in sys.path:
#     print(item)
#
# import db
# db.login()

'''
模块导入方式
    # 单模块的方式
    1、import
        import 模块名

    # 嵌套在文件夹下的方式。
    2、from
    格式：
        from 文件夹 import 模块名 as 模块别名
    # 从一个模块里取出所有的函数,不推荐这么做哦！防止导入模块的函数和当前的函数冲突。
    from 模块名 import *

# one ways
import lib.comment
lib.comment.login()


# two ways
# from lib import comment # 从当前目录的文件夹导入模块
# comment.login()

# from s4 import  * # 导入模块里所有的函数
# login()
# logout()
#

# 从不同的目录里取出相同名称的模块，可以用from xx import xx as 的方式做个别名。
# from lib import comment as lib_comment
# lib_comment.login()
# lib_comment.logout()
#
# from src import  comment as src_comment
# src_comment.login()
# src_comment.logout()
'''

############安装第三方模块##############
# http://www.cnblogs.com/wupeiqi/articles/5501365.html
# 例子 安装requests
# pip3 安装方式
# pip3 install requests
# 源码安装方式
# 解压源码,进入目录
# python3 setup.py install
# import  requests