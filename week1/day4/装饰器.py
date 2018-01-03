#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei


# 使用了开放封闭原则，不修改函数内部的功能在外部进行添加。

# def outer():
#     print("LOG")


'''
装饰器
产生的原因：
    100个已经写好的函数，现在要添加一个新功能。普通方法我需要到100个函数内部
    调用添加的新功能，方法比较费力，同时违反了开放封闭原则。有了装饰器之后
    一切就变的easy了起来。外部添加执行新功能，个性话添加新功能。

作用：
    不修改函数内部的功能，在外部进行添加修改代码。

'''
# def outer(func):
#     def inner():
#         # 在这个里面进行添加删除新功能。
#         print("log")
#         return func()
#     return inner


# def outer(func):
#     print("123",func)


# def outer(func):
#     return "111"



def outer(func):
    def inner(*args,**kwargs): # 这里也注意一下哦，注意装饰器参数的接收。哈哈用哪个万能参数。
        print("before")
        r = func(*args,**kwargs)  # 这个地方要注意一下哦！func()代表原函数，而原函数是有返回值的，so 要把原函数的值用r接收起来，
        # 最后return 下。
        print("after")
        return r
    return inner



############# 要装饰的函数 ############

# @ + 函数名
# 功能：
#   1、会自动的执行outer函数，并且将下面的函数名f1当做参数传递。
#   2、将outer的返回值，重新赋值给f1

@outer
def f1(*args):  # 注意哦 ！ 这里边有一个新的问题，在往原函数里边传参数时，装饰器和原函数都要接收参数的哦！
    print(args)
    return "呵呵哒"  # 注意 你要用了迭代器，这里我是有返回值的呀。


@outer
def f2(*args):
    print(args[0],args[1])
    print("f2")


@outer
def f100(args):
    print(args)
    print("f100")

# f1 = "222"
# print(f1)