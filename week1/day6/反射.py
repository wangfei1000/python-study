#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei
# python 反射

# 基础版
"""
import commons


def func():

    '''
    Action : 用户输入的内容
    为什么要用到反射呢？
    下面的方法一，假如导入的模块里面有100个函数，你还能写100次判断吗？好吧1000个函数。。。。。。。
    怂了吧！B格来了，用python的反射，hasattr 检查函数是否在导入的模块里面，getattr获取对应的函数（注意，这只是获取到这个函数而已）


    这里有个要注意的东西：
    def login():
        print("hehe")

    inp = "login"

    这里的f1 和 inp是不同的，f1()是一个函数，inp  是字符串而已。
    commons.inp()  如果你这样写的，就会到commons找inp这个函数和commons.login()没啥关系的。

    '''

    Action = input("> ")
    # 模仿网页登录操作，用户输入什么，就显示什么。

    # 方法一
    # 根据用户输入的内容，用if 语句来完成。弊端：工作量big，代码多。
    # if Action == "login":
    #     commons.login()
    # elif Action == "home":
    #     commons.home()
    # elif Action == "logout":
    # else:
    #     print("404")

    # 方法二
    # python的反射，先判断用户输入的函数在模块里面是否存在，如果存在就取出这个函数。
    # 利用字符串的形式去到模块中操作（寻找、删除、检查、设置）对象。

    delattr()
    setattr()

    if hasattr(commons,Action): # hsattr 判断函数是否在模块里面存在。
        func = getattr(commons,Action) # 从模块里面取出这个函数，注意这个只是取出函数。没有执行这个函数。
        func() # 执行取出的函数
    else:
        print("404")


if __name__ == '__main__':
    func()

"""





# 优化版
# 此时假如有很多模块，就都得导入,那样就太麻烦了。我们可以让用户自己输入模块名，然后我们导入这个模块。

def func():
    '''
    类似这样的输入，account/login   manager/order。
    用字符串的形式导入模块 import "commons" ,这样是不能导入的。__import__（"commons"）这样就可以用字符串的方式导入模块了。

    拓展知识：
        如果使用__import__ 到目录里面如导入相关的模块的话，如这样__import__("lib."+ f) ,这样是不能导入的，他只能导入到lib.需要后面加
        一个参数 fromlist = True 就可以了。

    '''

    inp = input("> ")
    m,f = inp.split("/")

    obj = __import__("lib."+m, fromlist=True)

    if hasattr(obj,f): # hsattr 判断函数是否在模块里面存在。
        func = getattr(obj,f) # 从模块里面取出这个函数，注意这个只是取出函数。没有执行这个函数。
        func() # 执行取出的函数
    else:
        print("404")


if __name__ == '__main__':
    func()