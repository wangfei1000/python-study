#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei
'''
usernmae = input("User: ")

# 用strip 来去除多输入的空格
if usernmae.strip() == "wangfei":
    print ("Welcome to system")
'''


'''
# split 以逗号为分割符，将这个变量分割，分开这后就变成了一个列表。
name = "a,b,c,d,e,f,g"
name2 = name.split(",")
print (name2)

# 合并列表,以|为分隔符，将各变量连接到一块。
print ("|".join(name2))

# 判断有没有空格
name = "wang fei"
print (" " in name)
'''

'''
# 格式化字符
name = "my name is {name},i am {old} years old."
# 方法一
msg = name.format(name = "wangfie", old = 23)
print (msg)

#  方法二
msg = "name{0}, name{1}"
print(msg.format("wangfei",19))
'''
# 切片
name = "a b c d e f g"
# 打印40个- ,将name变量放在这个中间
print (name.center(50,"_"))