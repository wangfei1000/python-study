#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

'''
# http://www.cnblogs.com/wupeiqi/articles/5484747.html
# 格式化字符 %
# %s %d 占位符
s = "hehe %s %d" %("MM", 40)
print(s)

# %[(name)][flags][width].[precision]typecode
# 右对齐
s2 = "hehe%(name)+10sand age %(age)-d" %{'name':'Mm','age':-40}
print(s2)

# 左对齐
s3 = "hehe%(name)-10sand" %{'name':'Mm','age':40}
print(s3)

# s3 = "fdafdahehe %s+10 %d" %("wf",26)
# print(s3)


# 小数
s4 = "hehe%(name)-10sand %(p)f" %{'name':'Mm','age':40,"p":1.234567}
print(s4)

# 只保留2位小数
s4 = "hehe%(name)-10sand %(p).2f" %{'name':'Mm','age':40,"p":1.234567}
print(s4)

Num = 65
s5 = "%c" %Num

print("%c" %(65))


# 字符串格式化里边，如果要打印出%需要用%%来表示。
print(" %s %%" %("hehe"))
print("%.2f" % 99.4444)
print("%(num).2f"%{"num":999.3363})
print("name %s" % "wangfei")
'''



####################################
# 格式化字符format
# [[fill]align][sign][#][0][width][,][.precision][type]
# s = "my name is {0},I am {1} years old.".format("wangfei",20)
# s = "my name is {0},I am {1} years old.".format("wangfei",20)
# s = "my name is {name:s},I am {age:d} years old.".format(name = "wangfei",age =18)
# s = "-----{:*^20s}-----{:a^20d}-----{:#}".format("wf",123,12)
# print(s)

# 支持所有类型，啥玩意都可以往里面塞。
# s = "my name is {},I am {} years old.".format("wangfei",20)
# print(s)

s = "my name is {},I am {} years old.".format(*["wangfei",20,"alex"])
print(s)

# s = "my name is {name},I am {age} years old.".format(name = "wangfei",age = 20)
# print(s)

# s = "my name is {name},I am {age} years old.".format(**{"name":"wangfei","age":20})
# print(s)


###################
'''

# 生成器
# 列如range(0)，生成的数据在pyhon2.7里边他是放到列表里的，将会占用内存。有了生成器就会生成对象，不会占用内存，他有能力
# 生成指定的数据。

# li = [11,22,33,44,55]
#
# result = filter(lambda a1:a1> 22,li)
# print(result) # 具有生成指定条件数据的能力的一个对象。只有循环它才能生成。

def func():
    print("123")
    yield 1 # 只要碰到yield就变成了生成器。
    print("2")
    yield 2
    print("3")
    yield 3

ret = func() # 看生成的是一个对象，不是列表，是数据。但他有能力生成你要的指定数据。他啥都没有干。
print(ret)
# print(ret)
# for i in ret:
#     print(i)

r1 = ret.__next__()  # __next__ 每次只取一个值，碰到yeild就会取后面的数据，然后停止执行
print(r1)

r2 = ret.__next__() # 到这一次执行的时候，就接着上一次yiled执行的位置，接着执行。
print(r2)

r3 = ret.__next__()
print(r3)



def myrange(args):
    start = 0
    while True:
        if start > args:
            return
        yield  start
        start += 1

ret = myrange(10)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
'''


######
# 迭代器


# 递归
'''当下面的函数执行时，首先n加上1得2，如果不等于4，又重新的执行f1这个函数，此时n
等于2，n > 4 ? False .继续执行f1函数。最终符合条件 return end


def f1(n):
    n += 1
    if n > 4:
        return "end"
    return f1(n)

r = f1(1)
print(r)
'''
