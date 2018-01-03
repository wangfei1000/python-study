#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

age = 25
count = 0
for i in range(10):  # range循环从 10，从0开始到9
    if count < 3:
        print ("counter:", count + 1)
        guess_num = int(input("input your guess num: "))
        if guess_num == age:
            print ("congratulations. you got it")
            break   # 跳出整个loop
        elif guess_num > age:
            print ("Think small...")
        else:
            print ("Think big...")
    else:
        continue_confirm = input("Do you want to continue ? y/n  ")
        if continue_confirm == "y":
            count = 0
            continue
        else:
            print("bye....")
            break
    count += 1