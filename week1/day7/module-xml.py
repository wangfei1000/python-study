#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

'''
<data>
# 对 xml 数据进行基础的操作。
# http://www.cnblogs.com/wupeiqi/articles/5501365.html


def func():
    from xml.etree import ElementTree as ET
    tree = ET.parse('/Users/feiwang/PycharmProjects/week1/day7/xo.xml')
    root = tree.getroot()
    # print(root) # 每一个节点都是element的对象
    # print(root.tag)  # 获取节点类型
    # print(root.attrib) # 获取当前节点属性
    # print(root.text)


    for child in root:
        for gradechild in child:
            # print(child)
            print(gradechild.tag, gradechild.attrib, gradechild.text)  # gradechild.text 获取当前节点的内容。


if __name__ == '__main__':
    func()
'''


# xml二种打开方式：

#1、打开一个字符串类型的xml文件。
#2、直接打开一个xml文件。
'''
#  修改保存string格式的xml文件.
from  xml.etree import ElementTree as ET
str_xml = open('xo.xml','r').read() # 打开文件，读取XML内容
root = ET.XML(str_xml)

# for node in root.iter('year'):  # 在当前节点的子孙中,查找指定的节点,并返回一个迭代器.
for node in root.iter('country'):  # 在当前节点的子孙中,查找指定的节点,并返回一个迭代器.
    print(node.tag)
    # new_year = int(node.text) + 1
    # node.text = str(new_year)
    # print(node.text)

    # 设置属性
    node.set('Panama', 'wangfeiiiiiiiiiiiiiiiiiiiiiii')
    # 删除属性
    # del node.attrib['name']

tree = ET.ElementTree(root)   #  转换成了tree格式的(就是那个直接打开xml文件的.)
tree.write('new_xo.xml',encoding='utf-8')
'''

'''
# 修改保存xml文件
from xml.etree import  ElementTree as ET

tree = ET.parse("xo.xml")
root = tree.getroot()

for node in root.iter('year'):
    new_year = int(node.text) + 88
    node.text = str(new_year)
    node.set("N",'wangfei')  # 设置属性的, N 属性 key , wangfei 属性的值values

tree.write('newxo.xml',encoding='utf-8')
'''


'''

创建xml
格式: class '类名'  ; 表示创建了一个类
格式: '类名'()  ; 表示创建了一个对象

root_list = []
ele = list()
向列表中添加数据
root_list.append(ele)


from xml.etree import  ElementTree as ET

tree = ET.parse("xo.xml")
root = tree.getroot()

# ele = ET.Element(tag='alex',attrib={'k1':'v1'})
ele = ET.Element('alex',{'k1':'v1'})  # set a new node.(tag and attribute)
root.append(ele) # append tag and atb to the object.
ele.text = 'abcdefg'    # set content
tree.write('new.xml',encoding='utf-8')
'''