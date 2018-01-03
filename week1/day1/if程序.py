#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

# user = "wangfei"
# password = "123456"
#
# username = input("Pls input you are name ")
# passwd = input("Pls input password ")
#
# if user == username:
#     #print ("username is correct.")
#     if password == passwd:
#         print ("welcom login.....")
#     else:
#         print ("password is invalid.....")
# else:
#     print ("username is invalid.")



User = 'wangfei'
Passwd = "abc"
Count = 0

while True:
    if Count < 3:
        GuessUser = input("Name:> ")
        GuessPasswd =  input("Passwd:> ")

        if User == GuessUser:
            if GuessPasswd == Passwd:
                print("login in....")
                break
            else:
                print(" passwd is error.")
        else:
            print("user  error.")
    else:
        print("no change...")
        break

    Count +=1