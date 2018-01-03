#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei
'''
 编写一个函数需要注意的规范。
    1. def 申明为函数。
    2. global申明为全局变量。
    3. 要写注释。
    4. 全局变量全大写（行业规范）。
    5. 函数之间用2行隔开。
'''

import os

def logging(username, password):
    '''
    用户登录验证模块。
    :param username: 表示用户输入的用户名。
    :param password: 表示用户输入的密码
    :return: 输入的用户名和密码错误返回False ，输入正确返回True
    '''
    if os.path.exists("db") is False:
        print("db file not found.")
        return False

    f = open("db","r")
    for line in f:
        line_list = line.strip().split("|")
        if line_list[0] == username and line_list[1] == password:
            return True
    print("The user:[%s] not found." %username)
    return False


def register(*args):
    '''
    用户注册模块。
    :param username: 表示用户输入的用户名
    :param password: 表示用户输入的密码
    :return: 注册成功返回True,注册失败返回False
    '''

    username = args[0]
    password = args[1]

    # 假如db文件不存在，就新建这个文件
    if os.path.exists("db") is False:
        with open("db","w",encoding="utf-8") as f :
        # f = open("db", "w")
            temp = "\n" + username + "|" + password
            f.write(temp)
            f.close()
            return True

    # 假如注册的用户已经存在了，就return False

    with open( "db","r",encoding="utf-8") as f:
    # f = open("db","r")
        for line in f:
            line_list = line.strip().split("|")
            if line_list[0] == username :
                print("The user:[%s] is exists." %username)
                return False

    # 如新注册的用户不存在就直接写入即可。
    f = open("db", "a")
    temp = "\n" + username + "|" + password
    f.write(temp)
    f.close()
    return  True


def main():
    '''
    主函数模块，输入用户名和密码。
    '''
    select_id = input("1 logging \n2 register\n> ")
    # 判断用户输入的是不是数字。
    if select_id.isdigit():
        select_id = int(select_id)
    else:
        print("input int.")
        return False

    # 对用户输入的数字进行判断，看用户想做什么。
    if select_id == 1:
        user = input("User：> ")
        pwd = input("Passowrd：> ")
        Msg = [user,pwd]
        Result = logging(*Msg)
        if Result == True:
            print("logging in....")
        else:
            print("logging error....")
    elif select_id == 2:
        user = input("User：> ")
        pwd = input("Passowrd：> ")
        Result = register(user, pwd)
        if Result == True:
            print("register ok.")
        else:
            print("register Failed.")
    else:
        print("input error.")

main()