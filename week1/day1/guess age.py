#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

age = 25

guess_num = int(input("input your guess num: "))

if guess_num == age:
    print ("congratulations. you got it")
elif guess_num > age:
    print ("Think small...")
else:
    print ("Think big...")
