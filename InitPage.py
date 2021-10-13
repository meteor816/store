'''
    1.数据类：
        只准备数据部分：不参与任何操作。
    任务1：
        将这个框架的数据源集中写到excel表里，使用xlrd读取
        xlrd参数化，mysql的参数化。
'''
import  xlrd
import pymysql

class InitPage:
#exclen表
    # wd = xlrd.open_workbook(filename="HKR.xlsx",encoding_override='UTF-8')
    # L = []
    # N = []
    # sheet = wd.sheet_by_index(0)
    # rows = sheet.nrows
    # for i in range(1, rows):
    #     rows_values = sheet.row_values(i)
    #     L.append({"username": rows_values[0], "password": str(int(rows_values[1])), "expect": rows_values[2]})
    # # print(L)
    # sheet = wd.sheet_by_index(1)
    # rows = sheet.nrows
    # for i in range(1, rows):
    #     rows_values = sheet.row_values(i)
    #     N.append({"username": rows_values[0], "password": str(int(rows_values[1])), "expect": rows_values[2]})
    # print(N)
#数据库
    con=pymysql.connect(host="localhost",user="root",password='root',database="登录数据")
    cursor=con.cursor()
    sql="select * from Login"
    cursor.execute(sql)
    con.commit()
    x = cursor.fetchall()
    L = []
    for i in range(len(x)):
        L.append({"username": x[i][0], "password": x[i][1], "expect": x[i][2]})
    print(L)


# class  InitPage:
#     login_success_data =[
#         {"username":"jason","password":"1234567","expect":"Student Login"},
#         {"username": "不再爱了", "password": "1234567", "expect": "Student Login"}
#     ]
#
#     login_error_data = [
#         # id : msg_uname
#         {"username": "jason1213123123123", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
#         {"username": "不再爱了", "password": "123456789898945", "expect": "账户名错误或密码错误!别瞎弄!"}
#     ]
        # id : msg_uname


















