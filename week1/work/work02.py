#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangfei
import  json
# 写入列表到json文件中。
# jsObj = json.dumps(ChinaMap)
# fileObject = open('/Users/feiwang/PycharmProjects/week1/china.json', 'w')
# fileObject.write(jsObj)
# fileObject.close()

# 从文件中读取大列表
f=open("china.json",  encoding='utf-8')
ChinaMap = json.load(f)
print(ChinaMap)
welcome_msg = "欢迎来到中国，现在请告诉我，你想去哪里？"
end_msg = "欢迎来到%s.".center(30,"*")
menu_one = "一级菜单【区域】".center(20,"*")
menu_two = "二级菜单【省份/直辖市】".center(20,"*")
menu_three = "三级菜单【市/区】".center(20,"*")
menu_select = "请输入ID号继续，按q退出，按b返回上一级。 >"
# 一级菜单
area_list = []
for i in ChinaMap:  # 遍历ChinaMap这个大列表，得到各个区域的字典
    for i in enumerate(i.keys()): # 取区域名；遍历区域的字典，取key，方法low
        area_list.append(i[1])    # 将遍历到的区域追加到area_list中。
while True:
    print(menu_one) # 打印体提示信息
    for i in enumerate(area_list):  # 遍历区域列表，获取区域，注意我用到了enumerate,同时能获取到下表和值。
        print(i[0], i[1])     # 打印下表和值。
    select_area_id = input("请输入ID号继续，按q退出。")
    if select_area_id == "q":     # 判断输入的是不是q，是否要退出。
        exit("bye....")    # 如果是就退出。
    else:
        if select_area_id.isdigit():   # 判断输入的是不是数字
            select_area_id = int(select_area_id)    # 转换为整数类型。
            if select_area_id >= len(area_list):     # 判断输入的数字在不在area_list 范围之内。
                print("输入的id号不存在，请重新的输入。")
                continue # 如果输入的不在范围之内的话，就继续循环，直到输入的对为止。
            else:
                select_area_dict = ChinaMap[select_area_id]  # 从大列表中取出选择的区域字典。
                for k in select_area_dict:
                    province_dict = select_area_dict[k]
                    province = province_dict.keys()
                # 二级菜单
                while True:
                    print(menu_two)
                    province_list = []
                    for k in enumerate(province):
                        province_list.append(k[1])
                        print(k[0], k[1])
                    select_provice_id = input(menu_select)
                    if select_provice_id == "q":
                        exit("bye....")
                    elif select_provice_id == "b":
                        break
                    else:
                        if select_provice_id.isdigit():
                            select_provice_id = int(select_provice_id)
                            if select_provice_id >= len(province_list):
                                print("输入的id号不存在，请重新输入。")
                                continue
                            else:
                                select_provice = province_list[select_provice_id]
                                city_list = province_dict[select_provice]
                                # 三级菜单
                                while True:
                                    print(menu_three)
                                    for i in enumerate(city_list):
                                        print(i[0], i[1])
                                    select_city_id = input(menu_select)
                                    if select_city_id == "q":
                                        exit("bye....")
                                    elif select_city_id == "b":
                                        break
                                    else:
                                        if select_city_id.isdigit():
                                            select_city_id = int(select_city_id)
                                            if select_city_id >= len(city_list):
                                                print("输入的id号不存在，请重新输入。")
                                                continue
                                            else:
                                                city = city_list[select_city_id]
                                                exit(end_msg % city)
                                        else:
                                            print("你输入的id号是无效的，请重新输入。")
                        else:
                            print("你输入的id号是无效的，请重新输入。")
        else:
            print("你输入的id号是无效的，请重新的输入。")