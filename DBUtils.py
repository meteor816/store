import pymysql
host="localhost"
user="root"
password="root"
database="bank"
def up_date(sql,param):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def select_date(sql,param):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()
    return cursor.fetchall()