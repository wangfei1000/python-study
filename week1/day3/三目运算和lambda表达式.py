#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei


if 1 == 1 :
    name = "hehe"
else:
    name = "heheda"

# 三元运算, 三目运算
# 上面的简单if语句就可以使用三元运算来写。
print("hehe") if 1 == 1 else name == print("heheda")

# lambda表达式
def f1(a1):
    return a1 + 100

# 使用lambda表达式后的效果，就和上面的是一样的。
f2 = lambda a2: a2 + 100

r1 = f1(10)
r2 = f2(9)
print(r1)
print(r2)