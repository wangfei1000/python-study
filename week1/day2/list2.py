​# 一个很长的列表，数不过来的那种
list = ['zhangsan', 9,'lisi', 'wanger',9, 'boluo', 'apple', 'wangerma',9, 'lining', 'bobo', 'dahai', 1 ,2, 3, 4, 5, 6, 6,7 ,8 ,9 ]
printed（9 in list）



#if 9 in list: # 判断列表的元素是否存在
if 9 in list:
    num_of_ele = list.count(9)  # 统计列表中指定元素的个数。
    position_of_ele = list.index(9) # 查找列表中元素的位置，但是你会发现他其实是第一个位置的值。
    list[position_of_ele] = 999  # 根据位置来改列表中元素的值。
    print ("count:[%d], position:[%s]  " %(num_of_ele, position_of_ele))
    print (list)

# 批量将列表中的元素9 改为999，得用到for循环
for i in range(list.count(9)):
    ele_index = list.index(9)
    list[ele_index] = 999
print (list)




list2 = ["jack", "tom", "rotina"]
# 扩展进来一个新的列表
list.extend(list2) #
print (list)

# 翻转
list.reverse()
print (list)

'''

list = ['zhangsan',[9,'lisi', 'wanger', 9, 'boluo'], 'apple', 'wangerma',9, 'lining', 'bobo', 'dahai', 1 ,2, 3, 4, 5, 6, 6,7 ,8 ,9 ]
#list.pop(0)  # 从列表中取出指定的元素，取出后，原列表就不含有这个元素了。

menu = list.copy() # copy一个列表  ,浅copy
list[0] = "ZHANGSAN"
#list[1][0] = "999999"  # 我修改的是list列表怎么menU也会修改的呢？里边的列表是共享的，然后我们打印发现，python复制了父列表，里面的列表是共享的。（深层次的列表不copy,因为第二层列表可能数据量非常的大；浪费内存，我只用表层的不用深层的列表）；第一层包含第二层的软连接，他包含知识一个连接，每个列表在内存中都有独立的空间。
print (list)
print (menu)


# 如果想真正的完全copy,用deepcoy完全copy。深copy
import copy
list1 = copy.deepcopy(list)
list[1][0] = "999999"
print (list1)

# 查看列表的长度
print (len(list))


# 只读列表，元组
r = (1,2,3,4,5,6,7,8,9)
print(r[0])


# 列表
name = [1,2,3,4,5,6,7,8,9]
# 取第一个数
print (name[0])
# 取第二个数
print (name[1])
# 取前3个字符
print (name[:3])
# 取最后3个字符
print (name[-3:])

# 取第3个到6个之间的所有数字；2:6 这种写法，含首不含尾
print (name[2:6])


# 在第2后插入b
name.insert(2,"b")
print (name)



# 移除b
name.remove("b")
print (name)


# 在后面追加10
name.append(10)
print (name)


user = ['zhangsan', 'lisi', 'wanger', 'boluo', 'apple', 'wangerma', 'lining', 'bobo', 'dahai']
user.insert(-2,"dabobo")
print (user)

user.insert(3,"chipe")
print (user)

user2 = user[3:6]
print (user2)


user.remove("lining")
print (user)

# 删除内存中的数据,第3个到第5个数据。
del user[3:6]
print (user)


# 删除一个列表
#del user

# 给bobo加上备注
user[5] = "bobo(my friends)"
print (user)

# 每隔一个位置打印
# 这里面有一个步长的概念，步长默认是1，可以不写。
print (user[0::2])
################################################################################################################
# 打印元素的时候，同时打印下标。
name = ["wangfei","lisi","wanger"]
for index,i in enumerate(name):
    print (index,i)
