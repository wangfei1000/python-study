# !/usr/bin/env python
# auth : wangfei
# 计算每个月的资金支出
# default
# {"SaveMoney": 4669.5, "EduMoney": 1000, "EmergencyMoney": 4434.78}

def Cal():

    # 打开配置文件，查看上一次的存款情况
    with open('db.txt', 'r', encoding='utf-8') as notebook:
        import json

        OldMyMoneyDic = json.loads(notebook.read())
        OldTotalSaveMoney = round(OldMyMoneyDic['SaveMoney'],2)
        OldTotalEmergencyMoney = round(OldMyMoneyDic['EmergencyMoney'],2)
        OldTotalEduMoney = round(OldMyMoneyDic['EduMoney'],2)

        if OldTotalEmergencyMoney < 10000: # 查看应急资金是否大于10000元
            emergency_money_per = 0.6 # 如果大于10000 ,需要补充
        else:
            emergency_money_per = 0 # 大于10000， 无需补充

    save_money_per = 0.6 # 存款百分比
    edu_money_per = 0.5 # 教育资金百分比
    total_money = int(input("1.本月工资> "))
    # life_money = int(input("2.本月生活费> "))
    life_money = 1500
    # shop_money = int(input("3.本月零花钱> "))
    shop_money = 1000
    hourse_money = int(input("4.本月房租> "))
    pay_money = life_money + shop_money + hourse_money # 本月支出金额

    emergency_money = (total_money - pay_money) * emergency_money_per
    if emergency_money + OldTotalEmergencyMoney > 10000: # 当本次的应急资金和上一次的应急资金加起来大于1w，取其差。
        emergency_money = 10000 - OldTotalEmergencyMoney


    save_money = (total_money - emergency_money - pay_money) * save_money_per # 本月存款金额
    edu_money =  (total_money - pay_money - emergency_money - save_money) * edu_money_per # 培训资金
    risk_money =  edu_money # 风险投资金额


    NowTotalEmergencyMoney = emergency_money + OldTotalEmergencyMoney
    NowTotalEduMoney = edu_money + OldTotalEduMoney
    NowTotalSaveMoney = save_money + risk_money + OldTotalSaveMoney
    NowTotalMoney = NowTotalEmergencyMoney + NowTotalEduMoney + NowTotalSaveMoney



    # 将最新的金额保存到文件里。
    with open('db.txt', 'w', encoding='utf-8') as notebook:
        import json
        my_money = {"SaveMoney": NowTotalSaveMoney,"EmergencyMoney":NowTotalEmergencyMoney,"EduMoney":NowTotalEduMoney}
        notebook.write(json.dumps(my_money))


    result_msg_last = '''
    +++++++上次结余情况++++++
    上次结余情况：
      应急资金: %d 元 ps: 应急资金最高为1w。
      培训资金: %d 元
      普蓝定投: %d 元
    ''' %( OldTotalEmergencyMoney, OldTotalEduMoney, OldTotalSaveMoney)


    result_msg_month = '''
    +++++++本月++++++
    支出情况：
      生活费: %d 元
      零花钱: %d 元
      房租费: %d 元

      本月总共消费支出: %d 元

    资金分配情况：
      本月应急资金: %d 元     ps: 当应急资金大于1w时，无需再存入。
      本月教育培训资金: %d 元
      本月普蓝定投资金: %d 元
      本月普蓝风险资金: %d 元

    最终存入情况：
      本月普蓝定投应存入(定投资金+风险资金): %d 元
      本月普蓝活期宝应存入(应急资金+教育资金)：%d 元

     ''' %(life_money, shop_money, hourse_money, pay_money, emergency_money, edu_money, save_money, risk_money, save_money +
           risk_money, emergency_money + edu_money)

    result_msg_now = '''
    ++++++最新资产情况+++++
      应急资金: %d 元 ps: 应急资金最高为1w。
      培训资金: %d 元
      普蓝定投: %d 元

      总资产: %d 元
    ''' %( NowTotalEmergencyMoney, NowTotalEduMoney, NowTotalSaveMoney,NowTotalMoney)



    print(result_msg_last, result_msg_month,result_msg_now)



if __name__ == '__main__':
    Cal()