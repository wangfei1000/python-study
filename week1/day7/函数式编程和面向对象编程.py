#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

# 函数式编程

def mail(ma,msg):
    print("send1")

# mail("wangfei@hr.com","hellow")

# 面向对象编程

class Foo:   # 类

    def mail(self,ma,msg):  # 对象
        print("send2")

# 使用这个类
# obj = Foo() # 创建一个对象，这个对象是由类Foo来进行创建。 这个obj就是类对象的指针，obj本身没有mail这个方法的，通过指针指向mail方法。
# obj.mail("wangfei@hrfa.com","hellow")



#------------- 以上这种方式就适合用函数式编程--------------------

# 假如有好多个函数，每个函数都传入相同的参数，这个时候就是面向对象编程的用武之地。如下：

class Foo:
    def fetch(self,sql):  # python会自动将对象里定义的host, user, passwd等参数传入进来。;不用将每个参数再单独的传入。
        print(self.host)
        print(self.user)
        print(self.passwd)
        print(sql)

    def modify(self,sql):
        print(self.host)
        print(self.user)
        print(self.passwd)
        print(sql)

    def remove(self,nid):
        print(self.host)
        print(self.user)
        print(self.passwd)
        print(sql)

    def create(self,sql):
        print(self.host)
        print(self.user)
        print(self.passwd)
        print(sql)


# 创建一个对象
obj = Foo() #
obj.host = "aaa.wangfei.com" # 这里定义的host user passwd 是在创建的对象里进行定义的值（封装值），到时Python会自动的将其带入到类方法里的self。
obj.user = "wangfei"
obj.passwd = "5201314mn"

# obj.fetch("select * from a")
# obj.create("select * from a")




# 那么self 到底是什么呢？ self 是一个形式参数，当创建多个对象时，哪个对象执行方法，self就是谁。
obj2 = Foo()
obj2.host="wf.com"
obj2.user="wf"
obj2.passwd="123456"
# obj2.fetch("select * from hehe.com;")


# 类中有一个特殊的方法叫做__init__(专业名称叫做构造方法），它是专门用来替代在对象里面封装值得（目的就是为了方便）。例子如下：
class Foo:

    def __init__(self,a1,a2,a3):   # 专业名称叫做构造方法，作用就是用来代替在创建的对象里直接封装值得。 在创建对象时会执行__init__
        # 这个方法，所以我们可以在构造方法__init__里进行封装值，同时为了让每次封装的值可自定义，可以改成往里面传参数的形式。
        self.host = a1
        self.user = a2
        self.passwd = a3
        # print("heheheda.")

    def fetch(self,sql):
        print(self.host)
        print(self.user)
        print(self.passwd)
        print(sql)

    def modify(self,sql):
        print(self.host)
        print(self.user)
        print(self.passwd)
        print(sql)

    def remove(self,nid):
        print(self.host)
        print(self.user)
        print(self.passwd)
        print(nid)

    def create(self,sql):
        print(self.host)
        print(self.user)
        print(self.passwd)
        print(sql)

obj= Foo("www.wf.com","wangfei","5201314mn") #  这个就是往__init__方法里面传递参数，封装值。  补充下：这里创建一个对象时，Foo()加上这个括号
# 就表示会自动的执行上面的__init__函数
# obj.remove("select * from aaaa.bbbb")

# 类的三大属性：封装，继承，多态

# 如下这个例子需要注意，有一层嵌套关系。
class c1:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class c2:
    def __init__(self,obj,money):
        self.obj = obj # 这里的obj 就是类c1
        self.money = money

    def show(self):
        print(self.money)
        return 1



obj1 = c1("wf","19")
obj2 = c2(obj1,858) # 将obj1传入obj2中，obj1就是类c1
# print(obj2.obj.name) # 使用obj1(类c1)里面的方法。


# ----------- 继承 -------------
class c1: # 父类，基类
    def show(self):
        print("show 1")
    def bar1(self):
        print("bar 1")

class c2(c1): # 子类，派生类
    def show1(self):
        print("show 2")
        return 1
    def bar(self):
        print("bar 2 ")


obj = c2()
# obj.show()

#
# ----------- 继承 -------------
class c1: # 父类，基类
    def f1(self):
        self.f3()

    def f3(self): # obj = c1; obj.f3() 我优先
        print("c1")

class c2(c1): # 子类，派生类
    def f2(self):
        self.f1()

    def f3(self):   # obj = c2; obj.f3()我优先
        print("c2")

# 当遇到子类里调用父类方法的时候，self表示子类。当父类和子类里的方法起冲突时，子类里的方法优先级别最高。

# obj = c2()
# obj.f2() #
#
# obj = c1()
# obj.f1()


