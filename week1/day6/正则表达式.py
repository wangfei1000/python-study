#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei
# 正则表达式
# http://www.cnblogs.com/wupeiqi/articles/5501365.html
import  re

'''



普通字符匹配

 - findall 

'alex': 要查找的内容.
'yunanaleSxalexwupeiqi': 查找的文本. 
'''

result = re.findall('alex','yunanaleSxalexwupeiqi')
print(result)


''''
元字符匹配

. ^ $ * + ? {} [] \

. 任意一个字符
^ 以...开头的字符
$ 以...结尾的字符
* 匹配前面的字符0到n次
+ 匹配前面的字符1到n次
? 0个或任意一个字符

{n1,n2} 匹配前面的字符,至少出现n1次,最多出现n2次 
{n1} 匹配前面的字符,出现n1次 
{n1,} 匹配前面的字符,至少出现n1次
{,n2} 匹配前面的字符,最多出现n2次 

[a-z] 匹配a-z里面的任意一个字符,字符的范围.
[0-9]
 - 代表范围
 * 
 ^ 逻辑非
 
 \d 匹配数字
 >>> re.findall('al[\d]x','yunanSal0xwupeiqi')
 ['al0x']

\b 匹配一个单词  # 以空格符为分隔符.
re.findall(r'w\b','w wyunan Sal Axwupeiq')

'''


'''
正则


# match   # 只匹配起始位置.

re.match(pattern, string, flages=0)  # flage 编译的标志位,用于修改正则表达式的匹配方式,如:是否区分大小写,多行匹配...
>>> re.match('com','comwww.runcomoob')  # 默认是返回的一个对象.
<_sre.SRE_Match object; span=(0, 3), match='com'>

>>> re.match('com','comwww.runcomoob').group()  # 使用group获取匹配到的结果.
'com'


#search
一旦匹配成功,就是一个match object对象,有以下方法.

group() 返回被RE匹配的字符串
start() 返回匹配开始的位置.
end() 返回匹配结束的位置.
span() 返回一个元组,包含(开始,结束)的位置



print(re.search('com','comwww.runcomoob').group()) 



#findall
返回的是一个列表


#finditer
返回的是对象,要想获取所有的结果,对它做一个遍历.
import  re
r = re.finditer('com','comxxx comaaaa combbb')
for i in r:
    print(i.group())



# sub subn
# 匹配替换

语法: re.sub(pattern, repl, string, max=0)

>>> re.sub("g.t","have",'I get A, I got B, I got C')
'I have A, I have B, I have C'
>>> re.sub("g.t","have",'I get A, I got B, I got C',1) #最大替换次数1, 只替换第一个匹配到的字符串.
'I have A, I got B, I got C'
>>> re.sub("g.t","have",'I get A, I got B, I got C',2)
'I have A, I have B, I got C'

# 将所有的匹配成功的字符串替换,并告知此次数.
>>> re.subn("g.t","have",'I get A, I got B, I got C')
('I have A, I have B, I have C', 3)


# split
对字符串做分割

>>> re.split('\d+','one1two2three3four4') # 以数字作为分隔符
['one', 'two', 'three', 'four', '']


# compile
将要匹配的字符封装成一个对象, 然后去调用.
>>> text = "JGood is a handsome body, he is cool, clever, and so on...."
>>> regex = re.compile(r'\w*oo\w*')
>>> print(regex.findall(text))
['JGood', 'cool']

'''



'''
# 为什么是4个\, python正则需要2个,pyhon需要2个\\才能表示成一个\


>>> a = re.search('\\\\com', 'www.run\comoob').group()
>>> a
'\\com'   #  为什么是2个\\, 多出的一个为Pyhon的

>>> a = re.search('\\\\', 'www.run\comoob').group()
>>> a
'\\'

>>> re.search(r'\\', 'www.run\comoob').group()  # 利用r 原生字符串可表示,来进行转义.
'\\'

# 
>>> re.search(r'\bblow', 'blow').group()  #　＼ｂ在pyhon里有特殊的意义 - 退格, 前面的r表示取消\b的作用,所以就变成匹配blow了.
'blow'

# 
>>> re.search('\\bblow', 'blow').group()  
'blow'
'''



