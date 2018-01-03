#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

# abs()
'''
求绝对值

print(abs(-10))
'''

# all()
'''
所有的值为真，结果为True，只要有一个假的，结果就为False

False 假的: [] () {} "" None 0

True 真的: 非空的列表，元组，字典，非0的数字，非空的字符串。

List1 = [1,2,3,4]
List2 = [0,1,2,3]

print(all(List1))
print(all(List2))
'''

# any()
'''
只要有一个为真的，及时真

List2 = [0,1,2,3]
print(any(List2))
'''


# bin()
'''
接收十进制，转换为二进制。

Num = 10
print(bin(Num))
'''

# bool()
'''
查看布尔值
举个列子：
True or False  = True
True or True = True
True and False = Flase
True and True = True
not True = False
not False = True

List = [] # 空的列表是假的
List2 = [1,2,3] # 非空的列表是真的
r1 = bool(List)
r2 = bool(List2)
print(r1)
print(r2)
'''

# bytes()
'''
字符串转换为字节类型需要用bytes()  ,记得加上encoding

补充知识：
一个汉字
    使用utf-8编码是3个字节
    使用gbk编码是2个字节
1字节  = 8位


Name = "学"
temp = bytes(Name,encoding="utf-8")
temp2 = bytes(Name,encoding="gbk")
# TempStr = bytes
print(type(temp))
# utf8编码3个字节
print(temp)
# gbk编码2个字节
print(temp2)
'''

# str()
'''
转换为字符串类型

list = [1,2,3]
Str = str(list)
print(type(Str))

Name = "学"
# 用什么编码打开的，转换回去也用这个编码
temp = bytes(Name,encoding="utf-8")
print(str(temp,encoding="utf-8"))
'''

# chr()
'''
在asscia码表里，将接收到的字符串转换为对应的数字

Num = 65
print(chr(Num))
'''

# ord()
'''
将字符串转换为十进制 ，ascia码表里对应的数字。

Lettr = "A"
print(ord(Lettr))
'''

# compile()
'''
将字符串转换为pyhon代码


s = 'print("hellow")'
Con = compile(s,'<string>','exec')
print(Con)
'''

# exec()
'''
接收代码或字符串，比eval功能多，没有返回值。
执行pyhon代码，没有返回值。

s = 'print("hellow")'
Con = compile(s,'<string>','eval')
mut = '8*8'
# 执行python代码
exec(Con)
# 执行字符串
exec(s)
# 没有返回值？
r = exec(mut)
print(r)
'''

# eval()
'''
执行含有表达式的字符串，有返回值

# mut = '8*8'
mut = "print('hellow')"

r = eval(mut)
print(r)
'''

# delattr()
'''
反射
# 还没有学习到
'''

# dict()
'''
转换含有键值对的列表，字符串为字典。

Dic = dict(one=1, two=2)
print(Dic)
Dic2 = dict([['two', 2], ['one', 1]])
print(Dic2)
'''

# dir()
'''
快速查看对象提供了那些功能。

print(dir(dict))
'''

# divmod()
'''
用于计算分页，如总共有100行，每10行一页，共计多少行。

# Result = divmod(100,10)
ResultTocal,Result = divmod(100,10)
# print(Result)
print(ResultTocal,Result)
'''


# enumerate()
'''
显示list\tup\set下标

List = [0,1,2,3,4,5]
# List = (0,1,2,3,4,5)
for i in enumerate(List):
    # print(i)
    Index = i[0]
    Num = i[1]
    print(Index,Num)
'''

# map()
'''
作用：
    可以迭代的对象（可以for循环的东西)
    对批量的数据做相同的操作。就可以用这个python再带的的内部模块map来做，方便，让代码边变的更加的简洁。
    当然你也可以不用这个模块来做。

# 要求：对这个列表内部的元素全部加上100
# 自己写函数来做，需要很多的代码来完成。
LIST = [11,22,33]
def f1(a1):
    Li = []
    for i in LIST:
        Li.append(i+100)
    return Li

r = f1(LIST)
print(r)

# 使用内置函数map来做
def f2(a2):
    return a2 + 100
r = map(f2,LIST)
print(list(r))

# lambda 表达式
r2 = map(lambda a2: a2 + 100, LIST)
print(list(r2))
'''

# filter()
'''
内部，循环第二个参数，将第二个参数放到函数的内部进行执行,如果符合条件
return True  同时将值返回，不符合条件return False  抛弃这个值。


# 判断下面列表中大于20的数字
List = [11,22,33,44,55]

# 老方法
def f1(a1):
    Li =[]
    for i in a1:
        if i > 20:
            Li.append(i)
    return Li

r = f1(List)
print(r)

# 使用filter
def f2(a2):
    if a2 > 20:
        return True
r2 = filter(f2, List)
print(list(r2))

# 使用lambda表达式
r3 = filter(lambda a3:a3 > 20, List)
print(list(r3))
'''


# float()
'''
转换含有小数的数字



num = 1.33
num2 =  2
print(float(num))
print(float(num2))
'''

# help()
'''
查看帮助


print(help(dir))
'''

# hex()
'''
接收十进制转换为16进制

Num = 10
print(hex(Num))
'''

# id()
'''
查看在内存中的地址。

print(id('s'))
'''

# input()
'''
接收用户输入的参数

Name = input("Name: ")
print(Name)
'''

# int()
'''
接收数字的字符串，转换类型为整数型

Num = "123"
print(type(Num))
NumInt = int(Num)
print(type(NumInt))
'''

# isinstance()
'''
检测对象是否是某个类的实例。


Str = "hehe"
print(isinstance(Str,str))
'''

