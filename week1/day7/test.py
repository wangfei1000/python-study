#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

# # 静态字段 & 普通字段
#
# class Foo:
#     name = "aa" # 静态字段： 更加的节省内存。代码加载时已经创建了。
#     # print(name)
#
#     def __init__(self):
#         self.nameb = "bb" # 普通字段 ； 保存在内存里的。
#
#     def show(self):
#         print(self.nameb)
#
#
# obj = Foo()
# # print(obj.show()) # 由对象来进行调用。
# # Foo.name # 静态字段由类来调用。
#
# # 注意事项，静态字段和普通字段需要分开访问。防止以后pyhon规则发生改变，代码需要重写。
#
#
# ### 方法
# class Foo:
#     name = "aa"
#     # print(name)
#
#     def __init__(self):
#         self.nameb = "bb"
#
#     def show(self): #普通方法
#         print(self.nameb)
#
#     # 静态方法
#     @staticmethod  # 上面加了一个装饰器
#     def show2(): # 静态方法  # 这里没有self  # 由类来直接调用
#         print("aaa")
#
#     # 静态方法和可以通过访问普通方法的形式去访问的。
#
#     # 类方法   # 至少有一个cls参数，返回类的名字。
#     @classmethod
#     def f2(cls,age):
#         print(cls,age)
#
#
# #
# obj = Foo()
# obj.show2()
# Foo.f2(12





# 属性
# 具有方法的写作形式，具有字段的访问形式。
# class Pager:
#
#     def __init__(self,count):
#         self.count = count
#
#     def all_pager(self):
#         a1,a2 = divmod(self.count,10)
#         if a2 == 0:
#             return  a1
#         else:
#             return a1 + 1
#
#     @property
#     def all_pager2(self):
#         a1, a2 = divmod(self.count, 10)
#         if a2 == 0:
#             return a1
#         else:
#             return a1 + 1
#
# obj = Pager(100)
# print(obj.all_pager())
# print(obj.all_pager2) # look  我通过属性来访问了， 是不是和访问字段的方法一样呢？

# 删除属性 修改属性

# class Pager:
#
#     def __init__(self,count):
#         self.count = count
#
#     def all_pager(self):
#         a1,a2 = divmod(self.count,10)
#         if a2 == 0:
#             return  a1
#         else:
#             return a1 + 1
#
#     @property
#     def all_pager2(self):
#         a1, a2 = divmod(self.count, 10)
#         if a2 == 0:
#             return a1
#         else:
#             return a1 + 1
#
#     # 修改属性
#     @all_pager2.setter
#     def all_pager2(self,values):
#         print(values)
#
#     # 修改属性
#     @all_pager2.deleter
#     def all_pager2(self):
#         print("I want to del " )
#
# obj = Pager(100)
# print(obj.all_pager())
# print(obj.all_pager2) # look  我通过属性来访问了， 是不是和访问字段的方法一样呢？
# obj.all_pager2 = 200
# del obj.all_pager2 # 属性拥有方法的写作形式，字段的访问形式。

#

# 属性的形式
class Foo:

    def f1(self):
        print("111111")

    def f2(self,values):
        print(values)

    def f3(self):
        print("33333")


    foo = property(fget=f1,fset=f2,fdel=f3)



obj = Foo()
# get
r = obj.foo
obj.foo = "aa"
del obj.foo