'''
    中国工商银行账户管理系统：
    ICBC：
'''
#1.准备一个数据库 和银行名称
import random

bank = {}
    # {"account":[{"username":'张三',"password":'111111',"country":"中国","province":"重庆","street":"创业街","gate":"123456","money":0}]}  #空的数据库
bank_name = "中国工商银行回龙观支行"  #银行名称写死的

#2.入口程序
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
def bank_addUser(account,username,password,country,province,street,gate):
    #1.判断数据库是否已满
    if len(bank)>=100:
        return 3
    #2.判断用户是否存在
    elif account in bank:
        return 2
    #3.正常开户
    bank[account]={
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "gate":gate,
        "money":0,
        "bank_name":bank_name
    }
    # bank[account].append(
    #     {"username": username, "password": password, "country": country, "province": province, "street": street, "gate": gate, "money": money})
    return 1

#用户的开户操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍:")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    # money =int (input("请输入您的开户余额："))  #将输入的余额换成int类型
    # 随机产生8位数字
    account = random.randint(10000000,99999999)

    status=bank_addUser(account,username,password,country,province,street,gate)
    if status == 3:
        print("对不起，用户库已满，请携带证件到其他行办理")
    elif status ==2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status== 1:
        # bank[username].append({"账号":account,"密码":password,"余额":money,"国籍":country,"居住省份":province,"街道":street,"门牌号":gate})
        print("开户成功！以下是您的个人开户信息")
        info ='''
            --------个人信息--------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份:%s
                街道:%s
                门牌号:%s
            余额:%s
            开户行地址：%s
            ----------------------- 
        '''
        print(info % (username,password,account,country,province,street,gate,bank[account]["money"],bank_name))

# 银行的存钱逻辑
def bank_savemoney(account,money):
    #判断账户在数据库中是否存在
    if account in bank.keys():
        bank[account]["money"]=bank[account]["money"]+money
        print("余额为:",bank[account]["money"])
    else:
        print("False")
#用户的存钱逻辑
def savemoney():
    account=int(input("请输入您的账号："))
    money=int(input("请输入您存入的金额:"))
    bank_savemoney(account,money)

# 银行的取钱逻辑
def bank_drawmoney(account, password, money):
    # 判断用户是否存在
    if account in bank.keys():
        if password in bank[account]["password"]:
            if money<=bank[account]["money"]:
                bank[account]["money"]=bank[account]["money"]-money
                print("取钱成功！",money)
                print("取钱成功！您的余额为:",bank[account]["money"])
            else:
                print("您的余额不足！请存入后再来！")
        else:
            print("您输入密码不正确")
    else:
        print("您输入的账号不存在")

# 用户的取钱逻辑
def drawmoney():
    account = int(input("请输入您的账号："))
    password = input("请输入您的密码：")
    money = int(input("请输入您要取出的金额"))
    bank_drawmoney(account, password, money)

#银行的转账逻辑
def bank_transfer(account1,account2,password,money):
    if account1 in bank.keys():
        if password==bank[account1]["password"]:
            if account2 in bank.keys():
                if money<=bank[account1]["money"]:
                   bank[account1]["money"]=bank[account1]["money"]-money
                   bank[account2]["money"]=bank[account2]["money"]+money
                   print("转出账户余额为：",bank[account1]["money"])
                   print("转入账号余额为：",bank[account2]["money"])
                else:
                    print("您转出的金额大于余额")
            else:
                print("您输入的账号不存在")
        else:
            print("您输入的密码不正确")
    else:
        print("您输入的账号不存在")
#用户的转账逻辑
def transfer():
    account1=int(input("请输入您的转出账号："))
    account2=int(input("请输入您的转入账号："))
    password=input("请输入您转出账号的密码：")
    money=int(input("请输入您转出的金额："))
    bank_transfer(account1, account2, password, money)
#查询
def bank_query(account,password):
    if account in bank.keys():
        if password==bank[account]["password"]:
            print("您的个人信息为：")
            print("当前账号：",account)
            print("密码：******")
            print("余额:",bank[account]["money"])
            print("用户居住地址",bank[account]["country"],bank[account]["province"],bank[account]["street"],bank[account]["gate"])
            print("当前账户的开户行",bank_name)
        else:
            print("您输入的密码错误")
    else:
        print("您输入的账号不存在")

def query():
    account=int(input("请输入您的账号："))
    password=input("请输入您的密码：")
    bank_query(account, password)


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