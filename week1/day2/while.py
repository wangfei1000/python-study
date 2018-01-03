#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei


count = 0
while True:  # 死循环
    count+= 1
    if count>50 and count<60: # 数字在大于50 小于60d的范围内，不打印。
        continue
    print("Forever...", count)
    if count == 100:
        print("haha ....good bye....")
        break
#
