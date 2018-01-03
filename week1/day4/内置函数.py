#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei
'''
# callable 检测函数能不能被正常的调用执行。

def f1():
    pass

f2 = "abc"

print(callable(f1))
print(callable(f2))

'''



'''
# chr() 在ascci表里将十进制转换为字符
r = chr(65)
print(r)

# ord() 在ascci表里将字符转换为十进制
r2 = ord("a")
print(r2)
'''




'''
# 制作一个随机验证码，6位数的。
# 我要一个6位数的随机数，


import random

li = [] # 定义一个空得列表

for i in range(6): # 我需要一个6位数的随机码，所以呢，我就循环6次。
    temp_num = random.randrange(0,5)
    if temp_num == 2 or temp_num == 4 : # 这一步是保证了，所有的位置都是随机的。
        num = random.randrange(0,9) # 随机的一个数字
        li.append(str(num)) # 将数字转换为字符串写入到列表中，因为列表里的整数是不支持拼接的
    else:
        temp = random.randrange(65,90) # 65 - 90 为ascci码里的26个大写字母的十进制。
        c = chr(temp) # 在ascci码里将十进制转换为字符
        li.append(c) # 将字符追加到列表里。
result = "".join(li) # 对列表里的元素进行拼接，就得到了我们要的结果。
print(result)
'''


'''
s = 'print("hellow , 树先生！")'
# compile将字符串转换为pYthon代码
r = compile(s,"<string>","exec")

# exec() 执行python代码； 接收：代码或字符串，比eval功能多，没有返回值。
exec(r)
# eval(r)


# 执行表达式，并且获取结果。接收执行含有表达式的字符串，并且有返回值。
s = "8*8"
r =  eval(s)
print(r)



# dir() 快速查看对象提供了那些功能。
# print(dir(dict)



# 可以用于计算分页，共100行，每页10行，需要多少页？
r = divmod(100,10) # 返回的是一个元组。
# r1, r2  = divmod(100,10) #
print(r)



# 反射
delattr()
getattr()



# isinstance() 判断对象是否是某个类的实例。
s = "hehe"
r = isinstance(s,dict)
print(r)
'''


'''
# filter,map
def f1(a1):
    li = []
    for i in a1:
        if i > 22:
            li.append(i)
    return li

list = [11,22,33,44,55]
r = f1(list)
print(r)


#filter(函数,可以迭代的对象)
def f2(a2):
    if a2>22:
        return True

li = [11,22,33,44,55]


# 原理
# filter内部，循环第二个参数，将第二个参数放到函数的内部进行执行,如果符合条件
# return True  同时将值返回，不符合条件return False  抛弃这个值。

result = []
for item in 第二个参数：
    if True:
        追加item到result列表里
return result

# 方法一
r = filter(f2, li)
print(list(r))

# 方法二
r2 = filter(lambda args: args > 22, li)
print(list(r2))




# map函数
# 作用：对批量的数据做相同的操作，让代码更少，实现跟多的功能。

# 要求： 列表里的每个元素，都加上100

# 根据以前的知识来做的方法。

li = [11,22,33,44,55]

def f1(args):
    result = []

    for i in args:
        result.append(i+100)
    return  result

r = f1(li)
print(r)

# map(函数，可以迭代的对象（可以for循环的东西)

# 方法一
def f2(a2):
    return a2 + 100


r2 = map(f2, li)
print(list(r2))

# 方法二
r3 = map(lambda a3: a3+ 100, li)
print(list(r3))


# locals() 显示局部变量
# globals() 显示的是全局变量

NAME = "wangfei"

def show():
    a = 123
    b = 456

    print(locals())
    print(globals())

show()



# hash() 显示hash值
s = "wangfei"
print(hash(s))


# id() 查看在内存中的地址。
print(id(s))

# python3里面是按字符进行读取的，python2.7里面是按照字节进行读取的。

# 按照字符读取，是2 。 一个汉字等于3个字节。
s = "王飞"
print(len(s))

# 按照字节读取，是6
s = bytes(s,encoding="utf8")
print(len(s))

# max min sum 求最大值  最小值   和

# reversed 翻转
li = [1,2,3,4]
reversed(li)

# round() 四舍五入
r = round(12.6)
print(r)

# slice() 步长
s = '123456789'
# 和下面的功能是一样的。
print(s[0:8:3])


# sorted 排序
li = [3,2,1,5,67,9]
print(li.sort())

print(sorted(li))


# zip() 将列表中得元素混合到一块。
# 怎么组合的？ 呵呵，请执行一遍。
l1 = ["hellow",11,22,33]
l2 = ["my",11,22,33]
l3 = ["girl",11,22,33]

r = zip(l1,l2,l3)
result = " ".join(list(r)[0])
print(result)
'''


# 装饰器
