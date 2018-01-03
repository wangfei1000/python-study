#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

'''
# json补充知识

s = '[11,22,33,44,55]'
print(type(s))
import json
r = json.loads(s)
print(type(r))

d = '{"k1":"v1","k2":"v2","k3":"v3"}' # 注意 ，这个形状类似字典的字符串，外面必须是单引号，内部必须是双引号。
print(d)
dict = json.loads(d)
print(type(dict))

'''


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

# 获取json模块，下面用户输入一个类似字符串的字典时，需要转换成字典。
import  json

def Fetch(backend):
    '''
    backend查询模块

    让用户输入backend,迭代读取原文件。然后查看每行是否是以backend开头并且比较是否是用户要查看的backend，如果是 就打个标记，告诉下面的就
    是要查看的内容，将其内容写入到一个空得列表里。当读取到一个backend时说明读取完毕了，再打个标记表示读取完了，return返回 列表的值，并打
    印出来。


    :param backend: 用户输入的backend的值。
    :return: 返回用户查看的record记录。
    '''
    FetchResultList = [] # 定义一个空得列表，查到的数据都放在这个空得列表里。
    Flage = False
    with open("ha.conf", "r", encoding="utf-8") as f:

        for line in f:

            if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                Flage = True
                continue

            if Flage and line.strip().startswith("backend"):
                Flage = False
                break

            if Flage and line.strip():
                FetchResultList.append(line.strip())

    return FetchResultList


def Add(**Dic):
    '''
    增加record记录的模块。

    将文件内容分为三大部分：
    1、要写入的backend前面部分的内容。
    2、要写入的backend内容。
    3、要写入的backend后面部分内容。

    第一部分和第三部分内容直接的写入，第二部分内容的record记录是迭代前面查询到的列表内容。

    具体做法：
        将用户输入的backend放到 backend查询模块，就会得到模块对应的record记录。然后查看用户输入的record记录在不在查询到得record记录里，
        如果在，就直接将原先的文件使用shutil复制一份即可。

        如果backend都不存在，那么直接在新文件的尾部追加内容即可。

        如果backend存在，但是record不存在。将查询到得record append到查询模块得到的列表里。迭代原文件的每一行，看每行的开头是不是
        backend开头并且是用户要添加的backend。如果是就打个标记，将backend行写入到文件，迭代查询模块查询到得record记录写入到文件。然后
        continue跳出，否则用户需要添加的recoed会写入2次。


    :param Dic: 用户输入的一个包含recode和backend的字典
    :return:
    '''
    backend = Dic["backend"]
    server = Dic["record"]["server"]
    weight = Dic["record"]["weight"]
    maxconn = Dic["record"]["maxconn"]

    FetchResultList = Fetch(backend)
    # print(FetchResultList)
    if not FetchResultList:

        with open("ha.conf","r",encoding="utf-8") as old, open("New.conf","w",encoding="utf-8") as new:

            for line in old:
                new.write(line)
            new.write("\n\nbackend " + backend)
            new.write("\n" + " " * 8 + "server " + server + server + " weight" +
                          weight + " maxconn" + maxconn)
    else:
        record =  "server %s %s weight %s maxconn %s" %(server, server, weight, maxconn)

        if  record in FetchResultList:
            import shutil
            shutil.copy("ha.conf","new.conf")

        else:

            FetchResultList.append(record)
            Flage = False
            with open("ha.conf","r",encoding="utf-8") as old, open("new.conf","w",encoding="utf-8") as new:

                for line in old:
                    if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                        Flage = True
                        new.write(line)
                        for recordline in FetchResultList:
                            new.write(" " * 8  + recordline + "\n")
                        continue

                    if line.strip().startswith("backend") and Flage:
                        new.write(line)
                        Flage = False
                        continue

                    if not Flage:
                    # if not Flage and line.strip():
                        new.write(line)
def Del():
    pass


def Main():
    '''
    主函数


    :return:
    '''
    Select = input("1. Fetch. \n2. Add. \n3. Del. \nNum > ")

    if Select == "1":
        Backend = input("Input record:")
        Result = Fetch(Backend)
        print(Result)

    elif Select == "2":
        # BackendRecoed = input("Input a backend recode dic.> ")
        BackendRecoed = '{"backend":"buy.oldboy.org","record":{"server":"100.1.7.88","weight":"20","maxconn":"3000"}}'
        BackendRecoedDic = json.loads(BackendRecoed)
        Add(**BackendRecoedDic)

    elif Select == "3":
        pass

    else:
        print("Invalid data type, input a number(range 1-3)")

Main()