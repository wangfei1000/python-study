#!/usr/bin/env python


LOGIN = {}


def check_login(func):
    def inner(*args, **kwargs):
        if LOGIN.get("is_login", None):
            ret = func(*args, **kwargs)
            return ret
        else:
            print("请先登录。")

    return inner

# @check_login
def check_admin(func):
    def inner(*args, **kwargs):
        if LOGIN.get("is_login",None):
            if LOGIN.get("user_type",None) == "0":
                ret = func(*args, **kwargs)
                return ret
            else:
                print("请用admin登录。")
        else:
            print("请先登录。")
    return inner


def login():
    '''
    登录模块
    :return:
    '''
    User = input("User: > ")
    if User == "admin":
        LOGIN["is_login"] = True
        LOGIN["user_type"] = "0"
    else:
        LOGIN["is_login"] = True
        LOGIN["user_type"] = "1"
    pass

@check_admin
def index():
    '''
    后台管理模块。
    :return:
    '''
    print("index")


@check_login
def home():
    '''
    查看用户信息模块。
    :return:
    '''
    print("home")


def main():
    '''
    主函数模块。
    :return:
    '''
    while True:
        Num = input("1.登录。2.查看信息。3.后台管理。\n >")
        if Num == "1":
            login()
        elif Num == "2":
            home()
        elif Num == "3":
            index()


main()