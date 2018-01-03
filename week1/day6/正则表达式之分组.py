#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

# 正则分组(从匹配到的数据结果里面,再去匹配)
import  re


# match
origin = "haf4444 habc dafdsafd"
# r = re.match("h(\w+)", origin)
# r = re.match("h(\w+)", origin)
# r = re.match("h(?P<name>\w+)", origin) # 和groupdict搭配使用

# print(r.group())  # 获取匹配到的所有结果
# print(r.groups())  # 获取模型中匹配到的分组结果
# print(r.groupdict())  # 获取模型中匹配到的分组结果


# findall
# origin = "hqweaarty habcaadefg dafdsafd"
# r = re.findall("h(\w+)aa(\w+)", origin)  # 他回匹配"h(\w+)" 这个表达式,但是他显示的是分组的内容.
# print(r)


# sub
# sub是替换的字符的,无分组.

# split
# 无分组
origin = "hello alex bcd alex lge alex acd 19"
r = re.split("alex", origin,1)
print(r)

# 有分组
origin = "hello alex bcd alex lge alex acd 19"
r1 = re.split("(alex)", origin, 1)  # (alex) 在要匹配的字符里是能够被匹配到的,而分组是在匹配到的结果里再去进行匹配.分组显示从外到内.
r2 = re.split("a(le)x", origin, 1)  # (alex)
print(r1)
# ['hello ', 'alex', ' bcd alex lge alex acd 19']  显示如此.
print(r2)
# ['hello ', 'le', ' bcd alex lge alex acd 19']

