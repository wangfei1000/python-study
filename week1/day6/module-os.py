#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei
# os 模块


'''
用于提供系统级别的操作：
os.getcwd()                 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")         改变当前脚本工作目录；相当于shell下cd
os.curdir                   返回当前目录: ('.')
os.pardir                   获取当前目录的父目录字符串名：('..')
os.makedirs('dir1/dir2')    可生成多层递归目录
os.removedirs('dirname1')   若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')         生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')         删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')       列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()                 删除一个文件
os.rename("oldname","new")  重命名文件/目录
os.stat('path/filename')    获取文件/目录信息
os.sep                      操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep                  当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep                  用于分割文件路径的字符串
os.name                     字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")   运行shell命令，直接显示
os.environ                  获取系统环境变量
os.path.abspath(path)       返回path规范化的绝对路径    # 重要
os.path.split(path)         将path分割成目录和文件名二元组返回
os.path.dirname(path)       返回path的目录。其实就是os.path.split(path)的第一个元素     # 重要
os.path.basename(path)      返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)        如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)         如果path是绝对路径，返回True
os.path.isfile(path)        如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)         如果path是一个存在的目录，则返回True。否则返回False

# 就是将文件名和路径组合到一块

import os
Dir = os.path.dirname(__file__) # 显示的文件目录所在的绝对路径
Abs = os.path.join(Dir,"aaa") # 现在开始组合
print(Abs)  # 这就组合了文件aaa的绝对路径

os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略   # 重要
#


os.path.getatime(path)      返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)      返回path所指向的文件或者目录的最后修改时间
'''
