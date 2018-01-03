#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

# def f1():
#     return a1+100
#
# f2 = 100+1
#
#
# print(callable(f2))

# print(chr(65))
# print(ord("a"))


# LIST = []
# import  random
# for line in range(6):
#     num = random.randrange(9)
#     if num == 3 or num == 5 or num == 1:
#         # num =  random.randrange(4)
#         LIST.append(str(num))
#     else:
#
#         num = random.randrange(65,90)
#         Str = chr(num)
#         LIST.append(Str)
#
#
#
#
#
# listnum = "".join(LIST)
# print(listnum)


# 将字符串转换为python代码
# s = 'print("hehe")'
# r = compile(s,"<string>","eval")
# print(eval(r))
# print(r)
# print(exec(r))
# print(eval(r))

# s = "8*8"
# # r = eval(s)
# r2 = exec(s)
# print(r2)

# r = divmod(100,10)
# print(r)

# r = isinstance(s,dict)
# print(r)


# 传统的方法
def f1(a1):
    rli = []
    for i in a1:
        if i > 3:
           rli.append(i)

    return rli

#
# li = [1, 2, 3, 4, 5, 6]
# # r = f1(li)
# # print(r)
#
#
# # filter方法
#
# def f2(a2):
#         if a2 > 3:
#             print(a2)
#             return True
#
# r = filter(f2,li)
# f3 = lambda a2 : a2 > 3
# r2 = filter(f3,li)
# print(list(r2))


# print(list(f3))

#
#
# def f2(a2):
#     nli = []
#     for i in a2:
#         nli.append(i+100)
#     return nli
#
# li = [1,2,3,4,5,6,7,8]
# r  =  f2(li)
# print(r)
#
# def f3(a3):
#     return a3 + "99"
#
# li = ["a","b","c"]
# r3 = map(f3,li)
# print(list(r3))
#
# print(list(map(lambda a4: a4+"99",li)))


# s = "name: %s  ,age :%d" % ("wf",26)
# print(s)

# %[(name)][flags][width].[precision]typecode
# 右对齐
# s2 = "name:%(name) +10and age %(age)" %{'name':'Mm','age':40}
# print(s2)

# 左对齐
# s3 = "hehe%(name)-10sand" %{'name':'Mm','age':40}
# print(s3)

# 小数
# s4 = "hehe%(name)   -2s and %(p)f" %{'name':'Mm','age':40,"p":1.234567}
# print(s4)

# 只保留2位小数
# s4 = "%(p).2f" %{"p":1.234567}
# print(s4)
#
# print("%c"%(65))

# print("%.2f" %(0.13455666))
# s = "%.2f" % (0.12345)
# s2 = "%(num).2f"%{"num":0.19345}
# s4 = "wangfei is %s" %("wangfei")
# print(s4)

# s1 = "my name is {0},i am {1} years old.".format("wangfei",20)
# print(s1)
# s2 = "my name is {name}, i am {age} year old.".format(name="wf",age=19)
# print(s2)
# s3 = "my name is {0},i am {1} years old.".format(*["wangfei",20])
# print(s3)
# s4 = "my name is {name},{age} years old.".format(name="wangfei",age=19)
# print(s4)
# s5 = "my name is {name},{age} years old.".format(**{"name":"wangfei","age":19})
# print(s5)


# def func():
#     print("123")
#     yield 1
#     print("456")
#     yield 2
#     print("789")
#     yield 3
#
# ret = func()
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())


# def f2(n):
#     n+=1
#     if n>10:
#         return "end"
#     print(n)
#
#     return f2(n)
#
# print(f2(1))


def  f1():
    print("1")
    yield  1
    print("2")
    yield 2
    print("3")
    yield 3
    print("4")
    yield 4
#
# r = f1()
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())
# print(list(r)[0])

import s4
s4.logging()




