#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei
# configparser 只能处理如下的这种格式的文件内容

'''
http://www.cnblogs.com/wupeiqi/articles/5501365.html
configparser用于处理特定格式的文件，其本质上是利用open来操作文件。


[section1] # 节点
k1 = v1    # 值
k2:v2       # 值

[section2] # 节点
k1 = v1    # 值
'''



# 1、获取所有节点

import configparser

# 创建一个可以帮你做操作的东西
config = configparser.ConfigParser()   # tmd 神奇了，Pycharm 提示没有configparser这个属性，但是在终端模式就可以使用。ps:原来是名字
# 和模块的名字冲突了
# 将材料给这个东西，（文件和编码）
config.read('/Users/feiwang/PycharmProjects/week1/day6/xxoo', encoding='utf-8')
ret = config.sections()  # 机器就可以做东西了，查看节点数
print(ret)


# 2、获取指定节点下所有的键值对
ret = config.items('section1')
print(ret)

# 3、获取指定节点下所有的建
ret = config.options('section1')
print(ret)

# 4、获取指定节点下指定key的值
v = config.get('section1', 'k1')
# v = config.getint('section1', 'k1')
# v = config.getfloat('section1', 'k1')
# v = config.getboolean('section1', 'k1')
print(v)

# 5、检查、删除、添加节点

# 检查
has_sec = config.has_section('section1')
print(has_sec)

# 添加节点
config.add_section("SEC_1")
config.write(open('xxxooo', 'w'))


# 删除节点
config.remove_section("SEC_1")
config.write(open('xxxooo', 'w'))

# 6、检查、删除、设置指定组内的键值对
# 检查
has_opt = config.has_option('section1', 'k1')
print(has_opt)

# 删除
config.remove_option('section1', 'k1')
config.write(open('xxxooo', 'w'))

# 设置
config.set('section1', 'k10', "123")
config.write(open('xxxooo', 'w'))