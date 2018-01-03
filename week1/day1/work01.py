#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

import os

User = "wangfei"
Password = "123456"
Count = 1
ErrorPassNum = 3
ErrorUserFile = "/tmp/erroruser.txt"



for i in range(10):
    print("counts:", Count)
    GuessName = input("Pls input you are name. > ")
    GuessPassword = input("Pls input you are password. > ")

    if os.path.exists(ErrorUserFile):
        ErrorUser = open("/tmp/erroruser.txt", "r")
        if ErrorUser.read() == GuessName:
            print("Sorry, user:%s is locked." %GuessName)
            break

    if GuessName == User:
        if GuessPassword == Password:
            print("welcome login.")
            break
        else:
            print("Sorry, user or Password invlid.")
            ErrorPassNum -= 1
            print("chance:", ErrorPassNum)
            # error password num.
            if ErrorPassNum == 0:
                ErrorUserFile = open('/tmp/erroruser.txt', 'w')
                ErrorUserFile.write(GuessName)
                ErrorUserFile.close()
                break
    else:
        if Count == 3:
            print ("too many attempts...bye ....")
            break
        print("Sorry, User or password invlid.")
    # error user num.
    Count += 1
~