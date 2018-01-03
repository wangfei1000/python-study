#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

'''
前面学习的模块
logging
time/datatime
json/pickle
requests
'''


############ 补充的模块 特殊的变量  ##########
'''
# 获取文件的注释(在''''''里面的注释)
__doc__
'''
import s2
print(s2.__doc__)


'''
__file__
# 运行的当前文件的路径（相对路径）
print(s2.__file__)

例子：
现在我要将当前文件的父目录的父目录添加到sys.path里区（可以理解为linux的环境变量PATH)

import  os
import  sys

# abspath 绝对路径
# print(os.path.abspath())
print(__file__)
print(os.path.abspath(__file__))
print(sys.path)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(sys.path)
'''



'''
# __package__  不常用
# 当前模块所在的包。
from  bin import admin  as hehe

print(hehe.__package__)
'''




'''
__cached__
# 就是那个.pyc编译的文件存放位置，（也可以理解为缓存文件）

print(s2.__cached__)
'''


'''
__name__   常用
# 只有执行当前文件的时候，__name__ 才会等于"__main__". 如果是模块导入的时候不相等。
__name__ == "__main__"
'''


