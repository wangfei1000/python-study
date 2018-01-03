#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

# 序列化：将python基本数据类型转换为字符串类型。
import  json
# dic = {"k":"v"}
# print(type(dic),dic)
#
# result = json.dumps(dic)
# print(type(result),result)

# 反序列化
# 将Python字符串转换为基本数据类型
s1 = '{"k1":"v1"}'
print(type(s1))
dic = json.loads(s1)
print(type(dic))