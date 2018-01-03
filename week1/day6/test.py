#!/usr/bin/env python
import  re
# r = re.findall(r"\byun","yunanaleSxal1xwupeiqi")
# print(r)

# r =  re.finditer("com","comwww.runcomoob")
# print(r)
# for i in r:
#     print(i.group())

# 匹配替换
# sub subn
r = re.sub("g.t","hehe",'I get A, I got B, I got C')
# print(r)

# subn
r = re.subn("g.t","hehe",'I get A, I got B, I got C',count=1)
# printnt(r)

# split
r = re.split("got",'I got A, I got B, I got C',3)
# print(r)

# compile
text = "JGood is a handsome body, he is cool, clever, and so on...."
regex =  re.compile(r"\w*oo\w*")
r = regex.findall(text)
# print(r)

# re.search
a = re.search(r'\\com', 'aaaaaaa\com').group()
# print(a)

origin = "haf4444 habc dafdsafd"
r = re.match("h(?P<name>\w+)",origin).groups()
# print(r)

# findall
origin = "hqweaarty habcaadefg dafdsafd"
r = re.findall("h(\w+)aa(\w+)", origin)  # 他回匹配"h(\w+)" 这个表达式,但是他显示的是分组的内容.
# print(r)

origin = "hello alex bcd alex lge alex acd 19"
r1 = re.split("(alex)",origin,1)
r2 = re.split("a(le)x",origin,1)

print(r1)
print(r2)