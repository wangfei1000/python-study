#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

import os # 取出os模块

User = "zhansan"
Password = "5201314mn"
GuessNum = 3 # 允许用户名输入的错误次数
GuessErrorNum = 3 # 允许密码输入错误的次数
GuessTotal = 10 # 总共允许尝试的次数s
# ErrorUserFile = "D:\TEMP\erroruser.txt"
ErrorUserFile = "erroruser.txt"

for i in range(GuessTotal):
    print("剩余用户次数：[%d]" % (GuessNum))
    GuessUser = input("Pls input you are name.> ")
    if os.path.exists(ErrorUserFile):  # 判断存放锁定用户的文件在不在，如果在就取出来，进行判断。
        ErrorUser = open(ErrorUserFile,"r")
        ErrorUser.close()

        if ErrorUser.read() == GuessUser: # 判断输入的用户是不是锁定的用户
            print("user:[%s] has locked..." % (GuessUser))
            break

    GuessPassword = input("Pls input you are password.> ")
    if GuessUser == User:
        if GuessPassword == Password: # 用户名和密码输入正确，正常登录。
            exit("Welcome logging in...")
        else:
            print("user or password is invalid.")
            GuessErrorNum -=1  # 每次用户的密码输入错误GuessErrorNum就减去1
            print("剩余密码输入次数：[%s]" % (GuessErrorNum))
            if GuessErrorNum == 0: # 如果3次密码都输入错误，就锁定这个用户。
                ErrorUser  = open(ErrorUserFile,"w")
                ErrorUser.write(GuessUser)
                ErrorUser.close()
                exit("user:[%s] has locked..." %(GuessUser))
    else:
        GuessNum -= 1 # 每次用户输入错误Guessnum就减去1
        print("user is invalid.")
        if GuessNum == 0:
            exit("Too many attempts.")