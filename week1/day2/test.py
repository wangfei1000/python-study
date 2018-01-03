#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

name = {
    1860:{
        'name':'wf',
        'age':18,
        'addr':'hz'
    },
    1861:{
        'name':'lisi',
        'age':20,
        'addr':'nj'
    },
    1862:{
        'name':'zhangsan',
        'age':21,
        'addr':'wenzhou'
    }
}



name2 = {
    1860:{
        'name':'wangfeixiaoer',
        'age':1999,
        'addr':'Dingyuan111111',
        'mobile':'18600000',
    },
}


# name[1860]['shouji'] = '18606511326'
# print(name[1860])
# # del name[1860]['shouji']
# name[1860].pop('shouji')
# print(name[1860])

# print(name.setdefault(1860,{1861:{'a':1,"b":2}}))

# print(name[1860])
# name.update(name2)
# print(name[1860])


# for k,v in name.items():
#     print(k,v)


# for k  in name:
#     print(k,name[k])
#


# tup = \

#     name.items()
#
# print(tup)


# print(name[1860])

# print(name.items())
# for a,b in name.items():
#     print(a)
#
# for k in name:



# name = input("Name> ")
# name=name.strip()
# if 'wangfei' == name:
#     print("login..in ..")
# else:
#     print("error")



# name = "my name is {name}, i am {age} year old."
# # print(name.format(name = "wf",age = 18))
# msg = name.format(name = "hehe",age = 99)
# # print(msg)
#
#
# print(msg.center(40,"-"))



list = ['zhangsan',['boluo','apple', 'wangerma']]

# print(list)
#
# print(10 in list)
# print(list.count(1))
# print(list.index(9))
# print(list[1])

# if 9 in list:
#     print(list.count(9))
#     print(list.index(9))
#     print(list)

#
# print("数量：",list.count(9))
# for  num in list:
#     # print(type(num))
#     # print(numm)
# #     if num == 9:
# #         # print()
# #         print("位置:", list.index(num))
# #         # print()
#
#
# # for num in list:
# #     if num == 9:
# #         pos = list.index(num)
# #         print("pos 9 :", pos)
# #         list.pop(pos)
#
#
#
# # for i in range(4):
# #     # print(list.index(9))
# #     list[list.index(9)] = 9090
# # print(list)
#
#
# nlist = ['w','f','a','n','g','h']
# list.extend(nlist)
# print(list)
# print(list)
#
# list.reverse()
# print(list)


# list.pop(1)
# print(list)

# print(list.pop(2))

# list2 = list.copy()
# print('old'.center(20,'-'))
# print("list1:",list)
# print("list2:",list2)

#
# import copy
#
# list3  = copy.deepcopy(list)
# print(list3)
# list[1][0] = 'bl'
# print(list)
# print(list3)

nlist = ['w','f','a','n','g','h']
# print(len(nlist))
# print(len(nlist))


r = (1,2,3,4,5,6,7,8,9)
#
# print(r[0])
name = [1,2,3,4,5,6,7,8,9]
# print(name[4:8])
# name.insert(3,"three")
# print(name)
# name.remove("three")
# print(name.remove(1))
# print(name)
# name.append(10)
# print(name)
# del name[2:]
# print(name)
# del name
# print(name[0::2])

# name.index(1)
# print(name.index(9))
# print(len(name))
# # print()l
# for a,b in enumerate(name):
#     print(a,b)

# print(len(name))

#
# for i in enumerate(name):
#     # print(j)
#     index = i[0]
#     val = i[1]
#     print(index,val)
#
# for i,j in enumerate(name):
#     print(i,j)

#
# name.insert(3,"three")
# print(name)
# name.remove("thr")
# print(name)
# name.append("10")
# print(name)


# list = [1,2,3,4,5,6]
# list.remove(6)
# del list[-1]
# print(list)

def f1():
    print("123")
    return 222
    print("456")

r = f1()
print(r)
