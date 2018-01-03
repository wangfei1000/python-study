#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

import os

# province_list = []

province_file = open("/Users/feiwang/Downloads/province/province.txt","r")
province = province_file.read().split("\n")
province_file.close()

print("menu".center(50,"-"))
print("ID  省份" )
for index,key in enumerate(province):
    print([index],key)

sel_province = input("[q=quit]  pls input you want to province [id].")
if sel_province == "q" or sel_province == "quit":
    print("bye")
elif sel_province == "0":
    city_file = open("/Users/feiwang/Downloads/province/city/beijing/beijing.txt","r")
    city = city_file.read().split("\n")
    print(city)
    # city_file.close()
    # print("city".center(50,"_"))
    # for index,key in enumerate(city):
    #     print([index],key)