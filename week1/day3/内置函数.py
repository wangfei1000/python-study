#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei

# ############################# 内置参数 ########################################

# 取绝对值
n = abs(-2)
print(n)

# False 假的: [] () {} "" None 0
# True 真的: 非空的列表，元组，字典，非0的数字，非空的字符串。
print(bool(None))

# all() 接收所有可以被迭代的东西，所有的为真才为真。
list = [0,0,0,0,0,1]
n = all(list)
print(n)

# any() ,只要有真，就是真的。
list = [0,1]
n = any(list)
print(n)


# ascill() 自动执行对象的_repr_方法   ;知道就行了。
# bin() # 接收十进制，转换为二进制。
print(bin(10))
# oct() # 接收十进制，转换为八进制。
print(oct(10))
# hex() # 接收十进制，转换为十六进制。
print(hex(10))

# bool() 布尔值  ;这个咱就不解释了吧？


# 字符串转换为字节类型需要用bytes()  ,记得加上encoding
# utf-8 一个汉字3个字节。
# gbk 一个汉字2个字节。
# 一个字节等于8位。

s = "王飞"
n = bytes(s,encoding="utf-8")
print(n)
n = bytes(s,encoding="gbk")
print(n)


# 字节转换为字符串，用str(); 用什么编码转换的，就用什么编码在转换回来。
name = "王飞"
# 用utf-8编码进行转换。
r = bytes(name,encoding='utf-8')
print(r)

# 现在再用utf-8编码转换回去。
r2 = str(r,encoding='utf-8')
print(r2)  # 哈哈 是不是好牛逼，现在又转换回来了！



## 文件操作。
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

'''
r+ 读写模式，如果文件不存在就会报错。
a+ 读写模式，在a的功能追加功能上多了r的功能。
w+ 读写模式，在w只写的功能上多了r的功能。


'''


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
'''
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