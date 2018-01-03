#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

# 集合是无序，不重复的。
# 集合的特点：无序的，不重复，可以嵌套

#{1,2,3,4,5} 集合
{"name":"wangfei", "age":18} 这就是一个字典


# a创建一个集合，方法有3种
# 方法一
s1 = {"123", "456"}
print(type(s1))
# 方法二
s2 = set()  # 创建一个空的集合
# 方法三
s3 = set(["a", "b", "c", "d","a","c"])  # 原理：list调用__init__，然后进行一个for循环
print(s3)

# 将元组转换为列表
letter = ("a", "b", "c", "d")
print (list(letter))


# b 功能(特性就是不重复)
s = set()
s.add("123")
s.add("123")
s.add("123")
print(s)

s1 = {11,22,33}
s2 = {22,33,44}
s3 = s1.difference(s2) # a中存在，b中不存在
print(s3)

s4 = s1.symmetric_difference(s2) # 对称差积；a中存在b中不存在的和b中存在a中不存在的
print(s4)

s1.difference_update(s2) # 将a中存在的，b中不存在的值，更新到a中去。
print(s1)


s1.symmetric_difference_update(s2)
print(s1)

s1.discard(11) # 移除集合中的值，有就移除，没有也不报错
print(s1)

s1.remove(111) # 移除集合中的值，有就移除，没有就报错
print(s1)

ret = s1.pop() # 集合是无序的，将移除的值赋予ret然后我打印出来，于是我就知道了我移除的值是那一个。pop移除的值是随机的。
print(s1)
print(ret)

s5 = s1.intersection(s2) # 求s1和s2的交集
print(s5)

s1.intersection_update(s2) # 将s1和s2的交集更新到s1中
print(s1)

s1.union(s2) # 求s1和s2的并集
print(s1)

# li = [5,6,7,8,9]
# li = (5,6,7,8,9)
# li = "wangfei"
# for i in "wangfei":
#     s1.update(i) # update可以接受一个被迭代(for 循环)的东西。

# s1.update(li)
# print(s1)


# 内存槽位
# 要求：1、删除那几个槽位？2、更新那几个槽位？3、增加哪几个槽位？

old_dic = {
    "#1":8,
    "#2":4,
    "#4":2
}

new_dic = {
    "#1":4,
    "#2":4,
    "#3":2
}

old_set = set(old_dic.keys())
new_set = set(new_dic.keys())

# 1、 删除槽位 ,a里存在的，b里不存在的
del_set =old_set.difference(new_set)
print(del_set)

# 2、更新槽位 ,a里有的,b里也有的。求得是交集
update_set = old_set.intersection(new_set)
print(update_set)

# 3、增加槽位。新的槽位里有，但是旧的槽位里面没有的。
add_set = new_set.difference(old_set)
print(add_set)