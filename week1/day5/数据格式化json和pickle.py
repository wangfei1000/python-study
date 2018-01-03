#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei
'''

pickle 和 json 的区别？


json:
    更加的时候跨语言，字符串，基本数据类型。

pickle:
    所有类型的序列化，仅仅适用于python


'''




'''

# json 知识



import  requests
import json
#
r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=%E6%9D%AD%E5%B7%9E")
Result = r.text
print(type(Result),Result)

Dic = json.loads(Result)
print(type(Dic))


li = "['wf','lisi']"  # 注意：json在进行反序列化的时候，最外面要是''单引号（在别的语言中，单引号是字符串，双引号是字符）。
li = '["wf","lisi"]'
result = json.loads(li)
print(type(result))


# json 的 dump和load

import  json

# dump 它有2个操作，先先序列化，然后写入到文件里。
li = [11,22,33,44]
json.dump(li,open("db.conf",'w'))

# load  有2个操作，先打开文件然后进行反序列化。
r = json.load(open("db.conf","r"))
print(type(r))
'''

import pickle
list = [1,2,3,4]

'''

# pickle dumps
s = pickle.dumps(list)
print(type(s),s)

# pickle loads
li = pickle.loads(s)
print(li,type(li))
'''


# pickle dump
pickle.dump(list,open("db2.conf","wb")) # pickle 用的是字节类型写入的。

# pickle load
Li = pickle.load(open("db2.conf","rb"))
print(Li)


