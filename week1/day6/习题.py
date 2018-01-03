#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Authour wangfei
'''
计算器2.7 源码
http://www.cnblogs.com/wupeiqi/articles/4949995.html

'''

import json

def cal(exp):
    return exp


def process():
    import re
    text = '(5*6-1)+8+(5*6-3)*12+(6-(((5*6-4)+5*6-1)*5*6-2)/77+2)*(3-7)+8'
    while True:
        regex = re.compile('\(([^\(\)]*)\)')
        obj = regex.split(text, 1)
        rcal = obj[1]

        # 新的表达式,已经用第一个括号的值,替换第一个括号的值.
        text = '(5*6-1)+8+(5*6-3)*12+(6-(((5*6-4)+5*6-1)*5*6-2)/77+2)*(3-7)+8'
        '''
                问题:
                    2\ 怎么更新原计算公式?  使用替换的方式,原来的表达式经过切割了,可以进行拼接.
                    3\ 怎么返回这个计算的总结果?对+-*/做处理,然后去做. 先解决掉所有的括号(括号里面也有乘除),最后进行一个加减.
                    4\ 如何计算加减乘除?(写对应的运算处理函数.)
        '''

if __name__ == '__main__':
    process()