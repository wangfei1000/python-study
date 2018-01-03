#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei
#http://www.cnblogs.com/alex3714/articles/5161349.html

import  time


'''


# 查看时间戳，从1970年到现在的秒数。
print(time.time())

# 查看当前系统时间
print(time.ctime())

# 将时间戳转换为字符串格式。
print(time.ctime(time.time()-86400))

# 显示格林威治时间
print(time.gmtime())

time_obj = time.gmtime()
print("{year} - {month}".format(year = time_obj.tm_year,month = time_obj.tm_mon))


# 查看本地系统的时间。
print(time.localtime())


# 转换为时间戳
print(time.mktime(time_obj))

# 做阻塞使用
time.sleep(5)

# 将strftime格式转换成指定的字符串格式。
# time.strftime()
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))

# strptime 将字符串格式转换成struct_time格式
tm = time.strptime("2017-03-04 12:04","%Y-%m-%d %H:%M")
print(tm)
'''


import datetime

'''
# 输出当前的日期
print(datetime.date.today())

# 将时间戳转换为日期
tm = datetime.date.fromtimestamp(time.time()-86400)
print(tm)

# 输出当前时间
print(datetime.datetime.now())
'''


current_time = datetime.datetime.now()
# 替换时间，why ? 自己减这个时间太麻烦了，直接替换更方便。
print(current_time.replace(1992,9,12))
print(current_time.replace(1992,9))
print(current_time.replace(1992))

### 加减时间
# 当前时间加上10天
print(datetime.datetime.now() + datetime.timedelta(days=+10))
# 当前时间减去10天
print(datetime.datetime.now() + datetime.timedelta(days=-10))
# 当前时间减去10小时
print(datetime.datetime.now() + datetime.timedelta(hours=-10))

# 字符串格式转为为时间格式。
print(datetime.datetime.strptime("2016-09-09 12:42","%Y-%m-%d %H:%M"))



# time  取时间戳
# datetime 取日期


# 二个时间间的比较

# current_time = datetime.datetime.now()
# time_obj = current_time.replace(2016,9,9)
# print(current_time>time_obj)


