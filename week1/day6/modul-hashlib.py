#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei
# hashlib  加密模块fda
'''

http://www.cnblogs.com/wupeiqi/articles/5501365.html
'''

import  hashlib

obj = hashlib.sha256()
obj.update(bytes('123',encoding='utf-8'))  # python2.7 obj.update("123"),python3 需要使用bytes。
password = obj.hexdigest()
print(password)

'''
以上加密算法虽然依然非常厉害，但时候存在缺陷.
即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。
'''
obj = hashlib.sha256(bytes('abcd',encoding='utf8'))
obj.update(bytes('123',encoding='utf-8'))
print(obj.hexdigest())