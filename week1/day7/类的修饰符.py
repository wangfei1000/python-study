#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

##  成员修饰符 ： 公有的，私有的。
# 公有的字段：可以在类里面和外面进行调用的。
# 私有的字段：只有类本身可以访问  __"字段名"
'''
# 公有字段
class Foo:

    def __init__(self,name):
        self.name = name # 公有字段

    def f1(self):
        print(self.name)

obj = Foo("wf")
r = obj.name # 在外面进行调用 可以
print(r)
obj.f1() # 在里面进行调用 也可以
'''

# 私有字段
'''
1.私有字段只能在类里面进行调用，不能在外面进行调用。
2.私有字段也也不能通过继承的方式来调用。
'''

'''
class Foo:
    __cc = "static_pri" # 静态私有字段
    def __init__(self,name):
        self.__name = name  # 这个就叫做私有字段，也叫做普通私有字段 ； 普通字段前面加2个__ 就变成私有的了

    def f1(self):
        print(self.__name)

    def f2(self): # 静态私有字段也是只支持内部调用
        print(Foo.__cc)

    @staticmethod  # 但是可通过静态方法的形式来进行外部调用。
    def f3():
        print(Foo.__cc)

# obj = Foo("wf")
# obj.f1()  # 私有字段就只能在里面用
# obj.f2() # 静态私有字段 内部调用
# Foo.f3() # 静态私有字段，间接内部调用

# r = obj.name  # 在外面调用 就会失败。
# print(r)



## 私有字段继承问题
class bar(Foo):

    def f5(self):
        print(self.__name)

obj = bar("wf")   # 私有字段通过继承也是不能调用的。
obj.f5()
'''

# 私有方法
class Foo:
    def __init__(self,name):
        self.name = name

    def __show(self): # 普通方法，
        print(self.name)

    @staticmethod  # 静态私有方法
    def __f1():
        print("static method")

    @classmethod
    def __f0(cls):
        print(cls)

    def f2(self):
        print(Foo.__f1())

    def f3(self):
        print(obj.__show())

    def f4(self):
        print(Foo.__f0())



obj = Foo("wangfei")
# Foo.__f1() # 外面调用静态私有方法。
# obj.f2() # 静态私有方法只能内部调用

# obj.__show() # 私有普通方法 ，外部调用失败。
obj.f3() #  私有的普通方法，也只能内部调用。

# obj.__f0() # 类方法，不用外面调用
# obj.f4() # 只能内部调用

