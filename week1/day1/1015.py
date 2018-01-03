#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei
#
# age = 29
# count = 0
#
# for i in range(10):
#     if count < 3:
#         guess_num = int(input("Pls input a num.... "))
#         if guess_num > age:
#             print ("Think small...")
#         elif guess_num < age:
#             print ("Think big.... ")
#         else:
#             print ("Congratulation!  you got it...")
#             break
#     else:
#         continue_result = input("Do you want to continue? y/n ")
#         if continue_result == "y":
#             count = 0
#             continue
#         else:
#             print ("bye.....")
#             break
#     count += 1
#
#     # 作业需求
#     # 1、流程图
#     # 2、readme

Age = 20
Count = 3
print("You can to guess three.")
for i in range(10):
    print("count:", Count)
    if Count > 0:
        GuessAge = int(input("Age:> "))
        if GuessAge > Age:
            print("think to small.")
        elif GuessAge < Age:
            print("think to big")
        elif GuessAge == Age:
            print("heheda")
            break
        else:
            print("Error")
    else:
        break
    Count -= 1

