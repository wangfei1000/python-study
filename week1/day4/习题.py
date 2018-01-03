#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei


LOGGING = {"is_logging": False}

def outer(func):
    '''
    装饰器

    检查的用户的权限是不是0 管理员权限。如果是，就执行对应的函数，如果不是就不执行。


    :param func:
    :return:
    '''
    def inner(*args,**kwargs):
        if LOGGING["is_logging"]:
            if LOGGING["current_per"] == "0":
                r = func(*args,**kwargs)
                return r
            else:
                print("请使用管理员用户执行。")
    return inner


def register(u,p,m,s = "1"):
    '''
    用户注册模块

    先检查存放用户的文件存不存在，如果存在再检查用户是否已经存在，不存在就在文件后面追加写入，用户存在就reture False
    如果文件不在的话，就新建一个文件并且写入。


    :param u: 用户输入的用户名
    :param p: 用户输入的密码
    :param m: 用户的邮箱
    :param s: 用户输入的权限位
    :return :
    '''
    import  os
    if os.path.exists("db.conf") is True:
        with open("db.conf","r",encoding="utf-8") as f:
            for line in f:
                UseMsgList = line.strip().split("|")
                if UseMsgList[0] == u:
                    print("用户已经存在了")
                    return False
        with open("db.conf","a",encoding="utf-8") as f:
             f.write( u + "|" + p + "|" + m + "|" + s + "\n")
    else:
        with open("db.conf","w",encoding="utf-8") as f:
             f.write( u + "|" + p + "|" + m + "|" + s + "\n")


def logging(u,p):
    '''
    用户验证模块
    检查输入的用户和密码在db.conf文件里面是否存在。如果正确，将is_logging置为True  current_user 置为 当前用户，
    currer_per 置为当前的权限位。
    如果密码不正确，就提示用户。



    :param u: 用户输入的用户名
    :param p: 用户输入的密码
    :return:
    '''
    with open("db.conf","r",encoding="utf-8") as f :
        Flage = False
        for line in f:
            UserMsgList = line.split("|")
            # print(UserMsgList)
            if UserMsgList[0] == u:
                Flage = True
                if UserMsgList[1] == p:
                    LOGGING["is_logging"] = True
                    LOGGING["current_user"] = u
                    Per = UserMsgList[-1]
                    LOGGING["current_per"] = Per.strip()
                    # print(LOGGING)
                    manager()
                else:
                    print("密码错误")
        if not Flage:
            print("用户名错误")


def password(u):
    '''
    密码修改模块
    打开db.conf文件，进行 行迭代。将迭代的行进行split转换为list。根据用户确定所在的行，找到用户所在的行时，拼接成用户修改
    过后的文件内容写入文件。

    思想：
        将修改的文件存入到一个临时的文件中，修改完成时。将修改的临时文件覆盖到db.conf。



    :return:
    '''
    NewPass = input("New password: > ")
    with open("db.conf" ,"r",encoding="utf-8") as old, open("db_temp.conf","w",encoding="utf-8") as new:
        for line in old:
            print(line)
            UseMsgList = line.split("|")
            if u in UseMsgList:
                User = UseMsgList[0]
                Mail = UseMsgList[2]
                Per = UseMsgList[3]

                # 这里不需要在行的末尾加上\n,因为UserMsgList[-3]里面有了一个\n,所以这里就不用了。
                new.write(User + "|" + NewPass + "|" + Mail + "|" + Per)
                print("aaa"+User + "|" + NewPass + "|" + Mail + "|" + Per+"bbb")
            else:
                new.write(line)
        # new.write(User+"|"+NewPass+"|"+Mail+"|"+Per+ "\n")
    import shutil
    shutil.copy("db_temp.conf","db.conf")


@outer
def deluser(u):
    '''
    1、判断用户在不在文件里。
    2、如果在就继续判断权限位，如果权限位是0，就不写了。如果权限位是1。就跳过这一行继续写。
    3、假如用户不在，那不用写了，直接return false

                  if UserMsgList[-1] == "0":
                    print("只能删除普通用户哦！")
                    return  False
                elif UserMsgList[-1] == "1":
                    continue


    思想：
        将老得文件迭代，写到新的文件里。如果某行是用户所在的行，就不将那行写入到新的文件里。
        最后将新文件的内容覆盖的老行。

    :param u: 用户输入的密码
    :return:
    '''

    Flage = False
    with open("db.conf","r",encoding="utf-8") as old, open("db_temp.conf","a+",encoding="utf-8") as new:
        # 这里我的目的是判断要删除的用户是不是管理员用户，如果是不那就不用做其他的事情了，最后给个检查的结果
        for line in old:
            UserMsgList = line.strip().split("|")
            if UserMsgList[0] == u:
                if UserMsgList[-1] == "0":
                    print("只能删除普通用户哦！")
                    return False
                Flage =  True

    with open("db.conf", "r", encoding="utf-8") as old, open("db_temp.conf", "w", encoding="utf-8") as new:
        # 这里我检查上一步的结果，如果是用户存在而且不是不管理员，就开始操作了。
        if not Flage:
            print("用户不存在")
            return False
        else:
            # 如果所在的行是要删得用户，就跳过去。不是的话就写入。
            for line in old:
                UserMsgList = line.strip().split("|")
                if UserMsgList[0] == u:
                        continue
                else:
                    new.write(line)


    import shutil
    shutil.copy("db_temp.conf","db.conf")


