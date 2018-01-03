'''
定义一个函数
必须是先定义，再去调用。

函数的结构：
	1、def 定义函数
	2、函数的名字
	3、函数体
	4、return 返回值

    def 函数名():
        函数体
        return 返回值

定义函数，函数是不执行的。
'''



def sendmail(xxoo, content):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    try: # 捕捉程序异常, 发送失败返回False ，发送成功返回True
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["王飞", '4836895@163.com'])
        msg['To'] = formataddr(["python测试邮件", '1005487137@qq.com'])
        msg['Subject'] = "测试邮件"

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("4836895@163.com", "5201314mn")
        server.sendmail('4836895@163.com', [xxoo,content ], msg.as_string())
        server.quit()
    except:
        # 发送失败
        return False
    else:
        # 发送成功
        return True

'''
补充：
用户捕获程序异常。

try :
    要执行的代码主体
except:
    如果有异常，就抛这个信息
else:
    如果正常就抛这个信息
'''


ret = sendmail("wangfei@hrfax.cn","test")
# 注意： 上面程序返回的时True or False是布尔类型的，不是普通的字符串。
if ret == True:
    print("发送成功。")
else:
    print("发送失败。")



# python中在遇到return语句后，函数执行过程立即终止。
def f1():
    print("123")
    return 111
    print("456")

r = f1()
print(r)


# python的函数如果不return值的话，会自动的return 一个默认值None。
def f2():
    print("hehe")

r = f2()
print(r)


'''
形式参数和默认参数
'''
# 形式参数,xxoo 就是一个形式参数。
def sendmail(xxoo):
    pass

# 实际参数
result = sendmail("wangfei1000@yeah.net")

def send(FromMail,Content,Msg): # 括号里面的参数是形式参数。形式参数是按照对应的位置进行接收的。
    print("邮件发送成功！", FromMail, Content, Msg)
    return True

while True:
    Email = input("请输入邮箱地址： ") # 实际参数
    Meg = input("请输入内容：")
    Meg2 = input("请输入内容：")

    Result = send(Email, Meg, Meg2)
    if Result == True:
        print("发送成功！")
    else:
        print("发送失败！")



'''
默认参数（默认参数必须放在参数列表的最后，否则的话会怎么样？想想先。假如要不这么规定的话，那调用
这个函数向里面传递参数，不就出问题了吗？python 它怎么会知道谁是第几个参数呢？是吧？）
如果最后一个形式参数Content没有传，就会使用Content="hehe"默认参数变量。
'''

def send(FromMail, Content="hehe"):
    print("邮件发送成功！", FromMail, Content)
    return True

# 传2个参数进去
send("wangfei@hrfax.cn", "hellow")
# 只传进一个参数进去，这个时候默认参数就生效了。
send("wangfei@hrfax.cn")


# 指定参数
# 将实际参数赋值给指定的形式参数
def send(FromMail, Content):
    print("邮件发送成功！", FromMail, Content)
    return True

# 普通的参数位置是一一对应的关系， 指定参数是指 指定形式参数的位置，仔细的对比 下面的指定参数和上面的形式参数位置。
send(Content="hellow", FromMail="wangfei")



# 动态参数
'''
* 接收任意个实际参数。
默认将传入的参数全部放入到元组中。
用于接收指定位置的参数。
'''

# 函数的参数里，用了*之后，他就能接收所有传给它的参数，并将他们单独的作为一个元素，放到元组里。
def f1(*args):
    print(args,type(args))

f1(11,22,"wangfei")

# 传入参数时，前面有* ，对传入的参数做个for循环，将参数里面的各参数做为一个元素放到元组里。（如列表里的元素也是作为
# 单个元素放到元组里的。
list = [11,22,33,44,55]
f1(list,"hehe")
name = 'wangfei'
f1(*list,name)

# ** 接收任意个实际参数。(是字典型，键值对。默认将传入的参数放入到了字典中。
# 用于接收含有键值对的参数。

def f1(**args):
    print(args,type(args))

f1(n1 = 11,n2 = 18)

dic = {"k1": "v1", "k2":"v2"}
f1(**dic)  # 传入的时候加上2个*，就可以将字典传入进去了。

# 万能参数
# 既能接收带一个*的，也能接收带2个*的。
def f1(*args, **kwargs):
    print(args,kwargs)

# args 接收11,22,33,44
# kwargs接收n1 = 66, n2 = 77
f1(11,22,33,44,n1 = 66, n2 = 77)


#格式化输出
#str.format()
# 占位符，0是第一个位置，1是第二个位置
Msg = "Hellow, my name is {0}, age {1}.".format("wangfei", "20")
print(Msg)

# format方法里面还有*args和**kwargs的方式，所以可以采用如下的几种方式传入参数。
# 使用列表的方式
Msg2 = "Hellow, my name is {0}, age {1}.".format(*["zhangsan",30])
print(Msg2)

# 使用形式参数的方式。传入的时候必须要指明名称的。
Msg3 = "Hellow, my name is {name}, age {age}.".format(name = "lisi", age = 18)
print(Msg3)

# 采用字典的形式传入参数。
dic = {"name":"wanger", "age":18}
Msg4 = "Hellow, my name is {name}, age {age}.".format(**dic)
print(Msg4)



# 补充一
# 最终的结果是64，为什么呢？因为python是从上往下执行的，相同的函数名，下面的函数会覆盖上面的函数。
def f2(a1,a2):
    return a1+a2

def f2(a1,a2):
    return a1*a2

ret = f2(8,8)
print(ret)

补充二
# python函数传递一个参数时，它传递的是一个引用关系，而不是重新的赋值。
def f3(a1):
    a1.append(999)
    # return a1

li = [11,22,33,44]

f3(li)
# 返回结果是11，22，33，44，99
print(li)



# 全局变量：在所有的作用域都可以读。（全局变量名为全 大写（行业潜规则））
# 局部变量只能在自己的作用域里面使用，局部变量优先全局变量使用。
name = "wangfei" # 不在函数里定义的变量都是全局变量。
def f1():
    global name # 如果需要声明为全局变量，进行重新的复制。在前面加上global即可。
    name = "lisi" # 函数里面定义的变量不能覆盖全局变量，只在自己的作用域里面生效。
    print(name)

def f2():
    print(name)

f1()
f2()


# 特殊：对于列表和字典这样特殊的变量的值，可以进行修改，但不能进行重新的赋值。
list = [11,22,33,44,55]
dic = {"name":"wangfei", "age":18}
def f1():
    list.append(66)
    dic["name"] = "lisi"
    dic["age"] = 20

f1()
print(list,",",dic)