# ------- 多继承 ---------
class F1:
    def show(self):
        print("show")


class F2:
    def bar(self):
        print("bar")


class F3(F1,F2):
    def f1(self):
        print("Foo3")


obj = F3()
obj.bar()
obj.f1()


# 多继承注意事项。

'''
1. 当只有一条道的时候，就是一条路走到底。子类继承父类，父类继承父父类。
2. 当有2条道的时候，左边的的优先于右边的。当左边的道走到第三步还没有走到时，就要返回同级走第二条道到底了。
3. 这里需要注意的是，self是代表是第一层的obj 就是最小的那代类。
'''

'''

### 多态
# 多种形态

# python
def func(arg):  # 什么都可往里边传
    print(arg)

func(1)
func("wf")
func([1,2,3])


# c# / java

def func(int,arg): # 只能是整数格式
    print(arg)


func(123)
func("abc") # 报错



# java 和 c  如何支持多态呢？
class A:
    pass

class B(A):
    pass

class C(A):
    pass

# arg参数： 必须是A类或A的子类类型

def func(A,arg):
    print(arg)

obj = B()
obj = C()
obj = A()



func(obj) # 都是没问题的。
'''


# 类成员  ： 字段   方法  属性

class Foo:
    cc = 123 # 字段（静态字段),保存在类里面   ； 当创建大量的对象，每个对象里都有共同的那个字段时，可以将这个字段变成静态字段，降低内存的使用。

    def __init__(self):
        self.name = "wangfei"  # 字段（普通的字段），保存在对象里面

    def show(self):
        print(self.name)


# for example
class province:
    country = "zhonguo" # 静态字段

    def __init__(self,name):
        self.name = name # 普通字段


ah = province("ah")
#



'''
静态字段和普通字段访问规则：
1.一般情况下是自己访问自己的。
静态字段通过类来访问。在代码加载时 已经创建
普通字段通过对象来访问

2.非一般情况，静态字段也可以通过采用访问普通字段的形式来进行访问


why 为什么要分开访问呢？
防止以后python语言的规则变了，代码需要重写


'''
print(ah.name) # 通过对象访问
print(ah.country) #

print(province.country) # 通过类来访问



hb = province("hb")
hn = province("hn")
sd = province("sd")

# 方法
class Province:
    country = "china"
    def __init__(self,name):
        self.name = name


    def f1(self):  # 这个叫做普通方法，至少有一个self ;由对象执行
        print(self.name)

    @staticmethod
    def show(arg1,arg2):   # 这个就是静态方法，首先他没有self,其次这个方法上面还加了个装饰器。staticmethod  ； 由类来执行
        print(arg1,arg2)   # 静态方法也是由类直接调用。用于节省内存。

    @classmethod
    def f2(cls): # python 特有的： 类方法  ；至少有一个cls 由类来执行。   ； 由类来执行
        print(cls)


# Province.show("a","b")
# Province.f2() # 返回的时类的名字


# 属性：
# 方法是男人，字段是是女人，属性就是不男不女。
# 具有方法的写作形式，具有字段的访问形式

class Pager:
    def __init__(self,all_count):
        self.all_count = all_count

    @property  # 方法上面加加个property 就是属性
    def all_pager(self):
        a1, a2 = divmod(self.all_count,10)
        if a2> 0:
            return a1 + 1
        else:
            return a1

p = Pager(101)
# r = p.all_pager() # 没变成属性就得这么玩。
r =p.all_pager  # 变成属性之后，就不需要通过执行方法的形式来调用了。
# print(r)

#  如何修改，删除属性的值呢？
class Pager:
    def __init__(self,all_count):
        self.all_count = all_count

    @property
    def all_pager(self):
        a1, a2 = divmod(self.all_count,10)
        if a2> 0:
            return a1 + 1
        else:
            return a1


    @all_pager.setter  # all_pager 是上面的方法.setter是修改的意思
    def all_pager(self,values):
        print(values)


    @all_pager.deleter # 这就是删除属性
    def all_pager(self):
        print("delete")

p = Pager(101)
# r =p.all_pager
# print(r)
p.all_pager = 111 # 修改属性；结合 all_pager.setter就可以修改all_pager属性的值了。
# del p.all_pager   # 删除属性

#

class Pager:
    def __init__(self,all_count):
        self.all_count = all_count

    def f1(self):
        print("f111111")

    def f2(self,values):
        print("f2222222")

    def f3(self):
        print("f33333333")


    foo = property(fget=f1,fset=f2,fdel=f3)


p = Pager(101)

result = p.foo  # 这种形式，会执行f1
p.foo = "aaa"   # 这种形式，会执行f2
del p.foo       # 这种形式，会执行f3


