#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

import json
import os

# 定义一个菜单，采用了列表结合元组的方式。
ShoppingList = [
    ("三星",998),
    ("小米",1000),
    ("Sony",2399),
    ("iphone",4799),
    ("mac air",8000),
    ("mac pro",9000),
    ("coffee",30),
    ("tesla",1000000),
    ("bike",800)
]

# 判断登入的用户是否正确
User = input("User: ")
if User == "wangfei":
    Password = input("password: ")
    if Password == "5201314mn":
        print("logging in...")
    else:
        exit("user or password invalid.")
else:
    exit("user or password invalid.")


# 判断用户是不是第一次输入工资，ps:检查存放用户工资的文件是否存在，如果在的话就取出来。
if os.path.exists("salary.json") is True:
    SalaryFile = open("Salary.json", encoding='utf-8')
    Salary = json.load(SalaryFile)

else:
    while True:
        Salary = input("Salary: ")
        if Salary.isdigit():  # 输入的工资类型，是否正确。
            Salary = int(Salary)
            break
        else:
            print("Data type is invaild.")
            continue

# 查看购物车文件是否存在，如果存在就取出来。
if os.path.exists("ShopCar.json") is True:
    ShopCarFile = open("ShopCar.json", encoding='utf-8')
    ShopCar = json.load(ShopCarFile)
else:
    ShopCar = []

# 大循环
while True:
    # 打印物品列表
    print("list".center(40,"*"))
    for Product in enumerate(ShoppingList):
        # print(Product)
        ProductId = Product[0]
        ProductNa = Product[1][0]
        ProductPr = Product[1][1]
        print("%d. %s %d元" %(ProductId,ProductNa,ProductPr))
    UserChoice = input("[q=quit,c=check]what dou you want to buy? ")
    if UserChoice == "q": # 如果是退出就保存用户的工资信息和购买的物品信息。
        print("""
message:
++++++++++++++++++++++++++++++++++++++++++++++++
shop car: %s
spare money : [%d] 元
++++++++++++++++++++++++++++++++++++++++++++++++
bye...
        """ %(ShopCar, Salary))
        # 保存剩余工资到文件中
        JsSalary = json.dumps(Salary)
        fileSalary = open('Salary.json', 'w')
        fileSalary.write(JsSalary)
        fileSalary.close()
        # 保存购物信息
        jsShaopCar = json.dumps(ShopCar)
        fileCar = open('ShopCar.json', 'w')
        fileCar.write(jsShaopCar)
        fileCar.close()

        break
    # 如果输入c就打印购物车里的物品和用户的工资信息。
    elif UserChoice == "c":
        print("""
message:
++++++++++++++++++++++++++++++++++++++++++++++++++++++
shop car: %s
salary: %d 元
++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """ %(ShopCar, Salary))
    elif UserChoice.isdigit():  # 判断用户输入的是否是数字正确。
        UserChoice = int(UserChoice)
        if UserChoice <= len(ShoppingList): # 判断用户输入的数字是否在范围之内。
            UserProductProvice = ShoppingList[UserChoice][1]
            if UserProductProvice <= Salary:  # 判断用户的工资是否够买下这个商品
                UserProduct = ShoppingList[UserChoice][0]
                ShopCar.append(UserProduct)
                Salary -= UserProductProvice
                print("---".center(50,"-"))
                print("Product: [\033[41;1m%s,%d\033[0m] ,into you're shop car. " %(UserProduct,UserProductProvice))
                print("salary: [\033[41;1m%d\033[0m]" %(Salary))
            else:
                Deposit = input("Don't have enough money, to deposit? [y]/[n] ")
                # 充值系统
                if Deposit  == "y":
                    DepositMoney = input("deposit money > ")
                    if DepositMoney.isdigit(): # 判断输入的是否是数字
                        DepositMoney = int(DepositMoney)
                        Salary += DepositMoney
                        print("Depoist: [%d], Total salary : [%d]" %(DepositMoney, Salary))
                        continue
                    else:
                        print("deposit money failed.")
                        continue
                elif Deposit == "n":
                    print("Only to buy less than [%d] goods." %Salary)
                    continue
                else:
                    continue
        else:
            print("Invalid data type.")
            continue
    else:
        print("Invalid data type.")
        continue