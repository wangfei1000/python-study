#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei


# 阶乘

def func(num):
    if num == 1 :
        return 1
    print(num)
    return num * func(num - 1)
            7*(6*(5*(4*(3*(2*(1))))))

number =  7
print(func(number))

