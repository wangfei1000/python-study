#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

age = 25
for i in range(10):  # range循环从 10，从0开始到9
    if i < 3:
        guess_num = int(input("input your guess num: "))
        if guess_num == age:
            print ("congratulations. you got it")
            break   # 跳出整个loop
        elif guess_num > age:
            print ("Think small...")
        else:
            print ("Think big...")
    else:

        print ("too many attempts...bye ....")
        break