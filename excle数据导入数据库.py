import xlrd
import pymysql
wd = xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)
con=pymysql.connect(host="localhost",user="root",password="root",database="excle")
cursor=con.cursor()
v=0
excel=['1Jan','2Feb','3Mar','4Apr','5May','6Jun','7Jul','8Aug','9Sep','10Oct','11Nov','12Dec']
for i in excel:
    sql = "CREATE TABLE if not exists " + i + " (`日期` VARCHAR(10),`服装名称` VARCHAR(10),`价格/件` FLOAT,`本月库存数量` FLOAT,`销售量/每日` FLOAT)"
    print(sql)

    cursor.execute(sql)
    con.commit()
    sheet = wd.sheet_by_index(v)
    rows = sheet.nrows
    cols = sheet.ncols
    for row in range(1, rows):
        date = sheet.row_values(row)
        sql1 = "insert into " + i + " values (%s,%s,%s,%s,%s)"
        print(sql1)
        param1 = date
        cursor.execute(sql1, param1)
        con.commit()
    v = v + 1   #v:月份
cursor.close()
con.close()

