'''
    中国工商银行账户管理系统：
    ICBC：
'''
#1.准备一个数据库 和银行名称
from DBUtils import up_date
from DBUtils import select_date
import random

# bank ={}
# bank_name = "中国工商银行回龙观支行"  #银行名称写死的

#2.入口程序
info = '''
          --------个人信息--------
          账号：%s
          密码：%s
          用户名：%s
          地址信息
              国家：%s
              省份:%s
              街道:%s
              门牌号:%s
          余额:%s
          开户行地址：%s
          ----------------------- 
      '''
def welcome():
    print("************************************")
    print("*      中国工商银行昌平支行            *")
    print("************************************")
    print("*1.开户                             *")
    print("*2.存钱                             *")
    print("*3.取钱                             *")
    print("*4.转账                             *")
    print("*5.查询                             *")
    print("*6.Bye!                            *")
    print("************************************")

#银行的开户逻辑
def B_addUser(account,username,password,country,province,street,gate,money):
    #1.判断数据库是否已满
    sql="select * from user1"
    date=select_date(sql,[])
    if len(date)>=100:
        return 3
    #2.判断用户是否存在
    elif account in date:
        return 2
    #3.正常开户
    else:
        sql1= "insert into user1 values(%s,%s,%s,%s,%s,%s,%s,%s)"
        param1=[account,username,password,country,province,street,gate,money]
        up_date(sql1,param1)
        return 1

#用户的开户操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍:")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    brank="中国工商银行"
    money =float (input("请输入您的开户余额："))  #将输入的余额换成int类型
    # 随机产生8位数字
    account = random.randint(10000000,99999999)

    status=B_addUser(account,username,password,country,province,street,gate,money)
    if status == 3:
        print("对不起，用户库已满，请携带证件到其他行办理")
    elif status ==2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status== 1:
        # bank[username].append({"账号":account,"密码":password,"余额":money,"国籍":country,"居住省份":province,"街道":street,"门牌号":gate})
        print("开户成功！以下是您的个人开户信息")
        print(info % (username,password,account,country,province,street,gate,money,brank))

# 银行的存钱逻辑
def savemoney():
    #判断账户在数据库中是否存在
    account = input("请输入您的账号：")
    sql2="select * from user1 where account=%s "
    param2=[account]
    date2=select_date(sql2,param2)
    if len(date2)>0:
        money = float(input("请输入您存入的金额:"))
        sql3 = "UPDATE user1 SET money = money + %s WHERE account = %s"
        param3 = [money, account]
        up_date(sql3, param3)
        print("存款成功！")
        aa = "select money from user1 where account = %s"
        bb = select_date(aa, account)
        print("账号余额为：", bb[0][0])
        return  True
    else:
        print("账号不存在！")
        return False

 # 银行的取钱逻辑
def drawmoney():
    # 判断用户是否存在
    account = input("请输入您的账号：")
    sql2="select * from user1 where account=%s"
    param2=[account]
    date2=select_date(sql2,param2)
    if len(date2)>0:
        password = input("请输入您的密码：")
        if password==date2[0][2]:
            money = float(input("请输入您要取出的金额:"))
            if money<date2[0][7]:
                sql4="UPDATE user1 set money= money -%s where account=%s"
                param4=[money,account]
                up_date(sql4,param4)
                print("取钱成功！")
                aa = "select money from user1 where account = %s"
                bb = select_date(aa, account)
                print("您的余额为：", bb[0][0])
            else:
                print("您的余额不足！请存入后再来！")
                return 3
        else:
            print("您输入密码不正确")
            return 2
    else:
        print("您输入的账号不存在")
        return 1

# #银行的转账逻辑
def transfer():
    account1 = input("请输入您的转出账号：")
    account2 = input("请输入您的转入账号：")
    sql2="select * from user1 where account =%s "
    param2=[account1]
    date2=select_date(sql2,param2)
    sql3="select * from user1 where account =%s"
    param3=[account2]
    date3=select_date(sql3,param3)
    if len(date2)>0 and len(date3)>0:
        password = input("请输入您转出账号的密码：")
        if password==date2[0][2]:
            money = float(input("请输入您转出的金额："))
            if money<date2[0][7]:
                sql5="UPDATE user1 set money = money - %s where account = %s"
                param5=[money,account1]
                up_date(sql5,param5)
                sql6="UPDATE user1 set money = money + %s where account = %s"
                param6=[money,account2]
                up_date(sql6,param6)
                print("转账成功！")
                aa = "select money from user1 where account= %s"
                bb = select_date(aa, account1)
                print("您转出账户的余额为：", bb[0][0])
            else:
                print("您转出的金额大于余额")
                return 3
        else:
            print("您输入的密码不正确")
            return 2
    else:
        print("您输入的账号不存在")
        return 1

 #查询
def query():
    account = input("请输入您的账号：")
    sql1="select * from user1 where account=%s"
    param1=[account]
    date1=select_date(sql1,param1)
    if len(date1)>0:
        password = input("请输入您的密码：")
        if password==date1[0][2]:
            print(info % (date1[0][0], date1[0][1], date1[0][2],date1[0][3], date1[0][4], date1[0][5], date1[0][6], date1[0][7], "中国工商银行"))
        else:
            print("您输入的密码错误")
            return 2
    else:
        print("您输入的账号不存在")
        return 1

#
while True:
    #打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose =="1":
        addUser()
    elif chose =="2":
        savemoney()
    elif chose =="3":
        drawmoney()
    elif chose =="4":
        transfer()
    elif chose =="5":
        query()
    elif chose =="6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入")