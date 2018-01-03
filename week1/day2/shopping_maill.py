#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

salary = input("Input your salar: ")
if salary.isdigit():
    salary=int(salary)
else:
    exit("invaild data type")

welcome_msg = 'Welcome to wangfei shopping mall'.center(50,'-')
print(welcome_msg)
product_list = [
    ("iphone",5888),
    ("mac air",8000),
    ("mac pro",9000),
    ("xiaomi 2",19.9),
    ("coffee",30),
    ("tesla",1000000),
    ("bike",800),
]

shop_car = []

exit_flage= False
while exit_flage is not True:
    print("product list".center(50,'-'))
    #for product_item in product_list:
    #    p_name,p_price= product_item
    for item in enumerate(product_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print (index,".",p_name,p_price)

    user_choice = input("[q=quit,c=check]what dou you want to buy?")
 ("End".center(40,'-'))
            print("you are balance is \033[41;1m[%s]\033[0m" %salary)    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary: # 买得起
                shop_car.append(p_item[0]) # 放入购物车
                salary -= p_item[1] # 减钱
                print ("Added [%s] into shop car，you current balance is \033[31m;1m[%s]\033[0m" %
                       (p_item, salary))
            else:
                print ("you are balance is [%s], cannot afford this..." %(salary))
    else:
        if user_choice == 'q' or user_choice == 'quit':
            print("purchased products as blow".center(50,'-'))
            for item in shop_car:
                print(item)
            print ("End".center(40,'-'))
            print("you are balance is [%s]" %salary)
            exit_flage = True
        elif user_choice == 'c' or user_choice == 'check':
            print("purchased products as below".center(50,'*'))
            for item in shop_car:
                print(item)
            print