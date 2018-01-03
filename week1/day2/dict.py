#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei


name = {
    1860:{
        "name":"wangfei",
        "age":18,
        "addr":"hangzhou"
    },
    1861:{
        "name": "lisi",
        "age": 19,
        "addr": "chuzhou"
    },
    1862: {
        "name": "wanger",
        "age": 20,
        "addr": "hefei"
    },
    1863: {
        "name": "wangerma",
        "age": 23,
        "addr": "beijing"
    },
}

'''
print(name[1863]["name"])
name[1863]["name"] = "wangwangwang" # 修改id为1863的name为wangerma
print (name[1863]["name"])


name[1863]["mobile"] = '186-0651-1327' # 往字典中添加一个信息
print (name[1863])

#del name[1863]["addr"] # 删除字典中的元素
#print (name[1863])

name[1863].pop("addr") # 也可以通过pop的方式来删除，但常用的是del来删除
print(name[1863])


User = name.get(1869) # 获取字典中的某一个值，也可以采用上面的方法name[1823],但如果没有对应值的话会报错
print(User)


# update语句将新字典中的数据更新到旧的字典中去，如果元字典存在就覆盖，不存在就添加。
dic2 = {
    "name":"hellow",
    1862: {
        "name": "wanger",
        "age": 20,
        "addr": "hefei"
    },
}
print(name)
name.update(dic2)
print(name)



#print(name.items()) # 将字典中的数据变成元组（列表）,注意：在字典的数据量比较大的时候，不要这么干。比较耗时。
print(name.values()) # 打印字典的所有values
print(name.keys()) # 打印字典的所有keys
print (1861 in name) # 判断一个key在字典中是否存在

# 从字典中取出一个值，如果存在就返回这个值，如果不存在，就返回默认的值。
print (name.setdefault(1869,"hahah"))


# 将列表中的元素取出来，作为key;职为values(不要用)
print (dict.fromkeys([1,2,3,4,5],"values"))
'''


# 此种方法效率低，不要采用，因为有一个字典转换为列表的过程
#for k,v in name.items():
 #   print (k,v)

# print (name.items())


# 效率高，在字典数据大的时候，请选用此方法。
for key in name:
    print (key, name[key])