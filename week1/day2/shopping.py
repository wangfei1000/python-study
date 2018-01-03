#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

exit_flage = False
shop_car = []
welcome_msg = " welcome to wangfei shopping mall "
product_list = [
    ("apple", 4),
    ("banana", 5),
    ("cherry", 6),
    ("watermelon", 7),
]
salary = input("Pls input you are salary.> ")
# 判断输入的金额是不是数字，如过是就转换为整数型的
if salary.isdigit():
    salary = int(salary)
else:
    exit("invalid data type.")

print (welcome_msg.center(100,"-"))

while exit_flage is False:   # 判断退出的标记是不是False如果不是就不执行了
    print ("fruit list".center(20,"*"))
    for item in enumerate(product_list): # 打印商品价格列表
        p_index= item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print (p_index,".",p_name, p_price)
    choice = input("[q=quit] or [c=check] Pls select you like fruit.> ")  # 让用户输入商品的序列号
    if choice.isdigit(): # 判断是不是数字
        choice = int(choice)
        if choice < len(product_list): # 判断输入的商品是不是在价格表内
            p_item = product_list[choice]



            if p_item[1] < salary: # 判断用户选择的商品价格是不是高于自己的工资
                shop_car.append(p_item[0]) # 添加到购物车里
                salary -= p_item[1] # 从工资里减掉购买商品的费用。
                print("you are shop car".center(50,"*"))
                print ("into [%s] to shop car, salary = [%s]" %(p_item, salary))
                print("End".center(50, "*"))
        else:
            print ("Sorry, you  not enought money.")
    else:
        if choice == "q" or choice == "quit":
            print ("you are shop car.".center(50,'*'))
            for item in shop_car:
                print(item)

            print ("current salarry : [%d]" %(salary))
            print ("bye".center(50,"*"))
            exit_flage = True
        elif choice == "c" or choice == "check":
            print ("you are shop car.".center(50,'*'))
            for item in shop_car:
                print(item)
            print("current salarry : [%d]" % (salary))
            print ("END".center(50,"*"))
