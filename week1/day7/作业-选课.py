#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei
import  pickle

class teacher:
    def __init__(self,name,age,fav,):
        '''
        :param name: 老师的姓名
        :param age:  老师的年龄
        :param fav:  老师的爱好
        :param asset: 老师的资产
        '''

        self.name = name
        self.age = age
        self.fav = fav
        self.asset = 0

    def accident(self):
        '''
        教学事故，每次扣1块钱。
        :return:
        '''

        self.asset =  self.asset -1

    def gain(self):
        '''
        老师每次教课都会获得收获。
        :return:
        '''
        self.asset += value



# 老师的信息，从文件里面去读取。
class subject(teacher):
    def __init__(self):
        '''
        从文件里读取老师的信息
        '''

        li = pickle.load(open("teache.txt", "rb"))


    def chinese(self):
        '''
        课时费 5
        负责老师
        返回学习内容

        :return:
        '''


    def math(self):
        '''
        课时费 6


        :return:
        '''

        pass

    def history(self):
        '''
        课时费 10

        :return:
        '''
        print("historyaaa")


class student(subject):
    def __init__(self):
        '''
        学生选课
        :param select:  学生选课内容
        '''
        obj = subject()
        sub = int(input(
        '''
        1.chinese
        2.match
        3.history
        > '''))

        if sub is 1:

            self.chinese()
        elif sub is 2:
            self.math()
        elif sub is 3:
            self.history()
        else:
            print("error.")


obj1 = teacher("wanger",30,"xxoo")
obj2 = teacher("lisi",40,"music")
obj3 = teacher("zhangsan",26,"bike")
pickle.dump([obj1,obj2,obj2],open("teache.txt","wb"))

obj = student()
# obj.go_to_class("history")