@outer
def search():
    '''
    查询模块
    分为精确搜索和模糊搜索。最大的区别在于。一个是in 一个是 == 的关系。
    关于那个打印信息，前面如果有搜索到对于的内容将将Flage 置为True。后面对Flage进行检查即可。


    :return:
    '''

    while True:
        print("用户信息搜索".center(50,"*"))
        Num = input("0.退出\n1.模糊匹配\n2.精确匹配.\n> ")
        if Num == "1":
            SearchStr = input("请输入你要查询的字符串> ")
            print("查询结果".center(50,"*"))
            Flage = False
            with open("db.conf", "r", encoding="utf-8") as f:
                for line in f:
                    UserMsgList = line.strip().split("|")
                    if SearchStr in UserMsgList[0] or SearchStr in UserMsgList[2]:
                        print("用户名：",UserMsgList[0],"密码：",UserMsgList[1],"邮箱：",UserMsgList[2],"权限位：",
                               UserMsgList[-1])
                        Flage = True
                if Flage is False:
                    print("没有搜索到'%s'相关信息。" %SearchStr)
        elif Num == "2":
            SearchStr = input("请输入你要查询的字符串> ")
            print("查询结果".center(50,"*"))
            Flage = False
            with open("db.conf", "r", encoding="utf-8") as f:
                for line in f:
                    UserMsgList = line.strip().split("|")
                    if SearchStr == UserMsgList[0] or SearchStr == UserMsgList[2]:
                        print("用户名：",UserMsgList[0],"密码：",UserMsgList[1],"邮箱：",UserMsgList[2],"权限位：",
                            UserMsgList[-1])
                        Flage = True
                if Flage is False:
                    print("没有搜索到'%s'相关信息。" % SearchStr)
        elif Num == "0":
            break
        else:
            print("请输入1或者是2.")


@outer
def root(u):
    '''
    普通用户提权模块
    '''


    Flage = False
    with open("db.conf","r",encoding="utf-8") as old, open("db_temp.conf","a+",encoding="utf-8") as new:
        for line in old:
            UserMsgList = line.strip().split("|")
            if UserMsgList[0] == u:
                if UserMsgList[-1] == "0":
                    print("只能提权普通用户哦！")
                    return False
                Flage =  True

    if not Flage:
        print("用户不存在")
        return False
    else:
        with open("db.conf", "r", encoding="utf-8") as old, open("db_temp.conf", "w", encoding="utf-8") as new:
            for line in old:
                UserMsgList = line.strip().split("|")
                if UserMsgList[0] == u:
                    new.write(UserMsgList[0] + "|" + UserMsgList[1] + "|" + UserMsgList[2] + "|" + "0" + "\n")
                else:
                    new.write(line)

    import shutil
    shutil.copy("db_temp.conf","db.conf")



def msg():
    '''
    查询用户信息模块
    :return:
    '''
    with open("db.conf", "r", encoding="utf-8") as f:
        for line in f:
            UserMsgList = line.split("|")
            if LOGGING["current_user"] == UserMsgList[0]:
                print("用户信息如下".center(30,"*"))
                print('用户名: %s 密码：%s 邮箱：%s 权限位：%s' % (UserMsgList[0], UserMsgList[1],
                                                      UserMsgList[2], UserMsgList[3]))
                break


def permissions():
    '''
    用户权限验证模块

    :return:
    '''

    Per = LOGGING["current_per"]

    if Per == "1":
        while True:
            print("功能列表".center(50, "*"))
            Num = input("0.退出\n1.查看用户信息\n2.修改密码\n> ")
            if Num == "1":
                msg()
            elif Num == "2":
                CurrentUser = LOGGING["current_user"]
                password(CurrentUser)
            elif Num == "0":
                LOGGING["is_logging"] = False
                print("Bye...")
                break
            else:
                print("输入的类型错误！")
    elif Per == "0":
        while True:
            print("功能列表".center(50, "*"))
            Num = input("0.退出\n1.查看当前用户信息\n2.修改密码\n3.修改普通用户密码\n4.搜索\n5.添加普通用户\n6.删除普通用户\n"
                        "7.提权普通用户\n> ")
            if Num == "1":
                msg()
            elif Num == "2":
                CurrentUser = LOGGING["current_user"]
                password(CurrentUser)
            elif Num == "3":
                NorUser = input("请输入要修改的普通用户> ")
                password(NorUser)
            elif Num == "4":
                search()
            elif Num =="5":
                User = input("user：>")
                Password = input("password: >")
                Mail = input("email: >")
                # Per = input("权限(1 普通用户 0 管理员): >")
                print("添加的普通用户信息:\n用户名:%s 密码:%s 邮箱：%s" %(User, Password, Mail))
                register(User,Password,Mail)
            elif Num == "6":
                User = input("输入要删除的普通用户。")
                deluser(User)
            elif Num == "7":
                User = input("输入要提权的普通用户")
                root(User)
            elif Num == "0":
                # print("Bye...".center(50,"*"))
                LOGGING["is_logging"] = False
                break



def manager():
    if LOGGING["is_logging"]:
        print("欢迎 %s 登录" %(LOGGING["current_user"]))
        permissions()
    else:
        print("请先登录!!!!!")


def main():
    while True:
        print("用户管理中心".center(20,"*"))
        Num = input("1.登录\n2.注册\n3.后台管理\n4.退出\n> ")
        if Num == "2":
            User = input("user：> ")
            Password = input("password: > ")
            Mail = input("email: > ")
            Per = input("权限(1 普通用户 0 管理员): > ")
            print("注册信息:\n用户名:%s 密码:%s 邮箱：%s 权限: %s" %(User, Password, Mail, Per))
            register(User,Password,Mail,Per)
        elif Num == "1":
            User = input("user：> ")
            Password = input("password: > ")
            logging(User,Password)
        elif Num == "3":
            manager()
        elif Num == "4":
            print("Bye....")
            break
        else:
            print("输入的类型错误！")


main()