# len()
'''
检查字符串的长度

Name = "pyhon"
print(len(Name))
'''

# list()
'''
转换类型为list，原理是对要转换的东西做个for循环，追加到列表中

Tup = (1,2,3,4,5,6)
print(type(Tup))
List = list(Tup)
print(type(List))
'''

# locals()
# globals()
'''
 locals()
显示所有的局部变量

globals()
显示所有的全局变量

NAME = "Pyhon"

def f1():
    Name = "I like python"
    print(locals())
    print(globals())

f1()
'''

# max()
'''
显示可以迭代的对象中最大的元素

List = [1,2,3,4,5]
Letter = ["a","c","b"]
print(max(List))
print(max(Letter))
'''

# min()
'''
显示可以迭代的对象中最小的元素

List = [1,2,3,4,5]
Letter = ["a","c","b"]
print(min(List))
print(min(Letter))
print(min(5,4,2,1,0))
'''


# oct()
'''
转换十进制为八进制

Num = 10
print(oct(Num))
'''

# open()

'''
打开文件

f = open("db.conf","r",encoding="utf-8")
f.read()

# 1、打开文件的正确姿势。
# open()
f = open("db", "r") # 只读
f2 = open("db", "rb") # 以二进制只读方式读
data = f.read()
data2 = f2.read()
print(data,type(data))
print(data2,type(data2))


f = open("db", "a") # 追加模式
f.write("hehe")
f.close()

# 文件用字节方式打开的，那么写入的时候就要把字符串转换为字节再存入到里面。
f = open("db", "ab")
f.write(bytes("王飞",encoding= "utf-8"))
f.close()

name = "王飞"
temp = bytes(name,encoding="utf-8")
print(temp)
f = open("db","a",encoding="utf-8") # 以utf8的编码形式打开。
f.write("王飞")
f.close()

f = open("db", "w") # 只写（写之前，清空文件）
f = open("db", "x") #　如果文件存在，报错；如果不存在，创建文件并只写内容

# r+ a+ w+ 都是可读可写模式，但是互相之间还是有差别的。

# 如果打开的模式无b,则read 按照字符读取
f = open("db", "r+", encoding="utf-8")
data = f.read()

# seek永远是用 字节 的方式找位置的。
# tell 当前的指针所在的位置（字节）。
f.seek(f.tell()) # 定位到指定的字节的后面。

# 当前指针位置开始向后覆盖。
f.write("111")
f.close()



# 2、 操作文件

read()
无参数，读全部。
有参数：
    b, 读取字节
    无b,读取字符。
readable()
判断是否可读
f = open("db","w",encoding="utf8")
f.write("飞哥6666")
print(f.readable())
tell()
获取当前指针的位置。
seek()
将指针跳转到指定的位置。
write()
写数据;
    b 写字节
    无b 写入字符串
writable()
判读是否可写
f = open("db","w",encoding="utf8")
print(f.writable())
close()
关闭打开的文件
flush()
强制的将保存在内存中得数据保存到磁盘中。
f = open("db","r+",encoding="utf8")
f.write("飞哥6666")
f.flush()
input("are you kinde me ?")
f.close()
# readline()
每次仅读取一行
f.readline()
f.readline()
f = open("wd","r", encoding="utf-8")
for line in range(3) :
    print(f.readline())
# truncate()
截断，(根据指针的位置)。指针位置后面的都清空。
f = open("wd","r+", encoding="utf8")
f.seek(2)
f.truncate()
f.close()
# 3、关闭文件
# f.close()
with open('wd') as f:
     pass
# 打开多个文件,将文件1的内容写入到文件2中。
# 搞个for循环，从文件1读一行，写入到文件2中。
with open('wd',"r",encoding="utf-8") as f, open("wd2","w",encoding="utf8") as f2:
    times = 0
    for line in f:
        if times <= 9:
            f2.write(line)
            times += 1
        else:
            break
'''

# pow()
'''
计算立方
# 如2的3次方
print(pow(2,3))'''

# print()
'''
打印内容

print("呵呵哒")
'''

# range()
'''
取值范围

Num = range(0,9,2) # 0 - 9 每隔2个取一个
Num2 = range(0,9) # 取值范围是 0 - 9
print(Num)
for i in Num:
    print(i)

for i in Num2:
    print(i)
'''

# round()
'''
四舍五入

Num = 1.67
Num2 = 1.3
print(Num, Num2)
'''


# set()
'''
集合

集合是无序的，不重合的。

# 创建一个集合
S = set() # 创建一个空的集合
S2 = {1,2,3} # 创建一个集合
print(type(S))
print(type(S2))
'''

# sum()
'''
迭代一个含有数字的，并相加。


List = [1,2,3,0]
# Str = "123456"
print(sum(List))
'''

# tuple()
'''
元组

元组的值是不可以修改的

Tup = (1,2,3,4)
print(type(Tup))
print(Tup[0])

# 元组的值不可以被更改哦!
Tup[0] = 1
'''

# type()
'''
查看参数的类型


Str = "python"
Int = 100
List = [1,23]
Dic = {"k1":"v1","k2":"v2"}
Tup = (1,2,3,4)
Set = {1,2,3,4}

print(type(Str))
print(type(Int))
print(type(List))
print(type(Dic))
print(type(Tup))
print(type(Set))
'''

# zip()
'''
混合列表中的元素
1对1 混合

'''
List1 = ["helow",1,2,3,4]
List2 = ["python","b","c","d","e"]

Tem = zip(List1,List2)
ResultList = list(Tem)
LetterList = ResultList[0]
print(" ".join(LetterList))
