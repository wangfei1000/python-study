#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei
'''
进度条  这就是一个进度条。。。。。。

http://www.cnblogs.com/wupeiqi/articles/5501365.html
'''

import sys
import time


def view_bar(num, total):
    '''
    \r' 回车，回到当前行的行首，而不会换到下一行，如果接着输出的话，本行以前的内容会被逐一覆盖；
    '\n' 换行，换到当前位置的下一行，而不会回到行首；
    '''


    rate = num/total
    rate_num = int(rate * 100)

    r = '\r%s> [ %d%% ]' % ("=" * num, rate_num) # \r回到当前行的首个位置。
    # print(r)
    sys.stdout.write(r)
    # sys.stdout.flush()


if __name__ == '__main__':
    for i in range(0, 101):
        # time.sleep(1)
        view_bar(i, 100)

# print()